# Large Language Models for Matching & Resolving Conflict Patterns in Business Process Models
Masterarbeit or Master Thesis report 

Supervised by: Dr.Qusai Ramadan (Primary Supervisor), Dr.Amirshayan Ahmadian (Second Supervisor)
 
This repository presents the artifacts and implementation details for our detailed study on leveraging Large Language Models (LLMs) to detect, explain, and suggest resolutions for conflicts in BPMN models. Building on the SecBPMN2 framework, this study explores integrating advanced AI capabilities to address key security and data-minimization requirements in business process models. Through a systematic and experimental approach, we provide insights into how LLMs can be effectively utilized for automated conflict detection, detailed explanations of identified issues, and the suggestion of actionable resolutions. This repository includes all artifacts, experimental results, and prompts developed throughout the study, offering a comprehensive resource.

This repository contains all the necessary resources, scripts, and results for conducting conflict analysis in BPMN models using Large Language Models (LLMs). The key components include:

Raw and Preprocessed Data:
  BPMN models and conflict patterns extracted from the SecBPMN2 tool, are stored in their original XML format.
  Preprocessed versions of the same data in JSONL format for seamless integration with the LLM analysis pipeline.

Scripts:
  Preprocessing scripts to prepare raw XML files for analysis.
  Experiment with scripts to automate conflict detection and analysis using LLMs.

Prompts:
  Incrementally developed and fine-tuned prompts, organized by conflict pattern groups.
  A specialized prompt for the full-scale case study.
  
Results:
  Experimental results, including LLM responses for each test case, are organized by experiment IDs.
  A detailed case study analysis of a comprehensive BPMN model, highlighting conflict detection and resolution suggestions.
