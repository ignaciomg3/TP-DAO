import pandas as pd

def generate_hardcoded_report():
    data = {
        'Room Number': [101, 102, 103, 104],
        'Type': ['Single', 'Double', 'Suite', 'Single'],
        'Status': ['Occupied', 'Vacant', 'Occupied', 'Vacant'],
        'Price': [100, 150, 200, 100]
    }
    df = pd.DataFrame(data)
    report = df.describe(include='all')
    report.to_csv('room_report.csv')
    print("Report generated and saved as 'room_report.csv'")

generate_hardcoded_report()
# Sample data
data = {
    'Room Number': [101, 102, 103, 104],
    'Type': ['Single', 'Double', 'Suite', 'Single'],
    'Status': ['Occupied', 'Vacant', 'Occupied', 'Vacant'],
    'Price': [100, 150, 200, 100]
}

# Create DataFrame
df = pd.DataFrame(data)

# Generate report
report = df.describe(include='all')

# Save report to a CSV file
report.to_csv('room_report.csv')

print("Report generated and saved as 'room_report.csv'")