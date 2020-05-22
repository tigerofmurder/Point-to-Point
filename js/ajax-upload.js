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



// Function to preview image after validation

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
