Using burpsuite, we can take a request containing a cookie and copy it to a text document. Using that request, we can the extract the users table containing the administrator password using sqlmap with the following command:
```
sqlmap -r req.txt --dump injection0x03_users
```
