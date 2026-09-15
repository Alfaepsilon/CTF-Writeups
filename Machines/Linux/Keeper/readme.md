# HTB Writeup: <Machine Name>

## Overview

| Field | Value |
|---------|---------|
| Machine | Keeper|
| IP Address | $TARGET_IP |
| OS | Linux |
| Difficulty | Easy |
| Date | 2026-xx-xx |
| Author | Alfaepsilon |

---

## Executive Summary

Brief description of the attack path.

Example:

1. Initial access obtained via exposed web application.
2. Credential leakage allowed service authentication.
3. Local privilege escalation through misconfigured sudo permissions.
4. Root/Administrator access achieved.
![First page](images/first_page.png)
---

# Enumeration

## Host Discovery

### Ping

```bash
ping -c 4 <IP>
```

### Observations

- Host reachable
- TTL suggests Linux/Windows

---

## Port Scanning

### Full TCP Scan

```bash
nmap -p- --min-rate 5000 -Pn <IP> -oA scans/full_tcp
```

### Targeted Service Scan

```bash
nmap -sCV -p <ports> <IP> -oA scans/service_scan
```

### Results

| Port | Service | Version |
|--------|--------|--------|
| 22 | SSH | OpenSSH x.x |
| 80 | HTTP | Apache x.x |
| ... | ... | ... |

### Notes

Document any unusual findings.

---

## Service Enumeration

### HTTP

#### Homepage

- Screenshot
- Interesting content
- Source code review

#### Directory Discovery

```bash
ffuf -u http://<IP>/FUZZ \
     -w /usr/share/seclists/... \
     -mc all
```

#### Findings

| Endpoint | Description |
|-----------|-----------|
| /admin | Admin panel |
| /api | API endpoint |

---

### DNS

```bash
dig axfr @<IP> domain.htb
```

Findings:

- Subdomains
- Internal naming conventions

---

### SMB

```bash
smbclient -L //<IP> -N
```

Shares discovered:

| Share | Access |
|---------|---------|
| Public | Read |
| Users | Restricted |

---

### LDAP

```bash
ldapsearch ...
```

Interesting objects:

- Users
- Groups
- Service accounts

---

### Other Services

Document findings for:

- FTP
- RDP
- WinRM
- MSSQL
- MySQL
- Redis
- Docker
- Kubernetes
- SNMP
- RPC

---

# Initial Access

## Vulnerability Identification

### Discovery

Describe:

- What vulnerability was identified
- Why it is exploitable
- Relevant evidence

### Exploitation

```bash
<commands>
```

OR

```python
# exploit script
```

### Proof

Show:

- Shell obtained
- User context
- Screenshots

```bash
whoami
hostname
ipconfig
```

Output:

```text
<output>
```

---

# Post Exploitation

## User Enumeration

### Current Context

```bash
id
groups
sudo -l
```

### Interesting Files

| Path | Notes |
|---------|---------|
| /var/www/html | Web root |
| /home/user | Credentials |

### Credentials Found

| Username | Password/Hash | Source |
|------------|------------|------------|
| user | ******** | config.php |

---

## Lateral Movement (If Applicable)

### Discovery

Describe:

- New hosts
- New credentials
- Trust relationships

### Pivot Technique

```bash
ssh -L ...
```

or

```bash
chisel ...
```

---

# Privilege Escalation

## Enumeration

### Linux

```bash
linpeas.sh
```

Important findings:

- Sudo permissions
- SUID binaries
- Writable files
- Capabilities

### Windows

```powershell
winPEAS.exe
```

Important findings:

- Services
- Scheduled tasks
- Token privileges
- Registry issues

---

## Root Cause

Explain:

- Why the privilege escalation works
- Security misconfiguration
- Technical details

---

## Exploitation Steps

### Step 1

```bash
<command>
```

### Step 2

```bash
<command>
```

### Step 3

```bash
<command>
```

### Result

```bash
whoami
```

Output:

```text
root
```

OR

```text
nt authority\system
```

---

# Flags

## User Flag

Location:

```text
<path>
```

Obtained:

```text
<redacted>
```

---

## Root/Admin Flag

Location:

```text
<path>
```

Obtained:

```text
<redacted>
```

---

# Attack Path Summary

```text
Reconnaissance
    ↓
Service Enumeration
    ↓
Vulnerability Discovery
    ↓
Initial Access
    ↓
Credential Harvesting
    ↓
Privilege Escalation
    ↓
Root/SYSTEM
```

---

# Indicators of Compromise

## Files Created

```text
/tmp/rev.sh
```

## Accounts Accessed

- user
- service_account
- administrator

## Network Connections

| Source | Destination | Purpose |
|----------|----------|----------|
| Attacker | Target | Reverse shell |
| Target | C2 | Callback |

---

# Lessons Learned

## Offensive Takeaways

- Key enumeration techniques that led to compromise.
- Missed indicators that could have accelerated exploitation.
- Alternative attack paths.

## Defensive Recommendations

- Patch vulnerable software.
- Restrict exposed services.
- Enforce least privilege.
- Remove credential exposure.
- Implement monitoring and alerting.

---

# References

- HTB Machine Page
- CVEs
- Exploit references
- Documentation
- Research articles

---

# Appendix

## Commands Used

```bash
# Enumeration

# Exploitation

# Privilege Escalation
```

## Tool Versions

| Tool | Version |
|----------|----------|
| Nmap | |
| Burp Suite | |
| ffuf | |
| Impacket | |

## Artifacts

- Screenshots
- Loot
- Configuration files
- Exploit code
