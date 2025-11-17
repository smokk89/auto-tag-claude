#!/usr/bin/env python3
"""
SMART MONEY TERMINAL - FINAL VERSION
Exactly like the screenshot but with 100% REAL verified data
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
from rich.align import Align
from rich import box
import sys
import time

class SmartMoneyTerminal:
    def __init__(self):
        self.console = Console()
        
    def get_market_hours(self):
        """Get market status and hours"""
        now = datetime.now()
        market_open = now.replace(hour=9, minute=30, second=0)
        market_close = now.replace(hour=16, minute=0, second=0)
        
        if now.weekday() >= 5:
            return "CLOSED", "Weekend"
        elif market_open <= now <= market_close:
            return "OPEN", "Trading Open"
        elif now < market_open:
            return "PRE-MARKET", "Pre-Market"
        else:
            return "AFTER-HOURS", "Trading Closed"
    
    def scan_smart_money(self, tickers):
        """Scan for REAL unusual options activity"""
        all_unusual = []
        
        for ticker in tickers:
            try:
                # Handle SPX ticker - needs ^ prefix for yfinance
                yf_ticker = f'^{ticker}' if ticker.upper() == 'SPX' else ticker
                stock = yf.Ticker(yf_ticker)
                info = stock.info
                current_price = info.get('currentPrice') or info.get('regularMarketPrice', 0)
                
                if not current_price:
                    continue
                
                # Get options for next 3 expiries
                expiries = stock.options[:3] if len(stock.options) >= 3 else stock.options
                
                for expiry in expiries:
                    opt_chain = stock.option_chain(expiry)
                    exp_date = datetime.strptime(expiry, '%Y-%m-%d')
                    dte = (exp_date - datetime.now()).days
                    
                    # Scan CALLS with REAL data
                    for _, row in opt_chain.calls.iterrows():
                        volume = int(row['volume']) if pd.notna(row['volume']) else 0
                        oi = int(row['openInterest']) if pd.notna(row['openInterest']) else 0
                        bid = row['bid'] if pd.notna(row['bid']) else 0
                        ask = row['ask'] if pd.notna(row['ask']) else 0
                        option_price = (bid + ask) / 2  # Option contract price
                        
                        if volume < 100 or bid == 0:
                            continue
                        
                        vol_oi_ratio = (volume / oi) if oi > 0 else 999
                        premium = option_price * volume * 100
                        
                        # Calculate score
                        score = 0
                        flags = []
                        
                        # Flags with emojis and text
                        # Check for extreme activity first
                        if vol_oi_ratio > 10 and oi > 100:
                            score += 40
                            flags.append("🔥 EXTREME")
                        elif vol_oi_ratio > 5 and oi > 100:
                            score += 30
                            flags.append("📈 HIGH")
                        elif vol_oi_ratio > 2:
                            score += 20
                            flags.append("👀 UNUSUAL")
                        
                        # Check for whale trades
                        if premium > 1000000:
                            score += 35
                            flags.append("🐋 WHALE")
                        elif premium > 500000:
                            score += 25
                            flags.append("💰 LARGE")
                        
                        # Check urgency
                        if dte <= 7:
                            score += 20
                            flags.append("⚡ URGENT")
                        
                        if True:  # Show all options with volume > 100
                            all_unusual.append({
                                'ticker': ticker,
                                'price': current_price,
                                'spot': option_price,  # Option contract price
                                'type': 'CALL',
                                'strike': row['strike'],
                                'expiry': expiry,
                                'dte': dte,
                                'volume': volume,
                                'oi': oi,
                                'ratio': vol_oi_ratio,
                                'bid': bid,
                                'ask': ask,
                                'premium': premium,
                                'iv': row['impliedVolatility'] if pd.notna(row['impliedVolatility']) else 0,
                                'score': score,
                                'flags': flags
                            })
                    
                    # Scan PUTS with REAL data
                    for _, row in opt_chain.puts.iterrows():
                        volume = int(row['volume']) if pd.notna(row['volume']) else 0
                        oi = int(row['openInterest']) if pd.notna(row['openInterest']) else 0
                        bid = row['bid'] if pd.notna(row['bid']) else 0
                        ask = row['ask'] if pd.notna(row['ask']) else 0
                        option_price = (bid + ask) / 2  # Option contract price
                        
                        if volume < 100 or bid == 0:
                            continue
                        
                        vol_oi_ratio = (volume / oi) if oi > 0 else 999
                        premium = option_price * volume * 100
                        
                        score = 0
                        flags = []
                        
                        # Flags with emojis and text
                        # Check for extreme activity first
                        if vol_oi_ratio > 10 and oi > 100:
                            score += 40
                            flags.append("🔥 EXTREME")
                        elif vol_oi_ratio > 5 and oi > 100:
                            score += 30
                            flags.append("📈 HIGH")
                        elif vol_oi_ratio > 2:
                            score += 20
                            flags.append("👀 UNUSUAL")
                        
                        # Check for whale trades
                        if premium > 1000000:
                            score += 35
                            flags.append("🐋 WHALE")
                        elif premium > 500000:
                            score += 25
                            flags.append("💰 LARGE")
                        
                        # Check urgency
                        if dte <= 7:
                            score += 20
                            flags.append("⚡ URGENT")
                        
                        if True:  # Show all options with volume > 100
                            all_unusual.append({
                                'ticker': ticker,
                                'price': current_price,
                                'spot': option_price,  # Option contract price
                                'type': 'PUT',
                                'strike': row['strike'],
                                'expiry': expiry,
                                'dte': dte,
                                'volume': volume,
                                'oi': oi,
                                'ratio': vol_oi_ratio,
                                'bid': bid,
                                'ask': ask,
                                'premium': premium,
                                'iv': row['impliedVolatility'] if pd.notna(row['impliedVolatility']) else 0,
                                'score': score,
                                'flags': flags
                            })
                            
            except Exception as e:
                continue
        
        # Sort by score
        all_unusual.sort(key=lambda x: x['score'], reverse=True)
        return all_unusual[:20]  # Top 20
    
    def create_main_table(self, data):
        """Create main table matching the screenshot style"""
        # Create table with exact styling
        table = Table(
            box=box.SQUARE,
            border_style="bright_cyan",
            header_style="bold white on blue",
            show_lines=True,
            padding=(0, 1)
        )
        
        # Headers exactly as in screenshot
        table.add_column("TICKER", style="bold cyan", width=8, justify="center")
        table.add_column("PRICE", style="white", width=10, justify="right")
        table.add_column("TYPE", style="yellow", width=6, justify="center")
        table.add_column("STRIKE", style="white", width=8, justify="right")
        table.add_column("DTE", style="dim white", width=5, justify="center")
        table.add_column("VOLUME", style="white", width=10, justify="right")
        table.add_column("OI", style="white", width=10, justify="right")
        table.add_column("V/OI", style="bold red", width=8, justify="right")
        table.add_column("PREMIUM", style="white", width=12, justify="right")
        table.add_column("BID/ASK", style="white", width=14, justify="right")
        table.add_column("IV", style="white", width=6, justify="right")
        table.add_column("FLAGS", style="bold yellow", width=25, justify="left")
        
        # Add rows with proper formatting
        for item in data:
            # Format flags exactly like screenshot
            flag_text = " ".join(item['flags'])
            
            # Format premium
            if item['premium'] >= 1000000:
                premium_text = f"${item['premium']/1000000:.1f}M"
            elif item['premium'] >= 1000:
                premium_text = f"${item['premium']/1000:.0f}K"
            else:
                premium_text = f"${item['premium']:.0f}"
            
            # Format V/OI
            ratio_text = f"{item['ratio']:.1f}x" if item['ratio'] < 100 else "NEW"
            
            # Color code premium based on size
            if item['premium'] > 1000000:
                premium_style = "bold green"
            elif item['premium'] > 100000:
                premium_style = "green"
            else:
                premium_style = "white"
            
            # Add row with colors matching screenshot
            table.add_row(
                item['ticker'],
                f"${item['price']:.2f}",
                item['type'],
                f"${item['strike']:.0f}",
                f"{item['dte']}d",
                f"{item['volume']:,}",
                f"{item['oi']:,}" if item['oi'] > 0 else "NEW",
                Text(ratio_text, style="bold red"),
                Text(premium_text, style=premium_style),
                f"${item['bid']:.2f}/${item['ask']:.2f}",
                f"{item['iv']:.0%}" if item['iv'] > 0 else "N/A",
                Text(flag_text, style="bold yellow")
            )
        
        return table
    
    def create_summary_panel(self, data):
        """Create market summary panel matching screenshot"""
        if not data:
            return Panel("No unusual activity detected", border_style="cyan")
        
        # Calculate metrics
        total_premium = sum(item['premium'] for item in data)
        call_premium = sum(item['premium'] for item in data if item['type'] == 'CALL')
        put_premium = sum(item['premium'] for item in data if item['type'] == 'PUT')
        
        whale_trades = len([item for item in data if 'WHALE' in item['flags']])
        extreme_trades = len([item for item in data if 'EXTREME' in item['flags']])
        urgent_trades = len([item for item in data if 'URGENT' in item['flags']])
        
        # Top tickers
        ticker_activity = {}
        for item in data:
            if item['ticker'] not in ticker_activity:
                ticker_activity[item['ticker']] = 0
            ticker_activity[item['ticker']] += item['premium']
        
        top_tickers = sorted(ticker_activity.items(), key=lambda x: x[1], reverse=True)[:3]
        
        market_status, status_text = self.get_market_hours()
        
        summary_text = f"""[bold cyan]SMART MONEY FLOW[/bold cyan]
