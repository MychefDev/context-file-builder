# Context builder

This project is a Python client that connects to the MyChef API to retrieve a set of frequently asked questions (FAQs) along with their answers. The data is saved in a text file called `COMMON_QUESTIONS.txt` in a specified format for easy reading and use.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)

## Requirements

- Python 3.6 or higher
- A valid MyChef API token
- A `.env` file containing the API authentication token

## Installation
1. Install the necessary dependencies. It’s recommended to do this in a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

2. Create a `.env` file in the project root to store your API authentication token:

    ```
    BEARER_TOKEN=your_authentication_token
    ```

## Configuration

Ensure that the `.env` file contains a variable called `BEARER_TOKEN` that holds your API access token. This token will be used in the authorization header to make the request.

## Usage

Run the script with the following command:

```bash
python context_builder.py
```

## License

This project is licensed under the MIT License.