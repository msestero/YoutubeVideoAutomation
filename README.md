# YouTube Video Automation

Automation tools for YouTube video processing and management, featuring ChatGPT-powered script generation.

## 🚀 Features

### Current Features
- **AI Script Generation**: Use ChatGPT to generate professional YouTube video scripts
- **Multiple Variations**: Generate multiple script versions for the same topic
- **Structured Output**: Scripts organized with hooks, intros, main content, CTAs, and outros
- **Flexible Customization**: Customize video length, style, target audience, and requirements
- **Multiple Formats**: Save scripts as both JSON and readable text files

### Planned Features
- YouTube video upload automation
- Thumbnail generation
- Video editing automation
- Analytics tracking
- Batch processing

## 📋 Prerequisites

- Python 3.7+
- OpenAI API key (for ChatGPT script generation)
- YouTube API credentials (for future upload features)

## 🔧 Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/msestero/YoutubeVideoAutomation.git
   cd YoutubeVideoAutomation
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API keys**:
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and add your OpenAI API key
   nano .env
   ```

## 🔑 API Setup

### OpenAI API Key
1. Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Create a new API key
3. Add it to your `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 💡 Usage

### Command Line Interface

Generate a single script:
```bash
python generate_script.py "How to Start a YouTube Channel in 2024"
```

Generate with custom parameters:
```bash
python generate_script.py "Python Tutorial for Beginners" \
  --length "15-20 minutes" \
  --style "tutorial" \
  --audience "programming beginners" \
  --requirements "Include code examples and practical exercises"
```

Generate multiple variations:
```bash
python generate_script.py "Best Productivity Apps 2024" --variations 3
```

### Python API

```python
from script_generator import VideoScriptGenerator

# Initialize the generator
generator = VideoScriptGenerator()

# Generate a script
script = generator.generate_script(
    topic="How to Learn Python Fast",
    video_length="10-12 minutes",
    style="educational and engaging",
    target_audience="programming beginners",
    additional_requirements="Include practical tips and resources"
)

# Save the script
filename = generator.save_script(script)
print(f"Script saved to: {filename}")
```

## 📁 Project Structure

```
YoutubeVideoAutomation/
├── script_generator.py      # Main script generation class
├── generate_script.py       # CLI interface
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
├── README.md               # This file
└── scripts/                # Generated scripts (created automatically)
```

## 🎬 Script Structure

Generated scripts include:

1. **Hook** (0-15 seconds) - Attention-grabbing opening
2. **Introduction** - Channel intro and topic overview
3. **Main Content** - Core content broken into sections
4. **Call to Action** - Subscribe/like/comment prompts
5. **Outro** - Wrap-up and next video tease

Each section includes:
- Script text
- Stage directions
- Timing estimates

## 🛠️ Customization Options

- **Video Length**: "5-10 minutes", "15-20 minutes", etc.
- **Style**: "educational", "entertaining", "tutorial", "review", etc.
- **Target Audience**: "beginners", "professionals", "teenagers", etc.
- **Additional Requirements**: Any specific requests or constraints

## 📊 Output Formats

Scripts are saved in two formats:
- **JSON**: Structured data with separate sections
- **TXT**: Human-readable format for easy review

## 🔮 Future Enhancements

- Integration with YouTube API for direct uploads
- Automated thumbnail generation
- Video editing automation with MoviePy
- Analytics and performance tracking
- Batch processing for multiple videos
- Voice synthesis integration
- SEO optimization suggestions

## 🐛 Troubleshooting

### API Key Issues
```bash
# Check if your API key is set
echo $OPENAI_API_KEY

# Set it temporarily
export OPENAI_API_KEY="your-key-here"
```

### Common Errors
- **"API key required"**: Set your OpenAI API key in `.env` file
- **"Rate limit exceeded"**: Wait a moment and try again
- **"Model not found"**: Check your OpenAI account has access to GPT-4

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details

## 🔗 Links

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [YouTube API Documentation](https://developers.google.com/youtube/v3)
- [MoviePy Documentation](https://moviepy.readthedocs.io/)

---

Made with ❤️ for content creators
