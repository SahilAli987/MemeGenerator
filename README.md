# AI Meme Generator with Gemini API

An AI-powered meme generator that creates clever and original memes using Google's Gemini API for text generation and ClipDrop for image generation.

## Features

- Uses Gemini API for creative and contextual meme text generation
- Generates high-quality images using ClipDrop API
- Customizable settings for meme generation
- Supports various image styles and themes
- Automatic text placement on images
- Saves generated memes with timestamps

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- ClipDrop API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/SahilAli987/MemeGenerator.git
cd MemeGenerator
```

2. Install required packages:
```bash
pip install -r Requirements.txt
```

3. Set up API keys:
   - Copy `assets/api_keys_empty.ini` to `api_keys.ini`
   - Add your API keys to `api_keys.ini`:
     ```ini
     [API Keys]
     Gemini_API_Key = your_gemini_api_key_here
     ClipDrop_API_Key = your_clipdrop_api_key_here
     ```

4. Configure settings (optional):
   - Modify `settings.ini` to customize:
     - Text model (default: gemini-1.5-pro-002)
     - Temperature
     - Image generation settings
     - Output preferences

## Usage

1. Run the meme generator:
```bash
python AIMemeGenerator.py
```

2. Follow the prompts to:
   - Enter a topic or theme for your meme
   - Wait for the AI to generate text and image
   - Find your generated meme in the `Outputs` folder

## Example Topics

Try these topics for fun memes:
- "programming bugs"
- "monday mornings"
- "cats being cats"
- "artificial intelligence"
- "weekend plans"

## Configuration

### Basic Settings (settings.ini)
```ini
[Basic]
Basic_Instructions = You will create funny memes that are clever and original
Image_Special_Instructions = The images should be photographic

[AI Settings]
Text_Model = gemini-1.5-pro-002
Temperature = 0.7
Image_Platform = clipdrop
```

## Output

Generated memes are saved in the `Outputs` folder with timestamps:
- Format: `meme_YYYY-MM-DD-HH-MM_N.png`
- A log file (`log.txt`) tracks all generations

## Troubleshooting

1. API Key Issues:
   - Ensure your API keys are correctly set in `api_keys.ini`
   - Verify your Gemini API key has sufficient credits
   - Check ClipDrop API key validity

2. Generation Errors:
   - Check internet connection
   - Verify Python version compatibility
   - Ensure all dependencies are installed correctly

3. Image Generation Issues:
   - Make sure prompts are clear and appropriate
   - Check ClipDrop API status
   - Verify output directory permissions

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Gemini API for text generation
- ClipDrop API for image generation
- Python imaging libraries for meme composition
