The first thing of interest I noted, was the fact that comments containing htlm looked weird (XSS?). For example, inserting <img src=x onerror=window.location.replace("http://localhost/index.php")> into the comment field yields the following output:
<screenshot>
Looking in the console, it seems like quotes are escaped:
<screenshot>
Replacing " with \` in the previous command (<img src=x onerror=window.location.replace(\`http://localhost/index.php\`)>) takes us back to index.php which means that we have a server-side (stored) XSS. For PoC running, running 
<script>alert(document.domain)</script>
yields:
