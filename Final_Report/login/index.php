<?php
	require_once '../dbconfig.php';
	if(isset($_GET["student_id"])) {
		$student_id = $_GET["student_id"];
	}
	$query = "SELECT `name` FROM students WHERE `student_id` = '{$student_id}'";
	$result = mysqli_query($connection, $query) or die("Error in Selecting " . mysqli_error($connection));
	$emparray = array();
        while($row =mysqli_fetch_assoc($result)) {
                $emparray[] = $row;
	}
	if (count($emparray) == 0) {
		$none =  array("NONE");
		echo json_encode($none);
	} else {
		echo json_encode(['students' => $emparray]);
	}
	mysqli_close($connection);
?>

