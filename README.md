# 🏠 Real Estate Market Insights & Price Predictor

An interactive property valuation dashboard built using **Python** and **Streamlit** for regional real estate price trends and smart price estimation.

## 🚀 Features

* **Smart Price Calculator:** Get an estimated market value by selecting location, area (sqft), and number of bedrooms.
* **Regional Price Distribution:** Box plot comparing property pricing ranges across locations and property types (House, Apartment, Plot).
* **Size vs Pricing Correlation:** Scatter plot showing how property size relates to price, with bubble size representing bedroom count.
* **Multi-location Coverage:** Includes Gulberg, DHA Phase 6, Johar Town, Samundri Road, and Canal Road.

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** Streamlit
* **Libraries:** Pandas, NumPy, Plotly Express

## 💻 How to Run Locally

1. Clone this repository or download `app.py`.
2. Open your terminal and install dependencies:

   ```bash
   pip install streamlit pandas numpy plotly
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Your default browser will open automatically at `http://localhost:8501` displaying the dashboard.

## 📊 Data

The app uses synthetic property data generated on the fly, containing:

* **Property_ID** – Unique property identifier
* **Location** – Gulberg, DHA Phase 6, Johar Town, Samundri Road, or Canal Road
* **Area_SqFt** – Property area in square feet (800–4500)
* **Bedrooms** – Number of bedrooms (1–6)
* **Price_PKR_Lakhs** – Property price in PKR Lakhs (40–650)
* **Property_Type** – House, Apartment, or Plot

> ⚠️ Note: This is synthetic/sample data for demonstration purposes only and does not represent real property listings or market prices.

## 📈 Usage

1. Use the **Smart Price Calculator** to select a location, area, and number of bedrooms, then view the estimated market value.
2. Check the **Regional Price Distribution** box plot to compare pricing ranges across locations and property types.
3. Explore the **Property Size vs Pricing Correlation** scatter plot to see how area and bedrooms affect price across locations.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to open a pull request or file an issue.

## 📄 License

This project is open-source and available under the MIT License.
