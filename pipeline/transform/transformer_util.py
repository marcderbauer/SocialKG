import re
from string import Template

def clean_text(text):
    return re.sub(r'[^\x00-\x7F]+',' ', text)


def convert_prompt_to_llm_query(data: str, prompt: tuple[str,str]) -> dict[str, str]:
    sys_prompt, user_prompt = prompt
    data = clean_text(data)
    user_content = Template(user_prompt).substitute(ctext=data)

    messages = [
    {"role": "system", "content": sys_prompt},
    {"role": "user", "content": user_content},
    {"role": "system", "content": "Output not just the first term-relation-triplet, but every triplet you can find in the text. Answer: (generated JSON with extracted data)"}
    ]

    return messages


def map_person_to_entity(results: dict) -> dict:
    # * this only makes sense because the person is always the same in a given CV

    person_id = results["entities"][0]["id"]
    for entity in results["entities"][1:]:

        relationship_label = f"HAS_{entity['label'].upper()}"
        entity_id = entity['id']

        results["relationships"].append(f"{person_id}|{relationship_label}|{entity_id}")
    
    return results


def process_response(response: str | None) -> dict:
    results = {}

    if not response:
        return results

    results["entities"] =response["entities"]

    if "relationships" in response:
        results["relationships"] = response["relationships"]
    
    return results

def post_process(results: str) -> dict:
    results = map_person_to_entity(results)
    return results