# FAQ Chatbot

This project is an FAQ chatbot built with FastAPI. The chatbot responds to user queries based on a predefined set of FAQs. The application is containerized using Docker, making it easy to set up and run.

## Prerequisites

Before setting up the project, ensure that you have the following software installed:

- **Docker Desktop**: Required for building and running the application containers. [Download Docker Desktop](https://www.docker.com/products/docker-desktop).
- **Python 3.9+**
- **Git**: To clone the project repository. [Download Git](https://git-scm.com/downloads).

## Setup and Run

Clone the repository to your local machine:

```git clone https://github.com/neil-spit/faq-chatbot.git faq```

```cd faq```

Configure your OpenAI API key:

- Open the docker-compose.yml file in the root of your project directory.

- Locate the environment section under the faq-backend service.

- Replace the placeholder with your actual OpenAI API key. 

In the terminal, build and start the Docker containers using Docker Compose:

```docker-compose up --build```

This will build the Docker image and start the container as specified in the docker-compose.yml file.

Once the containers are running, you can access the web-based frontend by opening a web browser and navigating to:

```http://localhost:8001```

You can ask questions in the chat interface, and the bot will respond based on the FAQs loaded in the backend.

## Additional Notes

The API documentation is available via Swagger UI at http://localhost:8000/docs.

If you need to modify the chatbot's behavior or the FAQ dataset, you can update the relevant files and restart the application.
