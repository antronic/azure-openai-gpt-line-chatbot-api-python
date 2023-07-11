from typing import List, Optional
import os
import openai

# Set OpenAI API key and other environment variables
openai.api_type = os.getenv("OPENAI_TYPE")
openai.api_base = os.getenv("OPENAI_BASE_URL")
openai.api_version = os.getenv("OPENAI_VERSION")
openai.api_key = os.getenv("OPENAI_KEY")
completion_engine = os.getenv("OPENAI_COMPLETION_ENGINE")

def ask_azure_gpt(question: str) -> Optional[str]:
    response = openai.Completion.create(
        engine=completion_engine,
        prompt=question,
        temperature=1,
        max_tokens=1000,
        top_p=0.5,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)

    if response.choices and len(response.choices) > 0: # type: ignore
        return response.choices[0].text.strip() # type: ignore
    else:
        return None
