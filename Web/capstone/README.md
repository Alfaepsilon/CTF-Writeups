The first thing of interest I noted, was the fact that comments containing htlm looked weird (XSS?). For example, inserting <img src=x onerror=window.location.replace("http://localhost/index.php")> into the comment field yields the following output: \\
<img src="https://github.com/user-attachments/assets/7a1568d5-1a9c-4760-94e7-a0416bd66fc5" width="300"/>
Looking in the console, it seems like quotes are escaped:
<img src="https://github.com/user-attachments/assets/05b57768-2d51-4040-96f7-26ebb7b2af46" width="600"/>
Replacing " with \` in the previous command (<img src=x onerror=window.location.replace(\`http://localhost/index.php`)>) takes us back to index.php which means that we have a server-side (stored) XSS. For PoC running, running 
<script>alert(document.domain)</script>
yields:
<img src="https://github.com/user-attachments/assets/05b57768-2d51-4040-96f7-26ebb7b2af46" width="600"/>
