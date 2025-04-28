Let's start with nmap:
```
nmap -p- -T4 -A 10.10.10.4
```
<img src="https://github.com/user-attachments/assets/55bba9bd-e143-4d14-a305-f781ab283378" width=300>

The first thing to note is that this is an Windows XP machine, which is a operating system that is known to have a lot of bugs, which is interesting. For now though, lets enumerate smb:

```
smbclient -L \\\\10.10.10.4\\ --user=guest
```

Trying this however gives us a "Login failure".

We can attempt to enumerate the smb service further with for example a tool like enum4linux:
```
enum4linux -a 10.10.10.4
```

This however does not yield much either. Since as said earlier Windows XP is known to be vulnerable, I attempted to Google information about this specific smb version. There were a few known vulnerabilities and one, ms08-076, had a metasploit module. Trying it out, I got a meterpreter shell with NT AUTHORITY\SYSTEM privileges:

<img src="https://github.com/user-attachments/assets/3615004f-f011-4599-85c1-048e841928d6" width=300>

<img src="https://github.com/user-attachments/assets/cbc0454d-be2f-4653-baf6-6a1ca54c3052" width=300>

There is no "Users" folder under C:\Users or C:\Windows\Users. To find the flags, we can search for their file names (user.txt and root.txt):
```
dir /S /B user.txt
```
```
dir /S /B root.txt
```

and we find them under
```
 C:\Documents and Settings\<username>\Desktop\
```
