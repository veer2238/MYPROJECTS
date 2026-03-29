#  Password & Authentication Tools

This section covers essential tools used for password auditing, hash cracking, and authentication testing in cyber security.

>  Disclaimer: Use these tools only in **legal lab environments** or systems you have **explicit permission** to test.

---

##  Tools Covered
- John the Ripper (JTR)
- Hashcat
- Hydra

---

#  1. John the Ripper (JTR)

##  Description
John the Ripper is a fast password cracking tool used to detect weak passwords by comparing hashes against wordlists.

##  Supported Hash Types
- MD5
- SHA1
- SHA256
- bcrypt (limited support)

---

##  Basic Usage

### Step 1: Save hash into a file
```bash
echo "5f4dcc3b5aa765d61d8327deb882cf99" > hash.txt


Step 2: Run John
```bash
john hash.txt



Step 3: Show cracked passwords
```bash
john --show hash.txt


Example
Hash (MD5):

5f4dcc3b5aa765d61d8327deb882cf99

Output:
password


Using Wordlist

john --wordlist=rockyou.txt hash.txt


2. Hashcat

Description
Hashcat is an advanced password recovery tool that supports GPU acceleration for high-speed cracking.



Common Hash Modes


| Hash Type | Mode |
| --------- | ---- |
| MD5       | 0    |
| SHA1      | 100  |
| SHA256    | 1400 |



Basic Usage
Step 1: Save hash
```bash
echo "098f6bcd4621d373cade4e832627b4f6" > hash.txt

Step 2: Dictionary Attack
```bash
hashcat -m 0 -a 0 hash.txt rockyou.txt

Step 3: Show Results
```bash
hashcat --show hash.txt


Example

Hash (MD5):
098f6bcd4621d373cade4e832627b4f6

Output:
test


3. Hydra
Description
Hydra is used to perform brute-force attacks on login forms, SSH, FTP, HTTP, etc.


Basic Syntax
```bash
hydra -l username -P passwords.txt target service


Example: HTTP Login Attack (Lab Only)
```bash
hydra -l admin -P passwords.txt testphp.vulnweb.com http-post-form "/login.php:username=^USER^&password=^PASS^:F=incorrect"



Example: SSH Attack (Local Lab)
```bash
hydra -l root -P passwords.txt ssh://127.0.0.1


Practice Questions

Crack the following MD5 hash using John:
5f4dcc3b5aa765d61d8327deb882cf99


Use Hashcat to crack:
098f6bcd4621d373cade4e832627b4f6


Create a wordlist of 20 common passwords and test it using John.

Perform a dictionary attack using Hashcat with rockyou.txt.

Crack a 4-digit numeric password using mask attack:
hashcat -a 3 -m 0 hash.txt ?d?d?d?d


Compare speed:
John vs Hashcat
 Which is faster and why?


Set up a local login page and perform Hydra attack.

Simulate brute-force attack on SSH (local VM only).

Analyze:
How long does it take to crack strong passwords?


theory questions

Why is hashing used instead of storing passwords in plain text?
Difference between MD5, SHA1, and bcrypt?
What makes a password strong?
What is salting in hashing?
How can systems prevent brute-force attacks?


