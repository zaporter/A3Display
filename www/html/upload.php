
<html>
<body>

<?php
file_put_contents("/home/pi/currentcode.py", $_POST["code"]);
exec("bash /home/pi/update.sh > /dev/null &");
?>
Preview: <?php echo $_POST["preview"]; ?><br>
</body>
</html>

