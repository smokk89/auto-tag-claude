# 📋 PROJECT OVERVIEW - Simple Explanation

## 🎯 **WHAT YOU ACTUALLY USE (2 Files)**

### 1. `smart_money_terminal_final.py` ⭐ **THIS IS THE ONE YOU USE**
- **What it does**: Shows options flow data in a clean table
- **Command**: `python smart_money_terminal_final.py SPX`
- **Output**: Clean table with TICKER, PRICE, TYPE, STRIKE, DTE, SPOT, VOLUME, OI, PREMIUM, BID/ASK, IV
- **Data**: Real data from Yahoo Finance (FREE, no API keys needed)
- **Status**: ✅ WORKING - This is what you've been using

### 2. `src/main.py` (via `main.py`)
- **What it does**: AI-powered options scanner with trading signals
- **Command**: `python main.py AAPL` or `python src/main.py AAPL`
- **Output**: Table with AI signals, probabilities, yields
- **Data**: Can use real data or mock data (`--mock` flag)
- **Status**: ✅ WORKING - More complex, has AI features

---

## 📁 **PROJECT STRUCTURE (What's Where)**


04btg/
│
├── smart_money_terminal_final.py  ⭐ USE THIS ONE
│   └── Standalone script - just run it with any ticker
│
├── src/                           (Modular code structure)
│   ├── main.py                    (Main entry point for AI scanner)
│   │
│   ├── data/                      (Data fetching)
│   │   └── sources/
│   │       ├── yahoo.py           (Yahoo Finance data)
│   │       └── polygon.py         (Polygon.io data - optional)
│   │
│   ├── ai/                        (AI signal generation)
│   │   └── generator.py          (5 AI models for trading signals)
│   │
│   ├── display/                   (Output formatting)
│   │   └── table.py              (Table display for main.py)
│   │
│   └── cli/                       (Command line parsing)
│       └── parser.py             (Argument parsing)
│
└── main.py                        (Redirects to src/main.py)
```

---

## 🔍 **WHAT EACH FILE DOES**

### **smart_money_terminal_final.py** (The one you use)
- **Purpose**: Simple options flow scanner
- **Input**: Ticker symbol (SPX, TSLA, NVDA, etc.)
- **Output**: Clean table showing unusual options activity
- **No dependencies**: Just needs `yfinance` library
- **No API keys**: Uses free Yahoo Finance data

### **src/main.py** (The AI scanner)
- **Purpose**: Advanced scanner with AI trading signals
- **Input**: Ticker symbols + filters (probability, yield, etc.)
- **Output**: Table with AI recommendations
- **Dependencies**: Needs API keys for AI models (optional)
- **Features**: 
  - Filters options by probability/yield
  - Gets AI signals from 5 models
  - Can export to CSV

### **src/data/sources/yahoo.py**
- **Purpose**: Fetches options data from Yahoo Finance
- **Used by**: Both `smart_money_terminal_final.py` and `src/main.py`
- **Status**: ✅ Working

### **src/display/table.py**
- **Purpose**: Formats and displays the table output
- **Used by**: `src/main.py` only
- **Not used by**: `smart_money_terminal_final.py` (has its own display)

---

## 🎯 **WHICH ONE SHOULD YOU USE?**

### Use `smart_money_terminal_final.py` if:
- ✅ You want simple, clean output
- ✅ You want to see options flow (volume, premium, etc.)
- ✅ You don't need AI signals
- ✅ You want it to "just work" with any ticker

**Command**: `python smart_money_terminal_final.py SPX`

### Use `src/main.py` if:
- ✅ You want AI-powered trading signals
- ✅ You want to filter by probability/yield
- ✅ You want CSV export
- ✅ You have API keys for AI models

**Command**: `python main.py AAPL` or `python src/main.py AAPL`

---

## 🔄 **CURRENT BRANCH STATUS**

You're on: **`master` branch**

Other branches:
- `admin/c1` - Old branch (probably not needed)
- `admin/c2` - Old branch (probably not needed)

**Recommendation**: Stay on `master` - that's where all the working code is.

---

## 💡 **QUICK REFERENCE**

### Run the simple scanner:
```bash
cd /Users/admin/.cursor/worktrees/Untitled__Workspace_/04btg
python smart_money_terminal_final.py SPX
```

### Run the AI scanner:
```bash
cd /Users/admin/.cursor/worktrees/Untitled__Workspace_/04btg
python main.py AAPL
```

### Test with mock data (no API keys):
```bash
python main.py --mock AAPL
```

---

## ❓ **COMMON QUESTIONS**

**Q: Why are there two different scanners?**
A: `smart_money_terminal_final.py` is simple and focused. `src/main.py` is more advanced with AI features.

**Q: Which one is better?**
A: Depends on what you need. For quick options flow data → use `smart_money_terminal_final.py`. For AI signals → use `src/main.py`.

**Q: Can I delete the other files?**
A: No, they're part of the modular structure. Just use what you need.

**Q: Where do I make changes?**
A: 
- For simple scanner → edit `smart_money_terminal_final.py`
- For AI scanner → edit files in `src/` folder

---

## 🎓 **SUMMARY**

**You have 2 main tools:**
1. **Simple scanner** (`smart_money_terminal_final.py`) - Just works, clean output
2. **AI scanner** (`src/main.py`) - More features, needs setup

**Everything else is supporting code** that makes these tools work.

**You're on the `master` branch** - that's fine, keep using it.

