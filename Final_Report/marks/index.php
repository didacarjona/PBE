<?php
        require_once '../dbconfig.php';
	if(!isset($client_web)) {
		$query_string = $_SERVER['QUERY_STRING'];
	} else {
		$query_string = $consulta;
	}
	parse_str($query_string,$variables);
        $query = "SELECT `subject`,`name`,`mark`  FROM `marks` WHERE `student_id`='{$variables[student_id]}'";
        if(count($variables) > 0) {
                foreach($variables as $key => $val) {
                        if($key != "limit" AND $key != "student_id") {
                                if(!is_array($val)){
                                        $query .= " AND {$key}='{$val}'";
                                }else{
                                        if($val[lt]!="0"){
                                                $query.=" AND `mark`<='{$val[lt]}'";
                                        }
                                }

                        }
                }
        }
        $query .= "ORDER BY `marks`.`subject` ASC";
        if(array_key_exists("limit",$variables)) {
                $query .= " LIMIT {$variables[limit]}";
        }
        $result = mysqli_query($connection, $query) or die("Error in Selecting " . mysqli_error($connection));
        $emparray = array();
        while($row =mysqli_fetch_assoc($result)) {
                $emparray[] = $row;
        }

	if(!isset($client_web)) {

        	echo json_encode(['marks' => $emparray]);
        }
	mysqli_close($connection);
?>
