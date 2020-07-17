<html>
<head>
<title>Algortimos punto a punto</title>
<link rel="stylesheet" href="style.css" />
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script src="js/ajax-upload.js"></script>


</head>
<body>
    
    <div class="img-upload">
        <h1 style="text-align: center;">Algortimos</h1>
        <form class="frmUpload" action="" method="post">
            <input type="checkbox" id="cascade" name="cascade" value="True">
            <label for="vehicle1"> EJECUTAR EN CASCADA </label><br>
            <p>Selecciona Algoritmo:
            <select id="Point_to_Point" name="Point_to_Point">
                <option value="exponential">Exponential Operator</option>
                <option value="logarithm">Logarithm Operator</option>
                <option value="thresholding">thresholding</option>
                <option value="histogramEq">Histogram Equalization</option>
                <option value="contrastSt">Contrast Stretching</option>
                <option value="squared">Squared Operator</option>
                <option value="raisePower">Raise of the Power</option>
                <option value="multiplication">Mulplication</option>
                <option value="blending">Blending</option>
                <option value="add">Add</option>
                <option value="subtract">Subtraction</option>
                <option value="divide">Divide</option>
                <option value="Oand">Operator AND</option>
                <option value="Oor">Operator OR</option>
                <option value="Oxor">Operator XOR</option>
                <option value="CamScan">Cam Scanner</option>
            </select>
            </p>
            <p id="c_cons" name="c_cons">Constante c:
                <input type="number" id="ccons" name="ccons" value=20 step=0.001>
            </p>
            <p id="b_cons" name="c_cons">Constante b:
                <input type="number" id="bcons" name="bcons" value=20 step=0.001>
            </p>
            <label>Subir Imagen:</label>
            <p id="image_change" name="image_change">
            <input type="file" name="userImage" id="userImage" class="user-image" required" />
            </p>
            <input type="submit" value="UPLOAD" class="btn-upload" />
        </form>
        <div class="img-preview"></div>
        <canvas width="600" height="800" id="my_canvas"></canvas>
        <div class="img-preview1"></div>
        <div class="upload-msg"></div>
    </div>
    
</body>
</html>
