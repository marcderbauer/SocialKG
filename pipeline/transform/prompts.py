# PERSON PROMPT

person_prompt_tpl="""From the Resume text for a job aspirant below, extract Entities strictly as instructed below
1. First, look for the Person Entity type in the text and extract the needed information defined below:
   `id` property of each entity must be alphanumeric and must be unique among the entities. You will be referring this property to define the relationship between entities. NEVER create new entity types that aren't mentioned below. Document must be summarized and stored inside Person entity under `description` property
    Entity Types:
    label:'Person',id:string,role:string,description:string //Person Node
2. Description property should be a crisp text summary and MUST NOT be more than 100 characters
3. If you cannot find any information on the entities & relationships above, it is okay to return empty value. DO NOT create fictious data
4. Do NOT create duplicate entities
5. Restrict yourself to extract only Person information. No Position, Company, Education or Skill information should be focussed.
6. NEVER Impute missing values
Example Output JSON:
{"entities": [{"label":"Person","id":"person1","role":"Prompt Developer","description":"Prompt Developer with more than 30 years of LLM experience"}]}
"""

person_extraction_prompt="""Question: Now, extract the Person for the text below -
$ctext"""




# POSITION PROMPT

postion_prompt_tpl="""From the Resume text for a job aspirant below, extract Entities & relationships strictly as instructed below
1. First, look for Position & Company types in the text and extract information in comma-separated format. Position Entity denotes the Person's previous or current job. Company node is the Company where they held that position.
   `id` property of each entity must be alphanumeric and must be unique among the entities. You will be referring this property to define the relationship between entities. NEVER create new entity types that aren't mentioned below. You will have to generate as many entities as needed as per the types below:
    Entity Types:
    label:'Position',id:string,title:string,location:string,startDate:string,endDate:string,url:string //Position Node
    label:'Company',id:string,name:string //Company Node
2. Next generate each relationships as triples of head, relationship and tail. To refer the head and tail entity, use their respective `id` property. NEVER create new Relationship types that aren't mentioned below:
    Relationship definition:
    position|AT_COMPANY|company //Ensure this is a string in the generated output
3. If you cannot find any information on the entities & relationships above, it is okay to return empty value. DO NOT create fictious data
4. Do NOT create duplicate entities. 
5. No Education or Skill information should be extracted.
6. DO NOT MISS out any Position or Company related information
7. NEVER Impute missing values
 Example Output JSON:
{"entities": [{"label":"Position","id":"position1","title":"Software Engineer","location":"Singapore",startDate:"2021-01-01",endDate:"present"},{"label":"Position","id":"position2","title":"Senior Software Engineer","location":"Mars",startDate:"2020-01-01",endDate:"2020-12-31"},{label:"Company",id:"company1",name:"Neo4j Singapore Pte Ltd"},{"label":"Company","id":"company2","name":"Neo4j Mars Inc"}],"relationships": ["position1|AT_COMPANY|company1","position2|AT_COMPANY|company2"]}
"""

position_extraction_prompt="""Question: Now, extract entities & relationships as mentioned above for the text below -
$ctext"""




# SKILL PROMPT

skill_prompt_tpl="""From the Resume text below, extract Entities strictly as instructed below
1. Look for prominent Skill Entities in the text. The`id` property of each entity must be alphanumeric and must be unique among the entities. NEVER create new entity types that aren't mentioned below:
    Entity Definition:
    label:'Skill',id:string,name:string,level:string //Skill Node
2. NEVER Impute missing values
3. If you do not find any level information: assume it as `expert` if the experience in that skill is more than 5 years, `intermediate` for 2-5 years and `beginner` otherwise.
Example Output Format:
{"entities": [{"label":"Skill","id":"skill1","name":"Neo4j","level":"expert"},{"label":"Skill","id":"skill2","name":"Pytorch","level":"expert"}]}
"""

skill_extraction_prompt="""Question: Now, extract entities as mentioned above for the text below -
$ctext"""




# EDUCATION PROMPT

