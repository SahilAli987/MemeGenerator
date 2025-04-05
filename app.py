from flask import Flask, render_template, request, jsonify
from AIMemeGenerator import generate_meme
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        topic = data.get('topic', '')
        
        if not topic:
            return jsonify({'error': 'Please provide a topic'}), 400
            
        # Generate meme using the existing function
        result = generate_meme(topic)
        
        if 'error' in result:
            return jsonify({'error': result['error']}), 500
            
        return jsonify({
            'success': True,
            'meme_text': result['meme_text'],
            'image_url': result['image_url']
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 