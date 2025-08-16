import re
text = "My email is user123@example.com and my phone number is 9502158357. Another email: chmnvkrishna@gmail.com"
email_pattern = r"[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]+"
emails = re.findall(email_pattern, text)
print("Emails found:", emails)
phone_pattern = r"\b\d{10}\b"
phones = re.findall(phone_pattern, text)
print("Phone numbers found:", phones)
h_words = re.findall(r"\b[hH]\w*", text)
print("Words starting with 'h' or 'H':", h_words)
