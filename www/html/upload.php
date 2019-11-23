
<html>
<body>
<?php
#$fp = fopen('/home/pi/currentcode.py', 'w');
#fwrite($fp, $_POST["code"]);
#fclose($fp);

shell_exec("bash /home/pi/update.sh > /dev/null &");
?>
Preview: <?php echo $_POST["preview"]; ?><br>
Pass: <?php echo $_POST["password"]; ?>
Code: <?php echo $_POST["code"]; ?>
</body>
</html>

