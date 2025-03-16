☁️ Weather Forecast Data App

🌍 Overview

This is a Streamlit-based Weather Forecast App that retrieves and visualizes weather data for a given location. Users can select the number of forecasted days and choose between temperature graphs or sky conditions.

📌 Features

User-friendly Streamlit interface for real-time weather forecast visualization.

Fetches weather data for 1 to 5 days.

Displays temperature trends using interactive Plotly charts.

Shows sky conditions with corresponding weather icons.

🖼️ Screenshots

Temperature Chart
![temp1](https://github.com/user-attachments/assets/fdb1e78b-0822-4805-9f4e-2f234dffdcdf)



Weather Icons Display

![sky1](https://github.com/user-attachments/assets/112d6281-c2fe-43cc-8ca2-5490eb5d7b4a)


🛠 Technologies Used

Python (Streamlit, Plotly)

API Integration (Weather data backend)

Image Processing (Weather icons for visualization)

🚀 Installation & Setup

1️⃣ Clone the Repository:

git clone [CLICK](https://github.com/PolytechnicCoder/weather-forecast-data-app/tree/master)


2️⃣ Create a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3️⃣ Install Dependencies:

pip install -r requirements.txt

4️⃣ Run the Application:

streamlit run main.py

By default, the application will open in your browser at http://localhost:8501/.

🌐 How It Works

Enter the location in the input field.

Select the number of days for the forecast.

Choose between temperature graph or sky conditions.

View the interactive weather visualization!

📂 Project Structure

weather-forecast-data-app/
│── images/            # Weather icons
│── backend.py         # Fetches weather data
│── main.py            # Streamlit app interface
│── .gitignore         # Ignored files
│── requirements.txt   # Python dependencies


🌦 Weather Forecast App - Powered by Python & Streamlit

