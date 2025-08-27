🚗 Car Price Prediction Web App
A Flask-based machine learning web application for predicting car prices, containerized with Docker. The project uses a trained Random Forest Regressor model (model.pkl) built from a dataset of 8,128 cars with features like year, km_driven, mileage, engine, max_power, and brand. The application provides a user-friendly web interface for inputting car details and receiving price predictions.
✨ Features

Machine learning model (Random Forest, R² ≈ 0.90) trained on a preprocessed car dataset.
Full Flask web application with a responsive frontend for user input and price predictions.
Dockerized for seamless deployment.
Simple, interpretable inputs: year, km_driven, mileage, engine, max_power, brand.
Returns predicted car price via a web interface or API endpoint.
Incorporates fuel efficiency through mileage for more accurate predictions.

📂 Project Structure
.
├── main.py # Flask application entry point
├── model
│ └── car_price_model.pkl # Trained Random Forest model
├── Dockerfile # Docker image configuration
├── templates/ # HTML templates for web interface
│ └── index.html # Main webpage for user input
├── readme.md # Project documentation
├── requirements.txt # Project requirements
└── main.ipynb # all the srcipts, eda, data processing and model training notebook

⚡ Getting Started

1. Clone the Repository
   git clone https://github.com/saugatshakya/ML_assignment1.git
   cd car-price-prediction-app

2. Run Locally (without Docker)
   Ensure Python 3.9+ is installed.
   pip install -r requirements.txt
   python app.py

The web app will be available at: http://127.0.0.1:5001 3. Run with Docker
Build the Docker image:
docker build -t car-price-app .

Run the container:
docker run -p 5001:5000 car-price-app

Visit: http://127.0.0.1:5001 to access the web app.
🌐 Web App Usage

Open the web app in your browser (http://127.0.0.1:5001).
Enter car details (year, km_driven, mileage, engine, max_power, brand) in the provided form.
Submit to receive the predicted car price.

API Endpoint: /predict
Method: POSTContent-Type: application/json
Request Example
{
"year": 2018,
"km_driven": 35000,
"mileage": 23.4,
"engine": 1497,
"max_power": 118,
"brand": "Honda"
}

Response Example
{
"predicted_price": 925000
}

📊 Model Info

Model: Random Forest Regressor
R² Score: ~0.90
Features used: year, km_driven, mileage, engine, max_power, brand
The model predicts the selling price of a car based on these core attributes, with mileage enhancing accuracy by factoring in fuel efficiency.

🚀 Deployment
The web app can be deployed to:

Local Docker container (default)
Cloud services (AWS ECS, GCP Cloud Run, Azure App Service, etc.)
Integrated into broader web or mobile app ecosystems

🛠 Tech Stack

Python 3.9+
Flask
Scikit-learn
Pandas / NumPy
Docker
HTML/CSS/JavaScript (for web interface)

📌 Future Improvements

Add support for additional features (fuel, transmission, etc.).
Enhance preprocessing for unseen brands.
Deploy to a public endpoint (Heroku, Render, AWS, etc.).
Add unit tests and CI/CD pipeline.
Improve web interface with advanced styling and interactivity.

👨‍💻 Author
Developed by Chaky’s Company Team✨ Contributions & pull requests welcome!
📝 Analysis Report
Project Overview
This project delivers a car price prediction web application for Chaky’s Company, leveraging a dataset of 8,128 cars.  
Key features in the dataset include:

year  
km_driven  
mileage  
engine  
max_power  
brand  
fuel (preprocessed, not used in final model)  
owner (preprocessed, not used in final model)

Data Preparation
Preprocessing steps included:

Owner mapping: e.g., First Owner → 1, Second Owner → 2.  
Removed CNG and LPG cars: due to different mileage units (km/kg vs kmpl).  
Cleaned numeric columns: stripped "kmpl" from mileage and "CC" from engine.  
Extracted brand: first word from car name.  
Dropped torque: inconsistent units.  
Removed Test Drive Cars: unusually inflated prices.  
Log-transformed selling_price: to stabilize variation (range: 29,999 → 10,000,000).

🔍 Exploratory Data Analysis (EDA)
Correlation analysis and Random Forest feature importance guided feature selection, capturing both linear and non-linear relationships.  
Selected Features:

Feature
Correlation
Importance
Rationale

Year
0.718
~0.518
Newer cars command higher prices due to less wear and modern tech.

Max_power
0.637
~0.335
Stronger engines → premium/sport models.

Engine
0.468
~0.078
Bigger engines → luxury/performance cars.

Km_driven
-0.185
~0.020
More mileage reduces price, but weaker than expected.

Mileage
0.152
~0.043
Higher efficiency slightly boosts value.

Brand
-0.018
~0.025
Premium perception boosts price (e.g., BMW vs Maruti).

Examples:

Year: 2018 Honda City → ₹925,000 vs 2006 Honda City → ₹158,000.  
Max_power: Jeep Compass (160.77 bhp, ₹2,100,000) vs Maruti Alto (47.3 bhp, ₹275,000).  
Engine: Toyota Fortuner (2982 CC, ₹1,500,000) vs Maruti 800 (796 CC, ₹45,000).  
Km_driven: Swift (145,500 km → ₹450,000) vs Swift (35,000 km → ₹675,000).  
Mileage: Maruti Swift (23 kmpl → ₹675,000) vs older hatchback (18 kmpl → ₹420,000).  
Brand: Mercedes-Benz B Class → ₹1,450,000 vs Maruti Alto → ₹275,000.

Skipped Features:

Feature
Correlation
Reason for Exclusion

Owner
-0.389
Effect captured by year + km_driven.

Fuel Type
-0.356
Correlates with engine. Adds redundancy.

Transmission
-0.343
Overlaps with max_power and engine.

Seats
0.273
Low variation (mostly 5 seats).

📊 Model Comparison
Tested models with the 6 selected features:

Model
R² Score

Random Forest
0.9016

Decision Tree
0.8411

Linear Regression
0.8239

K-Neighbors (KNN)
0.8831

Support Vector Regr.
0.8713

🚀 Conclusion
This project delivers a robust car price prediction web application with a user-friendly interface and strong predictive performance (R² ≈ 0.90). The inclusion of mileage enhances accuracy by accounting for fuel efficiency, making it valuable for Chaky’s Company. The system offers:

Ease of data collection  
High predictive accuracy  
Seamless web app integration
