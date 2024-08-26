# FastAPI Scraping Project

This project is a FastAPI application that scrapes GitHub repositories for a given username and returns the repository details including the project link.

## Features

- Scrapes GitHub repositories for a given username
- Returns repository details including name, description, language, and link
- Exports repository data to a CSV file

## Requirements

- Python 3.7+
- `pip` (Python package installer)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment**:
    ```sh
    mkdir env
    python3 -m venv env
    ```

3. **Activate the virtual environment**:
    - On macOS and Linux:
        ```sh
        source env/bin/activate
        ```
    - On Windows:
        ```sh
        .\env\Scripts\activate
        ```

4. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the FastAPI application**:
    ```sh
    uvicorn main:app --reload
    ```

2. **Access the API**:
    Open your browser and go to `http://127.0.0.1:8000`.

3. **Scrape GitHub repositories**:
    - Send a POST request to `/scrape` with a JSON payload containing the GitHub username.
    - Example using `curl`:
        ```sh
        curl -X POST "http://127.0.0.1:8000/scrape" -H "Content-Type: application/json" -d '{"username": "octocat"}'
        ```

4. **View the scraped data**:
    The API will return a JSON response with the repository details.

## Example

Here is an example of how to use the API:

1. **Start the server**:
    ```sh
    uvicorn main:app --reload
    ```

2. **Send a POST request**:
    ```sh
    curl -X POST "http://127.0.0.1:8000/scrape" -H "Content-Type: application/json" -d '{"username": "octocat"}'
    ```

3. **Response**:
    ```json
    {
        "repositories": [
            {
                "name": "Hello-World",
                "description": "My first repository on GitHub!",
                "language": "Python",
                "link": "https://github.com/octocat/Hello-World"
            },
            ...
        ]
    }
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.