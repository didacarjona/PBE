<?php
	require_once 'dbconfig.php';
	$query = "SELECT `name` FROM students WHERE `student_id` = '{$student_id}' AND `name` = '{$name}'";
	$result = mysqli_query($connection, $query) or die("Error in Selecting " . mysqli_error($connection));
	$emparray1 = array();
        while($row =mysqli_fetch_assoc($result)) {
                $emparray1[] = $row;
	}
	if (count($emparray1) != 0) {
		$_SESSION['student_id'] = $student_id;
		$_SESSION['name'] = $name;
	}
	mysqli_close($connection);
?>

