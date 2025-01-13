import os
import time
from datetime import datetime
from IPython.display import Markdown, display
from lxml import etree
import openai

def display_completion_content(content):
    display(Markdown(content))

def pre_process(file_path):
    with open(file_path, 'rb') as file:
        xml_content = file.read()
    root = etree.fromstring(xml_content)
    for bpmndi_tag in root.xpath(".//bpmndi:*", namespaces={'bpmndi': 'http://www.omg.org/spec/BPMN/20100524/DI'}):
        parent = bpmndi_tag.getparent()
        if parent is not None:
            parent.remove(bpmndi_tag)
    modified_xml = etree.tostring(root, pretty_print=True, encoding='unicode')
    return modified_xml

# Configure OpenAI client
client = openai.Client(api_key="YourChatgpt API key")

# Base directories and filenames
model_base = 'Models\Group 4 Error_D'
pattern_base = 'conflicts_Patterns'
output_base_folder = 'Experimentation Results'
prompt_folder = 'Prompts\Group4_prompt.txt'


model_filename = 'Group G4.7[Error_D_Anony(AI).Audit].bpmnml'

# All models in this group
# Group G4.1[Error_D_Anony.Account].bpmnml
# Group G4.2[Error_D_Anony(AI).Anony(PI)].bpmnml
# Group G4.3[Error_D_Anony(PI).Anony(AI)].bpmnml
# Group G4.4[Error_D_Anony(AI).Anony(AO)].bpmnml
# Group G4.6[Error_D_Anony(AI).Audit].bpmnml
# Group G4.7[Error_D_Anony(AI).Audit].bpmnml
# Group G4.8[Error_D_Anony(AI).Authen].bpmnml
# Group G4.9[Error_D_Anony(AI).NonDel].bpmnml
# Group G4.10[Error_D_Anony(AI).Non-Rep].bpmnml
# Group G4.11[Error_D_Anony(AI).Non-Rep].bpmnml
# Group G4.12[Error_D_unobserv.Account].bpmnml
# Group G4.13[Error_D_unobserv.Annoy(PI)].bpmnml
# Group G4.14[Error_D_unobserv.Audit].bpmnml
# Group G4.15[Error_D_unobserv.Authen].bpmnml
# Group G4.16[Error_D_unobserv.NonDel].bpmnml
# Group G4.17[Error_D_unobserv.Nonrep].bpmnml

pattern_filename = '(Error_D_Anony.Audit)(2) Auditiability-annotated task sends messages over an Anonymity(Anonymous,Insider)-annotated messageFlow.bpmnq'
# all conflcit patterns in this group 
# (Error_D_Anony.Account) Accountability-annotated task sends messages over an Anonymity(Anonymous,Insider)-annotated messageFlow.bpmnq
# (Error_D_Anony.Anony)(1) Anonymity(anonymous, insider)-annotated sends messages over an Anonymity(pseudonymity, insider)-annotated messageFlow.bpmnq
# (Error_D_Anony.Anony)(2) Anonymity(pseudonymity, insider)-annotated task sends messages over an Anonymity(anonymous, insider)-annotated messageFlow.bpmnq
# (Error_D_Anony.Anony)(3) Anonymity(anonymous, insider)-annotated sends messages over an Anonymity(anonymous, outsider)-annotated messageFlow.bpmnq
# (Error_D_Anony.Anony)(4) Anonymity(anonymous, outsider)-annotated task sends messages over an Anonymity(anonymous, insider)-annotated messageFlow.bpmnq
# (Error_D_Anony.Audit)(1) Anonymity(anonymous, insider)-annotated task sends messages over an Auditiability-annotated messageFlow.bpmnq
# (Error_D_Anony.Audit)(2) Auditiability-annotated task sends messages over an Anonymity(Anonymous,Insider)-annotated messageFlow.bpmnq
# (Error_D_Anony.Authen) Authenticity-annotated task sends messages over an Anonymity(Anonymous,Insider)-annotated messageFlow.bpmnq
# (Error_D_Anony.NonDel) Non-Delegation-annotated task sends messages over an Anonymity(Anonymous,Insider)-annotated messageFlow.bpmnq
# (Error_D_Anony.NonRep)(1) Anonymity(Anonymous,Insider)-annotated task sends messages over a Non-repudation-annotated messageFlow.bpmnq
# (Error_D_Anony.NonRep)(2) Non-repudation-annotated task sends messages over an Anonymity(Anonymous,Insider)-annotated messageFlow.bpmnq
# (Error_D_Unobserv.Account) Accountability-annotated task sends messages over an Unobservability-annotated messageFlow.bpmnq
# (Error_D_Unobserv.Anony) Anonymity(pseudonymous,insider)-annotated task sends messages over an Unobservability-annotated messageFlow.bpmnq
# (Error_D_Unobserv.Audit) Auditiability-annotated task sends messages over an Unobservability-annotated messageFlow.bpmnq
# (Error_D_Unobserv.Authent) Authenticity-annotated task sends messages over an Unobservability-annotated messageFlow.bpmnq
# (Error_D_Unobserv.NonDel) Non-delegation-annotated task sends messages over an Unobservability-annotated messageFlow.bpmnq
# (Error_D_Unobserv.NonRep) Non-repudation-annotated task sends messages over an Unobservability-annotated messageFlow.bpmnq



# Full paths for files
model = os.path.join(model_base, model_filename)
pattern = os.path.join(pattern_base, pattern_filename)


# Pre-process the files
start_time = time.time()  # Program start time
conflict_pattern = pre_process(pattern)
Model = pre_process(model)

# Load the default prompt
with open(prompt_folder, 'r') as file:
    default_system_prompt = file.read()

default_prompt = f'''
{default_system_prompt}

Conflict Pattern:
{conflict_pattern}

Model:
{Model}
'''

user_prompt = '''
Is there a conflict detected based on the criteria described in the provided XML content?
If so, explain what the conflict means for the use case, including which requirement is conflicting and why it is a conflict, and suggest a resolution.
'''

messages = [
    {
        "role": "system",
        "content": default_prompt
    },
    {
        "role": "user",
        "content": user_prompt
    }
]

# Call the API with the combined prompts
llm_start_time = time.time()  # LLM call start time
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=messages
)
llm_end_time = time.time()  # LLM call end time

completion_content = completion.choices[0].message.content

# Capture program runtime details
end_time = time.time()
total_runtime = end_time - start_time
llm_response_time = llm_end_time - llm_start_time

# Prompt for experiment ID
experiment_id = input("Enter the Experiment ID: ")

# Prepare output file
Result = f"""Experiment ID: {experiment_id}
Model: {model_filename}
Pattern: {pattern_filename}

Program Runtime: {total_runtime:.2f} seconds
LLM Response Time: {llm_response_time:.2f} seconds

LLM Response:
{completion_content}
"""

output_filename = f"{experiment_id}_{pattern_filename.split(')')[0].replace('(', '')}_{model_filename.split('[')[0]}.txt"
output_full_path = os.path.join(output_base_folder, output_filename)

# Write the output to file
with open(output_full_path, 'w') as file:
    file.write(Result)

print(f"File written: {output_full_path}")
