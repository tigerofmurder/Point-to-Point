<?php



if($_SERVER['REQUEST_METHOD'] == "POST" && isset($_FILES["userImage"]["type"])){
	$msg = '';
	$uploaded = FALSE;
	$extensions = array("jpeg", "jpg", "png");
	$fileTypes = array("image/png","image/jpg","image/jpeg");
	$file = $_FILES["userImage"];
	$file_extension = strtolower(end(explode(".", $file["name"])));
	$target_Algorithim = $_POST['Point_to_Point'];
	$target_valueC = $_POST['ccons'];
	$target_valueB = $_POST['bcons'];
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
				$msg = 'Image Subida .....!!';
				$uploaded = TRUE;
			}
		}
	}
	else
	{
		$msg = '***archivo invalido***';
	}
	echo ($uploaded ? $msg : '<span class="msg-error">'.$msg.'</span>');
	
	if ($target_Algorithim=="thresholding"){
		echo '<br><img src="uploads/histograma.png">';
	}
	else if ($target_Algorithim=="histogramEq"){
		echo '<br><img src="uploads/histograma.png">';
	}
	
	$exe = "/opt/lampp/htdocs/proccess/".$target_Algorithim.".py";
	$dir_file = "/opt/lampp/htdocs/proccess/".$targetPath;
	
	echo '<br>',$exe, '<br>';
	echo $dir_file, '<br>';
	
	$message = exec("/home/tigerofmurder/anaconda3/bin/python3.7 '$exe' '$dir_file' '$target_valueC' '$target_valueB' 2>&1");
	print_r($message);
	echo '<br><img src="'.$message.'">';
}

die();
?>
