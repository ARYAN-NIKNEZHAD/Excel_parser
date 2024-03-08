# Running the Django Project Excel Parser

This guide provides step-by-step instructions for running the Django Project Excel Parser.

## Prerequisites

Ensure that the following prerequisites are met before proceeding:

- [Python](installation.md): Make sure Python is installed on your system. Refer to the installation documentation for detailed instructions.

- [Virtual Environment (venv)](env.md): Install and activate a virtual environment on your system. Refer to the environment setup documentation for guidance.

## Step-by-Step Guide

### 1. Install PostgreSQL

First, you need to install PostgreSQL on your system or run it with Docker.


### 2. Create PostgreSQL database

connect to your database through the pgadmin or any other application and then run this command

```bash
CREATE DATABASE your_database_name;
```
This command creates a database using SQL.


### 3. Create a .env file

In the project's root directory, create a `.env` file and store important environment variables in it.

### 4. Make Migrations
Run the following command to generate migration files in the project directory:
```bash
python manage.py makemigrations
```
This command creates migration files based on the changes you've made to your models.

### 5. Apply Migrations
Run the following command to apply migrations and create database tables in the PostgreSQL database:
```bash
python manage.py migrate
```
This command synchronizes the database state with the current set of models and migrations.

### 6. Run server
Start the development server by running the following command:
```bash
python manage.py runserver
```

This command launches the Django development server on the default port `8000`. If DEBUG is set to `True` in your settings, the server runs in development mode; if DEBUG is set to `False`, it runs in production mode.


