from pipeline.transform.transformer_util import turn_query_into_messages
from pipeline.transform.llm import query_llm
from typing import Any

class Transformer():
    def __init__(self, config: dict[str, Any]) -> None:
        self.llm_config = config["llm"]
        self.query = config["query"]

    def process(self, data: str):
        results = {"nodes": [], "relationships": []}

        messages = turn_query_into_messages(data, self.query)

        response = query_llm(
            messages, 
            model_name=self.llm_config["model_name"], 
            temperature=self.llm_config["temperature"], 
            top_p=self.llm_config["top_p"], 
            seed = self.llm_config["seed"]
        )

        results["nodes"] += response["nodes"]
        results["relationships"] += response["relationships"]

        return results
