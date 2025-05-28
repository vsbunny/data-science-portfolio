# Times Higher Education (THE) World University Rankings Scraper & Data Wrangling

[![Python Version](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](../../../LICENSE) ## Description

This project demonstrates a Python-based pipeline for acquiring and processing data from the Times Higher Education (THE) World University Rankings website. It utilizes Selenium for robust web scraping of dynamic content and Beautiful Soup for efficient HTML parsing. The extracted data is then processed using Pandas for cleaning, standardization, and consolidation into a usable format.

## Project Structure
```
.
├── README.md                           <- This file
├── THE_Rankings_Scraper.ipynb          <- Jupyter Notebook containing the Selenium/Beautiful Soup scraper
├── THE_wrangling.ipynb                 <- Jupyter Notebook for data wrangling and combining scraped data
├── requirements.txt                    <- Python dependencies for this project
├── THE_rankings_raw_data/              <- Directory for raw scraped output CSVs (e.g., subject_rankings_year.csv)
```
)

## Features / Highlights

* **Dynamic Content Web Scraping:** Implements a robust scraper using Selenium WebDriver to navigate, render JavaScript-driven content, and interact with web elements.
* **HTML Parsing with Beautiful Soup:** Efficiently extracts structured data from the rendered HTML content using Beautiful Soup.
* **Data Acquisition Pipeline:** Covers the full spectrum from raw web data extraction to initial data cleaning, transformation, and structured output.
* **Data Wrangling & Standardization:** Applies Pandas for cleaning, transforming, and standardizing scraped datasets (e.g., handling missing columns, organizing data by year).
* **Robust Error Handling:** Incorporates `try-except` blocks and explicit waits (`WebDriverWait`) to manage common scraping issues like element timeouts and pop-up interceptions.
* **Dependency Management:** Clearly outlines Python and external browser driver dependencies for easy reproducibility across different environments.

## Installation and Setup

To run this project on your local machine, you'll need to set up a dedicated Python environment and install the necessary browser drivers.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/vsbunny/data-science-portfolio.git](https://github.com/vsbunny/data-science-portfolio.git)
    cd data-science-portfolio/scraping_projects/THE_world_rankings
    ```

2.  **Install WebDriver (for Selenium):**
    Selenium (used in `THE_Rankings_Scraper.ipynb`) requires a separate browser driver. Your scraper is configured to look for `chromedriver` directly in its current working directory.

    * **Determine your Chrome browser version:** Open Google Chrome and go to `chrome://version/`. Note the exact version number.

    * **Download matching ChromeDriver:** Go to [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads) and download the `chromedriver` that *exactly matches* your Chrome browser version.

        * **For macOS (Intel or Apple Silicon):**
            * Download the `.zip` file corresponding to your Mac's architecture (e.g., `chromedriver_mac_x64.zip` for Intel, `chromedriver_mac_arm64.zip` for Apple Silicon).
            * Unzip the downloaded file.
            * Move the `chromedriver` executable into this `THE_world_rankings/` project directory.
            * Grant executable permissions: `chmod +x chromedriver` (run this from within the `THE_world_rankings/` directory).

        * **For Windows:**
            * Download the `.zip` file for Windows (e.g., `chromedriver_win32.zip` or `chromedriver_win64.zip`).
            * Unzip the downloaded file. You will get a `chromedriver.exe` executable.
            * **Move this `chromedriver.exe` directly into this `THE_world_rankings/` project directory.** (No `sudo` or `chmod +x` is needed on Windows.)

    * **IMPORTANT NOTE ON `chromedriver` MANAGEMENT:**
        * **`chromedriver` is a large, platform-specific binary that should NOT be committed to Git.**
        * After you have finished running your scraper, **manually delete the `chromedriver` executable (or `chromedriver.exe`) from this `THE_world_rankings/` directory** before making any new `git add .` or `git commit` operations. You will need to place it here again each time you want to run the scraper.

3.  **Create and activate a dedicated Python virtual environment:**
    ```bash
    conda create -n the_scraper_env python=latest # Or specify a version like python=3.10
    conda activate the_scraper_env
    ```

4.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
## Usage

To run the scraper and data wrangling:

1.  Ensure your `the_scraper_env` is active (`conda activate the_scraper_env`).
2.  Launch Jupyter Lab from this directory:
    ```bash
    jupyter lab
    ```
3.  Open and run the notebooks in the following order:
    * **`THE_Rankings_Scraper.ipynb`**: Execute this notebook to run the scraper, which will save raw CSV files into the `THE_rankings_raw_data/` subfolder.
    * **`THE_Rankings_Wrangling.ipynb`**: After scraping, execute this notebook. It will read the raw CSVs from `THE_rankings_raw_data/`, perform data cleaning and transformations, and save combined yearly CSVs into the `Combined_THE_Rankings/` subfolder.

## Results and Insights

* **Successful Data Acquisition:** Successfully acquired structured university ranking data from the Times Higher Education website using Selenium and Beautiful Soup.
* **Robust Data Processing Pipeline:** Implemented a reliable pipeline for cleaning, standardizing, and combining raw scraped CSVs into a usable format, ready for analysis (e.g., creating consolidated yearly rankings).
* **Key Data Extracted:** Successfully extracted university rank, name, country/region, and various score components (Overall, Research Quality, Industry Income, International Outlook, Research Environment, Teaching).
* **Challenges Overcome:** Successfully tackled common web scraping complexities:
    * **Cookie Overlay Removal:** Developed robust mechanisms to identify and dismiss intrusive cookie consent overlays by executing JavaScript (`document.getElementById().remove()`) directly via Selenium, ensuring uninterrupted access to page content.
    * **Scalable Data Extraction:** Engineered the scraper to efficiently extract data across multiple subjects and years, successfully handling the iteration logic to gather comprehensive ranking data as prompted.
    * **Dynamic Content Loading:** Utilised Selenium WebDriver and explicit waits (`WebDriverWait`) to ensure JavaScript-rendered ranking data was fully loaded before extraction.

## Future Work

* Develop a data pipeline to store scraped data in a database (e.g., SQL, NoSQL).

## Author

[Vanya Fernandez Galabo]