# home.py
# Python Back-End For home.html Select Statement

# Import Required Packages
from flask import Flask, request, render_template, redirect, url_for, send_file
import pandas as pd
import numpy as np
import yfinance as yf
import datetime
import os
os.environ['MPLBACKEND'] = 'TkAgg'
import matplotlib.pyplot as plt
import io
import base64
from dotenv import load_dotenv
# import openai
# import os

# Initialize Flask
app = Flask(__name__, static_folder='static',template_folder='templates')

# Dictionary Of Data
formData = {}

# Display Home
@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == "POST":
        
        # Retrieve Form Inputs
        ticker1 = request.form['ticker1']
        ticker2 = request.form['ticker2']
        date = request.form['date']
        
        # Import Into Global Scope Dictionary
        formData['ticker1'] = ticker1
        formData['ticker2'] = ticker2
        formData['date'] = date
        
        return redirect(url_for("results")) 
    else:               
        return render_template('home.html')
    
# Python Back-End
    
# Display Results
@app.route('/results')
def results():
    
    # Gather Data Based On Stocks And Time Frame
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    t1_data = yf.download(formData['ticker1'], start=formData['date'], end=today)
    t2_data = yf.download(formData['ticker2'], start=formData['date'], end=today)

    # 1st Ticker Processing
    t1_data = t1_data.reset_index()
    t1_data.sort_values(by=['Date'], inplace=True, ascending=False)
    t1_data.insert(0, "Symbol", formData['ticker1'])

    # 2nd Ticker Processing
    t2_data = t2_data.reset_index()
    t2_data.sort_values(by=['Date'], inplace=True, ascending=False)
    t2_data.insert(0, "Symbol", formData['ticker2'])

    # Combine The Data
    stock_data = pd.DataFrame()
    stock_data = pd.concat([t1_data, t2_data], axis=0)

    # Indicator Data -----------------------------------------------------------------------------------
    MAwindow = 10
    StockDaysInYear = 250
    stock_list = [formData['ticker1'], formData['ticker2']]
    stocks_eod_data = pd.DataFrame(columns=['Symbol', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Log Return', 'Std Dev', 'Volatility', 'ADV', 'MDV'])

    for stock in stock_list:    
        temp_df = stock_data[stock_data['Symbol'] == stock].copy()
        temp_df["Log Return"] = np.log(temp_df["Close"] / temp_df["Close"].shift(-1))
        temp_df["Std Dev"] = temp_df["Log Return"].rolling(MAwindow).std().shift(-MAwindow + 1)
        temp_df["Volatility"] = temp_df["Std Dev"] * StockDaysInYear**0.5
        temp_df["ADV"] = temp_df["Volume"].rolling(MAwindow).mean().shift(-MAwindow + 1).round(2)
        temp_df["MDV"] = temp_df["Volume"].rolling(MAwindow).median().shift(-MAwindow + 1).round(2)
        stocks_eod_data = pd.concat([temp_df, stocks_eod_data], join="inner")
        
    stocks_eod_data = stocks_eod_data.sort_values(by=["Symbol", "Date"], ascending=[True, False])

    # Get Key Metrics From Complete Trading Dataset-----------------------------------------------------
    
    # Ticker 1
    close_ticker1 = stocks_eod_data[stocks_eod_data['Symbol'] == formData['ticker1']]['Close']
    return_ticker1 = str((((close_ticker1[len(close_ticker1) - 1] - close_ticker1[0])/close_ticker1[0])*100).round(2))+"%"
    
    returns_ticker1 = stocks_eod_data[stocks_eod_data['Symbol'] == formData['ticker1']]['Log Return']
    std_ticker1 = (returns_ticker1.std()*100).round(2)
    vol_ticker1 = ((returns_ticker1.std()*StockDaysInYear**.5)*100).round(2)
    
    volumes_ticker1 = stocks_eod_data[stocks_eod_data['Symbol'] == formData['ticker1']]['Volume']
    ADV_ticker1 = "{:,}".format(volumes_ticker1.mean().round(2))
    MDV_ticker1 = "{:,}".format(volumes_ticker1.median())
    
    start_ticker1 = close_ticker1[0].round(2)
    end_ticker1 = close_ticker1[len(close_ticker1) - 1].round(2)
    
    # Ticker 2
    close_ticker2 = stocks_eod_data[stocks_eod_data['Symbol'] ==formData['ticker2']]['Close']
    return_ticker2 = str((((close_ticker2[len(close_ticker2) - 1] - close_ticker2[0])/close_ticker2[0])*100).round(2))+"%"
    
    returns_ticker2 = stocks_eod_data[stocks_eod_data['Symbol'] == formData['ticker2']]['Log Return']
    std_ticker2 = (returns_ticker2.std()*100).round(2)
    vol_ticker2 = ((returns_ticker2.std()*StockDaysInYear**.5)*100).round(2)
    
    volumes_ticker2 = stocks_eod_data[stocks_eod_data['Symbol'] == formData['ticker2']]['Volume']
    ADV_ticker2 = "{:,}".format(volumes_ticker2.mean().round(2))
    MDV_ticker2 = "{:,}".format(volumes_ticker2.median())
    
    start_ticker2 = close_ticker2[0].round(2)
    end_ticker2 = close_ticker2[len(close_ticker2) - 1].round(2)
    
    # Correlation Coefficient
    
    adj_close1 = stocks_eod_data[stocks_eod_data['Symbol'] == formData['ticker1']]['Adj Close']
    adj_close2 = stocks_eod_data[stocks_eod_data['Symbol'] == formData['ticker2']]['Adj Close']

    # Calculate the correlation coefficient
    corr_coeff = adj_close1.corr(adj_close2).round(2)
    
    # Create The Chart-----------------------------------------------------------------------------------

    plt.figure(figsize=(14, 8))
    colors = ['blue', 'green']
    for i, symbol in enumerate(stocks_eod_data['Symbol'].unique()):
        stock = stocks_eod_data[stocks_eod_data['Symbol'] == symbol]
        
        # Caclulative Cumulative Return For The Stock
        stock= stock.sort_values('Date', ascending = True)
        stock['Cumulative Return'] = stock['Adj Close'] / stock['Adj Close'].iloc[0] - 1
        plt.plot(stock['Date'], stock['Cumulative Return'], label=symbol, color=colors[i % len(colors)])
        
    # Labels And Styling
    plt.xlabel("Date", fontsize=24)
    plt.ylabel("Adjusted Close Returns", fontsize=24)
    plt.title("Cumulative Returns (Adj Close) - " + formData['ticker1'] + " & "  + formData['ticker2'], fontsize=27)
    plt.legend(fontsize = 22)
    plt.grid(True)
    plt.xticks(fontsize = 17)
    plt.yticks(fontsize = 17)
    plt.axhline(y=0, color='r', linestyle='--')

    # Save the figure to a buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Encode the image to base64
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()
    
    # yfinance Data
    ticker1_info = yf.Ticker(formData['ticker1']).info
    ticker2_info = yf.Ticker(formData['ticker2']).info
    
    fund_ticker1 = []
    fund_ticker1.append(ticker1_info.get('trailingPE', "-"))
    fund_ticker1.append(ticker1_info.get('forwardPE', "-"))
    fund_ticker1.append(ticker1_info.get('ebitda', "-"))
    fund_ticker1.append(ticker1_info.get('returnOnEquity', "-"))
    fund_ticker1.append(ticker1_info.get('priceToBook', "-"))
    fund_ticker1.append(ticker1_info.get('pegRatio', "-"))
    fund_ticker1.append(ticker1_info.get('freeCashflow', "-"))
    fund_ticker1.append(ticker1_info.get('debtToEquity', "-"))
    fund_ticker1.append(ticker1_info.get('payoutRatio', "-"))
    fund_ticker1.append(ticker1_info.get('dividendYield', "-"))
    fund_ticker1.append(ticker1_info.get('shortRatio', "-"))
    
    # Formatting Numbers 
    for i in range(len(fund_ticker1)):
        if fund_ticker1[i] != "-":
            # Rounding
            rounded = [0,1,4,5,7,10]
            if i in rounded:
                fund_ticker1[i] = round(float(fund_ticker1[i]), 2)
            # Percent
            percent = [3,8,9]
            if i in percent:
                fund_ticker1[i] = str(round(float(fund_ticker1[i])*100, 2)) + "%"
            #Commas
            comma = [2,6]
            if i in comma:
                fund_ticker1[i] = "$" + str(format(fund_ticker1[i], ','))
    
    fund_ticker2 = []
    fund_ticker2.append(ticker2_info.get('trailingPE', "-"))
    fund_ticker2.append(ticker2_info.get('forwardPE', "-"))
    fund_ticker2.append(ticker2_info.get('ebitda', "-"))
    fund_ticker2.append(ticker2_info.get('returnOnEquity', "-"))
    fund_ticker2.append(ticker2_info.get('priceToBook', "-"))
    fund_ticker2.append(ticker2_info.get('pegRatio', "-"))
    fund_ticker2.append(ticker2_info.get('freeCashflow', "-"))
    fund_ticker2.append(ticker2_info.get('debtToEquity', "-"))
    fund_ticker2.append(ticker2_info.get('payoutRatio', "-"))
    fund_ticker2.append(ticker2_info.get('dividendYield', "-"))
    fund_ticker2.append(ticker2_info.get('shortRatio', "-"))
    
    # Formatting Numbers 
    for i in range(len(fund_ticker2)):
        if fund_ticker2[i] != "-":
            # Rounding
            rounded = [0,1,4,5,7,10]
            if i in rounded:
                fund_ticker2[i] = round(float(fund_ticker2[i]), 2)
            # Percent
            percent = [3,8,9]
            if i in percent:
                fund_ticker2[i] = str(round(float(fund_ticker2[i])*100, 2)) + "%"
            #Commas
            comma = [2,6]
            if i in comma:
                fund_ticker2[i] = "$" + str(format(fund_ticker2[i], ','))
    
    #ChatGPT---------------------------------------------------------------------------------------------
    
    # # Load environment variables from .env file
    # env_file = "env_vars.env"
    # if not load_dotenv(env_file):
    #     raise ValueError(f"Failed to load the environment variables from {env_file}")

    # # # Get OpenAI API key from environment variables
    # openai_api_key = os.getenv("OPENAI_API_KEY")
    # if openai_api_key is None:
    #     raise ValueError("OPENAI_API_KEY is not set in the environment variables.")
    # else:
    #     openai.api_key = openai_api_key

    # # ChatGPT Analysis
    # messages = [{"role": "system", "content": f"You are a brilliant stock analyst. Provide a summary comparison for" + formData['ticker1'] + "and" + formData['ticker2'] + ". Make sure that you provide a paragraph for each company that highlights their strong points and weak points as potential investments. You will only provide two paragraphs."}]
    # response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    # ChatGPT_reply = response["choices"][0]["message"]["content"]
    
    # Attempted to Use, But Could Not Get Working

    return render_template('results.html', ticker1=formData['ticker1'], ticker2=formData['ticker2'], date=formData['date'], today=today,return_ticker1=return_ticker1, 
                           std_ticker1=std_ticker1,vol_ticker1=vol_ticker1, ADV_ticker1=ADV_ticker1,MDV_ticker1=MDV_ticker1,start_ticker1=start_ticker1,end_ticker1=end_ticker1,
                           return_ticker2=return_ticker2, std_ticker2=std_ticker2,vol_ticker2=vol_ticker2, ADV_ticker2=ADV_ticker2,MDV_ticker2=MDV_ticker2,start_ticker2=start_ticker2, 
                           end_ticker2=end_ticker2, image=image_base64, trailingPE_ticker1=fund_ticker1[0], forwardPE_ticker1=fund_ticker1[1],ebitda_ticker1=fund_ticker1[2],
                           returnOnEquity_ticker1=fund_ticker1[3],priceToBook_ticker1=fund_ticker1[4], pegRatio_ticker1=fund_ticker1[5],freeCashflow_ticker1=fund_ticker1[6],
                           debtToEquity_ticker1=fund_ticker1[7],payoutRatio_ticker1=fund_ticker1[8],dividendYield_ticker1=fund_ticker1[9],shortRatio_ticker1=fund_ticker1[10],
                           trailingPE_ticker2=fund_ticker2[0], forwardPE_ticker2=fund_ticker2[1],ebitda_ticker2=fund_ticker2[2],returnOnEquity_ticker2=fund_ticker2[3],
                           priceToBook_ticker2=fund_ticker2[4], pegRatio_ticker2=fund_ticker2[5],freeCashflow_ticker2=fund_ticker2[6],debtToEquity_ticker2=fund_ticker2[7],
                           payoutRatio_ticker2=fund_ticker2[8],dividendYield_ticker2=fund_ticker2[9],shortRatio_ticker2=fund_ticker2[10], corr_coeff=corr_coeff)
    
    # gpt_analysis=ChatGPT_reply)
    
@app.route('/static/<path:path>')
def static_file(path):
    return send_file(path, as_attachment=True)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Main
if __name__ == '__main__':
    app.run()