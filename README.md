# Automation Indee Test

This project is an automation testing framework built using Python, Selenium, and Behave (BDD) for testing web applications.  
It follows the Page Object Model (POM) design pattern with separation of concerns for better maintainability.

---

## 📂 Project Structure

Automation_Indee_Test/
│── base_pages/ # Page Object Model classes
│ ├── base_page.py
│ ├── login_and_upload_page.py
│
│── configuration/ # Configuration files
│ ├── config.ini
│
│── features/ # BDD Feature files & Step Definitions
│ ├── application.feature
│ ├── steps/
│ │ ├── login_and_upload_steps.py
│ ├── environment.py
│
│── logs/ # Log files
│ ├── test.log
│
│── reports/ # Test Reports (generated after execution)
│
│── screenshots/ # Captured screenshots on failure
│
│── utilities/ # Utilities & Helpers
│ ├── customLogger.py
│ ├── locators.py
│ ├── read_properties.py
│
│── requirements.txt # Python dependencies
│── run.bat # Batch file for running tests (Windows)
│── README.md # Project Documentation


---

## ⚙️ Installation & Setup

Install dependencies

pip install -r requirements.txt

🚀 Running the Tests
Option 1: Using Behave directly
behave features/application.feature

Option 2: Run all tests and generate html report
behave -f behave_html_formatter:HTMLFormatter -o reports/html_report.html .\features\application.feature

Option 3: Using Batch File (Windows)
Simply run:
run.bat

📝 Reports & Logs

Logs → Stored under logs/test.log

Screenshots (on failure) → Stored under screenshots/

Reports → Generated under reports/

🧩 Example Feature (application.feature)
Feature: Profile Picture Upload

  Scenario: Verify profile picture upload
    Given I open the application
    When I login with valid credentials
    And I upload a file "path/to/file.png"
    Then I should see a success message

📌 Notes

Update config.ini with environment-specific details (URL, credentials, etc.).

Logs and screenshots will help in debugging failed test cases.