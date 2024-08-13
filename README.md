<a href="#readme-top"></a>
# Testing using Selenium

## Tech Stack
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Google Chrome](https://img.shields.io/badge/Google%20Chrome-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white)
![Firefox](https://img.shields.io/badge/Firefox-FF7139?style=for-the-badge&logo=Firefox-Browser&logoColor=white)

## Overview
This project provides a suite of automated tests using Python and Selenium WebDriver. These tests are designed to ensure the functionality and reliability of web applications through automated browser interactions.
The goal is to perform basic tests on the github and amazon websites.

For the Amazon website, we perform automated testing on the Chrome browser and test for the following functionalities:
<ol>
  <li>Load the webpage.</li>
  <li>Product search for empty, valid and invalid queries.</li>
  <li>Check for "Today's Deals" tab.</li>
</ol>

For the Github website, we perform automated testing on Mozilla Firefox browser and test for the following three functionalities:
<ol>
  <li>Github login.</li>
  <li>Github Search for empty, valid and invalid queries.</li>
  <li>Watch repository.</li>
</ol>


### Installation

1. Download the Chrome and Firefox drivers from the following links:
   <br>
        i. Chrome Driver: [https://developer.chrome.com/docs/chromedriver/downloads](https://developer.chrome.com/docs/chromedriver/downloads)
   <br>
       ii.  Firefox Driver: [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)

2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```

3. Install required packages
   ```sh
   pip install -r requirements.txt
   ```
   
<p align="right">(<a href="#readme-top">back to top</a>)</p>

