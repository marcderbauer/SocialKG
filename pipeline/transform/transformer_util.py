import re

from pipeline.transform.llm import extract_entities_relationships
from pipeline.transform.prompts import prompts
def clean_text(text):
    return re.sub(r'[^\x00-\x7F]+',' ', text)


from collections.abc import Iterator
from string import Template
import json

def generate_messages(query: str, prompts: list[tuple[str,str]]) -> Iterator[dict[str, str]]:
    for prompt_template, extraction_prompt in prompts:

        user_content = Template(extraction_prompt).substitute(ctext=clean_text(query))
        messages = [
        {"role": "system", "content": "You are a entity and relation extractor, precisely extracting information according to a given format."},
        {"role": "assistant", "content": prompt_template},
        {"role": "user", "content": user_content},
        {"role": "assistant", "content": "Answer: (generated JSON with extracted data)"}
        ]

        yield messages


# ! =======================================================================================================
# ! ##### This entire thing is a mess. Need to sit down and figure this out with/on a piece of paper
# ! 1. How does it currently work (on an concrete level)
# ! 2. How does it work on an abstract level
# ! 3. Does the abstract level fit to my use-case? 
# !     if yes: adapt to something that makes more sense structurally
# !     else:   write from scratch



def _run_query(messages: dict[str, str]) -> Iterator[dict]:
    
    extraction = extract_entities_relationships(messages)

    if extraction.strip() == '':
        return None # ? does that make sense?

    # load into json, verification will be redundant, can simplify once chatgpt in json mode
    extraction = json.loads(extraction)

    yield extraction



# ! code has been modified, but should work the same
def map_person_to_entity(results: dict) -> dict:
    # * this only makes sense because the person is always the same in a given CV

    person_id = results["entities"][0]["id"]
    for entity in results["entities"][1:]:

        relationship_label = f"HAS_{entity['label'].upper()}"
        entity_id = entity['id']

        results["relationships"].append(f"{person_id}|{relationship_label}|{entity_id}")
    
    return results

def process_response(extraction):
    results = []
    results["entities"].extend(extraction["entities"])

    if "relationships" in extraction:
        results["relationships"].extend(extraction["relationships"])


    
def run(user_query: str, prompts: list[tuple[str,str]]) -> dict:
    # query = move contruct messages into iterator function and iterate from that
    # want "messages" to be chatgpt query, which is constructed from user query
    # maybe query could be an object? with user query (str) and llm_query?
    results = []
    # ! This should still go another level up tbh
    messages_generator: Iterator[dict[str, str]] = generate_messages(user_query, prompts)

    for messages in messages_generator:
        # * get response as json dict
        responses: Iterator[dict] = _run_query(messages) # Don't like that you're saving to results in _run query and in map_person_to_entity

        # * load into proprietary data format
        results = [process_response(response) for response in responses] # ! mismatch betwen datatype for results
        results += map_person_to_entity(results)

    return results


# setup
# ? Could maybe move in prompts.py?
sample_que = """Developer <span class="hl">Developer</span> Developer - TATA CONSULTANTCY SERVICE Batavia, OH Relevant course work† Database Systems, Database Administration, Database Security & Auditing, Computer Security,Computer Networks, Programming & Software Development, IT, Information Security Concept & Admin,† IT System Acquisition & Integration, Advanced Web Development, and Ethical Hacking: Network Security & Pen Testing. Work Experience Developer TATA CONSULTANTCY SERVICE June 2016 to Present MRM (Government of ME, RI, MS) Developer†††† Working with various technologies such as Java, JSP, JSF, DB2(SQL), LDAP, BIRT report, Jazz version control, Squirrel SQL client, Hibernate, CSS, Linux, and Windows. Work as part of a team that provide support to enterprise applications. Perform miscellaneous support activities as requested by Management. Perform in-depth research and identify sources of production issues.†† SPLUNK Developer† Supporting the Splunk Operational environment for Business Solutions Unit aiming to support overall business infrastructure. Developing Splunk Queries to generate the report, monitoring, and analyzing machine generated big data for server that has been using for onsite and offshore team. Working with Splunk' premium apps such as ITSI, creating services, KPI, and glass tables. Developing app with custom dashboard with front- end ability and advanced XML to serve Business Solution unit' needs. Had in-house app presented at Splunk's .Conf Conference (2016). Help planning, prioritizing and executing development activities. Developer ( front end) intern TOMORROW PICTURES INC - Atlanta, GA April 2015 to January 2016 Assist web development team with multiple front end web technologies and involved in web technologies such as Node.js, express, json, gulp.js, jade, sass, html5, css3, bootstrap, WordPress.†Testing (manually), version control (GitHub), mock up design and ideas Education MASTER OF SCIENCE IN INFORMATION TECHNOLOGY in INFOTMATION TECHNOLOGY KENNESAW STATE UNIVERSITY - Kennesaw, GA August 2012 to May 2015 MASTER OF BUSINESS ADMINISTRATION in INTERNATIONAL BUSINESS AMERICAN INTER CONTINENTAL UNIVERSITY ATLANTA November 2003 to December 2005 BACHELOR OF ARTS in PUBLIC RELATIONS THE UNIVERSITY OF THAI CHAMBER OF COMMERCE - BANGKOK, TH June 1997 to May 2001 Skills Db2 (2 years), front end (2 years), Java (2 years), Linux (2 years), Splunk (2 years), SQL (3 years) Certifications/Licenses Splunk Certified Power User V6.3 August 2016 to Present CERT-112626 Splunk Certified Power User V6.x May 2017 to Present CERT-168138 Splunk Certified User V6.x May 2017 to Present CERT -181476 Driver's License Additional Information Skills† ∑††††SQL, PL/SQL, Knowledge of Data Modeling, Experience on Oracle database/RDBMS.† ∑††††††††Database experience on Oracle, DB2, SQL Sever, MongoDB, and MySQL.† ∑††††††††Knowledge of tools including Splunk, tableau, and wireshark.† ∑††††††††Knowledge of SCRUM/AGILE and WATERFALL methodologies.† ∑††††††††Web technology included: HTML5, CSS3, XML, JSON, JavaScript, node.js, NPM, GIT, express.js, jQuery, Angular, Bootstrap, and Restful API.† ∑††††††††Working Knowledge in JAVA, J2EE, and PHP.† Operating system Experience included: Windows, Mac OS, Linux (Ubuntu, Mint, Kali)††"""
results = {"entities": [], "relationships": []}