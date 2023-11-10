import json
import os
from openai import OpenAI

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

def run_text_model(
    model_name: str,
    temperature: float,
    top_p: float,
    messages: list[str],
):
    """Text Completion using a LLM"""
    completion = client.chat.completions.create(
        model = model_name,
        messages = messages,
        temperature = temperature,
        top_p = top_p
    )
    prediction = str(completion.choices[0].message.content)
    return prediction


def _process_response(response: str) -> str:
    if 'Answer:\n' in response:
        response = response.split('Answer:\n ')[1]

    response = response.replace("\'", "'").replace('`', '')
    return response


def query_llm(llm_query: list[str], model_name:str, temperature: float, top_p: float) -> dict | None:
    response = run_text_model(model_name, temperature, top_p, llm_query)
    response = _process_response(response)

    if not response.strip():
        return None

    response_dict = json.loads(response)
    
    return response_dict