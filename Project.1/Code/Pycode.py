import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("Project.1/Data/project6_public_transport_trips.csv")
print(df.shape)
df["Route"] = df["Route"].str.upper().str.strip()
df["Origin"] = df["Origin"].str.strip()
df.loc[df["Vehicle_Type"].str.strip().str.lower() == "brts","Vehicle_Type"] = df["Vehicle_Type"].str.upper().str.strip()
df.loc[df["Passenger_Type"].str.strip().str.lower() =='daily pass',"Passenger_Type"]  = df["Passenger_Type"].str.title().str.strip()
df["Trip_Duration_Min"] = pd.to_numeric(df["Trip_Duration_Min"],errors='coerce')
df.loc[df["Trip_Duration_Min"] < 0,"Trip_Duration_Min"] = pd.NA
df.loc[df["Fare_INR"] < 0,"Fare_INR"] = pd.NA
df["Origin"] = df["Origin"].fillna("Unknown")
df["Payment_Method"] = df["Payment_Method"].fillna("Unknown")

#print(df.columns) s
#print(df["Passenger_Rating"].unique())
df.drop_duplicates(inplace=True)


Total_Trip_By_origin = df.groupby("Origin")["Origin"].count()

Total_Trip_By_Destination = df.groupby("Destination")["Destination"].count()

Total_Trip_By_Passenger_Type = df.groupby("Passenger_Type")["Passenger_Type"].count()

Total_Trip_By_Route = df.groupby("Route")["Route"].count()

Avg_Trip_Price_Of_Vehicle_Type = df.groupby('Vehicle_Type')['Fare_INR'].mean().round(2)

Avg_Trip_Price_Of_Route = df.groupby('Route')['Fare_INR'].mean().round(2)

Avg_Trip_Duration_Time_By_Route = df.groupby("Route")["Trip_Duration_Min"].mean().round(2)

Avg_Trip_Duration_Time_By_Vehicle_Type = df.groupby("Vehicle_Type")["Trip_Duration_Min"].mean().round(2)

Avg_Rating_By_Vehicle_Type = df.groupby("Vehicle_Type")["Passenger_Rating"].mean().round(2)

Avg_Rating_By_Passsenger_Type = df.groupby("Passenger_Type")["Passenger_Rating"].mean().round(2)

Avg_Rating_By_Trip_Price = df.groupby("Fare_INR")["Passenger_Rating"].mean().round(2)

'''plt.bar(Avg_Rating_By_Passsenger_Type.index,Avg_Rating_By_Passsenger_Type.values)
plt.xlabel("Passenger Type")
plt.ylabel("Rating")
plt.title("Avg Trip INR by Vehicle type")
plt.tight_layout
plt.savefig("Project.1/Charts/Avg Rating by passenger type.png")
plt.show()'''
print(Avg_Rating_By_Trip_Price)
