import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY") # TODO: Add to common folder


def run_text_model(
    model_name: str,
    temperature: float,
    top_p: float,
    messages: list[str],
):
    """Text Completion using a LLM"""
    completion = openai.ChatCompletion.create(
        model = model_name,
        messages = messages,
        temperature = temperature,
        top_p = top_p
    )
    prediction = str(completion.choices[0].message.content)
    return prediction

def extract_entities_relationships(messages: list[str]):
    # ! Useless function
    try:
        result = run_text_model(model_name="gpt-3.5-turbo", temperature=0, top_p=0.8, messages=messages)
        if 'Answer:\n' in result:
            result = result.split('Answer:\n ')[1]
        result = result.replace("\'", "'").replace('`', '')
        return result
    except Exception as e:
        raise(e)
