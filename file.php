<?php
error_reporting(E_ERROR | E_WARNING | E_PARSE);


$msg = '';
$uploaded = FALSE;
$extensions = array("jpeg", "jpg", "png");
$fileTypes = array("image/png","image/jpg","image/jpeg");
$file = $_FILES["file"];


$file_extension = strtolower(end(explode(".", $file["name"])));
if (in_array($file["type"],$fileTypes) && in_array($file_extension, $extensions)) {
	if ($file["error"] > 0)
	{
		$msg = 'Error Code: ' . $file["error"];
	}
	else
	{
		if (file_exists("upload/" . $file["name"])) {
			$msg = $file["name"].' ya existe.';				
		}
		else
		{
			$sourcePath = $file['tmp_name'];
			$targetPath = 'uploads/'.$file['name'];
			move_uploaded_file($sourcePath,$targetPath);
			$uploaded = TRUE;
		}
	}
}
else
{
	$msg = '***archivo invalido***';
}
if($uploaded == TRUE){
	$dir_file = "/opt/lampp/htdocs/proccess/".$targetPath;
	$message = exec("/home/tigerofmurder/anaconda3/bin/python3.7 /opt/lampp/htdocs/proccess/esquinas.py '$dir_file' 2>&1");
	echo $message;
}

?>
