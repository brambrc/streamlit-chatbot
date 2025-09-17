# AI Chatbot with Streamlit

A modern, interactive AI chatbot built with Streamlit that supports multiple AI models via OpenRouter API.

## Features

### 🎨 **Enhanced UI Design**
- Professional chat interface with custom styling
- Responsive sidebar for settings
- Typing animation effects
- Clean message bubbles and modern layout

### 🤖 **Multiple AI Models**
- **Mistral 7B (Free)** - Powerful open-source model with good general capabilities
- **DeepSeek V3 (Free)** - Advanced model with strong reasoning abilities  
- **Llama 3.1 8B (Free)** - Meta's latest model with broad knowledge

### ⚙️ **Customizable Settings**
- Temperature control (0.0 - 1.0) for response creativity
- Model selection with descriptions
- Clear chat history functionality
- Real-time configuration

### 🚀 **User Experience**
- Real-time typing effect for AI responses
- Loading spinners and status indicators
- Error handling and user feedback
- Message history persistence
- Responsive design

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/brambrc/streamlit-chatbot.git
   cd streamlit-chatbot
   ```

2. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install streamlit requests
   ```

4. **Set up API Key:**
   - Get your API key from [OpenRouter](https://openrouter.ai/)
   - Add your API key to the `get_ai_response` function in the code
   
## Usage

1. **Run the basic chatbot:**
   ```bash
   streamlit run chatbot.py
   ```

2. **Run the enhanced chatbot (recommended):**
   ```bash
   streamlit run newchatbot.py
   ```

3. **Open your browser and navigate to:**
   - Local: `http://localhost:8501`
   - Network: `http://[your-ip]:8501`

## Project Structure

```
streamlit-chatbot/
├── chatbot.py          # Basic chatbot implementation
├── newchatbot.py       # Enhanced chatbot with advanced features
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
└── venv/              # Virtual environment (not tracked)
```

## Configuration

### API Setup
1. Sign up at [OpenRouter](https://openrouter.ai/)
2. Get your API key
3. Replace the empty `api_key` variable in the code:
   ```python
   api_key = "your-api-key-here"
   ```

### Model Selection
Choose from three free AI models:
- **Mistral 7B**: Best for general conversations
- **DeepSeek V3**: Excellent for reasoning tasks
- **Llama 3.1 8B**: Great for diverse knowledge queries

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [OpenRouter AI](https://openrouter.ai/)
- Uses free AI models from Mistral, DeepSeek, and Meta

---

**Made with ❤️ using Streamlit**
