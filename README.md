# Notebook Automation and Testing Repository
![Test Status](https://github.com/rossop/jupyter-automations/actions/workflows/tests.yml/badge.svg)

This repository is dedicated to exploring and mastering notebook automation, testing strategies, Continuous Integration (CI), and automatic generation of code and documentation. It serves as a learning platform and a reference for implementing best practices in managing and automating Jupyter notebooks, with a focus on enhancing productivity and ensuring code quality in data science and engineering projects.

## Overview

The project encapsulates a variety of tools and practices aimed at automating workflows around Jupyter notebooks. It covers the spectrum from testing notebooks using frameworks like `pytest` and `testbook`, to automating code and documentation generation, and integrating continuous integration pipelines to ensure code integrity and documentation are maintained to a high standard.

## Project Structure

The repository is organised into several directories, each serving a specific purpose in the development and testing lifecycle:

- `src`: Contains the source code that will be used within the notebooks.
- `tests`: Includes test cases and automation scripts for validating the notebooks and source code.
- `notebooks`: Jupyter notebooks that demonstrate various features and use cases.
- `docs`: Documentation for the project, including how-tos, reference materials, and examples.
- `scripts`: Utility scripts that support build processes, data management, and other automation tasks.
- `config`: Configuration files for various tools and services used within the project.
- `env`: Environment files specifying dependencies, ensuring consistency across development, testing, and production environments.
- `data`: (Optional) For projects that require access to datasets or specific configuration files.

## Getting Started

### Prerequisites

Ensure you have Python installed (version 3.8 or newer is recommended). Some aspects of the project may require additional software, tools, or accounts, which will be specified in the respective documentation sections.

### Setting Up the Environment

Clone the repository and navigate to the project directory:

```bash
git clone https://yourproject/repository.git
cd repository
```

Install the required dependencies:
```bash
pip install -r env/requirements.txt  # Or use conda/env with environment.yml
```

### Running Notebooks
To start Jupyter Notebook or JupyterLab:
```bash
jupyter notebook  # or jupyter lab
```

Navigate to the notebooks directory to explore and run the notebooks.

### Running the Tests
Execute automated tests using pytest:
```bash
pytest tests/
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Thanks to all the contributors and maintainers of the tools and libraries that make this project possible.
Special thanks to the broader Jupyter and Python communities for their invaluable resources and support.
