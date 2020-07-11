$(document).ready(function (e) {

var canvas = document.getElementById('my_canvas');
var context = canvas.getContext('2d');
var direction = null;


var img_salide = "";


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
			console.log(data);
			var values = $.parseJSON(data)
			console.log(values.success);
			console.log(values.cont);
			img_salide = values.success;
			if (values.histogram == "false"){
                $(".upload-msg").html('<img src="' + values.success + '" />');
            }
            else{
                $(".upload-msg").html('<img src="' + values.histogram + '" /><br><img src="' + values.success + '" />');
            }
            
            //var value_cas = $('#cascade :checked').val();
			//	console.log(value_cas);
			if (document.getElementById('cascade').checked){
				console.log("True cascade");
				//console.log(document.getElementById("userImage").value);
				//document.getElementById("userImage").value = values.success;
				//$("#userImage").attr("value",values.success);
				$("#image_change").html('<input type="text" id="fname" name="fname" value="' + img_salide + '" /><input type="number" id="fcont" name="fcont" value="' + values.cont + '" />');
				//console.log(document.getElementById("userImage").value);
				$(".img-preview").html('<img src="' + img_salide + '" />');
				
			}
			else{
			    //$("#image_change").html('<input type="file" name="userImage" id="userImage" class="user-image" required" />');
				console.log("False cascade");
			}
			//$("#userImage").val("");
		}
	});
}
));

