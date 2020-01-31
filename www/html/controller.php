<html>
<body>

<?php
$command = $_POST["command"];
file_put_contents ("controller_in.txt", $command, FILE_APPEND);
?>
</body>
</html>

