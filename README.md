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

`git clone https://github.com/your-username/faq-chatbot.git`
`cd faq-chatbot`

### 2\. Set Up a Python Virtual Environment

It's a good practice to create a virtual environment to isolate your project dependencies. You can do this with the following commands:

`python3 -m venv venv`

Activate the virtual environment:

-   **On Windows:**

    `.\venv\Scripts\activate`

-   **On macOS/Linux:**

    `source venv/bin/activate`

### 3\. Install Dependencies

Once the virtual environment is activated, install the required Python packages:

`pip install -r requirements.txt`

### 4\. Run the Backend API

Run the FastAPI application that will serve the backend API:

`uvicorn main:app --reload --host 0.0.0.0 --port 8000`

By default, the application will start on `http://127.0.0.1:8000`. This URL will serve as the API endpoint for your CLI.

### 5\. Run the CLI Application

In a separate terminal, while the FastAPI API is running, execute the CLI:

`python cli_app.py`

You can now enter queries directly into the terminal. The CLI will send requests to the FastAPI API and display the responses.

Using Docker
------------

If you prefer to run the application inside a Docker container, follow these steps:

### 1\. Building the Docker Image

Ensure that Docker Desktop is running, then build the Docker image with the following command:

`docker build -t faq-chatbot-faq-backend .`

### 2\. Running the Docker Container

Run the Docker container with the following command:

`docker run -p 8000:8000 faq-chatbot-faq-backend`

The application will now be accessible at `http://127.0.0.1:8000`.

To interact with the API via CLI, modify the `API_URL` in `cli_app.py` to:


`API_URL = "http://localhost:8000/faq/"`

Then run the CLI as usual:

`python cli_app.py`

Common Issues and Troubleshooting
---------------------------------

### FastAPI App Not Found

If you encounter an error like `App failed to load` when running the FastAPI API, ensure that:

-   The `main.py` file has the correct structure and includes the FastAPI `app` instance.
-   All dependencies are correctly installed in your virtual environment.

### Docker Issues

If you run into Docker issues such as ports already in use, ensure that no other services are running on port `8000`, or specify a different port in the `docker run` command.