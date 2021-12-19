<?php
	$client_web = true;
	$phpfile = parse_url($consulta,PHP_URL_PATH);
	$consulta = parse_url($consulta, PHP_URL_QUERY);
	switch($phpfile){
		case 'timetables':
			include("./timetables/index.php");
			break;
		case 'marks':
			include("./marks/index.php");
			break;
		case 'tasks':
			include("./tasks/index.php");
			break;
	}
?>
