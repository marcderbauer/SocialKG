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