<?php
	require_once '../dbconfig.php';


        if(!isset($client_web)) {
                $query_string = $_SERVER['QUERY_STRING'];
        } else {
                $query_string = $consulta;
        }
	parse_str($query_string, $variables);

	$query = "SELECT `date`,`subject`,`name` FROM `tasks` WHERE `student_id`='{$variables[student_id]}'";
	if(count($variables)>0){
		foreach($variables as $key => $val){
			if($key !="limit" AND $key!="student_id"){
				if(!is_array($val)){
					$query.=" AND `{$key}`='{$val}'";
				}else{
					$k=array_keys($val);
					switch($k[0]){
						case "gt":
						$query.=" AND `date`>";
						break;

						case "gte":
						$query.=" AND `date`>=";
						break;

						case "lt":
						$query.=" AND `date`<";
						break;

						case "lte":
						$query.=" AND `date`<=";
						break;
					}
					if($val[$k[0]]!="now"){
						$query.="'{$val[$k[0]]}'";
					}else{
						$query.="CURRENT_DATE";
					}
				}
			}
		}
	}
	$query .= " ORDER BY `date` ASC";
	if(array_key_exists("limit",$variables)){
		$query.= " LIMIT {$variables[limit]}";
	}
	$result = mysqli_query($connection,$query) or die("Error in Selecting " .mysqli_error($connection));
	$emparray = array();
	while($row = mysqli_fetch_assoc($result)){
		$emparray[] = $row;
	}

        if(!isset($client_web)) {

                echo json_encode(['tasks' => $emparray]);
        }


	mysqli_close($connection);
?>
