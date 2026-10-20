# Transport Project 1

## Overview

this project is training project to learn data analysis and visualization.

## Objectives

To Analyze Total Trips,Avg Price Of Trip,Avg Rating  by Passenger Type and To Understand Public Trasport Trips Pattern.

## Data Set

This Project Contains 153 Rows And 12 Columns With This Name

- Trip_ID: Unique ID Of every Trip
- Trip_Date: Date Of trip
- Departure_Time: Trip Starting time
- Route: Route Used in Trip
- Origin: Starting Poin of The Trip
- Destination: Ending Point Of The Trip
- Vehicle_Type: Type Of Vehicle Used
- Passenger_Type: Categoty Of Passenger
- Payment_Method: Methon Used to Pay Trip Fare
- Trip_Duration_Min: Time Taken for Trip
- Fare_INR: Fare Paid in Indian Rupees
- Passenger_Rating: Rating Given By The Passenger

## Tools And technologies

- Python
- Pandas Library Of Python
- Matplotlib

## Data Cleaning

The Data Set Contains Saveral Data Quality Issues ,Including

- Missing Origin Values
- Missing Payment_Method Values
- Missing Trip_Duration_Min Values
- Missing Fare_INR Values
- Missing Passenger Rating Values
- Inconsistent Values in Route 
- Inconsistent Values in Origin 
- Inconsistent Values in Vehicle_Type 
- Inconsistent Values in Passenger_Type 
- Invailid Values in Trip_Duration_Min
- Invailid Values in Fare_INR
- Duplicate Rows

## Handling Missing Values

- Replaced Missing origin Values With `Unknown`.
- Replaced Missing Paymnet_Method With `Unknown`.
- Kept missing Trip_Duration_Min values unchanged.
- Kept missing Fare_INR values unchanged.
- Duplicate rows removed

## Handling Invailid Values 

- Invialid Trip_Duration_min Values Converted into NAn
- Invialid Fare_INR Values Converted into NAn

## Analysis

- Total trips by origin
- Total trips by destination
- Total trips by passenger type
- Total trips by route
- Average fare by vehicle type
- Average fare by route
- Average trip duration by route
- Average trip duration by vehicle type
- Average passenger rating by vehicle type
- Average passenger rating by passenger type
- Average passenger rating by fare

## Keyinsights

- Students gave the highest average rating, at 3.88
- Bus passengers gave a higher average rating (3.80) than BRTS passengers.
- R5 is most used route in trips amung all route
- R1 is the highest average trip time 59.03
- The Unversity has highest trips
- 15.0 fare INR is the highest average rating 4.07