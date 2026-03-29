#  Web Security Testing Tools

This section covers essential tools used for **web application security testing**, including vulnerability scanning, request interception, and SQL injection testing.

---

##  Disclaimer
Use these tools only in **authorized environments** such as:
- Your own applications  
- Lab setups (DVWA, Juice Shop, etc.)  
- Platforms like TryHackMe / PortSwigger  

---

##  Tools Covered
- Burp Suite (Community)
- OWASP ZAP
- Nikto
- SQLMap

---

#  1. Burp Suite (Community)

##  Description
Burp Suite is a powerful tool used to **intercept, analyze, and modify HTTP/HTTPS requests** between browser and server.

---

##  Key Features
- Proxy (intercept requests)
- Repeater (modify & resend requests)
- Intruder (basic fuzzing – limited in community version)

---

##  Basic Setup
1. Open Burp Suite  
2. Enable Proxy (Intercept ON)  
3. Set browser proxy to:
127.0.0.1:8080

---

##  Example Use Case
- Intercept login request  
- Modify username/password  
- Forward request  

---

##  Learning
- Understand how web requests work  
- Identify hidden parameters  
- Test authentication logic  

---

#  2. OWASP ZAP

##  Description
OWASP ZAP is an **automated vulnerability scanner** for finding security issues in web applications.

---

##  Key Features
- Automated scan  
- Passive & active scanning  
- Spider (crawl website)

---

##  Basic Usage

### Start Scan
1. Open OWASP ZAP  
2. Enter target URL  
3. Click "Attack" → "Active Scan"  

---

##  Example
Scan:
http://testphp.vulnweb.com

---

##  Learning
- Detect common vulnerabilities:
  - XSS  
  - SQL Injection  
  - Security misconfigurations  

---

#  3. Nikto

##  Description
Nikto is a web server scanner that identifies:
- Outdated software  
- Dangerous files  
- Misconfigurations  

---

##  Basic Command

```bash
nikto -h http://example.com
 Example
nikto -h http://testphp.vulnweb.com
 Learning
Identify server vulnerabilities
Find exposed directories/files
 4. SQLMap
 Description
SQLMap is an automated tool used to detect and exploit SQL Injection vulnerabilities.
 Basic Usage
Test URL for SQL Injection
sqlmap -u "http://example.com/page?id=1" --dbs
 Example
sqlmap -u "http://testphp.vulnweb.com/listproducts.php?cat=1" --dbs
 Extract Tables
sqlmap -u "URL" -D database_name --tables

 Practice Questions

Intercept a login request using Burp Suite
Identify request method (GET/POST)
Scan a website using OWASP ZAP
Use Nikto to scan a test website
Find at least 3 vulnerabilities using ZAP
Modify request parameters using Burp

Perform SQL Injection using SQLMap
Extract database names from vulnerable site
Identify input fields vulnerable to injection
 Theory Questions
What is XSS and how does it work?
What is SQL Injection?
Difference between GET and POST requests?
What is a vulnerability scanner?
How can web apps prevent attacks?
 Prevention Techniques
Input validation & sanitization
Use prepared statements (SQL)
Implement WAF (Web Application Firewall)
Secure headers (CSP, HSTS)
Regular vulnerability scanning
 Conclusion
These tools help identify and exploit web vulnerabilities, enabling developers and security professionals to build secure web applications.