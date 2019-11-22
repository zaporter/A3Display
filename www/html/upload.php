<html>
<body>

<?php
echo shell_exec('echo 123 > testdir/yeah.txt');
?>
Welcome <?php echo $_POST["preview"]; ?><br>
Code: <?php echo $_POST["code"]; ?>

LS:
<?php
echo shell_exec("ls");
?>
</body>
</html>

