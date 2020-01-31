<!--Dev: Ted Clifford (c) 1.31.20-->
<html>
<body>

<?php
$file = 'controller2_in.txt';
$command = $_POST["command"];
file_put_contents ($file, $command, FILE_APPEND);
?>
</body>
</html>

