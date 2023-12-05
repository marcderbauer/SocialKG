import json


def format_properties(properties):
    if properties:
        return ", " + ", ".join([f"{key}: {repr(value)}" for key, value in properties.items()])
    return ""

def replace_space_with_underscore_in_node(node):
    node_new = []
    for entry in node:
        if isinstance(entry, str):
            node_new.append(entry.replace(" ", "_"))
        else:
            node_new.append(entry)
    return node_new

def create_node_cypher(node):
    node_name, category, properties = replace_space_with_underscore_in_node(node)
    properties_cypher = format_properties(properties)

    # Construct Cypher query
    cypher = f'CREATE (:{node_name} {{category: "{category}"{properties_cypher}}})'
    return cypher

def create_relationship_cypher(relationship):
    start_node, relationship_type, end_node, properties = replace_space_with_underscore_in_node(relationship)
    property_cypher = format_properties(properties)

    # Construct Cypher query ([2:] -> Prevent empty properties with a leading comma)
    match_statement = f"MATCH (start:{start_node}), (end:{end_node})"
    create_statement = f"CREATE (start)-[:{relationship_type}{{{property_cypher[2:]}}}]->(end)"

    cypher =  f"{match_statement} {create_statement}"

    return cypher

def generate_cypher_query(graph_data):
    cypher_queries = []

    # Process nodes
    for node in graph_data["nodes"]:
        cypher_queries.append(create_node_cypher(node))

    # Process relationships
    for relationship in graph_data["relationships"]:
        cypher_queries.append(create_relationship_cypher(relationship))

    return "\n".join(cypher_queries)

# Example usage
graph_data = {
    "nodes": [
        ["South Sudan", "Country", {}],
        ["Juba", "City", {}],
        ["Government", "Organization", {}]
    ],
    "relationships": [
        ["South Sudan", "has_conflict", "Civil War", {"levels": "high"}],
        ["Government", "located_in", "Juba", {}],
        ["Government", "endures_despite", "Civil War", {}],
        ["Government", "holds_together", "Military", {"since": 2018}],
        ["Government", "holds_together", "Security", {"since": 2018}],
        ["Government", "holds_together", "Rebel Factions", {"since": 2018}],
        ["Violence", "surges_in", "South Sudan", {}],
        ["Government", "uses_strategies_to_survive", "Violence", {}]
    ]
}

cypher_query = generate_cypher_query(graph_data)
print(json.dumps(cypher_query.split("\n"), indent=4))