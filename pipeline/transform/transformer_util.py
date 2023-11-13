import re
from string import Template


def clean_text(text):
    return re.sub(r"[^\x00-\x7F]+", " ", text)


def turn_query_into_messages(data: str, messages: dict[str, str]) -> dict[str, str]:
    data = clean_text(data)
    messages["user_prompt"]["content"] = Template(messages["user_prompt"]["content"]).substitute(ctext=data)
    return list(messages.values())


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
