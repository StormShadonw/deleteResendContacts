# Resend Bulk Contact Deleter 📧 🧹

A robust Python script designed to perform mass deletion of contacts within the **Resend** platform. This tool automates the process of clearing an entire contact list while ensuring security, error handling, and compliance with API rate limits.

---

## ✨ Features

* **Recursive Deletion:** Automatically loops through contact pages until the entire audience is cleared.
* **Security First:** Uses environment variables (`.env`) to prevent hardcoding sensitive API keys.
* **Graceful Error Handling:** Implements `try-except` blocks to manage individual contact failures without crashing the entire process.
* **Rate Limit Protection:** Built-in delays (`time.sleep`) to respect Resend's API throughput limits.
* **Real-time Logging:** Provides detailed console output for every deletion attempt and round progress.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **API Client:** [resend](https://github.com/resend/resend-python)
* **Configuration:** `python-dotenv`

## 📋 Prerequisites

Before running the script, ensure you have:

1.  A [Resend](https://resend.com) account.
2.  A valid **API Key** with "Full Access" or "Sending" permissions.
3.  Python 3.8+ installed on your machine.

## 🔧 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/StormShadonw/deleteResendContacts.git 
   cd deleteResendContacts
2.  Create a file in the same route that your main.py file ".env" with this content.
   ```bash
RESEND_API_KEY=re_**********************
```
3. run
```bash
python3 ./main.py
```
