# Planit
Objective: Perform UI automation tests for https://jupiter.cloud.planittesting.com/

## Pre-requisites:
1. Python 3.10+: https://www.python.org/downloads/
2. pip (Python package manager)
3. Git: https://git-scm.com/downloads

## Setup:
1. Clone this project locally: ```https://github.com/SharmaineBernardo/Planit.git```
2. Create a virtual environment:
```bash
cd <REPO_FOLDER>

#For Windows:
python -m venv .venv
.venv\Scripts\activate

#For macOS/Linux:
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Install Playwright browsers:
```bash
playwright install
```

## Run Tests:
To run all tests:
```bash
pytest tests/
```

To run a specific test:
```bash
pytest tests/steps/<test_example>.py
```
To run using a scenario tag:
```bash
pytest -m <tag_name>
```
