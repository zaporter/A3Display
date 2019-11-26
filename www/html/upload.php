
<html>
<body>

<?php
if ($_POST["password"] == "a3best3") {
	file_put_contents("/home/pi/currentcode.py", $_POST["code"]);
	exec("bash /home/pi/update.sh > /dev/null &");
	$result = "Success";
}
else {
	$result = "Incorrect Password";
}
echo $result;
?>
</body>
</html>

