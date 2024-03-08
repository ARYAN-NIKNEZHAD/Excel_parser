# Installation Guide

This guide provides instructions for installing the required packages for the project.

## Prerequisites

Before proceeding, ensure that you have the following prerequisites:

- [Virtual Environment (venv)](env.md): Install and activate a virtual environment on your system. This helps isolate project dependencies and avoid conflicts with other Python projects.

## Installation Steps

Follow these steps to install the required packages:

### 1. Development Environment

If you are setting up a development environment, run the following command to install the development dependencies:

```bash
pip install -r packages/development/requirements.txt
```

This command will install all the packages listed in the requirements.txt file located in the packages/development directory.


### 2. Production Environment

If you are setting up a production environment, run the following command to install the production dependencies:

```bash
pip install -r packages/production/requirements.txt
```

This command will install all the packages listed in the requirements.txt file located in the `packages/production` directory.


By following these steps, you will have all the necessary packages installed and ready for your project.