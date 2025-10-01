import yfinance as yf
import streamlit as st
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
import requests
import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta
import time

# =============================================================================
# RATE LIMITING AND CACHING
# =============================================================================

# Global variables for rate limiting
last_request_time = 0
REQUEST_DELAY = 2  # seconds between requests

def rate_limited_request():
    """Ensure we don't make requests too frequently"""
    global last_request_time
    current_time = time.time()
    time_since_last = current_time - last_request_time
    
    if time_since_last < REQUEST_DELAY:
        time.sleep(REQUEST_DELAY - time_since_last)
    
    last_request_time = time.time()

@st.cache_data(ttl=300)  # Cache for 5 minutes
def cached_fetch_stock_data(ticker, period):
    """Cached version of stock data fetching"""
    try:
        rate_limited_request()  # Add rate limiting
        stock = yf.Ticker(ticker)
        info = stock.info
        hist = stock.history(period=period)
        
        if hist.empty:
            return None
            
        return hist, info
            
    except Exception as e:
        if "Too Many Requests" in str(e):
            st.error("🚫 Rate limit exceeded. Please wait 1-2 minutes.")
        else:
            st.error(f"Error fetching data: {str(e)}")
        return None

@st.cache_data(ttl=600)  # Cache exchange rates for 10 minutes
def cached_get_exchange_rate(base_currency, target_currency):
    """Cached version of exchange rate fetching"""
    return get_exchange_rate_impl(base_currency, target_currency)

# =============================================================================
# MAIN APP FUNCTION
# =============================================================================

def show_financial_calculators():
    """Main function to display the financial calculators dashboard"""
    setup_page_config()
    load_custom_css()
    
    st.title("📈 Advanced Financial Calculators & Market Data")
    
    # Create tabs for different calculators
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Stock Analysis", "💰 Investment Calculator", "💱 Currency Converter", 
        "🏠 Mortgage Calculator", "🎯 Retirement Planner"
    ])
    
    with tab1:
        show_stock_analysis()
    with tab2:
        show_investment_calculator()
    with tab3:
        show_currency_converter()
    with tab4:
        show_mortgage_calculator()
    with tab5:
        show_retirement_planner()

# =============================================================================
# SETUP FUNCTIONS
# =============================================================================

def setup_page_config():
    """Configure the Streamlit page settings"""
    st.set_page_config(
        page_title="Financial Calculators", 
        page_icon="📈", 
        layout="wide"
    )

def load_custom_css():
    """Load custom CSS styles for the app"""
    st.markdown("""
    <style>
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
.calculator-box {
    background: #f0f8ff;  /* Light blue background */
    padding: 2rem;
    border-radius: 15px;
    border-left: 5px solid #667eea;
    margin: 1rem 0;
    color: #1a365d;  /* Dark blue text */
    font-weight: 500;
    border: 1px solid #c3dafe;
}
    .risk-high { background: linear-gradient(135deg, #dc3545 0%, #c82333 100%) !important; }
    .risk-medium { background: linear-gradient(135deg, #ffc107 0%, #e0a800 100%) !important; }
    .risk-low { background: linear-gradient(135deg, #28a745 0%, #218838 100%) !important; }
    </style>
    """, unsafe_allow_html=True)

# =============================================================================
# STOCK ANALYSIS FUNCTIONS
# =============================================================================

def show_stock_analysis():
    """Display the stock analysis calculator with real-time data"""
    st.header("📊 Real-time Stock Analysis & Technical Indicators")
    
    # Add warning about rate limits
    st.warning("""
    ⚠️ **Note:** Stock data is rate-limited. If you see errors, please wait a few moments before trying again.
    Data is cached for 5 minutes to reduce API calls.
    """)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        ticker, period, indicators = get_stock_inputs()
    
    with col2:
        if ticker:
            analyze_and_display_stock(ticker, period, indicators)

def get_stock_inputs():
    """Get user inputs for stock analysis"""
    st.subheader("Stock Search")
    
    # Initialize session state for stock selection
    if 'selected_stock' not in st.session_state:
        st.session_state.selected_stock = "AAPL"
    
    ticker = st.text_input("Enter stock symbol (e.g., AAPL, TSLA, GOOGL):", st.session_state.selected_stock).upper()
    
    period = st.selectbox(
        "Time Period:",
        ["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"],
        index=2
    )
    
    # Technical indicators
    st.subheader("Technical Indicators")
    show_ma = st.checkbox("Moving Averages", value=True)
    show_rsi = st.checkbox("RSI", value=True)
    show_volume = st.checkbox("Volume", value=True)
    show_macd = st.checkbox("MACD", value=False)
    
    # Quick stock buttons
    display_quick_stock_buttons()
    
    return ticker, period, {
        'show_ma': show_ma,
        'show_rsi': show_rsi, 
        'show_volume': show_volume,
        'show_macd': show_macd
    }

def display_quick_stock_buttons():
    """Display quick selection buttons for popular stocks"""
    st.markdown("---")
    st.markdown("**💡 Popular Stocks:**")
    popular_stocks = ["AAPL", "TSLA", "GOOGL", "MSFT", "AMZN", "NVDA", "META", "BRK-B"]
    cols = st.columns(4)
    
    for idx, stock in enumerate(popular_stocks):
        with cols[idx % 4]:
            if st.button(stock, key=f"stock_{stock}"):
                st.session_state.selected_stock = stock
                st.rerun()

