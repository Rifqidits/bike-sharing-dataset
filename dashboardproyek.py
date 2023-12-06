import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# https://bike-sharing-dataset-qidits.streamlit.app/

st.write(
    """
    # Hi! Welcome to Bike Sharing Dataset
    Here you can see many datas from Bike Rent
    """
)

st.title('Bike Rental Count by Hour, Day, and Season')
st.header("by Hour")
st.title('Bike Rental Count by Hour, Day, and Season')
st.header("by Hour")

# Data
data = {'hr': [18, 17, 8, 16, 12, 13, 14, 15, 19, 11, 7, 21, 20, 10, 22, 9, 0, 23, 6, 1, 2, 3, 5, 4],
        'cnt': [977, 976, 839, 783, 776, 760, 750, 750, 743, 663, 596, 584, 567, 539, 502, 426, 283, 256, 213, 168, 132, 79, 66, 28]}

df = pd.DataFrame(data)

# Plotting using seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(x='hr', y='cnt', data=df, marker='o')
plt.title('Bike Rental Count by Hour')
plt.xlabel('Hour')
plt.ylabel('Count')
plt.grid(True)
st.pyplot(plt)


st.header("Average by Hour")
data = {'hr': [17, 18, 8, 16, 19, 13, 12, 15, 14, 20, 9, 7, 11, 10, 21, 22, 23, 6, 0, 1, 2, 5, 3, 4],
        'average_cnt': [461.452055, 425.510989, 359.011004, 311.983562, 311.523352, 253.661180, 253.315934, 251.233196, 240.949246, 226.030220, 219.309491, 212.064649, 208.143054, 173.668501, 172.314560, 131.335165, 87.831044, 76.044138, 53.898072, 33.375691, 22.869930, 19.889819, 11.727403, 6.352941]}

df = pd.DataFrame(data)

# Plotting using seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(x='hr', y='average_cnt', data=df, marker='o')
plt.title('Average Bike Rental Count by Hour')
plt.xlabel('Hour')
plt.ylabel('Average Count')
plt.grid(True)
plt.show()
st.pyplot(plt)


st.header("Average by Weekday")
data = {'weekday': ["Friday", "Thursday", "Saturdau", "Wednesday", "Tuesday", "Monday", "Sunday"],
        'average_cnt': [4690.288462, 4667.259615, 4550.542857, 4548.538462, 4510.663462, 4338.123810, 4228.828571]}

df = pd.DataFrame(data)

# Plotting using seaborn
plt.figure(figsize=(8, 6))
sns.lineplot(x='weekday', y='average_cnt', data=df, marker='o')
plt.title('Average Bike Rental Count by Weekday')
plt.xlabel('Weekday')
plt.ylabel('Average Count')
plt.grid(True)
plt.show()
st.pyplot(plt)


st.header("Average by Day")
data = {'workingday': ["Workingday", "Not Working Day"],
        'average_cnt': [4584.82, 4330.168831]}

df = pd.DataFrame(data)

# Plotting using seaborn
plt.figure(figsize=(8, 6))
sns.barplot(x='workingday', y='average_cnt', data=df)
plt.title('Average Bike Rental Count by Working Day')
plt.xlabel('Working Day (1: Yes, 0: No)')
plt.ylabel('Average Count')
plt.show()
st.pyplot(plt)


st.header("Average by Season")
data = {'season': [3, 2, 4, 1],
        'average_cnt': [5644.303191, 4992.331522, 4728.162921, 2604.132597]}

df = pd.DataFrame(data)

# Plotting using seaborn
plt.figure(figsize=(8, 6))
sns.barplot(x='season', y='average_cnt', data=df)
plt.title('Average Bike Rental Count by Season')
plt.xlabel('Season')
plt.ylabel('Average Count')
plt.show()
st.pyplot(plt)
st.write("""
         Season explanation
         1: Springer
         2: Summer
         3: Fall
         4: Winter
         """)


st.header("Average by Normalized Humidity")
data = {'hum': [0.501667, 0.542917, 0.627500, 0.572917, 0.672500, 0.882500, 0.000000, 0.948261, 0.687500, 0.880000],
        'cnt': [8714.0, 8555.0, 8156.0, 8090.0, 8009.0, 627.0, 623.0, 605.0, 431.0, 22.0]}

df = pd.DataFrame(data)

# Plotting using seaborn
plt.figure(figsize=(12, 6))
sns.lineplot(x='hum', y='cnt', data=df, marker='o')
plt.title('Bike Rental Count by Humidity')
plt.xlabel('Humidity')
plt.ylabel('Count')
plt.grid(True)
plt.show()
st.pyplot(plt)


