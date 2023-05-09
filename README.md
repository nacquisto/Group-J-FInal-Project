# Group-J-FInal-Project
## By Peter Majors and Nick Acquisto
#### Stock Performance Comparison and Portfolio Analysis Application:
As we navigate the era of data-driven decision-making, Python has emerged as a versatile tool for financial market analysis, spurred by advances in computational power and data processing. This project presents a Python-based application designed to enable investors to strategically compare the historical performance of two chosen stocks from the S&P 500 index over a specific period. Leveraging data from Yahoo Finance, our application conducts an in-depth portfolio analysis, illustrating the power of data-driven insights. Furthermore, the project's initial design incorporated the GPT-3 model from OpenAI, aiming to provide a comparative analysis of the selected stocks based on AI-generated insights.
#### Statement of Problem:
The intricate nature of the stock market, coupled with its unpredictable influencing factors, presents a challenge for investors seeking to make informed decisions. Our project sought to unravel this complexity by developing an application that enables users to compare the performance of two chosen stocks over a given period. In addition, we intended to provide a data-driven portfolio analysis, leveraging historical data to offer insightful perspectives on the chosen stocks.
#### Approach to Problem:
To mitigate the complexities of stock market analysis, we developed a web-based application using Python and the Flask web framework. This application taps into the power of the yfinance package to extract historical stock data from Yahoo Finance, which it then processes to derive a multitude of stock metrics. These metrics, coupled with a chart of cumulative returns, offer a robust comparative analysis of the two selected stocks. Although we initially intended to use OpenAI's GPT-3 model for comparative analysis, this feature was not included in the final implementation.
#### Data:
The project leveraged data from two sources:
1.	S&P 500 List: A CSV file provided a comprehensive list of S&P 500 companies, serving as the basis for user stock selection.
2.	Yahoo Finance: The yfinance Python package was utilized to extract historical stock data for the selected companies from Yahoo Finance.
#### Methodology:
The code provided integrates Flask—a web framework—and Python to create a user-friendly web application that compares two stock tickers based on user input. The main components of this script include:
1.	Importing Necessary Packages: The application requires a variety of Python packages, including Flask, pandas, numpy, yfinance, datetime, os, matplotlib, io, base64, and dotenv.
2.	Initializing the Flask Application: The application structure includes a static folder for static files and a template folder for HTML templates, enabling seamless user interaction.
3.	Routing: Two routes are defined—'/' (home) and '/results'. The home route provides the user input form, while the results route processes user input, retrieves and processes stock data, and displays the results.
4.	Data Retrieval and Processing: The application uses the yfinance package to retrieve stock data based on user input and processes it to calculate various stock metrics such as log returns, standard deviation, volatility, average daily volume (ADV), and median daily volume (MDV).
5.	Data Combination and Sorting: The processed stock data is combined and sorted, readying it for further analysis.
6.	Key Metrics Retrieval: The application retrieves key metrics for each ticker, including closing prices, returns, standard deviation, volatility, and volume-related metrics.
7.	Correlation Calculation: The correlation coefficient between the two stocks is calculated, providing insight into the similarity of their price movements.
8.	Chart Creation: A chart of cumulative returns for the two stocks is generated using matplotlib and encoded as a base64 image for display on the results page.
9.	Fundamental Stock Information Retrieval: The yfinance package retrieves fundamental stock information for each ticker and formats the data for display.
10.	Rendering Results: The results.html template displays the calculated metrics, chart image, and fundamental stock information.

The script does not include the ChatGPT implementation (commented out) that would have provided a summary comparison for the two stock tickers.
#### Prerequisite Packages:
To ensure smooth execution of this project, the following Python packages were utilized and must be installed:
1.	pandas: A flexible and powerful data analysis/manipulation library.
2.	numpy: A package for scientific computing with powerful n-dimensional array object.
3.	yfinance: A simple and efficient package to download historical market data from Yahoo Finance.
4.	openai: The Python client for the OpenAI API, intended to interact with GPT-3 (though not used in the final implementation).
5.	datetime: A module to manipulate dates and times.
6.	os: A module providing a way of using operating system dependent functionality.
7.	dotenv: A module that allows application configuration to be stored in a .env file.
8.	flask: A lightweight WSGI web application framework.
9.	io: A module providing the Python interfaces to stream handling.
10.	base64: A module providing functions for the base64 encoding used to represent binary data in an ASCII string format.
#### Results and Conclusions
The final application successfully facilitates a robust comparison of the performance of two chosen stocks over a user-specified date range. It provides key stock metrics, a chart of cumulative returns, and fundamental stock information, ultimately enhancing data-driven decision making in stock investment. The intended feature to generate a comparison analysis using GPT-3 was unfortunately omitted in the final implementation due to the removal of the relevant code.

In conclusion, our project successfully achieved the primary objective of offering a tool for stock performance comparison and portfolio analysis. Nevertheless, we acknowledge room for enhancement and potential expansion in various areas:

1.	Integration of OpenAI's GPT-3 or its successor for generating comparison analysis: Our initial goal was to incorporate AI-driven comparative analysis of the chosen stocks. Owing to time constraints, this feature was not incorporated into the final version of our application. We firmly believe that AI-driven insights could significantly augment the utility and value of our application and intend to include this feature in future iterations.