def analyze_and_display_stock(ticker, period, indicators):
    """Main function to analyze and display stock data"""
    try:
        # Use cached function with rate limiting
        stock_data = cached_fetch_stock_data(ticker, period)
        if not stock_data:
            st.error(f"Unable to fetch data for {ticker}. Please try again in a few moments.")
            return
            
        hist, info = stock_data
        
        # Display all stock information
        display_stock_overview(ticker, info, hist)
        display_price_chart(ticker, hist, period, indicators['show_ma'])
        
        if indicators['show_rsi']:
            display_rsi_indicator(hist)
            
        if indicators['show_macd']:
            display_macd_indicator(hist)
            
        if indicators['show_volume']:
            display_volume_chart(hist)
            
        display_company_details(info)
        
    except Exception as e:
        if "Too Many Requests" in str(e):
            st.error("🚫 Rate limit exceeded. Please wait 1-2 minutes before making another request.")
            st.info("💡 Tip: Use the cached data for popular stocks, or try again shortly.")
        else:
            st.error(f"Error analyzing {ticker}: {str(e)}")

def display_stock_overview(ticker, info, hist):
    """Display stock overview and key metrics"""
    st.subheader(f"📊 {ticker} - {info.get('longName', 'N/A')}")
    
    # Calculate current metrics
    current_price = get_current_price(info, hist)
    prev_close = get_previous_close(info, hist)
    
    # Display metrics in columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        display_price_metric(current_price, prev_close)
    
    with col2:
        display_market_cap(info)
    
    with col3:
        display_pe_ratio(info)
    
    with col4:
        display_dividend_yield(info)

def get_current_price(info, hist):
    """Extract current price from stock data"""
    return info.get('currentPrice', 
           info.get('regularMarketPrice', 
           hist['Close'].iloc[-1] if not hist.empty else 'N/A'))

def get_previous_close(info, hist):
    """Extract previous close price from stock data"""
    return info.get('previousClose', 
           hist['Close'].iloc[-2] if len(hist) > 1 else 'N/A')

def display_price_metric(current_price, prev_close):
    """Display current price with change"""
    if current_price != 'N/A' and prev_close != 'N/A':
        change = current_price - prev_close
        change_pct = (change / prev_close) * 100
        st.metric(
            "Current Price", 
            f"${current_price:.2f}",
            f"{change:+.2f} ({change_pct:+.2f}%)"
        )
    else:
        st.metric("Current Price", "N/A")

def display_market_cap(info):
    """Display formatted market cap"""
    market_cap = info.get('marketCap', 'N/A')
    if market_cap != 'N/A':
        if market_cap >= 1e12:
            st.metric("Market Cap", f"${market_cap/1e12:.2f}T")
        elif market_cap >= 1e9:
            st.metric("Market Cap", f"${market_cap/1e9:.2f}B")
        else:
            st.metric("Market Cap", f"${market_cap:,.0f}")
    else:
        st.metric("Market Cap", "N/A")

def display_pe_ratio(info):
    """Display P/E ratio"""
    pe_ratio = info.get('trailingPE', 'N/A')
    st.metric("P/E Ratio", f"{pe_ratio:.2f}" if pe_ratio != 'N/A' else "N/A")

def display_dividend_yield(info):
    """Display dividend yield"""
    dividend_yield = info.get('dividendYield', 0)
    if dividend_yield:
        st.metric("Dividend Yield", f"{dividend_yield*100:.2f}%")
    else:
        st.metric("Dividend Yield", "0%")

def display_price_chart(ticker, hist, period, show_ma):
    """Display the main price chart with optional moving averages"""
    st.subheader("📈 Advanced Price Chart")
    fig = go.Figure()
    
    # Candlestick chart
    fig.add_trace(go.Candlestick(
        x=hist.index,
        open=hist['Open'],
        high=hist['High'],
        low=hist['Low'],
        close=hist['Close'],
        name='Price'
    ))
    
    # Add moving averages if requested
    if show_ma and len(hist) > 20:
        add_moving_averages(fig, hist)
    
    fig.update_layout(
        title=f"{ticker} Stock Price - {period}",
        xaxis_title="Date",
        yaxis_title="Price ($)",
        height=500,
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)

