<html>
<body>

<?php
$command = $_POST["command"];
file_put_contents ("/home/pi/A3Display/www/html/controller_in.txt", $command, FILE_APPEND);
?>
</body>
</html>

