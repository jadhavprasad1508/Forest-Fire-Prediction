🔥 Fire Weather Index (FWI) Prediction Web App

Project Overview

This project is a machine learning web application designed to predict the **Fire Weather Index (FWI)**, a globally recognized measure of fire danger. It serves as a practical, deployable demonstration of a data science model integrated with a modern, responsive user interface.

The application allows users to input current weather and environmental variables (like Temperature, Relative Humidity, and various moisture codes) and instantly receive a predicted FWI score, which can be used for risk assessment.

Key Features

FWI Prediction:** Utilizes a pre-trained **Ridge Regression Model** (loaded via `pickle`) to predict the FWI value.
Data Preprocessing:** Implements a **StandardScaler** to ensure raw input data is correctly normalized before prediction.
Modern Frontend (`home.html`):** Features a clean, visually enhanced, and fully **responsive** interface built with HTML5/CSS3 (Jinja2 templating), ensuring usability across various devices.
Robust Backend (`application.py`):** Uses **Flask** for routing, request handling, and dynamic content rendering. The backend includes **error handling** to prevent server crashes from invalid user input.
Compatibility Fixes:** The code has been specifically reviewed and corrected for compatibility issues related to form input names and result rendering between the Flask backend and the HTML frontend.

⚙️ Technology Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend** | Python, Flask | Handles API routing, prediction logic, and dynamic rendering. |
| **Machine Learning** | Scikit-learn, Pickle | Ridge Regression Model and Standard Scaling implementation. |
| **Frontend** | HTML5, CSS3, Jinja | User interface and dynamic result display. |

📁 Project Structure

To run the application successfully, your project directory must follow this structure:
FWI-Prediction-App/ ├── application.py # Flask application backend ├── requirements.txt # List of Python dependencies ├── models/ │ ├── ridge.pkl # Trained Ridge Regression Model file │ └── scaler.pkl # Fitted StandardScaler object file └── templates/ └── home.html # The main prediction page (Jinja template)

🚀 Setup and Installation

1. Prerequisites

You must have Python 3.10 installed on your system.

 2. Clone the Repository

bash
git clone https://github.com/jadhavprasad1508/Forest-Fire-Prediction.git
cd FWI-Prediction-App

3. Install Dependencies
It's highly recommended to use a virtual environment.

Bash

 Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate

 Install required packages
pip install flask scikit-learn numpy pandas

4. Place Model Files
Ensure you have saved your trained model (ridge.pkl) and scaler object (scaler.pkl) inside the models/ subdirectory. The application will crash if these files are missing or incorrectly named.

5. Run the Application
Start the Flask server from the main project directory:

Bash

python application.py

6. Access the App
Open your web browser and navigate to the local server address:

http://127.0.0.1:5000/

💡 Usage and Input Parameters
The application expects the following 9 inputs, which are standard components of fire weather analysis:

Temperature (°C)

Relative Humidity (RH) (%)

Wind Speed (Ws) (km/h)

Rain (mm)

Fine Fuel Moisture Code (FFMC)

Drought Moisture Code (DMC)

Initial Spread Index (ISI)

Classes (Categorical: Fire/Not Fire, often encoded as 0/1)

Region (Categorical: Geographic region, often encoded as 0/1)
