<?php

error_reporting(E_ERROR | E_WARNING | E_PARSE);


if($_SERVER['REQUEST_METHOD'] == "POST"){
	$cascade_value = $_POST['cascade'];
	$cont = $_POST['fcont'];
	if (!$_POST['fcont']){
		$cont = 0;
	}

    if($cascade_value == "True" and $cont>0){
		$targetPath = $_POST['fname'];
		//echo $targetPath;
	}
	else{
	    $msg = '';
	    $uploaded = FALSE;
	    $extensions = array("jpeg", "jpg", "png");
	    $fileTypes = array("image/png","image/jpg","image/jpeg");
	    $file = $_FILES["userImage"];
	    
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
					$msg = 'Image Subida .....!!';
					$uploaded = TRUE;
				}
			}
		}
		else
		{
			$msg = '***archivo invalido***';
		}
	}
	
	$target_Algorithim = $_POST['Point_to_Point'];
	$target_valueC = $_POST['ccons'];
	$target_valueB = $_POST['bcons'];
	if ($target_Algorithim=='add' or $target_Algorithim=="subtract" or $target_Algorithim=="blending" or $target_Algorithim=="divide" or $target_Algorithim=="Oand" or $target_Algorithim=="Oor" or $target_Algorithim=="Oxor"){
		$file1 = $_FILES["userImage1"];
		$sourcePath1 = $file1['tmp_name'];
		$targetPath1 = 'uploads/'.$file1['name'];
		move_uploaded_file($sourcePath1,$targetPath1);
	}
	if($target_Algorithim =='CamScan'){
		$p1x = $_POST['p1x'];
		$p1y = $_POST['p1y'];
		$p2x = $_POST['p2x'];
		$p2y = $_POST['p2y'];
		$p3x = $_POST['p3x'];
		$p3y = $_POST['p3y'];
		$p4x = $_POST['p4x'];
		$p4y = $_POST['p4y'];
	}
	
	
	
	$histogram = "false";
	
	if(!$target_valueC and !$target_valueB){$target_valueC=0;$target_valueB=0;}
	
	
	#echo ($uploaded ? $msg : '<span class="msg-error">'.$msg.'</span><br>');
	
	if ($target_Algorithim=="thresholding" or $target_Algorithim=="histogramEq"){
		//echo '<br><img src="uploads/histograma.png">';
		$histogram = 'uploads/histograma.png';
	}
	
	
	
	$exe = "/opt/lampp/htdocs/proccess/".$target_Algorithim.".py";
	$dir_file = "/opt/lampp/htdocs/proccess/".$targetPath;
	
	#echo '<br>',$exe, '<br>';
	#echo $dir_file, '<br>';
	
	if ($target_Algorithim=='add' or $target_Algorithim=="subtract" or $target_Algorithim=="Oand" or $target_Algorithim=="Oor" or $target_Algorithim=="Oxor" or $target_Algorithim=="blending" or $target_Algorithim=="divide"){
		$dir_file1 = "/opt/lampp/htdocs/proccess/".$targetPath1;
		if($target_Algorithim=="blending"){
			$message = exec("/home/tigerofmurder/anaconda3/bin/python3.7 '$exe' '$dir_file' '$dir_file1' '$target_valueB' 2>&1");
		}
		else{
			$message = exec("/home/tigerofmurder/anaconda3/bin/python3.7 '$exe' '$dir_file' '$dir_file1' 2>&1");
		}

		
	}
	else{
		if($target_Algorithim == 'CamScan'){
			$message = exec("/home/tigerofmurder/anaconda3/bin/python3.7 '$exe' '$dir_file' '$p1x' '$p1y' '$p2x' '$p2y' '$p3x' '$p3y' '$p4x' '$p4y' 2>&1");
			
		}
		else{
			$message = exec("/home/tigerofmurder/anaconda3/bin/python3.7 '$exe' '$dir_file' '$target_valueC' '$target_valueB' 2>&1");
		}
			
	}
	
	#print_r($message);
	//echo '<img src="'.$message.'">';
	//$array['success'] = $message;
	echo json_encode(array('success' => $message, 'histogram' => $histogram,"cont"=>$p1x));
	//echo json_encode($array)
}

die();
?>
