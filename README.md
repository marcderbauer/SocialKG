# Humanitarian KG

## What is This Repository About?

As the name might hint at, this repository's goal is to provide structured knowledge to humanitarian organisations and decisionmakers.  
It follows a standard ETL-Pipeline scheme with the following three steps:  

1. __Extract__: Extract text from a given source (e.g. `HTML`, `PDF`, `TXT` or maybe even from an `API`).
2. __Transform__: Take the text from step (1) and extract useful information into relational triplets (currently using an LLM).  
3. __Load__: Take the relational triplets and load them into a Graph Database ([Neo4j](https://neo4j.com/)).  
  
For now the main focus is to construct an MVP. This will be a proof of concept on how to use LLMs to construct a Knowledge Graph.  
Crucial to this is ensuring that the knowledge extracted can be traced throughout the whole system from the extraction step all the way into the KG database.  
  
During the development of this repository, the topical focus will be on the Sudans. They unfortunately haven't received much news coverage, despite both facing severe humanitarian crises.  

- Sudan recently surpassed it's worst case scenario and has [almost 5 million internally displaced people](https://centre.humdata.org/displacement-in-sudan-worse-than-the-worst-case-scenario/) and  
- Approximately [2/3rds of the population in South Sudan are in need of humanitarian assistance](https://civil-protection-humanitarian-aid.ec.europa.eu/where/africa/south-sudan_en).  
  
Once the technology works as intended, there are a few different directions I might develop this into:  

- Multi-Agent qualitative scenario forecasting
- Migration pattern prediction
- Policy evaluation; testing impact of certain policies
- ...
  
## Current State of Development  

You can track the current state of this project via [GitHub tickets](https://github.com/marcderbauer/humanitarianKG/issues). I'm trying to be as transparent as possible with its' development.  
Should you have any requests or questions, please feel free to create a ticket or reach out to me via [email](mailto:hello@marcanthonybauer.com).
