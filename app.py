from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint(): 
    if request.method=='GET':
        return render_template('home.html')
    else:
        data = CustomData(
            Job_Title=request.form.get('Job_Title'),
            Average_Salary=int(request.form.get('Average_Salary')),
            Years_Experience=int(request.form.get('Years_Experience')),
            Education_Level=request.form.get('Education_Level'),
            AI_Exposure_Index=float(request.form.get('AI_Exposure_Index')),
            Tech_Growth_Factor=float(request.form.get('Tech_Growth_Factor')),
            Risk_Category=request.form.get('Risk_Category'),
            Skill_1=request.form.get('Skill_1'), Skill_2=request.form.get('Skill_2'),
            Skill_3=request.form.get('Skill_3'), Skill_4=request.form.get('Skill_4'),
            Skill_5=request.form.get('Skill_5'), Skill_6=request.form.get('Skill_6'),
            Skill_7=request.form.get('Skill_7'), Skill_8=request.form.get('Skill_8'),
            Skill_9=request.form.get('Skill_9'), Skill_10=request.form.get('Skill_10')
        )

        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        
        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        
        # results[0] contains the Automation Probability percentage
        return render_template('home.html', results=round(results[0], 2))
    
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True) 