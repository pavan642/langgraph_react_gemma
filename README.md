python3 main.py

Pre-requisite

pip3 install langgraph langchain-ollama langchain-core


ollama pull qwen2.5:7b


Output

python3 main.py
/Users/pavankumar/practice/langgraph_mcp_gemma/venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
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