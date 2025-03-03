# README

## Project Overview

This project is a Requirement Quality Analyzer tool, designed to evaluate the quality of business requirements based on clarity, completeness, testability, feasibility, relevance, and acceptance criteria.

## Features

* Analyzes user stories for quality and adherence to best practices
* Evaluates requirements based on clarity, completeness, testability, feasibility, relevance, and acceptance criteria
* Provides a structured assessment, scoring each criterion from 1 (Poor) to 5 (Excellent)
* Includes a summary of strengths and weaknesses and suggests improvements

## Technology Stack

* Flask web framework
* Infisical SDK for secret management
* Google GenAI for natural language processing
* Bootstrap for front-end styling

## Getting Started

1. Clone the repository: `git clone https://github.com/DouglasOttoDavila/requirements-reviewer.git`
2. Create a new file named `.env` in the root directory of the project
3. Add the following environment variables to the `.env` file: 
```
INFISICAL_APP_BASE_URL="https://app.infisical.com"
INFISICAL_CLIENT_ID=your-infisical-client-id
INFISICAL_CLIENT_SECRET=your-infisical-client-secret
INFISICAL_PROJECT_ID=your-infisical-project-id
GEMINI_API_KEY=your-gemini-api-key
```
**Note**: Infisical secrets are only necessary if config/configuration.py
4. Replace the placeholders with the actual values of your Gemini API key (and Infisical keys if decided to use it).
5. Update the .env file (GEMINI_API_KEY is mandatory, other keys are need if using Infisical vault)
6. Install dependencies: `pip install -r requirements.txt`
7. Run the application: `python app.py`

## API Endpoints

* `/review_requirements`: Returns a rendered template for reviewing requirements
* `/api/analyze`: Analyzes a user story and returns a JSON response with the evaluation results

## Configuration

* [config/configuration.py](cci:7://file:///d:/GitHub/requirements-reviewer/config/configuration.py:0:0-0:0): Contains configuration settings for the application, including API keys and secret management settings

## Contributing

Contributions are welcome! Please submit a pull request with your changes and a brief description of what you've added or fixed.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