def add_moving_averages(fig, hist):
    """Add moving averages to the price chart"""
    hist['MA20'] = hist['Close'].rolling(window=20).mean()
    hist['MA50'] = hist['Close'].rolling(window=50).mean()
    
    fig.add_trace(go.Scatter(
        x=hist.index, y=hist['MA20'],
        mode='lines', name='MA20',
        line=dict(color='orange', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=hist.index, y=hist['MA50'],
        mode='lines', name='MA50',
        line=dict(color='red', width=2)
    ))

def display_rsi_indicator(hist):
    """Display RSI technical indicator"""
    if len(hist) > 14:
        st.subheader("📊 Technical Indicators")
        
        # Calculate RSI
        hist['RSI'] = calculate_rsi(hist['Close'])
        
        fig_rsi = go.Figure()
        fig_rsi.add_trace(go.Scatter(
            x=hist.index, y=hist['RSI'],
            mode='lines', name='RSI',
            line=dict(color='purple', width=2)
        ))
        fig_rsi.add_hline(y=70, line_dash="dash", line_color="red", annotation_text="Overbought")
        fig_rsi.add_hline(y=30, line_dash="dash", line_color="green", annotation_text="Oversold")
        fig_rsi.update_layout(title="Relative Strength Index (RSI)", height=300)
        st.plotly_chart(fig_rsi, use_container_width=True)

def calculate_rsi(prices, window=14):
    """Calculate Relative Strength Index"""
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def display_macd_indicator(hist):
    """Display MACD technical indicator"""
    if len(hist) > 26:
        macd_data = calculate_macd(hist['Close'])
        
        fig_macd = go.Figure()
        fig_macd.add_trace(go.Scatter(x=hist.index, y=macd_data['macd'], name='MACD', line=dict(color='blue')))
        fig_macd.add_trace(go.Scatter(x=hist.index, y=macd_data['signal'], name='Signal', line=dict(color='red')))
        fig_macd.add_trace(go.Bar(x=hist.index, y=macd_data['histogram'], name='Histogram', marker_color='gray'))
        
        fig_macd.update_layout(title="MACD Indicator", height=300)
        st.plotly_chart(fig_macd, use_container_width=True)

def calculate_macd(prices, fast=12, slow=26, signal=9):
    """Calculate MACD indicator"""
    exp1 = prices.ewm(span=fast).mean()
    exp2 = prices.ewm(span=slow).mean()
    macd = exp1 - exp2
    signal_line = macd.ewm(span=signal).mean()
    histogram = macd - signal_line
    
    return {'macd': macd, 'signal': signal_line, 'histogram': histogram}

def display_volume_chart(hist):
    """Display trading volume chart"""
    fig_volume = go.Figure()
    colors = ['red' if hist['Close'].iloc[i] < hist['Open'].iloc[i] else 'green' 
             for i in range(len(hist))]
    
    fig_volume.add_trace(go.Bar(
        x=hist.index, y=hist['Volume'],
        name='Volume',
        marker_color=colors
    ))
    fig_volume.update_layout(title="Trading Volume", height=300)
    st.plotly_chart(fig_volume, use_container_width=True)

def display_company_details(info):
    """Display detailed company information"""
    st.subheader("📋 Company Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        **Sector:** {info.get('sector', 'N/A')}  
        **Industry:** {info.get('industry', 'N/A')}  
        **52 Week High:** ${info.get('fiftyTwoWeekHigh', 'N/A')}  
        **52 Week Low:** ${info.get('fiftyTwoWeekLow', 'N/A')}  
        **Volume:** {info.get('volume', 'N/A'):,}
        **Beta:** {info.get('beta', 'N/A')}
        """)
    
    with col2:
        st.markdown(f"""
        **EPS:** ${info.get('trailingEps', 'N/A')}  
        **ROE:** {info.get('returnOnEquity', 'N/A')}  
        **Profit Margin:** {info.get('profitMargins', 'N/A')}  
        **Employees:** {info.get('fullTimeEmployees', 'N/A'):,}
        **Forward P/E:** {info.get('forwardPE', 'N/A')}
        """)

# =============================================================================
# INVESTMENT CALCULATOR FUNCTIONS - FIXED VERSION
# =============================================================================

def show_investment_calculator():
    """Display the investment calculator with advanced features"""
    st.header("💰 Advanced Investment Calculator")
    
    st.markdown("""
    <div class="calculator-box">
    Calculate the future value of your investments with compound interest, tax implications, and risk analysis
    </div>
    """, unsafe_allow_html=True)
    
    # Get user inputs
    investment_params = get_investment_inputs()
    
    # Calculate and display results
    if st.button("🚀 Calculate Future Value", type="primary"):
        calculate_and_display_investment_results(investment_params)

def get_investment_inputs():
    """Get user inputs for investment calculation"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Investment Parameters")
        initial_investment = st.number_input("Initial Investment ($)", min_value=0.0, value=10000.0, step=1000.0)
        monthly_contribution = st.number_input("Monthly Contribution ($)", min_value=0.0, value=500.0, step=100.0)
        years = st.slider("Investment Period (Years)", min_value=1, max_value=50, value=20)
        investment_type = st.selectbox("Investment Type", ["Stocks", "Bonds", "Real Estate", "Mixed Portfolio", "Cryptocurrency"])
    
    with col2:
        st.subheader("Return Expectations")
        expected_return = st.slider("Expected Annual Return (%)", min_value=1.0, max_value=30.0, value=7.0, step=0.5)
        inflation = st.slider("Expected Annual Inflation (%)", min_value=0.0, max_value=10.0, value=2.5, step=0.1)
        contribution_increase = st.slider("Annual Contribution Increase (%)", min_value=0.0, max_value=10.0, value=2.0, step=0.5)
        tax_rate = st.slider("Estimated Tax Rate on Gains (%)", min_value=0.0, max_value=50.0, value=15.0, step=1.0)
    
    return {
        'initial_investment': float(initial_investment),
        'monthly_contribution': float(monthly_contribution),
        'years': int(years),
        'investment_type': investment_type,
        'expected_return': float(expected_return),
        'inflation': float(inflation),
        'contribution_increase': float(contribution_increase),
        'tax_rate': float(tax_rate)
    }

def calculate_and_display_investment_results(params):
    """Calculate and display investment results with visualizations"""
    try:
        with st.spinner("Calculating your financial future..."):
            # Perform calculations
            results = calculate_advanced_investment(**params)
            
            if results and 'future_value' in results:
                # Display results
                display_investment_results(results)
                display_risk_analysis(params)
                display_investment_visualizations(results, params)
            else:
                st.error("Unable to calculate investment results. Please check your inputs.")
    
    except Exception as e:
        st.error(f"Error calculating investment results: {str(e)}")
        st.info("Please check that all input values are valid numbers.")

def calculate_advanced_investment(initial_investment, monthly_contribution, years,
                                expected_return, inflation, contribution_increase, tax_rate, **kwargs):
    """Calculate advanced investment scenario with taxes and inflation"""
    try:
        # Convert all inputs to float to ensure numerical operations
        initial_investment = float(initial_investment)
        monthly_contribution = float(monthly_contribution)
        years = int(years)
        expected_return = float(expected_return)
        inflation = float(inflation)
        contribution_increase = float(contribution_increase)
        tax_rate = float(tax_rate)
        
        monthly_rate = expected_return / 100 / 12
        months = years * 12
        
        # Calculate future value with compounding
        future_value = initial_investment
        total_contributions = initial_investment
        current_monthly = monthly_contribution
        
        projection_data = []
        
        for year in range(1, years + 1):
            # Add monthly contributions for the year
            for month in range(12):
                future_value += current_monthly
                future_value *= (1 + monthly_rate)
                total_contributions += current_monthly
            
            projection_data.append({
                'Year': year,
                'Portfolio Value': float(future_value),
                'Contributions': float(total_contributions)
            })
            
            # Increase monthly contribution for next year
            current_monthly *= (1 + contribution_increase / 100)
        
        # Calculate taxes and inflation adjustments
        interest_earned = future_value - total_contributions
        taxes_paid = interest_earned * (tax_rate / 100)
        after_tax = future_value - taxes_paid
        real_value = after_tax / ((1 + inflation/100) ** years)
        
        return {
            'future_value': float(future_value),
            'real_value': float(real_value),
            'after_tax': float(after_tax),
            'interest_earned': float(interest_earned),
            'taxes_paid': float(taxes_paid),
            'initial_investment': float(initial_investment),
            'total_contributions': float(total_contributions),
            'projection_data': pd.DataFrame(projection_data)
        }
    
    except Exception as e:
        st.error(f"Error in investment calculation: {str(e)}")
        # Return default values in case of error
        return {
            'future_value': 0.0,
            'real_value': 0.0,
            'after_tax': 0.0,
            'interest_earned': 0.0,
            'taxes_paid': 0.0,
            'initial_investment': float(initial_investment),
            'total_contributions': float(initial_investment),
            'projection_data': pd.DataFrame()
        }

def display_investment_results(results):
    """Display the main investment results"""
    st.success("🎉 Calculation Complete!")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
        <h3>Future Value</h3>
        <h2>${results['future_value']:,.2f}</h2>
        <p>Nominal amount</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card risk-low">
        <h3>Real Value</h3>
        <h2>${results['real_value']:,.2f}</h2>
        <p>Inflation-adjusted</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
        <h3>After Tax</h3>
        <h2>${results['after_tax']:,.2f}</h2>
        <p>Net amount</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card risk-medium">
        <h3>Interest Earned</h3>
        <h2>${results['interest_earned']:,.2f}</h2>
        <p>Investment growth</p>
        </div>
        """, unsafe_allow_html=True)

def display_risk_analysis(params):
    """Display risk analysis based on investment parameters"""
    st.subheader("📊 Risk Analysis")
    risk_profile = analyze_investment_risk(params['investment_type'], params['expected_return'], params['years'])
    
    st.markdown(f"""
    <div class="metric-card risk-{risk_profile['risk_level']}">
    <h3>Risk Profile: {risk_profile['risk_level'].upper()}</h3>
    <p>{risk_profile['description']}</p>
    </div>
    """, unsafe_allow_html=True)

def analyze_investment_risk(investment_type, expected_return, years):
    """Analyze risk profile based on investment parameters"""
    risk_scores = {
        "Bonds": 1,
        "Real Estate": 2,
        "Mixed Portfolio": 3,
        "Stocks": 4,
        "Cryptocurrency": 5
    }
    
    base_risk = risk_scores.get(investment_type, 3)
    
    # Adjust risk based on return and time horizon
    if expected_return > 15:
        base_risk += 1
    if years < 5:
        base_risk += 1
    
    base_risk = max(1, min(5, base_risk))
    
    risk_levels = {
        1: {"risk_level": "low", "description": "Conservative - Low volatility, stable returns"},
        2: {"risk_level": "low", "description": "Moderately Conservative - Some growth with stability"},
        3: {"risk_level": "medium", "description": "Moderate - Balanced risk and return"},
        4: {"risk_level": "medium", "description": "Moderately Aggressive - Growth-oriented with some risk"},
        5: {"risk_level": "high", "description": "Aggressive - High growth potential with significant risk"}
    }
    
    return risk_levels[base_risk]

def display_investment_visualizations(results, params):
    """Display investment visualizations and charts"""
    # Investment breakdown pie chart
    st.subheader("📈 Investment Breakdown")
    breakdown_data = {
        "Component": ["Initial Investment", "Total Contributions", "Interest Earned", "Taxes", "Net Value"],
        "Amount": [
            results['initial_investment'],
            results['total_contributions'] - results['initial_investment'],
            results['interest_earned'],
            results['taxes_paid'],
            results['after_tax']
        ]
    }
    
    fig_pie = px.pie(breakdown_data, values='Amount', names='Component', title="Investment Composition")
    st.plotly_chart(fig_pie, use_container_width=True)
    
    # Growth projection chart
    st.subheader("📊 Growth Projection")
    if not results['projection_data'].empty:
        fig_projection = px.line(results['projection_data'], x='Year', y='Portfolio Value', 
                               title="Portfolio Growth Over Time")
        fig_projection.update_traces(line=dict(width=4))
        st.plotly_chart(fig_projection, use_container_width=True)
    
    # Monte Carlo simulation
    st.subheader("🎯 Monte Carlo Simulation")
    monte_carlo_paths = run_monte_carlo_simulation(
        results['initial_investment'], 
        params['monthly_contribution'] * 12,  # Annual contribution
        params['years'], 
        params['expected_return']
    )
    if monte_carlo_paths:
        display_monte_carlo_chart(monte_carlo_paths, params['years'])

def run_monte_carlo_simulation(initial, annual_contribution, years, expected_return, simulations=100):
    """Run Monte Carlo simulation for investment returns"""
    try:
        results = []
        
        for _ in range(simulations):
            portfolio_value = float(initial)
            path = [portfolio_value]
            
            for year in range(years):
                # Random return based on expected return with some volatility
                annual_return = np.random.normal(expected_return, max(expected_return * 0.3, 5)) / 100
                portfolio_value = portfolio_value * (1 + annual_return) + annual_contribution
                path.append(max(portfolio_value, 0))  # Ensure non-negative
            
            results.append(path)
        
        return results
    
    except Exception as e:
        st.error(f"Error in Monte Carlo simulation: {str(e)}")
        return []

def display_monte_carlo_chart(monte_carlo_paths, years):
    """Display Monte Carlo simulation chart"""
    fig = go.Figure()
    
    # Plot individual simulation paths
    for i in range(min(50, len(monte_carlo_paths))):
        fig.add_trace(go.Scatter(
            x=list(range(years + 1)),
            y=monte_carlo_paths[i],
            mode='lines',
            line=dict(width=1, color='lightblue'),
            showlegend=False
        ))
    
    # Add mean line
    mean_path = np.mean(monte_carlo_paths, axis=0)
    fig.add_trace(go.Scatter(
        x=list(range(years + 1)),
        y=mean_path,
        mode='lines',
        line=dict(width=3, color='red'),
        name='Average Path'
    ))
    
    fig.update_layout(
        title="Monte Carlo Simulation - Possible Investment Paths",
        xaxis_title="Years",
        yaxis_title="Portfolio Value ($)"
    )
    st.plotly_chart(fig, use_container_width=True)

# =============================================================================
# CURRENCY CONVERTER FUNCTIONS
# =============================================================================

def show_currency_converter():
    """Display the currency converter with real-time exchange rates"""
    st.header("💱 Real-time Currency Converter")
    
    col1, col2 = st.columns(2)
    
    with col1:
        amount, base_currency, target_currency = get_currency_inputs()
    
    with col2:
        display_quick_conversion_buttons()
    
    # Perform conversion
    if st.button("🔁 Convert Currency", type="primary"):
        convert_currency(amount, base_currency, target_currency)

def get_currency_inputs():
    """Get user inputs for currency conversion"""
    st.subheader("Convert Currency")
    amount = st.number_input("Amount", min_value=0.01, value=100.0, step=10.0)
    
    col1a, col1b = st.columns(2)
    with col1a:
        base_currency = st.selectbox("From", ["USD", "EUR", "IDR", "SGD", "MYR", "JPY", "GBP", "AUD"], index=0)
    with col1b:
        target_currency = st.selectbox("To", ["IDR", "USD", "EUR", "SGD", "MYR", "JPY", "GBP", "AUD"], index=1)
    
    return amount, base_currency, target_currency

def display_quick_conversion_buttons():
    """Display quick conversion buttons for popular currency pairs"""
    st.subheader("💡 Popular Conversions")
    popular_conversions = [
        ("USD", "IDR", "Dollar to Rupiah"),
        ("EUR", "USD", "Euro to Dollar"),
        ("USD", "SGD", "Dollar to Singapore Dollar"),
        ("USD", "MYR", "Dollar to Malaysian Ringgit"),
    ]
    
    for base, target, label in popular_conversions:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{label}**")
        with col2:
            if st.button(f"🔄", key=f"{base}_{target}"):
                st.session_state.quick_convert = (base, target)
                st.rerun()

def convert_currency(amount, base_currency, target_currency):
    """Perform currency conversion and display results"""
    if base_currency == target_currency:
        st.warning("Please select different currencies")
        return
        
    with st.spinner("Getting latest exchange rates..."):
        rate = get_exchange_rate(base_currency, target_currency)
        
        if rate:
            converted_amount = amount * rate
            display_conversion_results(amount, base_currency, converted_amount, target_currency, rate)
        else:
            st.error("Unable to fetch exchange rate. Please try again later.")

def get_exchange_rate(base_currency, target_currency):
    """Get exchange rate from API with fallback (uses cached version)"""
    return cached_get_exchange_rate(base_currency, target_currency)

def get_exchange_rate_impl(base_currency, target_currency):
    """Actual implementation of exchange rate fetching"""
    try:
        rate_limited_request()  # Add rate limiting
        
        # Try multiple free API endpoints
        apis = [
            f"https://api.exchangerate-api.com/v4/latest/{base_currency}",
            f"https://open.er-api.com/v6/latest/{base_currency}",
        ]
        
        for api_url in apis:
            try:
                response = requests.get(api_url, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    rate = data['rates'].get(target_currency, None)
                    if rate:
                        return rate
            except:
                continue
        
        # Fallback rates
        return get_fallback_exchange_rate(base_currency, target_currency)
        
    except Exception as e:
        st.error(f"API Error: {str(e)}")
        return None

def get_fallback_exchange_rate(base_currency, target_currency):
    """Provide fallback exchange rates if API fails"""
    fallback_rates = {
        'USD': {'IDR': 15500, 'EUR': 0.92, 'SGD': 1.35, 'MYR': 4.75, 'JPY': 150.50, 'GBP': 0.79, 'AUD': 1.52},
        'EUR': {'USD': 1.09, 'IDR': 16900, 'SGD': 1.47, 'MYR': 5.18, 'JPY': 164.00, 'GBP': 0.86, 'AUD': 1.66},
        'IDR': {'USD': 0.000064, 'EUR': 0.000059, 'SGD': 0.000087, 'MYR': 0.00031, 'JPY': 0.0097, 'GBP': 0.000051, 'AUD': 0.000098},
    }
    return fallback_rates.get(base_currency, {}).get(target_currency, 1.0)

def display_conversion_results(amount, base_currency, converted_amount, target_currency, rate):
    """Display currency conversion results"""
    st.success(f"**💱 Conversion Result:**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
        <h3>From</h3>
        <h2>{amount:,.2f} {base_currency}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <h1>➡️</h1>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card risk-low">
        <h3>To</h3>
        <h2>{converted_amount:,.2f} {target_currency}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    st.info(f"**Exchange Rate:** 1 {base_currency} = {rate:.4f} {target_currency}")

# =============================================================================
# MORTGAGE CALCULATOR FUNCTIONS
# =============================================================================

def show_mortgage_calculator():
    """Display the mortgage calculator with amortization schedule"""
    st.header("🏠 Advanced Mortgage Calculator")
    
    st.markdown("""
    <div class="calculator-box">
    Calculate your monthly mortgage payments, amortization schedule, and compare different loan options
    </div>
    """, unsafe_allow_html=True)
    
    # Get mortgage inputs
    mortgage_params = get_mortgage_inputs()
    
    # Calculate and display results
    if st.button("🏠 Calculate Mortgage", type="primary"):
        calculate_and_display_mortgage_results(mortgage_params)

def get_mortgage_inputs():
    """Get user inputs for mortgage calculation"""
    col1, col2 = st.columns(2)
    
    with col1:
        home_price = st.number_input("Home Price ($)", min_value=10000.0, value=500000.0, step=10000.0)
        down_payment_pct = st.slider("Down Payment (%)", min_value=0.0, max_value=100.0, value=20.0, step=1.0)
        loan_term = st.selectbox("Loan Term (Years)", [10, 15, 20, 30], index=3)
        loan_type = st.selectbox("Loan Type", ["Fixed Rate", "Adjustable Rate (ARM)", "FHA", "VA"])
    
    with col2:
        interest_rate = st.slider("Interest Rate (%)", min_value=0.1, max_value=15.0, value=6.5, step=0.1)
        property_tax = st.number_input("Annual Property Tax ($)", min_value=0.0, value=5000.0, step=500.0)
        home_insurance = st.number_input("Annual Home Insurance ($)", min_value=0.0, value=1500.0, step=100.0)
        pmi_rate = st.slider("PMI Rate (%) (if down payment < 20%)", min_value=0.0, max_value=2.0, value=0.5, step=0.1)
    
    # Additional inputs
    hoa_fees = st.number_input("Monthly HOA Fees ($) (if applicable)", min_value=0.0, value=0.0, step=50.0)
    
    return {
        'home_price': home_price,
        'down_payment_pct': down_payment_pct,
        'loan_term': loan_term,
        'loan_type': loan_type,
        'interest_rate': interest_rate,
        'property_tax': property_tax,
        'home_insurance': home_insurance,
        'pmi_rate': pmi_rate,
        'hoa_fees': hoa_fees
    }

def calculate_and_display_mortgage_results(params):
    """Calculate and display mortgage results"""
    # Calculate basic mortgage values
    loan_amount = params['home_price'] * (1 - params['down_payment_pct'] / 100)
    down_payment = params['home_price'] - loan_amount
    
    # Calculate monthly payments
    monthly_payment = calculate_monthly_mortgage_payment(loan_amount, params['interest_rate'], params['loan_term'])
    total_monthly = calculate_total_monthly_payment(monthly_payment, params)
    
    # Display results
    display_mortgage_results(loan_amount, down_payment, monthly_payment, total_monthly)
    display_mortgage_breakdown(monthly_payment, params)
    display_amortization_schedule(loan_amount, params['interest_rate'], params['loan_term'])
    display_mortgage_analysis(loan_amount, params['loan_term'], monthly_payment, params)

def calculate_monthly_mortgage_payment(loan_amount, interest_rate, loan_term):
    """Calculate monthly mortgage payment (principal + interest)"""
    monthly_rate = interest_rate / 100 / 12
    total_payments = loan_term * 12
    
    if monthly_rate > 0:
        return loan_amount * (monthly_rate * (1 + monthly_rate) ** total_payments) / ((1 + monthly_rate) ** total_payments - 1)
    else:
        return loan_amount / total_payments

def calculate_total_monthly_payment(monthly_payment, params):
    """Calculate total monthly payment including taxes, insurance, etc."""
    pmi_payment = 0
    if params['down_payment_pct'] < 20:
        pmi_payment = (params['home_price'] * (1 - params['down_payment_pct'] / 100) * (params['pmi_rate'] / 100)) / 12
    
    return (monthly_payment + 
            (params['property_tax'] / 12) + 
            (params['home_insurance'] / 12) + 
            pmi_payment + 
            params['hoa_fees'])

def display_mortgage_results(loan_amount, down_payment, monthly_payment, total_monthly):
    """Display main mortgage calculation results"""
    st.success("📊 Mortgage Calculation Complete!")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Loan Amount", f"${loan_amount:,.2f}")
    with col2:
        st.metric("Down Payment", f"${down_payment:,.2f}")
    with col3:
        st.metric("Monthly Payment (P&I)", f"${monthly_payment:,.2f}")
    with col4:
        st.metric("Total Monthly", f"${total_monthly:,.2f}")

def display_mortgage_breakdown(monthly_payment, params):
    """Display mortgage payment breakdown"""
    st.subheader("💰 Payment Breakdown")
    
    pmi_payment = 0
    if params['down_payment_pct'] < 20:
        pmi_payment = (params['home_price'] * (1 - params['down_payment_pct'] / 100) * (params['pmi_rate'] / 100)) / 12
    
    breakdown_data = {
        "Component": ["Principal & Interest", "Property Tax", "Home Insurance", "PMI", "HOA Fees"],
        "Amount": [
            monthly_payment, 
            params['property_tax']/12, 
            params['home_insurance']/12, 
            pmi_payment, 
            params['hoa_fees']
        ]
    }
    
    fig_pie = px.pie(breakdown_data, values='Amount', names='Component', title="Monthly Payment Composition")
    st.plotly_chart(fig_pie, use_container_width=True)

def display_amortization_schedule(loan_amount, interest_rate, loan_term):
    """Calculate and display amortization schedule"""
    st.subheader("📅 Amortization Schedule (First 5 Years)")
    schedule = calculate_amortization_schedule(loan_amount, interest_rate, loan_term)
    st.dataframe(schedule.head(60), use_container_width=True, height=400)

def calculate_amortization_schedule(loan_amount, interest_rate, loan_term):
    """Calculate detailed amortization schedule"""
    monthly_rate = interest_rate / 100 / 12
    total_payments = loan_term * 12
    
    monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** total_payments) / ((1 + monthly_rate) ** total_payments - 1)
    
    schedule = []
    balance = loan_amount
    
    for month in range(1, total_payments + 1):
        interest_payment = balance * monthly_rate
        principal_payment = monthly_payment - interest_payment
        balance -= principal_payment
        
        schedule.append({
            'Month': month,
            'Payment': monthly_payment,
            'Principal': principal_payment,
            'Interest': interest_payment,
            'Remaining Balance': max(balance, 0)
        })
    
    return pd.DataFrame(schedule)

def display_mortgage_analysis(loan_amount, loan_term, monthly_payment, params):
    """Display mortgage cost analysis"""
    st.subheader("💵 Total Cost Analysis")
    
    total_interest = calculate_total_interest(loan_amount, params['interest_rate'], loan_term)
    total_payments = monthly_payment * loan_term * 12
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Interest Paid", f"${total_interest:,.2f}")
    with col2:
        st.metric("Total Payments", f"${total_payments:,.2f}")
    with col3:
        interest_ratio = (total_interest / loan_amount) * 100
        st.metric("Interest to Loan Ratio", f"{interest_ratio:.1f}%")

def calculate_total_interest(loan_amount, interest_rate, loan_term):
    """Calculate total interest paid over loan term"""
    monthly_rate = interest_rate / 100 / 12
    total_payments = loan_term * 12
    
    monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** total_payments) / ((1 + monthly_rate) ** total_payments - 1)
    return (monthly_payment * total_payments) - loan_amount

# =============================================================================
# RETIREMENT PLANNER FUNCTIONS
# =============================================================================

def show_retirement_planner():
    """Display the retirement planning calculator"""
    st.header("🎯 Retirement Planner")
    
    st.markdown("""
    <div class="calculator-box">
    Plan your retirement savings, estimate your retirement income, and track your progress towards retirement goals
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Current Situation")
        current_age = st.slider("Current Age", 20, 70, 30)
        retirement_age = st.slider("Planned Retirement Age", 50, 80, 65)
        current_savings = st.number_input("Current Retirement Savings ($)", value=50000.0)
        annual_contribution = st.number_input("Annual Retirement Contribution ($)", value=10000.0)
    
    with col2:
        st.subheader("Retirement Goals")
        desired_income = st.number_input("Desired Annual Retirement Income ($)", value=60000.0)
        inflation_rate = st.slider("Expected Inflation Rate (%)", 1.0, 5.0, 2.5, step=0.1)
        investment_return = st.slider("Expected Investment Return (%)", 1.0, 15.0, 7.0, step=0.5)
        life_expectancy = st.slider("Life Expectancy", 75, 100, 85)
    
    if st.button("🎯 Calculate Retirement Plan", type="primary"):
        calculate_retirement_plan(
            current_age, retirement_age, current_savings, annual_contribution,
            desired_income, inflation_rate, investment_return, life_expectancy
        )

def calculate_retirement_plan(current_age, retirement_age, current_savings, annual_contribution,
                            desired_income, inflation_rate, investment_return, life_expectancy):
    """Calculate and display retirement plan"""
    years_to_retirement = retirement_age - current_age
    retirement_years = life_expectancy - retirement_age
    
    if years_to_retirement <= 0:
        st.error("Retirement age must be greater than current age")
        return
    
    # Calculate retirement savings at retirement
    future_savings = calculate_future_savings(current_savings, annual_contribution, investment_return, years_to_retirement)
    
    # Calculate required retirement savings
    required_savings = calculate_required_retirement_savings(desired_income, inflation_rate, investment_return, retirement_years)
    
    # Display results
    display_retirement_results(future_savings, required_savings, years_to_retirement, retirement_years)
    display_retirement_savings_projection(current_savings, annual_contribution, investment_return, years_to_retirement)

def calculate_future_savings(current_savings, annual_contribution, return_rate, years):
    """Calculate future value of retirement savings"""
    future_value = current_savings
    for year in range(years):
        future_value = future_value * (1 + return_rate/100) + annual_contribution
    return future_value

def calculate_required_retirement_savings(desired_income, inflation_rate, return_rate, retirement_years):
    """Calculate required retirement savings to support desired income"""
    # Adjust desired income for inflation
    inflated_income = desired_income * (1 + inflation_rate/100) ** retirement_years
    
    # Calculate required savings (simplified 4% rule)
    required_savings = inflated_income * 25  # 4% withdrawal rate
    return required_savings

def display_retirement_results(future_savings, required_savings, years_to_retirement, retirement_years):
    """Display retirement planning results"""
    st.success("🎉 Retirement Calculation Complete!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Projected Savings at Retirement", f"${future_savings:,.2f}")
    
    with col2:
        st.metric("Required Retirement Savings", f"${required_savings:,.2f}")
    
    with col3:
        savings_gap = required_savings - future_savings
        status = "On Track 🎯" if savings_gap <= 0 else "Needs Improvement 📈"
        st.metric("Savings Gap", f"${savings_gap:,.2f}", status)
    
    # Retirement readiness assessment
    st.subheader("📊 Retirement Readiness Assessment")
    readiness_score = min(100, max(0, (future_savings / required_savings) * 100))
    
    if readiness_score >= 100:
        st.success(f"**Excellent!** You're on track for retirement. Readiness score: {readiness_score:.1f}%")
    elif readiness_score >= 75:
        st.warning(f"**Good progress.** You're getting close to your retirement goal. Readiness score: {readiness_score:.1f}%")
    else:
        st.error(f"**Needs attention.** Consider increasing your savings rate. Readiness score: {readiness_score:.1f}%")

def display_retirement_savings_projection(current_savings, annual_contribution, return_rate, years):
    """Display retirement savings projection chart"""
    st.subheader("📈 Retirement Savings Projection")
    
    projection_data = []
    savings = current_savings
    
    for year in range(years + 1):
        projection_data.append({
            'Year': year,
            'Savings': savings,
            'Age': year  # You can adjust this based on current age
        })
        savings = savings * (1 + return_rate/100) + annual_contribution
    
    df_projection = pd.DataFrame(projection_data)
    fig = px.line(df_projection, x='Year', y='Savings', title='Retirement Savings Growth Over Time')
    st.plotly_chart(fig, use_container_width=True)

# =============================================================================
# RUN THE APPLICATION
# =============================================================================

if __name__ == "__main__":
    show_financial_calculators()
