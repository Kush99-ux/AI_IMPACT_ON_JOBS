AI Job Impact Predictor 2030
This project is a Machine Learning application designed to estimate the probability of various job roles being automated by the year 2030. It analyzes specific metrics such as salary, years of experience, and a diverse set of professional skills to provide a data-driven risk assessment.

Project Overview
The application is built using a modular software engineering approach. It includes a complete end-to-end pipeline from data ingestion to a live web interface.

Key Technical Achievements
- High Accuracy: The model achieved an R2 score of 0.867, meaning it explains approximately 87 percent of the variance in the dataset.

- Robust Preprocessing: Uses a custom pipeline that handles missing values, scales numerical data, and encodes categorical features while gracefully ignoring unknown inputs.

- Interactive Interface: A Flask-based web application allows users to input their own career data and receive real-time predictions.

Technical Stack
- Language: Python 3.8+

- Machine Learning: Scikit-learn, XGBoost, CatBoost, and Random Forest

- Web Framework: Flask

- Frontend: HTML5 and Bootstrap 5

Project Structure
- src/components: Contains data ingestion, transformation, and model training logic.

- src/pipeline: Manages the prediction workflow for the web interface.

- artifacts: Stores the trained model and preprocessing objects as pickle files.

- templates: Contains the web interface files.

How to Run
1. Clone the repository to your local machine.

2. Install dependencies using the command: pip install -r requirements.txt.

3. Run the data ingestion script to train the model: python src/components/data_ingestion.py.

4. Launch the web app: python app.py.

5. Open your browser to the local address   provided in the terminal.