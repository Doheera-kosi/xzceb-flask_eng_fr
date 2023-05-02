<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Built With](#built-with)
  - [🚀 Live Demo](#live-demo)
- [💻 Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
  - [Usage](#usage)
  - [Run tests](#run-tests)
  - [Deployment](#deployment)
- [👥 Authors](#authors)
- [🔭 Future Features](#future-features)

## 📖 About the Project <a name = "about-project"></a>

This project aims to create functions that translate English to French and French to English by utilizing IBM Watson APIs. 

### 🛠 Built With <a name = "built-with"></a>

#### Tech Stack

- Python
- Flask

#### Key Features

- Translate English to French
- Translate French to English
- Run unit tests
- Check code against Python coding standards
- Package functions and tests as a standard Python package

### 🚀 Live Demo <a name = "live-demo"></a>

This project is not currently deployed on a live demo.

# 💻 Getting Started

## Setup

1. Clone the repository
   ```sh
   git clone <paste_your_repo_name>
   ```
2. Change to the final_project folder
   ```sh
   cd xzceb-flask_eng_fr/final_project
   ```
3. Create folder named machinetranslation and change to that directory
   ```sh
   mkdir machinetranslation
   cd machinetranslation
   ```
4. Create a virtual environment and activate it
   ```sh
   python3 -m venv myenv
   source myenv/bin/activate
   ```
5. Install dependencies
   ```sh
   python3 -m pip install python-dotenv
   python3 -m pip install ibm_watson
   python3 -m pip install Flask
   ```

## Prerequisites

Before running the project, you should have the following:

- An instance of the Watson Language Translator service provisioned on IBM Cloud.
- API key and URL of the Watson Language Translator service.

## Usage

To run the project:

1. Set the environment variables for the API key and URL. Create a file `.env` under the `machinetranslation` directory, and set the `apikey` and `url` variables with the API key and URL of the Watson Language Translator service, respectively.
   ```
   apikey=<your-api-key>
   url=<your-url>
   ```
2. Change to the `machinetranslation` directory
   ```
   cd machinetranslation
   ```
3. Start the server
   ```
   python3 server.py
   ```
4. Open your web browser and go to `http://localhost:5000`

## Run tests

To run the tests:

1. Change to the `final_project` directory
   ```
   cd xzceb-flask_eng_fr/final_project
   ```
2. Run the tests
   ```
   python3 tests.py
   ```

## Deployment

To deploy the application on IBM Code Engine:

1. Follow the instructions [here](https://cloud.ibm.com/docs/codeengine?topic=codeengine-getting-started) to set up your IBM Cloud account and create an IBM Code Engine project.
2. Build a container image of the application using the following command:
   ```
   ibmcloud ce build --name <your-image-name> --context . --no-cache
   ```
3. Deploy the application on IBM Code Engine using the following command:
   ```
   ibmcloud ce app create --name <your-app-name> --image <your-image-name> --port 8080
   ```
4. Get the URL of the application using the following command:
   ```
   ibmcloud ce app show --name <your-app-name>
   ``` 

# 👥 Authors

- [Your Name](https://github.com/your_username)

# 🔭 Future Features

- Support for more languages.