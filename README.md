# Nifty50 Stock Price Prediction

This project involves building a machine learning-based web application that predicts stock prices for the Nifty50 index. By leveraging historical data and advanced machine learning models, the application aims to provide accurate predictions to help users make informed investment decisions.

---

## Features

### 1. **Predictive Model**
- **Target Variable:** Nifty50 stock price.
- **Input Features:**
  - Opening Price
  - Closing Price
  - High
  - Low
  - Volume
  - Moving Averages
  - Technical Indicators (e.g., RSI, MACD)

### 2. **User-Friendly Interface**
- Interactive frontend developed using **HTML, CSS, and JavaScript** for a seamless user experience.
- Backend built with **Django**, ensuring robust server-side operations and smooth integration with the machine learning model.

### 3. **Database**
- **SQLite** database used to efficiently manage and store historical stock data and user inputs.

### 4. **Insights and Trends**
- Provides a detailed analysis of stock performance and future trends based on historical data.

---

## How It Works

1. Users input relevant stock details or select a stock from the Nifty50 list.
2. The application processes the data and passes it to the trained machine learning model.
3. The model predicts the stock price and displays it to the user along with additional insights.
4. Users can view historical trends and graphs for better decision-making.

---

## Technology Stack

### Frontend
- **HTML**, **CSS**, **JavaScript**

### Backend
- **Django** Framework

### Database
- **SQLite**

### Machine Learning
- Trained model utilizing time-series data for stock price prediction.

---

## Requirements for the Project

### Python
- Version: 3.10 or higher
- Compatible with modern libraries and tools.

### Django Framework
- Version: 4.x or higher
- Leverages features such as class-based views and enhanced ORM capabilities.

### Libraries
- **NumPy**: For numerical operations.
- **Pandas**: For data manipulation.
- **joblib**: For loading the serialized machine learning model.
- **scikit-learn**: For building and training the machine learning model.
- **matplotlib/seaborn**: For data visualization.

### Front-End Libraries
- Optional: **Bootstrap 5.x** for responsive design.

### Deployment
- **Gunicorn**: For WSGI server.
- **WhiteNoise**: For serving static files in production.

---

## Steps to Run the Project

1. Clone the repository or download the project files.
2. Navigate to the project directory in your terminal:
   ```bash
   cd nifty50_stock_price_prediction
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run database migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. Open your browser and visit `http://127.0.0.1:8000` to access the application.

---

## Future Enhancements

- Expand the dataset to include global stock indices and additional features.
- Incorporate deep learning models for improved accuracy.
- Add user authentication for personalized stock predictions.
- Include a portfolio tracker for better investment management.

---

## License
This project is licensed under the [MIT License](LICENSE).

