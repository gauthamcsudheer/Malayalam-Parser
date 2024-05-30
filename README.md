# Malayalam Parser Project

This project aims to parse Malayalam text from user input or CSV files, performing Named Entity Recognition (NER), Part-of-Speech (POS) tagging, and sentiment analysis. The project addresses the scarcity of annotated datasets in the Malayalam language for NLP applications.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Malayalam Parser Project is designed to process Malayalam / English text data, providing functionalities such as:
- Named Entity Recognition (NER)
- Part-of-Speech (POS) tagging
- Sentiment analysis

This project leverages NLP techniques and tools to generate annotated datasets, facilitating further research and development in Malayalam language processing.

## Features

- **NER**: Identifies and classifies entities in the text.
- **POS Tagging**: Tags each word with its corresponding part of speech.
- **Sentiment Analysis**: Determines the sentiment conveyed in the text.
- **Dataset Creation**: Allows the users to download the proccessed datasets till done.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/malayalam-parser.git
    cd malayalam-parser
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations and start the Django development server:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

## Usage

1. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

2. Open your web browser and navigate to `http://127.0.0.1:8000`.

3. Enter the text to be parsed into the input field on the website.

4. The system will process the text, performing NER, POS tagging, and sentiment analysis.

5. The results will be displayed in a tabulated format on the website.

6. You can also download the processed CSV file with the annotated data.

## File Structure

- `views.py`: Contains the logic for handling file uploads and processing text data.
- `finalReport.pdf`: Documentation detailing the project's objectives, methodologies, and results.
- `requirements.txt`: Lists the Python dependencies needed for the project.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add feature: description"
    ```
4. Push to the branch:
    ```bash
    git push origin feature/your-feature-name
    ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
