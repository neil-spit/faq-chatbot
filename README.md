# FAQ Chatbot CLI Application

This project is an FAQ chatbot built with FastAPI. It provides an interactive API that can be used to retrieve answers from a predefined dataset of FAQs. The backend is served by FastAPI, and you can interact with the API via Swagger UI provided by FastAPI.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setting Up the Environment](#setting-up-the-environment)
  - [Clone the Repository](#clone-the-repository)
  - [Configure the OpenAI API Key](#configure-the-openai-api-key)
  - [Build and Start Docker Containers](#build-and-start-docker-containers)
  - [Access Swagger UI](#access-swagger-ui)
- [Common Issues and Troubleshooting](#common-issues-and-troubleshooting)
- [License](#license)

## Prerequisites

Before you start, make sure you have the following software installed on your machine:

- **Docker Desktop**: Ensure Docker Desktop is installed and running on your machine. [Download Docker Desktop](https://www.docker.com/products/docker-desktop).

## Setting Up the Environment

Begin by cloning the repository to your local machine:

git clone https://github.com/your-username/faq-chatbot.git
cd faq-chatbot

Next, configure your OpenAI API key. Open the .env file in the root of your project directory and update the OPENAI_API_KEY variable with your actual API key. For example:

OPENAI_API_KEY=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
With the configuration in place, build and start the Docker containers. Use Docker Compose to handle the setup:

docker-compose build
docker-compose up
This will build the Docker image according to the Dockerfile and start the container as specified in the docker-compose.yml file.

Once the containers are running, you can access the Swagger UI to interact with the API. Open a web browser and navigate to:

http://localhost:8000/docs
Swagger UI provides an interactive interface for testing the API endpoints. You can explore available endpoints, test them, and view the responses directly in your browser.

## Common Issues and Troubleshooting
If you encounter an error like "App failed to load" when running the FastAPI API, make sure that:

The main.py file has the correct structure and includes the FastAPI app instance.
The .env file is correctly configured with the OpenAI API key.
All dependencies are correctly specified in the requirements.txt.
For Docker issues such as ports already in use, ensure that no other services are running on port 8000. You may also specify a different port in the docker-compose.yml file or adjust the docker run command if necessary.

## License
This project is licensed under the MIT License - see the LICENSE file for details.