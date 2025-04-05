# AI Meme Generator

A full-stack AI-powered meme generator that creates original memes using Google's Gemini 1.5 Pro for text generation and ClipDrop for image generation.

## Features

- Uses Gemini 1.5 Pro for creative and contextual meme text generation
- Generates custom images using ClipDrop API
- Modern web interface built with Flask and Tailwind CSS
- Automatic text placement and formatting
- Error handling and fallback responses
- Configurable settings for customization

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Full-Stack-AI-Meme-Generator.git
cd Full-Stack-AI-Meme-Generator
```

2. Install the required packages:
```bash
pip install -r Requirements.txt
```

3. Set up your API keys:
   - Create an `api_keys.ini` file in the root directory
   - Add your API keys in the following format:
   ```ini
   [Keys]
   Gemini = your_gemini_api_key
   ClipDrop = your_clipdrop_api_key
   StabilityAI = your_stabilityai_api_key
   ```

4. Configure settings (optional):
   - Modify `settings.ini` to customize:
     - Model settings
     - Temperature
     - Output preferences
     - Font settings

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Enter your meme concept in the text box and click "Generate Meme"

## Configuration

### settings.ini
```ini
[AI Settings]
Text_Model = gemini-1.5-pro-002
Temperature = 0.7
Image_Platform = clipdrop
```

## Requirements

- Python 3.8+
- Google Gemini API key
- ClipDrop API key (for image generation)
- Internet connection for API access

## Error Handling

The application includes robust error handling for:
- API connection issues
- Content generation failures
- Image processing errors
- Invalid configurations

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Gemini for AI text generation
- ClipDrop for image generation
- Flask for web framework
- Tailwind CSS for styling
