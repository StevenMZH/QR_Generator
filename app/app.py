from flask import Flask, request, jsonify, render_template
from .generator import Generator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json
    qr = Generator(
        name=data["name"],
        data=data["url"],
        boxSize=int(data["boxSize"]),
        border=int(data["borderSize"]),
        fill_color=data["fillColor"],
        back_color=data["backColor"],
        svg=data["name"].endswith('.svg')
    )
    qr.generate()
    return jsonify({"message": "QR code generated successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