Total Premium: [bold green]${total_premium/1000000:.1f}M[/bold green]
Call Flow: [green]${call_premium/1000000:.1f}M[/green] ({call_premium/total_premium*100:.0f}%)
Put Flow: [red]${put_premium/1000000:.1f}M[/red] ({put_premium/total_premium*100:.0f}%)

[bold cyan]ALERTS[/bold cyan]
🐋 Whale Trades: [bold yellow]{whale_trades}[/bold yellow]
🚨 Extreme V/OI: [bold red]{extreme_trades}[/bold red]
⏰ Urgent (≤7 DTE): [bold yellow]{urgent_trades}[/bold yellow]

[bold cyan]TOP ACTIVITY[/bold cyan]"""
        
        for ticker, premium in top_tickers:
            summary_text += f"\n{ticker}: ${premium/1000000:.1f}M"
        
        summary_text += f"\n\n[bold cyan]MARKET STATUS[/bold cyan]\n{market_status} - {status_text}"
        
        return Panel(
            summary_text, 
            title="📊 MARKET SUMMARY",
            border_style="bright_cyan",
            box=box.SQUARE
        )
    
    def create_legend_panel(self):
        """Create legend panel with emojis"""
        legend_text = """[bold cyan]FLAG MEANINGS[/bold cyan]
