# Import the neo4j dependency
import os
from neo4j import GraphDatabase
from neo4j._sync.driver import Neo4jDriver
def run_create_query(tx,  cypher_query: str) -> None:
    return tx.run(cypher_query)

def get_driver(uri, username, password) -> Neo4jDriver:
    driver: Neo4jDriver = GraphDatabase.driver(
        uri = uri,
        auth=(username, password),
        # configuration: None
    ) 
    driver.verify_connectivity()

class Database():

    def __init__(self, uri: str, username: str, password: str) -> None:
        self.uri = uri
        self.username = username
        self.password = password


    def create_entities_and_relations(self, cypher_queries: list[str]) -> None:
        # ! # Don't like this in here. Need to figure out driver lifecycle
        driver = get_driver(self.uri, self.username, self.password)
        session = driver.session()#database="people")

        for cypher_query in cypher_queries:
            record = session.execute_write(run_create_query, cypher_query)
            print(cypher_query)

        session.close()
        print("Finished creating entities and relations...")
        return

    
if __name__ == "__main__":
    test_queries = [
        "CREATE (:South_Sudan {category: \"Country\"})",
        "CREATE (:Juba {category: \"City\"})",
        "CREATE (:Government {category: \"Organization\"})",
        "MATCH (start:South_Sudan), (end:Civil_War) CREATE (start)-[:has_conflict{levels: 'high'}]->(end)",
        "MATCH (start:Government), (end:Juba) CREATE (start)-[:located_in{}]->(end)",
        "MATCH (start:Government), (end:Civil_War) CREATE (start)-[:endures_despite{}]->(end)",
        "MATCH (start:Government), (end:Military) CREATE (start)-[:holds_together{since: 2018}]->(end)",
        "MATCH (start:Government), (end:Security) CREATE (start)-[:holds_together{since: 2018}]->(end)",
        "MATCH (start:Government), (end:Rebel_Factions) CREATE (start)-[:holds_together{since: 2018}]->(end)",
        "MATCH (start:Violence), (end:South_Sudan) CREATE (start)-[:surges_in{}]->(end)",
        "MATCH (start:Government), (end:Violence) CREATE (start)-[:uses_strategies_to_survive{}]->(end)"
    ]

    URI = os.getenv("NEO4J_URI")
    USERNAME = os.getenv("NEO4J_USERNAME")
    PASSWORD = os.getenv("NEO4J_PASSWORD")

    db = Database(URI, USERNAME, PASSWORD)
    db.create_entities_and_relations(test_queries)

    db.driver.close()
