class LLM_Request():
    """central unit of operation. Things get added to this. hotdogstand pattern (or whatever it's called)"""

    def __init__(self, user_data: str) -> None:
        self.user_data = user_data
    