2.	Expansion beyond the S&P 500: Currently, our application supports only stocks from the S&P 500 list. As we continue to evolve this project, we anticipate broadening this functionality to include stocks from other indices and potentially stocks from international markets.

3.	Incorporation of real-time data: While our application harnesses historical data from Yahoo Finance to lay a robust foundation for comparison and analysis, the inclusion of real-time data could provide users with current insights, thereby enabling more timely and informed decisions.

4.	Enhanced user interface: The current interface, although functional, offers room for refinement. In future versions, we aim to enhance the user interface to offer a more intuitive and aesthetically pleasing user experience.

5.	Inclusion of advanced portfolio analysis: While our application currently provides a basic portfolio analysis based on historical data, we envisage the inclusion of advanced portfolio analysis techniques, such as modern portfolio theory, to further enrich our tool.

We firmly believe that these enhancements will significantly improve the functionality of our application, providing a more comprehensive tool for stock performance comparison and portfolio analysis.
#### Lessons Learned
The development of this project offered us invaluable insights into integrating various Python libraries and packages to develop an efficient application. We gained hands-on experience in retrieving and processing stock data from online sources like Yahoo Finance, implementing the Flask web framework to create user-friendly interfaces, and utilizing data visualization libraries like matplotlib to generate insightful charts.

Although the OpenAI's GPT-3 model's integration for comparison analysis was not included in the final implementation, our exploratory work with this technology offered crucial insights into the potential of advanced AI techniques in enhancing user experience and providing more nuanced analysis.

To conclude, this project offered us profound lessons in data retrieval, processing, visualization, web application development, and the potential incorporation of AI technologies for stock market analysis.

Below is a link to a demonstration video of the program in action:

https://share.vidyard.com/watch/CiM8ewdVhVsqR2KpwCVydp?autoplay=1&vyetoken=94fbb624-16fc-41c8-b6cc-bf9c0daea4fwe

Please find the link below to access our code repository on GitHub, which includes our Python scripts, HTML templates, and other resources used in this project.

https://github.com/pmajors/stock_performance_comparison](https://github.com/nacquisto/Group-J-FInal-Project/tree/main

To run the code, you will need to install the prerequisite Python packages listed in our report. Once the packages are installed, you can download our code from GitHub, navigate to the directory containing the code in your terminal or command prompt, and run the command python app.py to start the Flask server. Then, you can access the application by opening your web browser and going to http://localhost:5000/.

Please note that the instructions above are intended for local testing. If you would like to deploy the application on a live server, you will need to follow additional steps, which are beyond the scope of this report. If you encounter any issues while running our code, feel free to raise an issue on our GitHub repository or contact us directly.

## Proof of Concept - Jupyter Notebook (POC.ipynb)
A proof of concept Jupyter notebook, titled POC.ipynb, was developed to showcase the potential of integrating Python, financial data, and OpenAI's GPT-3 model for stock analysis. The notebook demonstrates a step-by-step process of the application from stock selection to detailed stock analysis, which includes:

1.	Selection of two stocks from the S&P 500 list and the input of a date range for analysis.
2.	Fetching of historical stock data for the selected stocks within the specified date range from Yahoo Finance.
3.	Calculation of various technical indicators such as log returns, standard deviation, volatility, average daily volume (ADV), and median daily volume (MDV).
4.	Use of OpenAI's GPT-3 model to generate a comparison analysis of the selected stocks.
5.	Execution of an optimization analysis on the user-selected stocks and subsequent display of the program calculations.

This notebook shows how the user can get a detailed comparison and analysis of the selected stocks, including visual representations of stock performance, risk comparison, and potential portfolio fit. The notebook also demonstrates the use of the Efficient Frontier Model to show the point of Maximum Sharpe Ratio, giving insights into the combined performance of the two stocks in a portfolio.

The POC.ipynb notebook can be found in the GitHub repository linked earlier in this report. To run the notebook, you will need to have Jupyter Notebook installed and the prerequisite Python packages listed in the notebook.

The output of the OpenAI GPT-3 model integration is demonstrated in the proof of concept Jupyter notebook but is not included in the final version of the web application because the pertinent code has been removed.

This project's Python code is accessible on GitHub. To make the analysis easier to understand, markdown cells have been added and each.py file has been commented. The project's relevant files are available in the GitHub repository, where you can also keep up with its progress.

https://github.com/nacquisto/Stock-Picker-Main 

Make sure that the .env file has an OpenAI API key to run the program. If it is missing, please try “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” instead. If all else fails, you will have to sign up for a pay as you go API on OpenAI.

Input:
This project is a comprehensive stock analysis tool that allows users to select two stocks and a date range for analysis. Leveraging OpenAI's GPT-3 model, it provides a summary comparison of the selected stocks. This summary consists of a dedicated paragraph for each stock and an overall comparison of the two. By setting self.messages to equal [{"role": "system", "content": f"You are a stock analyst. Provide a summary comparison of the following companies: {', '.join(stock_symbols)}. Make sure that you provide a paragraph for each company and a summary of your comparison, that is all you need."}] 

 
