
<html>
<body>

<?php
$hash = "$2y$10$5BiJzTZOAznF6.wi2r066Oa3mrGievQd92xoJTVm6ypvTcSeHWpN2";
if (password_verify($_POST["password"], $hash)){
	file_put_contents("/home/pi/currentcode.py", $_POST["code"]);
	exec("bash /home/pi/update.sh > /dev/null &");
	$result = "Success";
}
else {
	$result = "Incorrect Password";
}
echo $result;
/*echo password_hash("pw", PASSWORD_DEFUALT);*/
?>
</body>
</html>

