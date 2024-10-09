from src import LLM

# Using default model name from config
default_llm = LLM()
response = default_llm.generate_completion("Hello, world!")

print(response)