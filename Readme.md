# Sentiment Analysis with Flask
This project is an example of creating a Python-based web application using Flask to perform sentiment analysis on user-inputted text. The sentiment analysis is done by calling an external API that uses a pre-trained machine learning model.

## Getting Started
These instructions will help you set up and run the project on your local machine.


## Prerequisites
You will need Python 3.x and pip installed on your machine.


## Installing Dependencies
To install the required dependencies, navigate to the project root directory and run:

```
pip install -r requirements.txt.
```

This command will install the necessary packages, such as Flask and python-dotenv.


## Configuration
Create a .env file in the root directory of your project to store your API key:

```
API_KEY=your_api_key_here
```

Replace your_api_key_here with your actual API key.


## Running the Application
To run the application, navigate to the project root directory and run:

```
python app.py
```

The application will start on the default address: http://127.0.0.1:5000/. Open this URL in your web browser to access the web application.


## Usage
Enter the text you want to analyze in the input field.
Click the "Analyze Sentiment" button.
The application will display the sentiment of the text as either "POSITIVE" or "NEGATIVE".


## Project Structure
`app.py`: The main file for the Flask application.
`config.py`: Configuration settings, such as the API key and model URL.
`sentiment_analysis.py`: Handles sentiment analysis by calling the external API.
`templates/index.html`: HTML template for the main page of the web application.
`requirements.txt`: A list of required Python packages.
`.env`: A file to store environment variables (not included in the repository; you need to create it yourself).
`.gitignore`: A file specifying which files and directories to ignore in the Git repository.


## License
This project is open-source and available under the MIT License.