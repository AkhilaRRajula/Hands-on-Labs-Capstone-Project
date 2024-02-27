# -*- coding: utf-8 -*-
"""Web-Scraping-Lab_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CKBHwdrZuiuXGNK6DCP9kmLTqsg0HH7u

# **Hands-on Lab : Web Scraping**

Estimated time needed: **30 to 45** minutes

## Objectives

In this lab you will perform the following:

* Extract information from a given web site
* Write the scraped data into a csv file.

## Extract information from the given web site
You will extract the data from the below web site: <br>
"""

#this url contains the data you need to scrape
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"

"""The data you need to scrape is the **name of the programming language** and **average annual salary**.<br> It is a good idea to open the url in your web broswer and study the contents of the web page before you start to scrape.

Import the required libraries
"""

# Your code here
import requests
from bs4 import BeautifulSoup

"""Download the webpage at the url

"""

# Download the webpage at the url
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the webpage content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all table rows
    rows = soup.find_all('tr')

    # Initialize lists to store programming languages and average annual salaries
    languages = []
    salaries = []

    # Loop through each row and extract data
    for row in rows[1:]:  # Skipping the header row
        cols = row.find_all('td')
        language = cols[1].text.strip()
        salary = cols[3].text.strip()

        languages.append(language)
        salaries.append(salary)

    # Print the extracted data
    for language, salary in zip(languages, salaries):
        print(f"Programming Language: {language}, Average Annual Salary: {salary}")
else:
    print("Failed to retrieve the webpage")

"""Create a soup object

"""

from bs4 import BeautifulSoup

# Assuming 'response' contains the downloaded webpage content
soup = BeautifulSoup(response.content, 'html.parser')

# Now 'soup' is the BeautifulSoup object representing the webpage content

"""Scrape the `Language name` and `annual average salary`.

"""

# Find all table rows
rows = soup.find_all('tr')

# Initialize lists to store programming languages and average annual salaries
languages = []
salaries = []

# Loop through each row and extract data
for row in rows[1:]:  # Skipping the header row
    cols = row.find_all('td')
    language = cols[1].text.strip()
    salary = cols[3].text.strip()

    languages.append(language)
    salaries.append(salary)

# Print the extracted data
for language, salary in zip(languages, salaries):
    print(f"Language: {language}, Average Annual Salary: {salary}")

"""Save the scrapped data into a file named *popular-languages.csv*

"""

import csv

# Open the CSV file in write mode
with open('popular-languages.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['Language', 'Average Annual Salary'])

    # Write the data rows
    for language, salary in zip(languages, salaries):
        writer.writerow([language, salary])

print("Data saved successfully to popular-languages.csv")

# List the files in the current directory
import os
os.listdir('.')