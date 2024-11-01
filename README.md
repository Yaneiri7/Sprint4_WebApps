# Sprint4_WebApps
Car Advertisement Data Dashboard
This project is an exploratory data analysis (EDA) and dashboard web application built to analyze and visualize a car advertisement dataset. The application uses Streamlit for an interactive experience, allowing users to gain insights into various attributes of the cars listed in the dataset.

Project Description
This tool provides a set of visualizations to explore data patterns in car advertisements. By examining the dataset's key features, such as car price, model year, odometer (mileage), and condition, users can uncover valuable insights about the cars listed for sale. This project includes:

An EDA.ipynb notebook for initial exploratory data analysis and visualization creation.
A Streamlit dashboard built from the EDA work, which includes interactive charts and filters.
Features
Histograms to show distributions, such as car prices and model years.
Scatter plots to analyze relationships, such as between price and mileage, and price and model year.
Checkbox interactions to toggle additional visualizations on and off.
Interactivity through Streamlit, allowing users to explore data dynamically.
Dataset
The dataset used is vehicles_us.csv, containing information about various cars listed for sale in the US. Key columns include:

price: Price of the car.
model_year: Year the car model was manufactured.
odometer: Mileage (distance) the car has been driven.
condition: Condition of the car (e.g., good, excellent).
cylinders, fuel, transmission, type, paint_color: Various characteristics of the cars.
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/Yaneiri7/Sprint4_WebApps
Navigate to the project directory:
bash
Copy code
cd your-repository
Install the required packages:
bash
Copy code
pip install -r requirements.txt
Ensure that streamlit, pandas, and plotly are installed.
Running the Application
Explore the Data:

Open EDA.ipynb in Jupyter Notebook or VS Code.
Run the notebook to view the initial exploratory analysis and visualizations.
Launch the Streamlit Dashboard:

From the project root, run:
bash
Copy code
streamlit run app.py
The dashboard should open in a new browser tab, where you can explore data through the provided charts and filters.
Project Structure
plaintext
Copy code

SPRINT4_WEBAPP_PROJECT/
├── .idea/                        # IDE-specific configuration files
├── .ipynb_checkpoints/           # Jupyter notebook checkpoint files
├── .streamlit/                   # Streamlit configuration directory
│   └── config.toml               # Streamlit configuration file
├── notebook/
│   └── EDA.ipynb                 # Jupyter Notebook with exploratory data analysis
├── venv/                         # Virtual environment directory
├── .gitignore                    # Git ignore file
├── app.py                        # Streamlit app for the dashboard
├── README.md                     # Project documentation
├── requirements.txt              # List of dependencies
└── vehicles_us.csv               # Dataset file
           

Usage
Explore car price distributions and how they vary by attributes like model year and mileage.
Use scatter plots to examine correlations between features, such as price vs. mileage.
Toggle additional insights with checkboxes to explore more dimensions in the data.