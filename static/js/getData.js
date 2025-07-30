function updateQRImage() {
    var name = document.getElementById('QR_name').value;
    var url = document.getElementById('QR_URL').value;
    var boxSize = document.getElementById('QR_boxSize').value;
    var borderSize = document.getElementById('QR_borderSize').value;
    var fillColor = document.getElementById('QR_fillColor').value;
    var backColor = document.getElementById('QR_backColor').value;

    // Enviar los datos al servidor Flask utilizando AJAX
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/generate_qr', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            console.log('QR code generated successfully!');
        }
    };
    xhr.send(JSON.stringify({
        name: name,
        url: url,
        boxSize: boxSize,
        borderSize: borderSize,
        fillColor: fillColor,
        backColor: backColor
    }));
}

document.getElementById('qrForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
    updateQRImage();
});
