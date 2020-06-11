$(document).ready(function (e) {
	
$(".frmUpload").on('submit',(function(e) {
	e.preventDefault();
	$(".upload-msg").text('Loading...');	
	$.ajax({
		url: "upload.php",
		type: "POST",
		data: new FormData(this),
		contentType: false,
		cache: false,
		processData:false,
		success: function(data)
		{
			$(".upload-msg").html(data);
		}
	});
}
));

$('#Point_to_Point').change(function() {
    var funtionID = $('#Point_to_Point').val();
    console.log(10);
    console.log(funtionID);
    
    if(funtionID == "exponential"){
    	$("#c_cons").html('Constante C : <input type="number" id="ccons" name="ccons" value=20 step=0.001>');
        $("#b_cons").html('Constante B : <input type="number" id="bcons" name="bcons" value=1.01 step=0.001>');
    }
    else if(funtionID == "logarithm"){
    	$("#c_cons").html('Constante C : <input type="number" id="ccons" name="ccons" value=70 step=0.001>');
        $("#b_cons").html('');
    }
    else if(funtionID == "squared"){
    	$("#c_cons").html('Constante C : <input type="number" id="ccons" name="ccons" value=15 step=0.001>');
        $("#b_cons").html('');
    }
    else if(funtionID == "thresholding"){
    	$("#c_cons").html('Valor minimo : <input type="number" id="ccons" name="ccons" value=190 step=0.001>');
        $("#b_cons").html('Valor maximo : <input type="number" id="bcons" name="bcons" value=200 step=0.001>');
    }
    else if(funtionID == "histogramEq"){
    	$("#c_cons").html('');
        $("#b_cons").html('');
    }
    else if(funtionID == "contrastSt"){
    	$("#c_cons").html('');
        $("#b_cons").html('');
    }
    else if(funtionID == "raisePower"){
    	$("#c_cons").html('Constante C : <input type="number" id="ccons" name="ccons" value=0.05 step=0.001>');
        $("#b_cons").html('Constante R : <input type="number" id="bcons" name="bcons" value=1.5 step=0.001>');
    }
    else if(funtionID == "multiplication"){
    	$("#c_cons").html('Constante C : <input type="number" id="ccons" name="ccons" value=2 step=0.001>');
        $("#b_cons").html('');
    }
    else if(funtionID == "add" || funtionID == "subtract" || funtionID == "divide" || funtionID == "Oand" || funtionID == "Oor" || funtionID == "Oxor"){
    	$("#c_cons").html('Segunda imagen: <input type="file" name="userImage1" id="userImage1" class="user-image" required />');
        $("#b_cons").html('');
    }
    else if(funtionID == "blending"){
        $("#c_cons").html('Segunda imagen: <input type="file" name="userImage1" id="userImage1" class="user-image" required />');
    	$("#b_cons").html('Constante X : <input type="number" id="bcons" name="bcons" value=0.25 step=0.001>');
    }
    $("#userImage1").change(function() {
		$(".upload-msg").empty(); 
		var file = this.files[0];
		var imagefile = file.type;
		var imageTypes= ["image/jpeg","image/png","image/jpg"];
		if(imageTypes.indexOf(imagefile) == -1)
		{
			$(".upload-msg").html("<span class='msg-error'>Please Select A valid Image File</span><br /><span>Only jpeg, jpg and png Images type allowed</span>");
			return false;
		}
		else
		{
			var reader = new FileReader();
			reader.onload = function(e){
				$(".img-preview1").html('<img src="' + e.target.result + '" />');				
			};
			reader.readAsDataURL(this.files[0]);
		}
	});
});

$("#userImage").change(function() {
	$(".upload-msg").empty(); 
	var file = this.files[0];
	var imagefile = file.type;
	var imageTypes= ["image/jpeg","image/png","image/jpg"];
	if(imageTypes.indexOf(imagefile) == -1)
	{
		$(".upload-msg").html("<span class='msg-error'>Please Select A valid Image File</span><br /><span>Only jpeg, jpg and png Images type allowed</span>");
		return false;
	}
	else
	{
		var reader = new FileReader();
		reader.onload = function(e){
			$(".img-preview").html('<img src="' + e.target.result + '" />');				
		};
		reader.readAsDataURL(this.files[0]);
	}
});	
});
