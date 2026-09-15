# `README.md`

```markdown
# LangGraph Weather Agent (Memory, Guardrails & Error Handling)

A modular, stateful ReAct AI agent built with **LangGraph**, **LangChain**, and local inference via **Ollama (`qwen2.5:7b`)**. The system features conversation thread memory via `MemorySaver`, strict input validation guardrails, and robust runtime error handling for local LLM invocation.

---

## 🌟 What the Application Does

The Weather Agent acts as a specialized assistant designed to execute weather inquiries and temperature conversions while enforcing high operational safety and computational efficiency:

1. **Input Guardrails & Validation:**
   - **Context Length Limit:** Rejects inputs exceeding configured character limits.
   - **Greeting Interception:** Detects standard conversational greetings (`hi`, `hello`) and short-circuits execution with a default response without spending LLM compute tokens.
   - **Gibberish Filtering:** Identifies invalid character noise, non-alphanumeric streams, or unparseable input patterns.
   - **Domain Restriction:** Enforces strict domain limits—rejecting non-weather topics (e.g., general knowledge questions like *"What is the capital of France?"*).

2. **Stateful Conversation Memory (`MemorySaver`):**
   - Retains context history per `thread_id`. 
   - Allows multi-turn follow-up questions without re-stating context (e.g., asking *"Can you convert that temperature to Fahrenheit?"* immediately after querying Tokyo's weather).

3. **Deterministic Tool Execution (ReAct Workflow):**
   - Automatically selects and invokes custom Python functions (`get_weather`, `convert_temperature`) via LangGraph's prebuilt ReAct agent loop.

4. **API & Engine Failure Safeguards:**
   - Wraps LLM invocations in defensive `try-except` blocks to handle network disconnects, model timeouts, or missing dependencies gracefully.

---

## 📁 Project Architecture

```text
langgraph_react_gemma/
├── config.py             # Global configurations, model targets, and guardrail thresholds
├── guardrails.py         # Input validation rules (length, greetings, gibberish, domain enforcement)
├── tools.py              # Custom weather and temperature conversion tools
├── agent_builder.py      # ReAct agent builder with MemorySaver & API failure handlers
├── main.py               # Interactive CLI entry point and execution loop
└── README.md             # Project documentation

```

---

## 🛠️ Prerequisites

Ensure you have Python **3.10+** installed.

### 1. Install Dependencies

```bash
pip3 install langgraph langchain-ollama langchain-core

```

### 2. Pull Ollama Model

Make sure [Ollama](https://ollama.ai) is running locally, then pull the tool-compatible model:

```bash
ollama pull qwen2.5:7b

```

---

## 🚀 Execution

Run the application entry point:

```bash
python3 main.py

```

---

## 📋 Sample Output & Application Logs

```text
$ python3 main.py
/Users/pavankumar/practice/langgraph_mcp_gemma/venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: [https://github.com/urllib3/urllib3/issues/3020](https://github.com/urllib3/urllib3/issues/3020)
  warnings.warn(
/Users/pavankumar/practice/langgraph_mcp_gemma/venv/lib/python3.9/site-packages/langgraph/checkpoint/base/__init__.py:18: LangChainPendingDeprecationWarning: The default value of `allowed_objects` will change in a future version. Pass an explicit value (e.g., allowed_objects='messages' or allowed_objects='core') to suppress this warning.
  from langgraph.checkpoint.serde.jsonplus import JsonPlusSerializer

=================================================================
   WEATHER AGENT (MEMORY, GUARDRAILS & ERROR HANDLING)   
=================================================================

User: 'hi, how are you'
Agent: I am restricted to answering questions related to weather information and temperature conversions only.
-----------------------------------------------------------------
User: 'What is the capital of France?'
Agent: I am restricted to answering questions related to weather information and temperature conversions only.
-----------------------------------------------------------------
User: 'asdfghjklqwrtyxzcvbnm!@#$'
Agent: Your input appears to be invalid or unintelligible. Please ask a clear weather-related question.
-----------------------------------------------------------------
User: 'What is the weather in Tokyo?'
Agent: The current weather in Tokyo is 22°C and it's sunny.
-----------------------------------------------------------------
User: 'Can you convert that temperature to Fahrenheit?'
Agent: The temperature in Tokyo is 71.6°F.
-----------------------------------------------------------------

```

```

```