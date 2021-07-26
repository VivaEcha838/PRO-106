import plotly_express as px
import csv 
import numpy as np

def drawGraph():
    with open("data.csv") as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x="Days Present", y="Marks In Percentage")
        fig.show()

def getDataSource(data_path):
    daysHere = []
    marksPerc = []

    with open(data_path) as csvFile:
        data = csv.DictReader(csvFile)
        for row in data:
            daysHere.append(float(row["Days Present"]))
            marksPerc.append(float(row["Marks In Percentage"]))
        
    return{"x": daysHere, "y": marksPerc}

def calcCorr(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print(correlation)

def main():
    data_path = "data.csv"
    datasource = getDataSource(data_path)
    calcCorr(datasource)

    drawGraph()

main()
    
    


    

