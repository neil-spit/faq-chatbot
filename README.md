`# FAQ Chatbot CLI Application

This is a simple FAQ chatbot application built with FastAPI, but it interacts via a Command-Line Interface (CLI). Users can input questions, and the application will respond with answers based on a predefined dataset of FAQs. The backend is served by FastAPI, while the CLI uses HTTP requests to communicate with the FastAPI API.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setting Up the Environment](#setting-up-the-environment)
 - [1\. Clone the Repository](#1-clone-the-repository)
 - [2\. Set Up a Python Virtual Environment](#2-set-up-a-python-virtual-environment)
 - [3\. Install Dependencies](#3-install-dependencies)
 - [4\. Run the Backend API](#4-run-the-backend-api)
 - [5\. Run the CLI Application](#5-run-the-cli-application)
- [Using Docker](#using-docker)
 - [1\. Building the Docker Image](#1-building-the-docker-image)
 - [2\. Running the Docker Container](#2-running-the-docker-container)
- [Common Issues and Troubleshooting](#common-issues-and-troubleshooting)
- [License](#license)

## Prerequisites

Before you start, make sure you have the following software installed on your machine:

- [Python 3.10+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop) (for Docker setup)

## Setting Up the Environment

### 1. Clone the Repository

First, clone the repository to your local machine using the following command:

`git clone https://github.com/neil-spit/faq-chatbot.git`

`cd faq-chatbot`

### 2\. Set Up a Python Virtual Environment

It's good practice to create a virtual environment to isolate project dependencies. You can do this with the following commands:

`python3 -m venv venv`

Activate the virtual environment:

-   **On Windows:**

    `.\venv\Scripts\activate`

-   **On macOS/Linux:**

    `source venv/bin/activate`

### 3\. 

Once the virtual environment is activated, run Docker Desktop. Then, build and run the containers in the terminal on VSCode:

`docker-compose up --build`

### 4\. Running the CLI

Open a new terminal and run the cli_app.py file:

`python cli_app.py`

Common Issues and Troubleshooting
---------------------------------

### FastAPI App Not Found

If you encounter an error like `App failed to load` when running the FastAPI API, ensure that:

-   The `main.py` file has the correct structure and includes the FastAPI `app` instance.
-   All dependencies are correctly installed in your virtual environment.

### Docker Issues

If you run into Docker issues such as ports already in use, ensure that no other services are running on port `8000`, or specify a different port in the `docker run` command.