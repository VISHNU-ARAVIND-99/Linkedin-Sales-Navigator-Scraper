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

```

### 3. Configuration & Usage

1. Open the main Python script in your editor.
2. Configure your ChromeDriver path, target **Sales Navigator Search URL**, and login credentials/session cookies as prompted in the script.
3. Run the scraper:

```bash
python main.py

```

*(Note: Replace `main.py` with your exact script filename if different).*

4. **Authenticate:** Log into your LinkedIn account in the automated Chrome window (complete any 2FA/CAPTCHA if prompted).
5. **Automated Extraction:** The script will automatically iterate through the search pages, scroll through lead cards, parse the HTML, and save the output Excel file in your project directory.

---

## 📊 Output Data Structure

The exported Excel spreadsheet contains structured columns ready for B2B outreach:

| Field | Description |
| --- | --- |
| **Name** | Full name of the prospect |
| **Title / Role** | Current designation and mapped seniority level |
| **Company** | Current organization name |
| **Location** | City, State, or Country of the lead |
| **Profile URL** | Direct link to the Sales Navigator / LinkedIn profile |

---

## ⚠️ Best Practices & Rate Limiting

To protect your LinkedIn account from temporary restrictions:

* **Use Human-Like Delays:** Keep `time.sleep()` intervals randomized between page loads and scroll actions.
* **Avoid Excessive Volume:** Limit scraping sessions to a reasonable number of pages per run (e.g., 1,000–1,500 leads per day).
* **Session Persistence:** Use Chrome user profiles or session cookies rather than logging in from scratch on every script execution.

---

## ⚖️ Disclaimer

This project was created strictly for **educational and research purposes**. Automated scraping of LinkedIn may violate LinkedIn's User Agreement. Use this tool responsibly and at your own risk. The author is not responsible for any account restrictions or misuse of the software.

---

## 👤 Author

**Vishnu Aravind**

* GitHub: [@VISHNU-ARAVIND-99](https://github.com/VISHNU-ARAVIND-99)

---

*If you found this project useful, please consider giving it a ⭐ on GitHub!*

```

**Quick Tip Before Committing:**
In the **Usage** section (`python main.py`), swap `main.py` with the exact `.py` or `.ipynb` filename in your repository so anyone cloning it can run the command directly.

```
