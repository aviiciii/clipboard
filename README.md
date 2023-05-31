# clipboard

A simple website for storing and retrieving text data.

The website utilizes the fetch API to interact with a Flask API hosted on Azure Web Apps. The Flask API is responsible for communicating with the Google Firebase Realtime Database to retrieve and update data.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The clipboard website provides a convenient way to store and access text data. It leverages the power of a Flask API hosted on Azure Web Apps and integrates with the Google Firebase Realtime Database for seamless data management.

## Features

- Store and retrieve text data easily.
- Seamless integration with Google Firebase Realtime Database.
- Fast and responsive user interface.

## Installation

To set up the clipboard website locally, follow these steps:

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Deploy the Flask API on Azure Webapps.
4. Create a Google Firebase Realtime Database.
5. Configure the Flask API to communicate with your Google Firebase Realtime Database. Refer to the Flask and Firebase documentation for more information.
6. Start the Flask server using `python app.py`.

## Usage

1. Access the clipboard website by navigating to the appropriate URL.
2. Use the provided text input field to enter your desired text data.
3. Click the "Save" button to store the text data in the database.
4. To retrieve the stored text data, click the "Get" button.
5. The retrieved text data will be displayed on the website.

## Contributing

Contributions to the clipboard project are welcome! If you would like to contribute, please follow these steps:

1. Raise an issue over at issues tab and report to the developer
2. Fork the repository and create a new branch for your feature or bug fix.
3. Commit your changes with descriptive commit messages.
4. Push your branch to your forked repository.
5. Submit a pull request, detailing your changes and their benefits.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

