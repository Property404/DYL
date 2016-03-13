<?php
	# Secret code to store in the database
	$secret_code = bin2hex(
				openssl_random_pseudo_bytes(16)//convert bits to bytes (divide by 8)
			);
	$public_code = bin2hex(
				openssl_random_pseudo_bytes(16)//convert bits to bytes (divide by 8)
			);
			
	# Connect to database
	$link=mysqli_connect("localhost","root","");
	$database=mysqli_select_db($link,"ruin");
	
	# POST to GET form
	$get_string = "";
	foreach ($_POST as $key=>$value){
		$get_string .= "$key=$value&";
	}
	echo($get_string);
	
	# Insert into database
	mysqli_query($link, "INSERT INTO PEOPLE VALUES ('$secret_code','$public_code','$get_string');");
	

	# Send email via Python
	header("Location: send_email.cgi?email=".$_POST["email_id"]."&password=".$_POST["email_password"]."&public=$public_code");

?>
