# AutoTM

This repository contains the source code of Android test case migration tool AutoTM.

## How to use AutoTM
1. Prerequisites
   - Android emulator with API 24+ with target app installed
   - Source app test case code
   - Target app package name and launch activity
   - GPT-4 of OpenAI API Key
   - Python 3.8+

2. Usage
   - Install the required packages using the command: `pip3 install -r requirements.txt`.
   - Populate the `main.py` file with the information mentioned in the Prerequisites section, and then initiate the program.
   - You can view the operation logs of the four agents (test semantic analyzer, event contextual semantic analyzer, event selector, test script generator) in the console or in the `log/run.log` file.
   - After the migration is complete, you will find a markdown file summarizing the workflow of this migration in the folder containing the 'source app test case code'.

