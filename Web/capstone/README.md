The first thing of interest I noted, was the fact that comments containing htlm looked weird (XSS?). For example, inserting <img src=x onerror=window.location.replace("http://localhost/index.php")> into the comment field yields the following output: 

<img src="https://github.com/user-attachments/assets/7a1568d5-1a9c-4760-94e7-a0416bd66fc5" width="300"/> 

Looking in the console, it seems like quotes are escaped: 

<img src="https://github.com/user-attachments/assets/3f9e6be2-2019-490e-ba5e-7b64f54b2ccf" width="500"/> 

Replacing " with \` in the previous command (<img src=x onerror=window.location.replace(\`http://localhost/index.php`)>) takes us back to index.php which means that we have a server-side (stored) XSS. For PoC running, running
<script>alert(document.domain)</script>
yields: 

<img src="https://github.com/user-attachments/assets/9016a95f-272e-40ac-a1ce-76427f89e810" width="500"/>
