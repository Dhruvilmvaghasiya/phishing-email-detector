"""
Phishing Email Detection Tool
Author: Dhruvil Vaghasiya
Description: This Python script analyzes email headers to detect signs of phishing attacks.
"""

import re
from email import message_from_string

def detect_phishing(header_text):
    """
    Analyzes the given email header text for signs of phishing.
    Checks for SPF failure, From/Reply-To mismatch, and suspicious IP addresses.
    """
    issues = []

    # Check for SPF failure
    if "SPF: fail" in header_text or "Received-SPF: fail" in header_text:
        issues.append("SPF check failed")

    # Check From and Reply-To domain mismatch
    from_match = re.search(r'From: .*<(.+?)>', header_text)
    reply_to_match = re.search(r'Reply-To: (.+)', header_text)

    if from_match and reply_to_match:
        from_domain = from_match.group(1).split('@')[-1].lower()
        reply_domain = reply_to_match.group(1).split('@')[-1].lower()
        if from_domain != reply_domain:
            issues.append("From and Reply-To domain mismatch")

    # Check for suspicious IP address
    ip_matches = re.findall(r'Received:.*\[(\d{1,3}(?:\.\d{1,3}){3})\]', header_text)
    for ip in ip_matches:
        if ip.startswith("185.") or ip.startswith("194.") or ip.startswith("45."):
            issues.append(f"Suspicious IP address detected: {ip}")

    # Final result
    print("\n📬 Email Header Analysis Result:")
    print("------------------------------------")
    if issues:
        print("⚠️ This email is potentially PHISHING:")
        for issue in issues:
            print(f" - {issue}")
    else:
        print("✅ This email appears SAFE.")

# Load email header from a file (default: sample1.txt)
def main():
    try:
        with open("header_samples/sample1.txt", "r") as f:
            header_text = f.read()
            detect_phishing(header_text)
    except FileNotFoundError:
        print("❌ Header file not found. Please place a sample header in 'header_samples/sample1.txt'.")

if __name__ == "__main__":
    main()
