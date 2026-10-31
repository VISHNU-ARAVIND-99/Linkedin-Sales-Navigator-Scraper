# 🔍 LinkedIn Sales Navigator Scraper

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?logo=selenium&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-HTML_Parser-orange)
![Pandas](https://img.shields.io/badge/Pandas-Data_Export-150458?logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

An automated B2B lead generation and data extraction tool built with **Python**, **Selenium**, and **BeautifulSoup**. This scraper navigates LinkedIn Sales Navigator search results, handles dynamic lazy-loading via automated scrolling and pagination, parses prospect details, maps role hierarchies, and exports clean, structured lead lists directly to Excel.

---

## ✨ Key Features

* **Automated Browser Control:** Uses Selenium WebDriver to handle authentication sessions, dynamic DOM rendering, and multi-page navigation.
* **Smart Lazy-Load Scrolling:** Automatically scrolls through Sales Navigator result containers to ensure all 25+ prospect cards per page are fully rendered in the DOM before parsing.
* **Comprehensive Lead Extraction:** Extracts key prospect metadata using BeautifulSoup and Regular Expressions (`re`):
  * Full Name & Profile URL
  * Job Title & Role Hierarchy Mapping
  * Company Name
  * Geographic Location
  * Connection Degree & Premium/OpenLink Indicators
* **Structured Excel Export:** Cleans and compiles extracted records into a Pandas DataFrame and exports directly to `.xlsx` / `.csv` for immediate CRM or outreach import.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Browser Automation:** `selenium` (ChromeDriver)
* **HTML Parsing:** `beautifulsoup4` (bs4)
* **Pattern Matching:** `re` (Regular Expressions)
* **Data Manipulation & Export:** `pandas`, `openpyxl`

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have the following installed on your system:
* [Python 3.8+](https://www.python.org/downloads/)
* [Google Chrome](https://www.google.com/chrome/)
* [ChromeDriver](https://chromedriver.chromium.org/) (matching your installed Chrome version)
* An active **LinkedIn Sales Navigator** account

### 2. Installation

Clone the repository and install the required dependencies:

```bash
git clone [https://github.com/VISHNU-ARAVIND-99/Linkedin-Sales-Navigator-Scraper.git](https://github.com/VISHNU-ARAVIND-99/Linkedin-Sales-Navigator-Scraper.git)
cd Linkedin-Sales-Navigator-Scraper
pip install selenium beautifulsoup4 pandas openpyxl
