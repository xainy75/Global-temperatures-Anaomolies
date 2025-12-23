import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# --- STEP 1: Generate Mock Climate Data (Historical: 1950-2024) ---
np.random.seed(42) # Keep results consistent
years_hist = np.arange(1950, 2025)
n_years = len(years_hist)

# Simulating a rising temperature trend with noise
base_trend = np.linspace(-0.2, 1.2, n_years)
noise = np.random.normal(0, 0.15, n_years)
temperature_anomaly = base_trend + noise

df = pd.DataFrame({
    'Year': years_hist,
    'Temp_Anomaly_C': temperature_anomaly
})

# Calculate 5-Year Moving Average for context
df['5_Year_Moving_Avg'] = df['Temp_Anomaly_C'].rolling(window=5).mean()


# --- STEP 2: Linear Regression Modeling ---

# 2a. Prepare data for scikit-learn
# Sklearn expects features (X) to be a 2D array (a matrix), hence double brackets [['Year']]
X_historical = df[['Year']]
y_historical = df['Temp_Anomaly_C']

# 2b. Instantiate and train the model
model = LinearRegression()
# The model learns the relationship between Year (X) and Temp (y)
model.fit(X_historical, y_historical)

# Get the slope (m) and intercept (b) of the line (y = mx + b)
slope = model.coef_[0]
intercept = model.intercept_
print(f"--- Model Summary ---")
print(f"Trend: Temperatures are increasing by approximately {slope:.4f}°C per year.")


# --- STEP 3: Predicting the Future (2025-2030) ---

# Create 2D array for future years
future_years = np.arange(2025, 2031).reshape(-1, 1)

# Make predictions
future_predictions = model.predict(future_years)

# Create a DataFrame to hold future results for easier reading
df_future = pd.DataFrame({
    'Year': future_years.flatten(),
    'Predicted_Anomaly_C': future_predictions
})

print("\n--- Future Predictions (Linear Trend) ---")
print(df_future)
prediction_2030 = df_future[df_future['Year'] == 2030]['Predicted_Anomaly_C'].values[0]
print(f"\n*** Predicted Temperature Anomaly for 2030: {prediction_2030:.2f}°C ***")


# --- STEP 4: Visualization ---

plt.figure(figsize=(12, 7))
sns.set_style("whitegrid")

# 1. Historical Raw Data (Gray Dots)
sns.scatterplot(data=df, x='Year', y='Temp_Anomaly_C', color='gray', alpha=0.5, label='Historical Annual Data')

# 2. Historical 5-Year Moving Average (Red Line)
sns.lineplot(data=df, x='Year', y='5_Year_Moving_Avg', color='red', linewidth=2, label='5-Year Moving Avg (Historical)')

# 3. The Regression Trend Line (Historical fit)
# We predict on historical years to show the "best fit" line through past data
historical_trend = model.predict(X_historical)
plt.plot(df['Year'], historical_trend, color='blue', linestyle='--', linewidth=2, label='Linear Trend Line')

# 4. Future Predictions (Blue markers)
plt.scatter(future_years, future_predictions, color='blue', marker='X', s=100, label='Future Predictions (2025-2030)')

# Formatting
plt.title('Global Temperature Anomaly: Historical Trend & 2030 Prediction', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Temperature Anomaly (°C)', fontsize=12)
plt.axhline(0, color='black', linewidth=1, linestyle='-')
plt.axvline(2024.5, color='green', linestyle=':', linewidth=1.5, label='Present Day') # Separator line

# Add annotation for the 2030 data point
plt.annotate(f'2030 Prediction:\n{prediction_2030:.2f}°C',
             xy=(2030, prediction_2030),
             xytext=(2022, prediction_2030 + 0.3),
             arrowprops=dict(facecolor='blue', shrink=0.05),
             fontsize=10, color='blue', fontweight='bold')

plt.legend(loc='upper left')
plt.tight_layout()
plt.show()