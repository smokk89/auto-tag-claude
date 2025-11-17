# AI-Augmented Options Trading Scanner

A sophisticated Python command-line tool that scans options markets for profitable opportunities, fetches real-time data from multiple sources, and generates AI-powered trading signals from 5 different models.

## Features

- 🔍 **Options Scanning**: Scan specific tickers or auto-fetch top active stocks
- 🤖 **AI Integration**: Get trading signals from 5 AI models (Claude, Perplexity, Grok, Gemini, ChatGPT)
- 📊 **Rich Display**: Beautiful colored tables with blue background and white text
- 📈 **Key Metrics**: Premium %, probability, collateral, gains, and more
- 📁 **CSV Export**: Export results for further analysis
- ⚡ **Async Processing**: Fast parallel API calls

## Installation

1. **Clone/Download** the project files
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up API keys**:
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

## Usage

### Basic Examples

```bash
# Scan AVGO with defaults
python main.py AVGO

# Scan top 10 most active stocks
python main.py

# Custom scan with filters
python main.py --tickers BMNR,HIMS --type put --expiry 2025-08-22 --min_prob 60 --min_yield 5

# Export results to CSV
python main.py AAPL MSFT --export results.csv

# Use mock data for testing (no API keys needed)
python main.py --mock AAPL MSFT
```

### Command Line Arguments

- `tickers`: Space-separated list of ticker symbols (optional)
- `--tickers`: Comma-separated list of ticker symbols
- `--type`: Options type - `put` (default) or `call`
- `--expiry`: Expiry date in YYYY-MM-DD format (default: next Friday)
- `--min_prob`: Minimum probability percentage (default: 60)
- `--min_yield`: Minimum yield percentage (default: 5)
- `--export`: Export results to CSV file
- `--mock`: Use mock data for testing

### Demo Mode

Test the scanner with mock data (no API keys required):

```bash
python test_scanner.py
```

## API Keys Required

Get your API keys from these providers:

- **Alpha Vantage**: [alphavantage.co](https://www.alphavantage.co/support/#api-key) (free tier available)
- **Anthropic Claude**: [console.anthropic.com](https://console.anthropic.com/)
- **Perplexity**: [perplexity.ai/settings/api](https://www.perplexity.ai/settings/api)
- **xAI Grok**: [console.x.ai](https://console.x.ai/)
- **Google Gemini**: [aistudio.google.com](https://aistudio.google.com/app/apikey)
- **OpenAI**: [platform.openai.com](https://platform.openai.com/api-keys)

## Output Format

The scanner displays results in a blue-themed table with these columns:

| Column | Description |
|--------|-------------|
| Symbol | Stock ticker symbol |
| Type | PUT or CALL |
| Strike | Strike price |
| Expiry | Expiration date |
| Prob (%) | Probability of profit |
| Bid/Ask | Option bid/ask prices |
| Contracts | Trading volume |
| Premium | Premium amount and yield % |
| Collateral | Required collateral |
| Gains | Potential profit |
| Signal | AI-generated trading signal |
| Confidence Sources | Individual AI model confidences |

## File Structure

```
options-scanner/
├── main.py              # Entry point with CLI parsing
├── data_fetcher.py      # Options/stock data fetching
├── signal_generator.py  # AI model integration
├── display.py           # Table rendering and CSV export
├── test_scanner.py      # Demo script with mock data
├── requirements.txt     # Python dependencies
├── .env.example         # API key template
└── README.md           # This file
```

## Error Handling

- Graceful handling of API failures with fallback to mock data
- Rate limiting protection for API calls
- Input validation for all parameters
- Clear error messages for troubleshooting

## Customization

The scanner is designed to be extensible:

- Add new AI models in `signal_generator.py`
- Modify table styling in `display.py`
- Add new data sources in `data_fetcher.py`
- Customize option filtering logic in `main.py`

## License

MIT License - feel free to modify and distribute.

## Disclaimer
This tool is for educational and research purposes only. Always do your own research and consider consulting with a financial advisor before making any trading decisions. Options trading involves significant risk and may not be suitable for all investors.
