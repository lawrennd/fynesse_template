# Fynesse Template

[![Tests](https://github.com/lawrennd/fynesse_template/workflows/Test/badge.svg)](https://github.com/lawrennd/fynesse_template/actions/workflows/test.yml)
[![Code Quality](https://github.com/lawrennd/fynesse_template/workflows/Code%20Quality/badge.svg)](https://github.com/lawrennd/fynesse_template/actions/workflows/code-quality.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Poetry](https://img.shields.io/badge/poetry-1.0+-blue.svg)](https://python-poetry.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a *GitHub template repository* for data analysis projects using the Fynesse framework. The template uses Poetry for dependency management, pytest for testing, and follows current Python development best practices.

## What is a GitHub Template?

A GitHub template repository allows you to quickly create new repositories with the same structure and files. When you use this template, you'll get a complete project setup with:

- Modern Python development environment (Poetry)
- Comprehensive testing framework (pytest)
- Code quality tools (black, mypy, flake8)
- Fynesse framework structure ready for implementation
- Documentation and examples

## How to Use This Template

### Option 1: Use the "Use this template" Button (Recommended)

1. *Click the green "Use this template" button* at the top of this repository
2. *Choose "Create a new repository"*
3. *Name your new repository* (e.g., "my-data-analysis-project")
4. *Select visibility* (public or private)
5. *Click "Create repository from template"*

Your new repository will be created with all the template files, and you can start working immediately!

### Option 2: Clone and Customize

```bash
# Clone the template
git clone https://github.com/lawrennd/fynesse_template.git my-project-name
cd my-project-name

# Remove the template's git history and start fresh
rm -rf .git
git init

# Add your new remote repository
git remote add origin https://github.com/yourusername/my-project-name.git
```

## Quick Start (After Using Template)

### Prerequisites
- Python 3.9 or higher
- Poetry (install via `curl -sSL https://install.python-poetry.org | python3 -`)

### Installation
```bash
# After creating your repository from the template:
cd your-new-project-name

# Install dependencies with Poetry
poetry install

# Activate the virtual environment
poetry shell

# Run tests to verify installation
poetry run pytest
```

### Development Workflow
```bash
# Install development dependencies
poetry install --with dev

# Run tests
poetry run pytest

# Format code
poetry run black fynesse/

# Type checking
poetry run mypy fynesse/

# Linting
poetry run flake8 fynesse/
```

### Next Steps After Setup

1. *Update project metadata* in `pyproject.toml`:
   - Change the project name and description
   - Update author information
   - Modify the repository URLs

2. *Customize the framework*:
   - Implement your data access logic in `fynesse/access.py`
   - Add data assessment functions in `fynesse/assess.py`
   - Create analysis functions in `fynesse/address.py`

3. *Configure your environment*:
   - Edit `fynesse/defaults.yml` for your data sources
   - Create `fynesse/machine.yml` for local settings
   - Add your data files to the project

4. *Start development*:
   - Write your first test
   - Implement your data pipeline
   - Document your analysis process

One challenge for data science and data science processes is that they do not always accommodate the real-time and evolving nature of data science advice as required, for example in pandemic response or in managing an international supply chain. The Fynesse paradigm is inspired by experience in operational data science both in the Amazon supply chain and in the UK Covid-19 pandemic response.

The Fynesse paradigm considers three aspects to data analysis, Access, Assess, Address.

## Framework Structure

The template provides a structured approach to implementing the Fynesse framework:

```
fynesse/
├── access.py      # Data access functionality
├── assess.py      # Data assessment and quality checks
├── address.py     # Question addressing and analysis
├── config.py      # Configuration management
├── defaults.yml   # Default configuration values
└── tests/         # Comprehensive test suite
    ├── test_access.py
    ├── test_assess.py
    └── test_address.py
```

## Modern Development Features

- *Poetry Dependency Management*: Modern Python packaging with `pyproject.toml` and `poetry.lock`
- *Comprehensive Testing*: 43 test stubs with pytest and coverage reporting
- *Code Quality Tools*: Black formatting, mypy type checking, flake8 linting
- *Virtual Environment*: Isolated development environment with Poetry
- *Documentation*: Enhanced docstrings and module documentation 

## Access

Gaining access to the data, including overcoming availability challenges (data is distributed across architectures, called from an obscure API, written in log books) as well as legal rights (for example intellectual property rights) and individual privacy rights (such as those provided by the GDPR).

It seems a great challenge to automate all the different aspects of the process of data access, but this challenge is underway already through the process of what is commonly called *digital transformation*. The process of digital transformation takes data away from physical log books and into digital devices. But that transformation process itself comes with challenges. 

Legal complications around data are still a major barrier though. In the EU and the US database schema and indices are subject to copyright law. Companies making data available often require license fees. As many data sources are combined, the composite effect of the different license agreements often makes the legal challenges insurmountable. This was a common challenge in the pandemic, where academics who were capable of dealing with complex data predictions were excluded from data access due to challenges around licensing. A nice counter example was the work led by Nuria Oliver in Spain who after a call to arms in a national newspaper  was able to bring the ecosystem together around mobility data.

However, even when organisation is fully digital, and license issues are overcome, there are issues around how the data is managed stored, accessed. The discoverability of the data and the recording of its provenance are too often neglected in the process of digtial transformation. Further, once an organisation has gone through digital transformation, they begin making predictions around the data. These predictions are data themselves, and their presence in the data ecosystem needs recording. Automating this portion requires structured thinking around our data ecosystems.

## Assess

Understanding what is in the data. Is it what it's purported to be, how are missing values encoded, what are the outliers, what does each variable represent and how is it encoded.

Data that is accessible can be imported (via APIs or database calls or reading a CSV) into the machine and work can be done understanding the nature of the data. The important thing to say about the assess aspect is that it only includes things you can do *without* the question in mind. This runs counter to many ideas about how we do data analytics. The history of statistics was that we think of the question *before* we collect data. But that was because data was expensive, and it needed to be excplicitly collected. The same mantra is true today of *surveillance data*. But the new challenge is around *happenstance data*, data that is cheaply available but may be of poor quality. The nature of the data needs to be understood before its integrated into analysis. Unfortunately, because the work is conflated with other aspects, decisions are sometimes made during assessment (for example approaches to imputing missing values) which may be useful in one context, but are useless in others. So the aim in *assess* is to only do work that is repeatable, and make that work available to others who may also want to use the data.

## Address

The final aspect of the process is to *address* the question. We'll spend the least time on this aspect here, because it's the one that is most widely formally taught and the one that most researchers are familiar with. In statistics, this might involve some confirmatory data analysis. In machine learning it may involve designing a predictive model. In many domains it will involve figuring out how best to visualise the data to present it to those who need to make the decisions. That could involve a dashboard, a plot or even summarisation in an Excel spreadsheet.

## Using the Framework

### Template Implementation
The framework is provided as a template with stub implementations. Each module contains:

- *`access.py`*: Implement the `data()` function to load your data sources
- *`assess.py`*: Implement data quality assessment functions (`data()`, `query()`, `view()`, `labelled()`)
- *`address.py`*: Implement analysis and question-addressing functionality

### Error Handling and Logging

The framework includes basic error handling and logging to help you debug issues:

**Basic Error Handling:**
```python
try:
    df = pd.read_csv('data.csv')
    print(f"Loaded {len(df)} rows of data")
except FileNotFoundError:
    print("Error: Could not find data.csv file")
    return None
```

**Simple Logging:**
```python
import logging
logger = logging.getLogger(__name__)
logger.info("Starting data analysis")
logger.error("Failed to load data")
```

**Key Principles:**
- Use try/except blocks for operations that might fail
- Provide helpful error messages for debugging
- Log important events and errors
- Check data validity before processing
- Handle edge cases (empty data, missing files, etc.)

### Configuration
- Edit `fynesse/defaults.yml` for default configuration values
- Create `fynesse/machine.yml` for machine-specific settings
- Use `_config.yml` for project-specific configuration

### Testing
The template includes comprehensive test stubs:
```bash
# Run all tests
poetry run pytest

# Run specific module tests
poetry run pytest fynesse/tests/test_access.py

# Run with coverage
poetry run pytest --cov=fynesse
```

## Contributing

### Development Setup
1. Fork the repository
2. Install Poetry: `curl -sSL https://install.python-poetry.org | python3 -`
3. Install dependencies: `poetry install --with dev`
4. Create a feature branch: `git checkout -b feature/your-feature`

### Code Quality
- All code must pass tests: `poetry run pytest`
- Code must be formatted: `poetry run black fynesse/`
- Type checking must pass: `poetry run mypy fynesse/`
- Linting must pass: `poetry run flake8 fynesse/`

### Commit Guidelines
- Use conventional commit messages
- Include tests for new functionality
- Update documentation as needed

## License

MIT License - see LICENSE file for details.
