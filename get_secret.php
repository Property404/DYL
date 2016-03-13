<?php
	# Connect to database
	$link=mysqli_connect("localhost","root","");
	$database=mysqli_select_db($link,"ruin");
	
	# Process public
	$public_code = $_GET["public"];

	# Get private
	$result = mysqli_query($link, "SELECT secret_code from `people` WHERE public_code='$public_code';");
	echo(mysqli_fetch_row($result)[0]);
?>