import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
data = pd.read_csv("main_data.csv")

def main():
    st.title('Influence of Season and Weather on Hourly in Daily Bicycle Rentals')

    # Display all data
    st.subheader('All Data:')
    st.write(data)

    # Plotting for Season
    st.subheader('Seasonal Influence:')
    plot_seasonal_influence()

    # Plotting for Weather
    st.subheader('Weather Influence:')
    plot_weather_influence()

def plot_seasonal_influence():
    new_df = pd.DataFrame(data)
    seasonal_data = new_df.groupby('season_daily')['count_daily'].mean()
    season_names = ['winter', 'summer', 'fall', 'spring']
    fig, ax = plt.subplots()
    ax.bar(season_names, seasonal_data)
    ax.set_title('The influence of season on the number of daily bicycle rentals')
    ax.set_xlabel('Season')
    ax.set_ylabel('Average Rental')
    st.pyplot(fig)

    st.write("Conclusion: The highest number of bicycle renters can be seen when the season is fall and the lowest when the season is winter.")

def plot_weather_influence():
    new_df = pd.DataFrame(data)
    weather_data = new_df.groupby('weather_situation_daily')['count_daily'].mean()
    weather_names = ['Clear', 'Mist', 'Heavy Rain']
    fig, ax = plt.subplots()
    ax.pie(weather_data, labels=weather_names, autopct="%1.1f%%")
    ax.set_title('The influence of weather on the number of hourly in daily bicycle rentals')
    st.pyplot(fig)

    st.write("Conclusion:Based on the pie chart, it can be seen that in the clear weather the number of bicycle renters is the highest and the least in heavy rain.")

st.caption('Copyright © Dicoding 2024')

if __name__ == "__main__":
    main()
