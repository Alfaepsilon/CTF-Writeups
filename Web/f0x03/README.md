Trying to change the content and filetype via burpsuite fails indicating a serverside file check.
The first thing to notice, is that some file extension yields different error messages than others. For example .php, .php3 and .php4 all yield messages directed to those file types specifically. While .phptml and .php5 gets a generic response.
This hints at the fact of the server blacklisting some extensions specifically, and others not. By using magic bytes of a PNG file, we succeed in uploading a file injected with:
```
<?php system($_GET['cmd']); ?>
```
with a .phtml extension which when executed allows us to interact with the server.
