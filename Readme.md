# Secrect Santa Game

## Introduction

The Tool will automate the process of assigning secret children to employees based on the provided employee information.

## Table of Contents

1. [Installation](#Installation)
2. [Run](#Run)
3. [Tool-Execution](#Tool-Execution)
4. [Purpose-Secret-Santa](#Purpose-Secret-Santa)

##  Installation

The following topics need to be installed before using the tool.

### Python Download link
- [Download Python latest version ](https://www.python.org/downloads/)

### Environment build

- Please put the source files in a folder after downloading and installing Python.

- In the terminal window, open the folder.

- Use the command below to change the Environment_name to the appropriate name.
    ```bash
        python3 -m venv Environment_name
    ```

- To activate the environment, press the command below
    ```bash
        source Environment_name/bin/activate
    ```

- To install the necessary library, type the command below. 
    ```bash
        pip install -r requirements.txt
    ```

- Use the command below to install the necessary libraries. 

## Run

- To launch the utility, type the following command into the terminal.
    ```bash
        python3 Secrect-Santa-code.py
    ```

## Tool-Execution

- The GUI will appear and choose the corresponding last year's output csv file as the input after the run command has been executed.

- **Note:** Please keep ***Secret-Santa-Game-Result-2023*** as the filename. The tool will automatically generate the current year for this file name if the year is entered in the final element.

- In the appropriate path where the input csv is provided, the final output csv will be produced.


## Purpose-Secret-Santa

- Each employee is required to choose another employee as their secret child, to whom they will anonymously give a gift during the event. 

- Tool automate the process of assigning secret children to employees based on the provided employee information. 
