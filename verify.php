<?php
	$ver_code = $_POST["code"];
	
	# Connect to database
	$link=mysqli_connect("localhost","root","");
	$database=mysqli_select_db($link,"ruin");
	
	# Check if matching
	$result = mysqli_query($link, "SELECT info from `people` WHERE secret_code='$ver_code';");
	if(empty($result)){
		echo("<!DOCTYPE HTML><body><div class='midcenter'>Verification Incorrect</div></body></html>");
	}else{
		$get_string = mysqli_fetch_row($result)[0];
		header("Location: ruin_life.cgi?$get_string");
	}

?>