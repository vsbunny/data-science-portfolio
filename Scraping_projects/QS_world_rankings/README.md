# QS World University Rankings Scraper & Data Wrangling

[![Python Version](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](../../../LICENSE) ## Description

This project showcases a data acquisition and processing pipeline for QS World University Rankings. It utilises the powerful Scrapy framework integrated with Selenium for extracting data from dynamic web pages, followed by data wrangling using Pandas to clean, standardize, and organize the scraped information. This project addresses common challenges in web scraping, such as handling dynamic content and organizing varied output data.

## Project Structure
```
.
├── README.md                           <- This file
├── QS_World_Rankings_Scraper.ipynb     <- Jupyter Notebook containing the Scrapy spider for rankings extraction
├── QS_wrangling.ipynb                  <- Jupyter Notebook for data wrangling, cleaning, and combining scraped data
├── requirements.txt                    <- Python dependencies for this project
└── csv_rankings/                       <- Directory for raw scraped output CSVs (e.g., QS_Rankings_subject-year.csv)
```

## Features / Highlights

* **Dynamic Content Web Scraping:** Implements a robust Scrapy spider integrated with Selenium WebDriver to handle JavaScript-rendered content on complex websites.
* **Structured Data Extraction:** Efficiently extracts university ranking details, names, locations, and various performance indicators.
* **Comprehensive Data Wrangling Pipeline:** Demonstrates cleaning, standardizing, and combining raw scraped data using Pandas. Includes handling of missing columns and dynamic assignment of categorical features.
* **Output Organization:** Structures raw and processed data into dedicated subfolders for clarity and manageability.
* **Dependency Management:** Clearly outlines Python and external browser driver dependencies for easy reproducibility.

## Installation and Setup

To run this project on your local machine, you'll need to set up a dedicated Python environment and install the necessary browser drivers.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/vsbunny/data-science-portfolio.git](https://github.com/vsbunny/data-science-portfolio.git)
    cd data-science-portfolio/scraping_projects/QS_world_rankings
    ```

2.  **Install WebDriver (for Selenium/Scrapy):**
    Selenium (used in `QS_World_rankings_scraper.ipynb` for dynamic content) requires a separate browser driver. Your spider is configured to look for `chromedriver` directly in its current working directory.

    * **Determine your Chrome browser version:** Open Google Chrome and go to `chrome://version/`. Note the exact version number.

    * **Download matching ChromeDriver:** Go to [https://chromedriver.chromium.org/downloads](https://chromedriver.com/downloads) and download the `chromedriver` that *exactly matches* your Chrome browser version.

        * **For macOS (Intel or Apple Silicon):**
            * Download the `.zip` file corresponding to your Mac's architecture (e.g., `chromedriver_mac_x64.zip` for Intel, `chromedriver_mac_arm64.zip` for Apple Silicon).
            * Unzip the downloaded file.
            * Move the `chromedriver` executable into this `QS_world_rankings/` project directory.
            * Grant executable permissions: `chmod +x chromedriver` (run this from within the `QS_world_rankings/` directory).

        * **For Windows:**
            * Download the `.zip` file for Windows (e.g., `chromedriver_win32.zip` or `chromedriver_win64.zip`).
            * Unzip the downloaded file. You will get a `chromedriver.exe` executable.
            * **Move this `chromedriver.exe` directly into this `QS_world_rankings/` project directory.** (No `sudo` or `chmod +x` is needed on Windows.)

    * **IMPORTANT NOTE ON `chromedriver` MANAGEMENT:**
        * **`chromedriver` is a large, platform-specific binary that should NOT be committed to Git.**
        * After you have finished running the scraper, **manually delete the `chromedriver` executable (or `chromedriver.exe`) from this `QS_world_rankings/` directory** before making any new `git add .` or `git commit` operations. 

3.  **Create and activate a dedicated Python virtual environment:**
    ```bash
    conda create -n scraper_env python=latest # Or specify a version like python=3.10
    conda activate scraper_env
    ```
4.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
## Usage

To run the scraper and data wrangling:

1.  Ensure your `scraper_env` is active (`conda activate scraper_env`).
2.  Launch Jupyter Lab from this directory:
    ```bash
    jupyter lab
    ```
3.  Open and run the notebooks in the following order:
    * **`QS_World_Rankings_Scraper.ipynb`**: Execute this notebook to run the Scrapy spider, which will scrape data and save raw CSV files into the `csv_rankings/` subfolder.
    * **`QS_wrangling.ipynb`**: After scraping, execute this notebook. It will read the raw CSVs from `csv_rankings/`, perform data cleaning and transformations, and save combined yearly CSVs into the `Combined_Rankings/` subfolder.

## Results and Insights

* **Successful Data Acquisition:** Successfully acquired structured ranking data from web sources using Scrapy and Selenium.
* **Robust Data Processing Pipeline:** Implemented a reliable pipeline for cleaning, standardizing, and combining raw scraped CSVs into a usable format, adhering to common data analysis standards (e.g., creating consolidated yearly rankings).
* **Key Data Extracted:** Successfully extracted university rankings, names, locations, and various performance indicators.
* **Challenges Overcome:** Successfully handled common web scraping complexities, including:
    * **Dynamic Content Loading:** Integrated Selenium WebDriver and implemented explicit waits (`WebDriverWait`) to ensure JavaScript-rendered content (like ranking data) was fully loaded and present before extraction.
    * **Pop-up Interception & Dismissal:** Developed robust mechanisms to identify and dismiss intrusive pop-ups (e.g., cookie consent banners, survey modals) by executing JavaScript (`document.getElementById().remove()`) directly via Selenium, which required careful targeting and error handling. This significantly enhanced the scraper's reliability and uninterrupted data flow.
 
## Future Work

* Implement more sophisticated anti-bot measures (e.g., rotating proxies, user agents).
* Develop a data pipeline to store scraped data in a database (e.g., SQL, NoSQL).

## Author

[Vanya Fernandez Galabo]