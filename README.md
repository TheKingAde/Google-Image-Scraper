# Google Image Scraper
## Overview
The Google Image Scraper is a web application that allows users to search for images on Google, view the results, and download the selected images in a ZIP file. The application leverages the SerpApi for fetching image results from Google and provides an easy-to-use interface for users to input their search queries and advanced options.

## Features
Search for Images: Enter a query to search for images on Google.
Advanced Options: Customize the number of images to fetch and the image format.
View Results: Display the fetched images on the web page.
Download Images: Download the selected images in a ZIP file.
Responsive Design: The application is designed to work on various screen sizes.

## Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Flask, Python
API: SerpApi for Google Image Search
Libraries: jszip, FileSaver.js
Styling: Custom CSS
Setup and Installation
Prerequisites
Python 3.x
Flask
Requests
SerpApi API Key
Installation
Clone the repository:

<code>
git clone https://github.com/your-username/google-image-scraper.git
</code>

<code>
cd google-image-scraper
</code>

Install the dependencies:

<code>pip install flask requests flask-cors</code>

Set up the API key:

Replace YOUR API KEY in the backend.py file with your actual SerpApi API key.
Running the Application
Start the Flask server:

<code>python app.py<code>

Open the application:

Navigate to http://localhost:5005 in your web browser.

## Usage
### Search for Images:

Enter a search query in the input field and click the "Search" button.

### Advanced Options:

Click the "Advanced Options" button to set the image quantity and format.

### View Results:

The images will be displayed below the search bar.

### Download Images:

Click the "Download Images" button to download the selected images as a ZIP file.
## Project Structure
app.py: The main Flask application file.
backend.py: Contains the function for scraping Google images using SerpApi.
templates/index.html: The main HTML file for the web interface.
static/css/style.css: The CSS file for styling the web interface.
static/js/scripts.js: The JavaScript file for handling frontend interactions.

## Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.

## Acknowledgements
SerpApi for providing the Google Image Search API.
Flask for the web framework.