[bold]🐋 WHALE[/bold] = Premium > $1M
[bold]🔥 EXTREME[/bold] = V/OI > 10x  
[bold]⚡ URGENT[/bold] = Expires ≤7 days
[bold]📈 HIGH[/bold] = V/OI > 5x
[bold]👀 UNUSUAL[/bold] = V/OI > 2x
[bold]💰 LARGE[/bold] = Premium > $500K

[bold cyan]WHAT TO WATCH[/bold cyan]
• Multiple flags = Strong signal
• 🐋 + 🔥 = Institution loading
• ⚡ + 📈 = Event imminent
• NEW (no OI) = Fresh position

[bold cyan]DATA SOURCE[/bold cyan]
Yahoo Finance (FREE)
Refresh: Every scan"""
        
        return Panel(
            legend_text, 
            title="📖 LEGEND",
            border_style="bright_cyan",
            box=box.SQUARE
        )
    
    def print_text_output(self, data):
        """Print data in simple text format that won't get truncated"""
        # Print table header with SPOT column
        # Calculate exact widths to ensure IV column aligns properly
        header = f"{'TICKER':<8} {'PRICE':>10} {'TYPE':<6} {'STRIKE':>10} {'DTE':>3} {'SPOT':>12} {'VOLUME':>12} {'OI':>12} {'PREMIUM':>15} {'BID/ASK':>16} {'IV':>4}"
        print(header)
        print("-" * len(header))
        
        # Print each row
        for item in data:
            # Format premium
            if item['premium'] >= 1000000:
                premium_text = f"${item['premium']/1000000:.1f}M"
            elif item['premium'] >= 1000:
                premium_text = f"${item['premium']/1000:.0f}K"
            else:
                premium_text = f"${item['premium']:.0f}"
            
            # Format V/OI
            ratio_text = f"{item['ratio']:.1f}x" if item['ratio'] < 100 else "NEW"
            
            oi_text = f"{item['oi']:,}" if item['oi'] > 0 else "NEW"
            
            # Format BID/ASK to exactly 16 characters (matching header width)
            bid_ask_text = f"${item['bid']:>6.2f}/${item['ask']:<6.2f}"
            bid_ask_formatted = f"{bid_ask_text:>16}"
            
            # Format IV - ensure it aligns properly under IV header (right-aligned, 4 chars wide)
            iv_text = f"{item['iv']*100:.0f}%"
            iv_formatted = f"{iv_text:>4}"
            
            # Format DTE - ensure it's exactly 3 characters (e.g., "2d" or "10d")
            dte_text = f"{item['dte']}d" if isinstance(item['dte'], int) else str(item['dte'])
            dte_formatted = f"{dte_text:>3}"
            
            # Format SPOT (option contract price)
            spot_price = item.get('spot', 0)
            spot_formatted = f"${spot_price:>10.2f}"
            
            # Build row with SPOT column
            row = f"{item['ticker']:<8} ${item['price']:>8,.2f} {item['type']:<6} ${item['strike']:>9.0f} {dte_formatted:>3} {spot_formatted:>12} {item['volume']:>11,} {oi_text:>12} {premium_text:>15} {bid_ask_formatted} {iv_formatted}"
            print(row)
    
    def display_terminal(self, tickers):
        """Display terminal exactly like screenshot"""
        # Scan for activity first
        data = self.scan_smart_money(tickers)
        
        if not data:
            data = []
        
        # Always use clean text output
        self.print_text_output(data)

