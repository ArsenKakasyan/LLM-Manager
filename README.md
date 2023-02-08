# LLM Manager


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) [![MIT Licence](https://badges.frapsoft.com/os/mit/mit-125x28.png?v=103)](https://opensource.org/licenses/mit-license.php) [![Open Source Love](https://badges.frapsoft.com/os/v3/open-source-175x29.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

## Project Description

LLM Manager is a chatbot application designed for managing language models from OpenAI. It allows users to choose their own language model and use their own API key with the limits defined by them. The application also stores request history in the form of JSON files for future reference.

This project was built using Python and its various libraries such as Tkinter for GUI, filedialog for file management, and OpenAI API for language model interactions.

Some of the challenges faced while building this project were integrating the OpenAI API and ensuring its smooth functioning within the Tkinter interface. In the future, we hope to implement advanced features such as real-time updates on API key usage, better file management options, and improved GUI design.
## How to Install and Run the Project

1. Clone the repository to your local machine
2. Install the required packages mentioned in the requirements.txt file

```sh
pip install -r requirements.txt
```

3. Run the llm_manager.py file
```sh
python llm_manager.py
```
## How to Use the Project

1. The main interface of the LLM Manager contains two options - 'File' and 'Key'.
        - Under the 'File' option, you can select a JSON file or create a new one.
        - Under the 'Key' option, you can add an API key environment variable.
2. To add an API key, select the 'Key' option and click on 'ENV'. A file dialog will appear, select the API key file and set it as an environment variable.
3. To select a JSON file or create a new one, select the 'File' option and click on 'JSON'. A file dialog will appear, select the existing JSON file or create a new one by specifying its name and location.

## License

MIT
