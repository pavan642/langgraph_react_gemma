# main.py
import warnings
# Suppress urllib3 LibreSSL warning on macOS
warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")

import logging
from agent_builder import build_agent, execute_agent_with_safeguards

logging.basicConfig(level=logging.ERROR)

def main():
    agent = build_agent()
    thread_id = "user_session_101"

    print("\n" + "="*65)
    print("   WEATHER AGENT (MEMORY, GUARDRAILS & ERROR HANDLING)   ")
    print("="*65 + "\n")

    test_queries = [
        "hi, how are you",                                      # 1. Intercepted: Greeting
        "What is the capital of France?",                      # 2. Blocked: Out of Domain
        "asdfghjklqwrtyxzcvbnm!@#$",                            # 3. Blocked: Gibberish
        "What is the weather in Tokyo?",                       # 4. Valid Execution
        "Can you convert that temperature to Fahrenheit?",     # 5. Valid (Uses MemorySaver for 22°C context)
    ]

    for query in test_queries:
        print(f"User: '{query}'")
        response = execute_agent_with_safeguards(agent, query, thread_id=thread_id)
        print(f"Agent: {response}")
        print("-" * 65)

if __name__ == "__main__":
    main()