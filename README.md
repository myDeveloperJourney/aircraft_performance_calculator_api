# Aircraft Performance Calculator

Welcome to the Aircraft Performance Calculator project! This application uses FastAPI and Swagger UI to allow users to calculate the performance of an aircraft.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Aircraft Performance Calculator is a web application that provides users with the ability to calculate various performance metrics of an aircraft. The application is built using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.10 based on standard Python type hints. Swagger UI is integrated to provide a user-friendly interface for interacting with the API.

## Features

- Interactive API documentation with Swagger UI.
- High-performance and an easy-to-use API endpoint.

## Installation

This application has been dockerized for easy deployment. To run the application, follow these steps:

1. Clone the repository:

2. Change into the project directory:

```bash
cd aircraft-performance-calculator
```

3. Build the Docker image:

```bash
docker build -t aircraft-performance-calculator .
```

4. Run the Docker container:

```bash
docker run -d -p 8000:8000 aircraft-performance-calculator
```

5. Access the Swagger UI by navigating to `http://localhost:8000/docs`.



## Usage

COMING SOON

## API Endpoints

Here are some of the key API endpoints available in the Aircraft Performance Calculator:

- `GET /calculate`: Provides data regarding various performance metric based on pre-determined values.
.

## Contributing

We welcome contributions to the Aircraft Performance Calculator project! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push the branch to your fork.
4. Create a pull request with a detailed description of your changes.

## License

TBD