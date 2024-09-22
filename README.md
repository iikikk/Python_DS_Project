# Project #1: Continuous Integration for Python Data Science

This project demonstrates a robust setup for a Python data science project using continuous integration with GitHub Actions to ensure code quality and functionality.

## Project Structure

- `analysis.ipynb`: Jupyter notebook containing cells that perform descriptive statistics. This can use either Pandas depending on the project specifics.
- `Makefile`: Automates tasks such as testing, linting, and installing dependencies.
- `test_script.py`: Contains tests for the main Python script.
- `test_lib.py`: Contains tests for utility functions in the library.
- `requirements.txt`: Lists all dependencies with pinned versions to ensure reproducibility.
- `script.py`: Main Python script (if applicable, describe briefly what it does).
- `lib.py`: Python library with functions used across the project.

## Features

- **Descriptive Statistics in Jupyter Notebook**: Analyze data using comprehensive statistical methods provided by Pandas.
- **Testing with nbval**: Ensures that all notebook cells execute correctly using the `nbval` plugin for `pytest`.
- **Continuous Integration**: Utilizes GitHub Actions to automate testing, linting, and other checks.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-name>

2. **Install Dependencies**
   ```bash
   make install
   
3. **Run Tests**
   ```bash
   make test

4. **Linting**
   ```bash
   make lint

5. **Format Code**
   ```bash
   make format


## Continuous Integration Status
[![Install Dependencies](https://github.com/iikikk/Python_DS_Project/actions/workflows/install.yml/badge.svg)](https://github.com/iikikk/Python_DS_Project/actions/workflows/install.yml)

[![Code Formatting](https://github.com/iikikk/Python_DS_Project/actions/workflows/format.yml/badge.svg)](https://github.com/iikikk/Python_DS_Project/actions/workflows/format.yml)

[![Lint Code](https://github.com/iikikk/Python_DS_Project/actions/workflows/lint.yml/badge.svg)](https://github.com/iikikk/Python_DS_Project/actions/workflows/lint.yml)

[![Run Tests](https://github.com/iikikk/Python_DS_Project/actions/workflows/test.yml/badge.svg)](https://github.com/iikikk/Python_DS_Project/actions/workflows/test.yml)