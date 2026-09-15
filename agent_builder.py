# agent_builder.py
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage, AIMessage

import config
from tools import weather_tools
from guardrails import validate_input

def build_agent():
    """Initializes ChatOllama, binds tools, and attaches MemorySaver checkpointer."""
    try:
        llm = ChatOllama(
            model=config.OLLAMA_MODEL,
            temperature=0,
            base_url=config.OLLAMA_BASE_URL
        )
    except Exception as e:
        print(f"[Initialization Error]: Could not instantiate Ollama client: {e}")
        raise e

    # In-memory checkpointing for conversation history persistence
    checkpointer = MemorySaver()

    system_prompt = (
        "You are a specialized weather assistant. You must ONLY answer questions using the provided tools "
        "(get_weather and convert_temperature). Follow previous conversation context accurately."
    )

    # Construct the ReAct agent graph with state persistence
    agent = create_react_agent(
        model=llm,
        tools=weather_tools,
        prompt=system_prompt,
        checkpointer=checkpointer
    )
    return agent

def execute_agent_with_safeguards(agent, user_query: str, thread_id: str) -> str:
    """Applies guardrails validation and handles API errors during execution."""
    
    # 1. Run Guardrails Pre-Validation
    guard_result = validate_input(user_query)
    if not guard_result["is_valid"]:
        return guard_result["response"]

    # 2. Set Up Thread ID Memory Config
    thread_config = {"configurable": {"thread_id": thread_id}}
    input_payload = {"messages": [HumanMessage(content=user_query)]}

    # 3. Invocation with API Error Interception
    try:
        result = agent.invoke(input_payload, config=thread_config)
        
        # Extract the final AI message response
        last_msg = result["messages"][-1]
        if isinstance(last_msg, AIMessage):
            return last_msg.content
        return str(last_msg.content)

    except ConnectionError:
        return "[API Error]: Could not connect to local Ollama server. Ensure 'ollama serve' is active."
    except Exception as e:
        return f"[System Error]: Execution failure: {str(e)}"