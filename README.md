# web-autoexercise-selenium-python
End-to-end web automation for automationexercise.com using Selenium in Python


# Selenium Automation Setup on macOS

This project demonstrates how to set up and run Selenium-based automation scripts using Python on macOS.

---

## Requirements

* macOS with Python 3 pre-installed
* Internet connection to install packages

---

## Setup Instructions

### 1. Check Python & pip Versions

Make sure Python3 and pip are installed:
=> python3 --version
=> python3 -m pip --version

---

### 2. Install Selenium

=> python3 -m pip install -U selenium

---

### 3. Create Virtual Environment (Recommended)

To isolate dependencies:

=> python3 -m venv venv
=> source venv/bin/activate

---

### 4. Install Dependencies

=> pip install -U selenium
=> pip install --upgrade webdriver-manager
=> pip install chromedriver-autoinstaller
=> pip install --upgrade pip

---

### 5. Freeze Dependencies

Save all installed packages to `requirements.txt`:

=> pip freeze > requirements.txt

> Example minimal `requirements.txt`:

```txt
selenium==4.34.2
webdriver-manager==4.0.1
chromedriver-autoinstaller
```

---

### 6. Install from `requirements.txt` (Optional)

=> pip install -r requirements.txt

---

## Project Structure (Example)

```
selenium-test/
├── venv/
├── requirements.txt
├── README.md
└── main.py
```

---

## How to Run (Summary)

1. **Activate the environment**
   
   source venv/bin/activate

2. **Upgrade pip (inside venv)**
    
   python3 -m pip install --upgrade pip

3. **Install dependencies**

   pip install -r requirements.txt

4. **Run the script**

   python main.py
---

## ⚠️ Notes

* Avoid modifying or deleting the system Python in `/usr/bin`.
* Always use a virtual environment (`venv`) to manage dependencies cleanly and safely.
