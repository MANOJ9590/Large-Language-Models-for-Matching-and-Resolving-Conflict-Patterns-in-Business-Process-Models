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
model_base = 'Models\Group 3 Error_B'
pattern_base = 'conflicts_Patterns'
output_base_folder = 'Experimentation Results'
prompt_folder = 'Prompts\Group2_prompt.txt'



model_filename = 'Group G3.1[Error_B_Anony.Audit].bpmnml'

# All models in this group
# Group G3.1[Error_B_Anony.Audit].bpmnml
# Group G3.2[Error_B_Anony.NonRep].bpmnml
# Group G3.3[Error_B_Anony.Unobserv].bpmnml
# Group G3.4[Error_B_Unobserv.Audit].bpmnml
# Group G3.5[Error_B_Unobserv.NonRep].bpmnml

pattern_filename = '(Error_B_Anony.Audit) Anonymity (anonymous, insider)- and Auditability-annotated messageFlow.bpmnq'
# all conflcit patterns in this group 
# (Error_B_Anony.Audit) Anonymity (anonymous, insider)- and Auditability-annotated messageFlow.bpmnq
# (Error_B_Anony.NonRep) Anonymity (anonymous, insider)- and Non-repudation-annotated messageFlow.bpmnq
# (Error_B_Anony.Unobserv) Anonymity(anonymous, outsider)- and Unobservability-annotated messageFlow.bpmnq
# (Error_B_Unobserv.Audit) Unobservability  and Auditability are required by the same messageFlow.bpmnq
# (Error_B_Unobserv.NonRep) Unobservability and Non-repudation are required by the same messageFlow.bpmnq



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
