# HTB Writeup: Knife

## Overview

| Field | Value |
|---------|---------|
| Machine | Knife |
| IP | $TARGET_IP |
| OS | Linux |
| Difficulty | Easy |
| Date | 2026-09-12 |
| Author | Alfaepsilon |

---

## Executive Summary

Initial access was gained via a backdoor in PHP/8.1.0-dev running on the webserver, and then privilege escalation by using the installed knife tool to execute a arbitrary ruby script with sudo privileges.

---

# Enumeration

## Port Scanning

### Full TCP Scan

```bash
nmap -p- -A -T4 $TARGET_IP
```

### Results

| Port | Service | Version |
|--------|--------|--------|
| 22 | SSH | OpenSSH 8.2p1 |
| 80 | HTTP | Apache 2.4.41 |


## Service Enumeration

### HTTP

#### Homepage
\!\[First page\]\(images/first_page.png\)

Source code of website did not seem to contain anything interesting.

#### Directory Discovery

```bash
nikto -h http://$TARGET_IP
```

#### Findings

PHP version seemed to be a dev build, which might be interesting: PHP/8.1.0-dev. 

---

# Initial Access

## Vulnerability Identification

### Discovery
Investigating the PHP version further, there seemed to be a backdoor built into it. The backdoor is activated if the "User-Agentt" header is present in requests to the web server. ExploitDB had a Python script to exploit the backdoor [1].

### Exploitation


```bash
python3 php-8-1-0-backdoor.py
```
The script prompted for the target host and then spawned a pseudo shell on the server.

### Proof
\!\[Backdoor access\]\(images/php-8.1.0-backdoor-shell.png\)
---

# Post Exploitation

## User Enumeration

### Current Context
Initial user on system was "james", which had access to the user flag in /home/james/user.txt.
A reasonable next step was to upgrade the current "pseudo-shell" to a better one. First thought to come to mind was ssh. An initial check in james home directory showed both a public and private ssh key. Downloading the private ssh key, creating authorized_keys and then adding the public key to it allowed for ssh authentication.

On target:
```bash
touch home/james/.ssh/authorized_keys
echo "<public_key>" > home/james/.ssh/authorized_keys
```

On local host:
```bash
chmod 600 private_key
ssh -i private_key james@$TARGET_IP
```
\!\[ssh access as james\]\(images/ssh_james.png\)
---

# Privilege Escalation

## Enumeration
Once authenticated as james via ssh, I checked my privileges.
```bash
sudo -l
```
This returned something interesting, the fact that james had passwordless sudo permissions on /usr/bin/knife.

\!\[Sudo permissions for james\]\(images/sudo_james.png\)

Investigating the knife tool, it seems to be a command line utility for chef, which is a infrastructure provisioning tool like Ansible. Apparently, it is possible to execute local ruby scripts using knife:

```bash
knife exec script.rb
```
Seeing this, and the fact that james can execute knife using passwordless sudo, we can construct a malicious ruby script and then run it as root. Like the following:
script.rb:
```ruby
system('/bin/bash -i')
```

```bash
sudo knife exec script.rb
```
Executing the above command spawned a shell as root, which allowed the root flag to be read.
---

# References
[1] https://www.exploit-db.com/exploits/49933
