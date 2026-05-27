import pandas as pd

# Load dataset
df = pd.read_csv('../data/airline_bookings.csv')

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.fillna(0)

# Convert date column
df['booking_date'] = pd.to_datetime(df['booking_date'])

# Save cleaned dataset
df.to_csv('../data/cleaned_airline_bookings.csv', index=False)

print("Data cleaned successfully")
