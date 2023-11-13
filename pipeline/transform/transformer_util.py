import re
from string import Template


def clean_text(text):
    return re.sub(r"[^\x00-\x7F]+", " ", text)


def convert_prompt_to_llm_query(data: str, prompt: tuple[str, str]) -> dict[str, str]:
    sys_prompt, user_prompt = prompt
    data = clean_text(data)
    user_content = Template(user_prompt).substitute(ctext=data)

    messages = [
        # ! Can move in its entirety into config.yaml
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_content},
        # TODO: Check if this system prompt is necessary in this context
        {
            "role": "system",
            "content": "Output not just the first term-relation-triplet, but every triplet you can find in the text. Answer: (generated JSON with extracted data)",
        },
    ]

    return messages


def process_response(response: str | None) -> dict:
    results = {}

    if not response:
        return results

    results["entities"] = response["Nodes"]

    if "Relationships" in response:
        results["relationships"] = response["Relationships"]

    return results


def post_process(results: str) -> dict:
    # results = map_person_to_entity(results)
    # Currently nothing to post process
    return results
