import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object 

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:

            model_path ='artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)
    
        


class CustomData:
    def __init__(self,
        Job_Title: str,
        Average_Salary: int,
        Years_Experience: int,
        Education_Level: str,
        AI_Exposure_Index: float,
        Tech_Growth_Factor: float,
        Risk_Category: str,
        Skill_1: str, Skill_2: str, Skill_3: str, Skill_4: str, Skill_5: str,
        Skill_6: str, Skill_7: str, Skill_8: str, Skill_9: str, Skill_10: str):
        
        self.Job_Title = Job_Title
        self.Average_Salary = Average_Salary
        self.Years_Experience = Years_Experience
        self.Education_Level = Education_Level
        self.AI_Exposure_Index = AI_Exposure_Index
        self.Tech_Growth_Factor = Tech_Growth_Factor
        self.Risk_Category = Risk_Category
        self.Skill_1 = Skill_1
        self.Skill_2 = Skill_2
        self.Skill_3 = Skill_3
        self.Skill_4 = Skill_4
        self.Skill_5 = Skill_5
        self.Skill_6 = Skill_6
        self.Skill_7 = Skill_7
        self.Skill_8 = Skill_8
        self.Skill_9 = Skill_9
        self.Skill_10 = Skill_10

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Job_Title": [self.Job_Title.strip()],
                "Average_Salary": [self.Average_Salary],
                "Years_Experience": [self.Years_Experience],
                "Education_Level": [self.Education_Level.strip()],
                "AI_Exposure_Index": [self.AI_Exposure_Index],
                "Tech_Growth_Factor": [self.Tech_Growth_Factor],
                "Risk_Category": [self.Risk_Category.strip()],
                "Skill_1": [self.Skill_1], "Skill_2": [self.Skill_2],
                "Skill_3": [self.Skill_3], "Skill_4": [self.Skill_4],
                "Skill_5": [self.Skill_5], "Skill_6": [self.Skill_6],
                "Skill_7": [self.Skill_7], "Skill_8": [self.Skill_8],
                "Skill_9": [self.Skill_9], "Skill_10": [self.Skill_10]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
    