This is a [`SonarScannerCli`](https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/scanners/sonarscanner/) project launched with  [`Docker`](https://www.docker.com) and the [`Docker SDK for Python`](https://docker-py.readthedocs.io/en/stable/).

## Requirements

- Docker
- Python 3 with PiP
- Recommended: venv or Conda

## Getting Started

1.- First, create a `.env` file from the template.

2.- Next, using the settings of your SonnarQube Project create a `<project-name>.json` settings file from the templates in the *./projects* folder.

3.- [Optional but highly recommended]: Create a virtual environment with [`venv`](https://docs.python.org/3/library/venv.html) or [`Conda`](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

4.- Install the dependencies:

```bash
python3 -m pip install -r requirements.txt
```

## Getting Started

1.- Launch the script with the `<project-name>` as argument:

```bash
python3 app.py <project-name>
```