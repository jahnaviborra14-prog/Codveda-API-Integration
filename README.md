# API Integration using Python

## Project Overview

This project demonstrates how to integrate an external REST API with Python using the `requests` library. The program sends a GET request to a public API, retrieves JSON data, processes the response, and displays selected information in a readable format.

## Objective

The objective of this project is to understand the basic concepts of API integration in Python, including:

- Sending HTTP GET requests
- Receiving JSON data from an API
- Processing API responses
- Displaying useful information
- Handling API connection errors

## API Used

**JSONPlaceholder**

API Endpoint:

`https://jsonplaceholder.typicode.com/posts`

JSONPlaceholder is a free online REST API used for testing and development.

## Technologies Used

- Python
- Requests
- REST API
- JSON

## Project Structure

```text
Level_2_API_Integration/
│
├── api_integration.py
├── requirements.txt
└── README.md
```

## How It Works

1. The program defines the API endpoint.
2. Python sends a GET request using the `requests` library.
3. The API returns data in JSON format.
4. The JSON response is converted into Python data.
5. The program displays the total number of posts received.
6. The first five posts are displayed with their ID, title, and body.
7. Request errors are handled using exception handling.

## Installation

Install the required dependency using:

```bash
pip install -r requirements.txt
```

## Running the Project

Run the following command:

```bash
python api_integration.py
```

## Sample Output

```text
API Integration Project Started!
Total posts received: 100

Post ID: 1
Title: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
Body: quia et suscipit
...
```

## Features

- REST API integration
- JSON response handling
- Error handling
- Simple and readable Python implementation
- External API data retrieval

## Learning Outcome

Through this project, I learned how to connect Python applications with external APIs, retrieve JSON data, process API responses, and handle request-related errors.

## Internship Task

This project was developed as part of the **Codveda Python Development Internship – Level 2**.