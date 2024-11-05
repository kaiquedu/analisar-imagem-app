from flask import Flask, request, jsonify, send_from_directory 
from flask_cors import CORS
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from googletrans import Translator
import torch

app = Flask(__name__, static_folder='../frontend', static_url_path='/') 
CORS(app)

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

translator = Translator()

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

@app.route('/analyze-image', methods=['POST'])
def analyze_image():
    if 'image' not in request.files:
        return jsonify({'error': 'Nenhum arquivo de imagem fornecido.'}), 400
    
    file = request.files['image']
    
    try:
        image = Image.open(file.stream).convert("RGB")
    except Exception as e:
        return jsonify({'error': f'Erro ao abrir a imagem: {str(e)}'}), 400

    inputs = processor(images=image, return_tensors="pt").to(device)

    out = model.generate(
        **inputs,
        max_new_tokens=50,  
        num_beams=3,        
        early_stopping=True
    )
    
    description = processor.decode(out[0], skip_special_tokens=True)

    translated_description = translator.translate(description, dest='pt').text

    return jsonify({'prompt': translated_description}), 200

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)