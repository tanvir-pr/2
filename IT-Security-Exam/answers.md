# Introduction to Information System Security - Test 2 — Answers

## Multiple Choice (Q1–20)

**1. Which technique involves physically following someone to gain access to a restricted area?**
**Answer: c) Tailgating**

**2. Which measure directly prevents unauthorized access to a stolen computer?**
**Answer: b) Disk encryption**

**3. Why is simple "delete" not secure?**
**Answer: b) Data remains and can be recovered**

**4. Which firewall type tracks active connections using a state table?**
**Answer: c) Stateful inspection**

**5. What is the key difference between an IDS and a firewall?**
**Answer: c) IDS detects but does not block**

**6. Which type of IDS uses known attack signatures?**
**Answer: b) Misuse detection**

**7. What is the purpose of a honeypot?**
**Answer: b) Attracting attackers for analysis**

**8. Which of the following are TRUE about firewalls? (2 points)**
**Answer: a) They analyze packet headers, c) They can block unauthorized access**

**9. Which methods do NOT guarantee permanent data deletion? (2 points)**
**Answer: a) Delete, b) Format**

**10. Which device hides internal IP addresses from the internet?**
**Answer: b) NAT**

**11. Which are TRUE about IDS? (3 points)**
**Answer: a) Detects suspicious activity, c) Can analyze logs, d) Is usually placed behind firewall**

**12. Which statements about proxies are TRUE? (3 points)**
**Answer: a) They can hide client IP, c) They can cache content, d) They can filter access**

**13. Which port is used for HTTP?**
**Answer: c) 80**

**14. Which statement about formatting is TRUE?**
**Answer: c) Data may still be recoverable**

**15. Which are features of stateful firewalls? (3 points)**
**Answer: a) Track connections, b) Use state tables, c) Analyze only packet headers**

**16. Which are benefits of NAT? (3 points)**
**Answer: a) Hides internal IPs, b) Saves public IP addresses, d) Enables multiple devices to share one IP**

**17. Which statement is FALSE?**
**Answer: b) ITIL is a law**

**18. Which standards are related to IT? (3 points)**
**Answer: a) ISO 27001, b) ISO 20000, c) ISO 9001**

**19. Which actions are GDPR-compliant? (3 points)**
**Answer: a) Collecting data with consent, b) Protecting personal data, d) Securing storage systems**

**20. Which statements about honeypots are TRUE? (3 points)**
**Answer: a) They attract attackers, b) They are used for analysis, d) They can be risky**

---

## Written Questions (Q21–25)

### 21. ACL Analysis (3 points)

**Given ACL:**
```
access-list 101 permit tcp 192.168.1.0 0.0.0.255 10.0.0.0 0.0.255.255 eq 443
```

**Packet:** Source IP: 192.168.2.45 | Destination IP: 10.1.5.10 | Protocol: TCP | Port: 443

**Answer: The packet is DENIED.**

- Step 1 — Source: 192.168.1.0 0.0.0.255 = range 192.168.1.0 – 192.168.1.255. Source IP 192.168.2.45 does NOT match.
- Since the source IP fails, the packet is denied.

### 22. Three types of social engineering attacks (3 points)

1. **Phishing** — Fake emails or websites to steal credentials
2. **Pretexting** — Inventing a scenario to gain trust
3. **Baiting** — Offering something appealing that contains malware

### 23. Three types of application-level attacks (3 points)

1. **SQL Injection** — Inserting malicious SQL code to access or manipulate databases
2. **Cross-Site Scripting (XSS)** — Injecting malicious scripts into trusted websites
3. **Cross-Site Request Forgery (CSRF)** — Forcing a user to perform unwanted actions while authenticated

### 24. Three types of authentication and credential attacks (3 points)

1. **Brute-force attacks** — Trying many password combinations until one works
2. **Dictionary attacks** — Using lists of common passwords
3. **Credential stuffing** — Reusing stolen username/password pairs across multiple services

### 25. Two goals of ITIL (2 points)

1. **Improve customer satisfaction**
2. **Reduce costs and risks**