def main():
    terminal = SmartMoneyTerminal()
    
    # Check for --text flag
    force_text = '--text' in sys.argv
    if force_text:
        sys.argv.remove('--text')
        import os
        os.environ['FORCE_TEXT_OUTPUT'] = '1'
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--help":
            print("""
SMART MONEY TERMINAL - Professional Options Flow Scanner

Usage:
  python smart_money_terminal_final.py              # Default tickers
  python smart_money_terminal_final.py NVDA        # Single ticker
  python smart_money_terminal_final.py --top10     # Top 10 most active
  python smart_money_terminal_final.py SPY,QQQ     # Custom list
  python smart_money_terminal_final.py PLTR --text # Force text output

All data is 100% REAL from Yahoo Finance
Every strike and option shown can be verified on your broker
            """)
            return
        elif sys.argv[1] == "--top10":
            tickers = ['SPY', 'QQQ', 'NVDA', 'TSLA', 'AAPL', 'AMD', 'META', 'AMZN', 'MSFT', 'GOOGL']
        else:
            tickers = sys.argv[1].upper().split(',')
    else:
        # Default
        tickers = ['SPY', 'QQQ', 'NVDA', 'TSLA', 'AAPL', 'AMD', 'META', 'AMZN', 'MSFT', 'GOOGL']
    
    try:
        terminal.display_terminal(tickers)
    except KeyboardInterrupt:
        print("\n\nTerminal stopped.")

if __name__ == "__main__":
    main()