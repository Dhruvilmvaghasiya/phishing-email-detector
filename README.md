# phishing-email-detector
# 📧 Phishing Email Detection using Email Header Analysis

This is a simple yet effective Python project to **detect phishing emails** by analyzing their **email headers**. The tool checks for common signs of spoofed or malicious emails like:

- ❌ SPF (Sender Policy Framework) failures
- ⚠️ Mismatched `From` and `Reply-To` domains
- 🛑 Suspicious sender IP addresses

> 🔐 Developed as part of a **Cyber Security Summer Internship Project**.

---

## 🧠 What is an Email Header?

An email header contains metadata about an email such as the sender, receiver, IP path, authentication status (SPF, DKIM), and more. Attackers often manipulate headers to spoof legitimate senders.

This project uses **email header inspection** to detect such frauds.

---

## 🛠️ Tech Stack

- **Python 3**
- Built-in modules: `email`, `re`
- Sample header files in `.txt` format

---

## 📁 Project Structure
phishing-email-detector/
├── header_samples/
│ └── sample1.txt # Sample suspicious email header
├── detector.py # Main script to analyze header
├── README.md # You're reading it!


---

## 🚀 How to Run

### 📌 Step 1: Install Python (if not already installed)

Download from: https://www.python.org/downloads/

### 📌 Step 2: Add a sample email header

Paste a header into this file:
header_samples/sample1.txt

You can get email headers from Gmail via:
More (⋮) → Show Original → Copy Header

### 📌 Step 3: Run the script

```bash
python detector.py

Output Example:
📬 Email Header Analysis Result:
------------------------------------
⚠️ This email is potentially PHISHING:
 - SPF check failed
 - From and Reply-To domain mismatch
 - Suspicious IP address detected: 185.45.67.89

Sample Results:
| Test Case   | Result      |
| ----------- | ----------- |
| sample1.txt | Phishing ⚠️ |
| sample2.txt | Safe ✅     |
