# PythonWithPlaywrightFramework
 Python with Playwright Framework

## Setup
This project requires an up-to-date version of Python 3.
It also uses [conda](https://docs.conda.io) to manage packages.

To set up this project on your local machine:
1. Clone it from this GitHub repository and open the project in the terminal.
2. Run `conda env create --file Config/environment.yml` from the command line in the project's root directory (it will create virtual env with all dependencies available in the environment.yml file).
3. After virtual env created, select it on your IDE or To activate this project's virtualenv , run `conda activate PythonWithPlaywrightVEnv`.
4. If you update or install any new package so update Config/environment.yml file also by using command `conda env export --file Config/environment.yml`

## Setup .env file

Create .env file at the root of the project location, and add below values like sensitive information password or key
```
PASSWORD=<place-your-password-here>

```

## Running Web Tests by command line or terminal
To run a single test file pass in the name of the test file that you want to run.
```pytest .\Web\Test\test_qapage_examples.py` 
To run a set of test files pass in the names of the test files that you want to run.
```pytest .\Web\Test```
To run a specific test pass in the function name of the test you want to run. 
```pytest -k test_demo_02```

## Running Api Tests by command line or terminal
To run a single test file pass in the name of the test file that you want to run.
```pytest .\API\Test\test_api_examples.py` 
To run a set of test files pass in the names of the test files that you want to run.
```pytest .\API\Test```
To run a specific test pass in the function name of the test you want to run. 
```pytest -k test_get_example```