$('#Point_to_Point').change(function() {
    var funtionID = $('#Point_to_Point').val();
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
    else if(funtionID == "CamScan"){
        $("#c_cons").html('Point1x: <input type="number" id="p1x" min="0" max="600" step="0.001" disabled><br>Point1y: <input type="number" id="p1y" min="0" max="600" step="0.001" disabled><br><br>Point2x: <input type="number" id="p2x" min="0" max="600" step="0.001" disabled><br>Point2y: <input type="number" id="p2y" min="0" max="600" step="0.001" disabled>');
        $("#b_cons").html('Point3x: <input type="number" id="p3x" min="0" max="600" step="0.001" disabled><br>Point3y: <input type="number" id="p3y" min="0" max="600" step="0.001" disabled><br><br>Point4x: <input type="number" id="p4x" min="0" max="600" step="0.001" disabled><br>Point4y: <input type="number" id="p4y" min="0" max="600" step="0.001" disabled>');
        if(context){
            console.log("INICIADO");
            /*points_draw(0,0);
            points_draw(0,100);
            points_draw(100,0);
            function points_draw(x,y){
                var pointSize = 3;
                context.fillStyle = "#ff2626";
                context.beginPath();
                context.arc(x, y, pointSize, 0, Math.PI * 2, true);
                context.fill();
            }*/
            if (canvas && canvas.getContext) {
                if (context) {
                    drawImg(direction,0,0);
                    context.globalAlpha = 0.25;
                    var isDragging = false;
                    var delta = new Object();

                    function oMousePos(canvas, evt) {
                        var rect = canvas.getBoundingClientRect();
                        return { // devuelve un objeto
                            x: Math.round(evt.clientX - rect.left),
                            y: Math.round(evt.clientY - rect.top)
                        };
                    }

                    function dibujarUnPoligono(X, Y, R, L, paso, color) {
                        var beta = L / paso;
                        var rad = (2 * Math.PI) / beta;
                        context.fillStyle = color;
                        context.beginPath();
                        for (var i = 0; i < L; i++) {
                            x = X + R * Math.cos(rad * i);
                            y = Y + R * Math.sin(rad * i);
                            context.lineTo(x, y);
                        }
                        context.closePath();
                        context.fill();
                    }
                    function actvalue(){
                        document.getElementById("p1x").value = poligonosRy[0].X;
                        document.getElementById("p1y").value = poligonosRy[0].Y;
                        document.getElementById("p2x").value = poligonosRy[1].X;
                        document.getElementById("p2y").value = poligonosRy[1].Y;
                        document.getElementById("p3x").value = poligonosRy[2].X;
                        document.getElementById("p3y").value = poligonosRy[2].Y;
                        document.getElementById("p4x").value = poligonosRy[3].X;
                        document.getElementById("p4y").value = poligonosRy[3].Y;
                    }
                    function dibujarPoligonos() {
                        for (var i = 0; i < poligonosRy.length; i++) {
                            dibujarUnPoligono(poligonosRy[i].X, poligonosRy[i].Y, poligonosRy[i].R, poligonosRy[i].L, poligonosRy[i].paso, poligonosRy[i].color);
                        }
                        console.log(poligonosRy[0].Y);
                        actvalue();
                    }

                    var poligonosRy = [
                        {'X':10, 'Y':10,'R':8, 'L':4, 'paso':1,'color':'#FF0E00', 'bool':false},
                        {'X':200, 'Y':10,'R':8, 'L':4, 'paso':1,'color':'#FF0E00', 'bool':false},
                        {'X':10, 'Y':200,'R':8, 'L':4, 'paso':1,'color':'#FF0E00', 'bool':false},
                        {'X':200, 'Y':200,'R':8, 'L':4, 'paso':1,'color':'#FF0E00', 'bool':false}
                    ];


                    poligonosRy.sort(function(a, b) {
                        return b.R - a.R
                    })
                    
                    dibujarPoligonos();

                    // click mouse
                    canvas.addEventListener('mousedown', function(evt) {
                        isDragging = true;
                        var mousePos = oMousePos(canvas, evt);
                        for (var i = 0; i < poligonosRy.length; i++) {
                            //dibujarUnPoligono(X,Y,R,L,paso,color)	
                            dibujarUnPoligono(poligonosRy[i].X, poligonosRy[i].Y, poligonosRy[i].R, poligonosRy[i].L, poligonosRy[i].paso, poligonosRy[i].color);
                            if (context.isPointInPath(mousePos.x, mousePos.y)) {
                                poligonosRy[i].bool = true;
                                delta.x = poligonosRy[i].X - mousePos.x;
                                delta.y = poligonosRy[i].Y - mousePos.y;
                                break;
                            }
                            else {
                                poligonosRy[i].bool = false;
                            }
                        }

                        drawImg(direction,0,0);
                        dibujarPoligonos();
                    }, false);

                    // se mueve el mouse
                    canvas.addEventListener('mousemove', function(evt) {
                        if (isDragging) {
                            var mousePos = oMousePos(canvas, evt);
                            for (var i = 0; i < poligonosRy.length; i++) {
                                if (poligonosRy[i].bool) {
                                    drawImg(direction,0,0);
                                    X = mousePos.x + delta.x, Y = mousePos.y + delta.y
                                    poligonosRy[i].X = X;
                                    poligonosRy[i].Y = Y;
                                    break;
                                }
                            }
                            dibujarPoligonos();
                        }
                    }, false);

                    // no click mouse
                    canvas.addEventListener('mouseup', function(evt) {
                        isDragging = false;
                        for (var i = 0; i < poligonosRy.length; i++) {
                            poligonosRy[i].bool = false
                        }
                        drawImg(direction,0,0);
                        dibujarPoligonos();
                    }, false);

                    // mouse fuera de rango
                    canvas.addEventListener('mouseout', function(evt) {
                        isDragging = false;
                        for (var i = 0; i < poligonosRy.length; i++) {
                            poligonosRy[i].bool = false
                        }
                        drawImg(direction,0,0);
                        dibujarPoligonos();
                    }, false);
                    
                }
            }
        }
        else{
            console.log("NO INICIADO");
        }
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
			//$(".img-preview").html('<img src="' + e.target.result + '" />');
			direction = e.target.result;
			drawImg(e.target.result,0,0);
		};
		reader.readAsDataURL(this.files[0]);
	}
});
function drawImg(src,x,y){
    var imgPath = src;
    var imgObj = new Image();
    imgObj.src = imgPath;
    var x = 0;
    var y = 0;
    imgObj.onload = function(){
        scaleToFit(this);
        //context.drawImage(imgObj, x, y);
        //context.drawImage(imgObj, x, y, imgObj.width * 0.3, imgObj.height * 0.3);
    };
    function scaleToFit(img){
        var scale = Math.min(canvas.width / img.width, canvas.height / img.height);
        var x = (canvas.width / 2) - (img.width / 2) * scale;
        var y = (canvas.height / 2) - (img.height / 2) * scale;
        context.drawImage(img, x, y, img.width * scale, img.height * scale);
    }
}
});
