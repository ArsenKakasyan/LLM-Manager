# LLM-Manager
LLM Manager

A language model management tool for OpenAI API users.
Project Description

This application allows users to manage their API keys and language models from OpenAI API in an organized and efficient way.

With the ability to choose your own language model and using your own API key, you have full control over your API limits. The application also keeps a record of your requests in JSON files for easy reference in the future.

This project was developed using Python and its standard libraries, including Tkinter for GUI.

Some of the challenges faced during the development of this project include handling the API key securely and efficiently processing the selected language model.

There is potential for future implementation of additional features, such as the ability to save custom configurations and integration with other API services.
How to Install and Run the Project

    Clone the repository to your local machine.
    Make sure you have Python 3 installed on your system.
    Navigate to the cloned repository using the command line.
    Install the required libraries using the following command:

pip install -r requirements.txt

Run the following command to start the application:

    python llm_manager.py

How to Use the Project

    Upon launching the application, you will be presented with the main window.
    Go to the "File" menu and select either "JSON" or "ENV" to access their respective functions.
        JSON: Select a JSON file or create a new one in your local directory.
        ENV: Add an API key as an environment variable on your system.
    After adding the API key, you can proceed to use the selected language model.

License

This project is licensed under the MIT license.
Badges

License: MIT

<style>
body {
    font-family: Arial, sans-serif;
    font-size: 14px;
    line-height: 1.5;
}

h1, h2, h3 {
    font-weight: bold;
}

h1 {
    font-size: 36px;
    margin-bottom: 20px;
}

h2 {
    font-size: 24px;
    margin-bottom: 20px;
}

h3 {
    font-size: 18px;
    margin-bottom: 10px;
}

code {
    font-family: monospace;
    background-color: #f9f9f9;
    padding: 2px 5px;
    border-radius: 5px;
}

pre {
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 5px;
}

ul {
    margin-bottom: 20px;
    list-style-type: square;
}

li {
    margin-bottom: 10px;
}
</style>
