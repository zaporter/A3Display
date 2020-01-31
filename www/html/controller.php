<html>
<body>

<?php
$file = 'controller_in.txt';
$command = $_POST["command"];
file_put_contents ($file, $command, FILE_APPEND);
?>
</body>
</html>

