<html>
<body>

<?php
echo shell_exec('echo 123 > testdir/yeah.txt');
?>
Welcome <?php echo $_POST["name"]; ?><br>
Your email address is: <?php echo $_POST["city"]; ?>
LS:
<?php
echo shell_exec("ls");
?>
</body>
</html>

