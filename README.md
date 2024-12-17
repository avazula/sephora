# sephora
Python web app for testing AWS Cognito integration

## Prerequisites

This project uses Micromamba to create a virtual environment and install all dependencies.
Get micromamba from the [official page](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html).

Once micromamba is set up open a terminal at the root of the project and run `direnv allow` to install the project dependencies.

To spin up the server:

```bash
cd src
python app.py
```

or use the Just command:
```bash
just server::launch
```

## Utilities

- Run `just setup` to install and configure pre-commit checks for the project
