# Large Language Models for Matching & Resolving Conflict Patterns in Business Process Models
Masterarbeit
Supervised by: Dr.Qusai Ramadan (Primary Supervisor), Dr.Amirshayan Ahmadian (Second Supervisor)
 
This repository presents the artifacts and implementation details for our detailed study on leveraging Large Language Models (LLMs) to detect, explain, and suggest resolutions for conflicts in BPMN models. Building on the SecBPMN2 framework, this study explores integrating advanced AI capabilities to address key security and data-minimization requirements in business process models. Through a systematic and experimental approach, we provide insights into how LLMs can be effectively utilized for automated conflict detection, detailed explanations of identified issues, and the suggestion of actionable resolutions. This repository includes all artifacts, experimental results, and prompts developed throughout the study, offering a comprehensive resource.


## Repository Overview
This repository contains all the necessary resources, scripts, and results for conducting conflict analysis in BPMN models using Large Language Models (LLMs). The key components include:

1. Raw and Preprocessed Data:
  - BPMN models and conflict patterns extracted from the SecBPMN2 tool, are stored in their original XML format.
  - Preprocessed versions of the same data in JSONL format for seamless integration with the LLM analysis pipeline.

2. Scripts:
  - Preprocessing scripts to prepare raw XML files for analysis.
  - Experiment with scripts to automate conflict detection and analysis using LLMs.

3. Prompts:
  - Incrementally developed and fine-tuned prompts, organized by conflict pattern groups.
  - A specialized prompt for the full-scale case study.

4. Results:
  - Experimental results, including LLM responses for each test case, are organized by experiment IDs.
  - A detailed case study analysis of a comprehensive BPMN model, highlighting conflict detection and resolution suggestions.

## Requirements

To reproduce the experiments and access the results in this repository, the following are required:

1. **STS Tool**:  
   Download and install the [STS tool](http://www.sts-tool.eu/downloads/secbpmn-dm/) to access and work with SecBPMN2 models and conflict patterns.

2. **OpenAI API Access**:  
   Obtain a valid OpenAI API key with access to GPT-4 from [OpenAI's platform](https://platform.openai.com). Ensure the API key is linked to an active account with sufficient credits to run the experiments.

3. **Repository Files**:  
   The repository includes all necessary files and directories:
   - `Models/`: Raw BPMN models.
   - `Conflict_Patterns/`: Raw conflict patterns.
   - `Experiment_Results/`: Outputs from experiments.
   - `Case_Study/`: Comprehensive case study data and results.
     - `/Preprocessed_Inputs/`: Files prepared for direct analysis.
 
4. **Python Environment**:  
   Ensure Python 3.x is installed on your system. If any dependencies are missing, install them as required when running the scripts.



## Reproducing the Study

After meeting the requirements, the following steps can be followed to reproduce the experiments and analyze the results:

1. **Access the Models and Patterns**:  
   - Raw BPMN models and conflict patterns are available in the `Models/` and `Conflict_Patterns/` folders.  
   - Preprocessed versions of these files are stored in the `Preprocessed_Inputs/` folder for direct use in experiments.

2. **View Experiment Results**:  
   - Results of individual experiments, including LLM responses, are stored in the `Experiment_Results/` folder.  
   - Each result file is named by its unique experiment ID for easy reference.

3. **Review the Case Study**:  
   - A full-scale case study is documented in the `Case_Study/` folder.  
   - This includes models, conflict patterns, and analysis outputs.

4. **Run Additional Experiments (Optional)**:  
   - The provided Python scripts can be used to preprocess additional models and conflict patterns or to execute new experiments. These scripts are designed for straightforward adaptation to new inputs.

## Acknowledgments

This study builds upon prior work utilizing the SecBPMN2 framework in the STS tool. We acknowledge the foundational contributions provided by [SoSyM-conflictsDetection](https://github.com/QRamadan/SoSyM-conflictsDetection). 

Supervision and guidance for this work were provided by **Qusai Ramadan**. His expertise and support were instrumental in the successful completion of this study.

For more details about the foundational methodology, visit the original repository at [SoSyM-conflictsDetection](https://github.com/QRamadan/SoSyM-conflictsDetection).
