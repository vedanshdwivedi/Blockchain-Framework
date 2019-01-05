<?php
		
	require_once('config.php');
	//echo "<br><h2>Functions Added</h2>";
	//HELPER FUNCTIONS

	//This Function will redirect to pages
	function redirect($value){
		header("Location: $value");
	}

	//This Function will query database
	function query($sql){
		global $connection;
		return mysqli_query($connection,$sql);
		//echo "<br>".$sql;
	}

	//This Function will display appropriate message if no result of query is obtained
	function confirm($result){
		global $connection;
		if(!$result){
			die("Query Failed : ".mysqli_error($connection));
		}
	}

	//This Function will trim user input strings to avoid SQL Injections
	function escape_string($string){
		global $connection;
		return mysqli_real_escape_string($connection,strip_tags($string));
	}

	//This Function will fetch data from associative arrays
	function fetch($result){
		return mysqli_fetch_assoc($result);
	}

?>