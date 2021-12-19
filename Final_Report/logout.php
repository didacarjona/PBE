<?php
@session_start();
session_destroy();
header("Location: course_manager.html");
?>