st.header("Average by Weathersit")
data = {'weathersit': [1, 2, 3],
        'average_cnt': [4876.786177, 4035.862348, 1803.285714]}

df = pd.DataFrame(data)

# Plotting using seaborn
plt.figure(figsize=(8, 5))
sns.barplot(x='weathersit', y='average_cnt', data=df)
plt.title('Average Bike Rental Count by Weathersit')
plt.xlabel('Weathersit')
plt.ylabel('Average Count')
plt.show()
st.pyplot(plt)
st.write("""
        Weathersit: 
        1: Clear, Few clouds, Partly cloudy, Partly cloudy
	2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
	3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds)
        """)


st.header("Average by Normalized Windspeed")
data = {'windspeed': [0.247521, 0.227604, 0.283583, 0.1163, 0.083975],
        'cnt': [8714.0, 8555.0, 8395.0, 8362.0, 8294.0]}

df = pd.DataFrame(data)

# Plotting using seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(x='windspeed', y='cnt', data=df, marker='o')
plt.title('Bike Rental Count by Windspeed')
plt.xlabel('Windspeed')
plt.ylabel('Count')
plt.show()
st.pyplot(plt)


st.header("Average by Normalized Temperature in Celcius")
data = {'temp': [0.601667, 0.6, 0.61, 0.633333, 0.529167],
        'cnt': [8362.0, 8294.0, 8227.0, 8009.0, 7907.0]}

df = pd.DataFrame(data)

# Plotting using seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(x='temp', y='cnt', data=df, marker='o')
plt.title('Bike Rental Count by Temperature')
plt.xlabel('Temperature')
plt.ylabel('Count')
plt.show()
st.pyplot(plt)


st.title("RFM (Recency, Frequency, Monetary)")
st.subheader("Advanced Analysis: Recency by Date")
st.write("To know the date of the last recorded sale along with the amount of rents")
data = {'cnt': [2729, 1796, 1341, 3095, 2114],
        'date': ['2012-12-31', '2012-12-30', '2012-12-29', '2012-12-28', '2012-12-27']}
df = pd.DataFrame(data)
plt.figure(figsize=(10, 6))
sns.barplot(x='date', y='cnt', data=df, palette='viridis')
plt.title('Bike Rental Count by Date')
plt.xlabel('Date')
plt.ylabel('Count (Mean)')
plt.xticks(rotation=45)
plt.show()

st.subheader("Advanced Analysis: Frequency by Date")
st.write("To know how often bicycles are rented based on the time of day. Every day and even every hour there is always bicycle rental activity, so the narrowest index (hr) is taken and searched using the average number of users in that hour to find out at what time the most frequent bicycle rental occurs.")
data = {'hr': [17, 18, 8, 16, 19, 13, 12, 15, 14, 20, 9, 7, 11, 10, 21, 22, 23, 6, 0, 1, 2, 3, 5, 4],
        'value': [461.452055, 425.510989, 359.011004, 311.983562, 311.523352, 253.661180, 253.315934,
                  251.233196, 240.949246, 226.030220, 219.309491, 212.064649, 208.143054, 173.668501,
                  172.314560, 131.335165, 87.831044, 76.044138, 53.898072, 33.375691, 22.869930,
                  19.889819, 11.727403, 6.352941]}
df = pd.DataFrame(data)
df = df.sort_values(by='hr')
plt.figure(figsize=(10, 6))
sns.barplot(x='hr', y='value', data=df, palette='viridis')
plt.title('Values by Hour')
plt.xlabel('Hour')
plt.ylabel('Count (Mean)')
plt.show()

st.subheader("Advanced Analysis: Monetary by Season")
st.write("To know in which season the bicycle rental service generates the most income is calculated from the total number of bicycle rental users including Casual and Registered.")

st.title("Conclusion")
st.write(""" 
The highest number of bicycle rental usage is at 18 and 19. The highest average bicycle rental usage is at 18 and the highest average bicycle rental usage is at 5.
The average bicycle rental user prefers to borrow on weekdays.
The average bicycle rental user prefers to borrow a bicycle in the fall season.

The normalized humidity level of 0.5 is the level at which the average rental bicycle is used.
The average bicycle rental user prefers to borrow a bicycle in Clear, Few clouds, Partly cloudy, Partly cloudy weather.
The wind speed normalization level of 0.247521 is the level at which the average bicycle rental is used.
The normalized temperature level of 0.601667 in Celsius is the level at which the average rental bicycle is used.
         """)