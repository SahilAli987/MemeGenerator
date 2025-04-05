from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from AIMemeGenerator import generate_meme
import configparser
import json

app = Flask(__name__)

# Load configuration
def load_config():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    return config

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        topic = data.get('topic', '')
        
        # Generate meme using the existing function
        result = generate_meme(topic)
        
        if result and 'meme_path' in result:
            return jsonify({
                'success': True,
                'meme_path': result['meme_path'],
                'text': result.get('text', ''),
                'image_prompt': result.get('image_prompt', '')
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to generate meme'
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/outputs/<path:filename>')
def serve_meme(filename):
    return send_from_directory('Outputs', filename)

@app.route('/settings', methods=['GET'])
def get_settings():
    config = load_config()
    return jsonify({
        'text_model': config.get('AI Settings', 'Text_Model'),
        'temperature': float(config.get('AI Settings', 'Temperature')),
        'image_platform': config.get('AI Settings', 'Image_Platform')
    })

if __name__ == '__main__':
    app.run(debug=True) 