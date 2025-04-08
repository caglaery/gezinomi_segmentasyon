import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from numpy.ma.extras import unique

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df=pd.read_excel("datasets/miuul_gezinomi.xlsx")
df.head()
df.info()
df.shape
df.describe().T
df["SaleCityName"].value_counts()
df["SaleCityName"].unique()
df["ConceptName"].value_counts()
df["ConceptName"].unique()
df.groupby("SaleCityName").agg({"Price": "mean"})
df.groupby("ConceptName").agg({"Price": "mean"})
df.groupby(["SaleCityName", "ConceptName"]).agg({"Price": "mean"})
df["SaleCheckInDayDiff"]=df["SaleCheckInDayDiff"].astype("category")
df["EB_Score"]=["Last_Minuters" if x<7 else
                "Potential_Planers" if x<30 else
                "Planners" if x<90 else
                "Early_Bookers"for x in df["SaleCheckInDayDiff"]]
df.head(100)

df.groupby(["SaleCityName","ConceptName","EB_Score"]).agg({"Price": ["mean","count"]})
df.groupby(["SaleCityName","ConceptName","Seasons"]).agg({"Price": ["mean","count"]})
df.groupby(["SaleCityName","ConceptName","CInDay"]).agg({"Price": ["mean","count"]})
agg_df=df.groupby(["SaleCityName","ConceptName","Seasons"]).agg({"Price": "mean"}).sort_values(by="Price",ascending=False)
agg_df.reset_index(inplace=True)
agg_df["sales_level_based"]=agg_df["SaleCityName"]+"_"+ agg_df["ConceptName"]+"_"+ agg_df["Seasons"]
agg_df["Price"].dtypes
agg_df.head(20)
agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], 4, labels=["D", "C", "B", "A"])
agg_df.groupby(["SEGMENT"]).agg({"Price": ["mean","max","sum"]})
agg_df.sort_values(by="Price")
new_user="Antalya_Herşey Dahil_High"
agg_df[agg_df["sales_level_based"]==new_user].agg({"Price": "mean"})
agg_df[agg_df["sales_level_based"]==new_user].agg("SEGMENT")