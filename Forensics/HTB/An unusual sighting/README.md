We are given a ZIP file containing a bash_history.txt and ssh logs and a service to connect to. It took me a little while, but I eventually realised that we had to connect to the service and answer some questions. The answer to these questions can be found in the bash_history and sshd logs.

Question 1: We can find the answer at the beginning of the file or any inbound connection to the server.
Question 2: We can look for the first "Accepted password" string.
Question 3: We can look for connection times that are out of the ordinary, like late evening, night or early morning.
Question 4: We can see this by inspecting the login at the odd time.
Question 5: We can match the login time with the first command in bash history matching the same time frame.
Question 6: We can do the same as Q5, but look for the last command instead.