edu_prompt_tpl="""From the Resume text for a job aspirant below, extract Entities strictly as instructed below
1. Look for Education entity type and generate the information defined below:
   `id` property of each entity must be alphanumeric and must be unique among the entities. You will be referring this property to define the relationship between entities. NEVER create other entity types that aren't mentioned below. You will have to generate as many entities as needed as per the types below:
    Entity Definition:
    label:'Education',id:string,degree:string,university:string,graduationDate:string,score:string,url:string //Education Node
2. If you cannot find any information on the entities above, it is okay to return empty value. DO NOT create fictious data
3. Do NOT create duplicate entities or properties
4. Strictly extract only Education. No Skill or other Entities should be extracted
5. DO NOT MISS out any Education related entity
6. NEVER Impute missing values
Output JSON (Strict):
{"entities": [{"label":"Education","id":"education1","degree":"Bachelor of Science","graduationDate":"May 2022","score":"0.0"}]}
"""

edu_extraction_prompt="""Question: Now, extract Education information as mentioned above for the text below -
$ctext"""

prompts = [
    (person_prompt_tpl, person_extraction_prompt),
    (postion_prompt_tpl, position_extraction_prompt),
    (skill_prompt_tpl, skill_extraction_prompt),
    (edu_prompt_tpl, edu_extraction_prompt)
]

sample_query = """Developer <span class="hl">Developer</span> Developer - TATA CONSULTANTCY SERVICE Batavia, OH Relevant course work† Database Systems, Database Administration, Database Security & Auditing, Computer Security,Computer Networks, Programming & Software Development, IT, Information Security Concept & Admin,† IT System Acquisition & Integration, Advanced Web Development, and Ethical Hacking: Network Security & Pen Testing. Work Experience Developer TATA CONSULTANTCY SERVICE June 2016 to Present MRM (Government of ME, RI, MS) Developer†††† Working with various technologies such as Java, JSP, JSF, DB2(SQL), LDAP, BIRT report, Jazz version control, Squirrel SQL client, Hibernate, CSS, Linux, and Windows. Work as part of a team that provide support to enterprise applications. Perform miscellaneous support activities as requested by Management. Perform in-depth research and identify sources of production issues.†† SPLUNK Developer† Supporting the Splunk Operational environment for Business Solutions Unit aiming to support overall business infrastructure. Developing Splunk Queries to generate the report, monitoring, and analyzing machine generated big data for server that has been using for onsite and offshore team. Working with Splunk' premium apps such as ITSI, creating services, KPI, and glass tables. Developing app with custom dashboard with front- end ability and advanced XML to serve Business Solution unit' needs. Had in-house app presented at Splunk's .Conf Conference (2016). Help planning, prioritizing and executing development activities. Developer ( front end) intern TOMORROW PICTURES INC - Atlanta, GA April 2015 to January 2016 Assist web development team with multiple front end web technologies and involved in web technologies such as Node.js, express, json, gulp.js, jade, sass, html5, css3, bootstrap, WordPress.†Testing (manually), version control (GitHub), mock up design and ideas Education MASTER OF SCIENCE IN INFORMATION TECHNOLOGY in INFOTMATION TECHNOLOGY KENNESAW STATE UNIVERSITY - Kennesaw, GA August 2012 to May 2015 MASTER OF BUSINESS ADMINISTRATION in INTERNATIONAL BUSINESS AMERICAN INTER CONTINENTAL UNIVERSITY ATLANTA November 2003 to December 2005 BACHELOR OF ARTS in PUBLIC RELATIONS THE UNIVERSITY OF THAI CHAMBER OF COMMERCE - BANGKOK, TH June 1997 to May 2001 Skills Db2 (2 years), front end (2 years), Java (2 years), Linux (2 years), Splunk (2 years), SQL (3 years) Certifications/Licenses Splunk Certified Power User V6.3 August 2016 to Present CERT-112626 Splunk Certified Power User V6.x May 2017 to Present CERT-168138 Splunk Certified User V6.x May 2017 to Present CERT -181476 Driver's License Additional Information Skills† ∑††††SQL, PL/SQL, Knowledge of Data Modeling, Experience on Oracle database/RDBMS.† ∑††††††††Database experience on Oracle, DB2, SQL Sever, MongoDB, and MySQL.† ∑††††††††Knowledge of tools including Splunk, tableau, and wireshark.† ∑††††††††Knowledge of SCRUM/AGILE and WATERFALL methodologies.† ∑††††††††Web technology included: HTML5, CSS3, XML, JSON, JavaScript, node.js, NPM, GIT, express.js, jQuery, Angular, Bootstrap, and Restful API.† ∑††††††††Working Knowledge in JAVA, J2EE, and PHP.† Operating system Experience included: Windows, Mac OS, Linux (Ubuntu, Mint, Kali)††"""