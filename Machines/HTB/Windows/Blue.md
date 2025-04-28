The first thing to do is to enumerate the machine, this can be done with a nmap scan:
```
nmap -p- -T4 -A 10.10.10.40
```
<img src="https://github.com/user-attachments/assets/07cf375e-cd37-4c88-ad0d-ac6a670e5641" width="400"/>

From the output above, we can see that most of the ports open are msrpc ports. Another port that is open is 139 and 445, which means that smb is open. Let's see if we can connect to it! We can list the shares, and there are two that are interesting: "Share" and "Users":

<img src="https://github.com/user-attachments/assets/6211d611-8d69-442b-b85c-e85934000524" width="300"/>

Poking in these two shares doesn't seem to yield much. Another thing that we could do is take a look at the smb service info from the nmap scan. Googling this does yield a result that is very interesting. There seems to be an exploit for this version, "EternalBlue" (ms17-010), that is very well known. There seems to be some metasploit modules for this, which we can try:

<img src="https://github.com/user-attachments/assets/69488100-fe51-4c9d-9a08-3449a9129477" width="300"/>

Executing the first one listed from the search result (search Eternal) gives us a meterpreter shell with NT AUTHORITY\SYSTEM privileges!
