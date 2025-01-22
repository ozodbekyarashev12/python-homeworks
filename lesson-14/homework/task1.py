from bs4 import BeautifulSoup

# HTML data as a string (this is the content you provided)
html_data = """
<!DOCTYPE html>
<html>
<head>
    <title>Weather Forecast</title>
</head>
<body>
    <h4>5-Day Weather Forecast</h4>
    <table>
        <thead>
            <tr>
                <th>Day</th>
                <th>Temperature</th>
                <th>Condition</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Monday</td>
                <td>25°C</td>
                <td>Sunny</td>
            </tr>
            <tr>
                <td>Tuesday</td>
                <td>22°C</td>
                <td>Cloudy</td>
            </tr>
            <tr>
                <td>Wednesday</td>
                <td>18°C</td>
                <td>Rainy</td>
            </tr>
            <tr>
                <td>Thursday</td>
                <td>20°C</td>
                <td>Partly Cloudy</td>
            </tr>
            <tr>
                <td>Friday</td>
                <td>30°C</td>
                <td>Sunny</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
"""

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_data, 'html.parser')

# Extract the weather table
table = soup.find('table')

# Initialize lists to store the data
days = []
temperatures = []
conditions = []

# Loop through the rows in the table (skipping the header row)
for row in table.find_all('tr')[1:]:  # Start from the second row to skip the header
    cells = row.find_all('td')
    day = cells[0].get_text()
    temperature = cells[1].get_text()
    condition = cells[2].get_text()
    
    days.append(day)
    temperatures.append(temperature)
    conditions.append(condition)

# Display Weather Data
print("5-Day Weather Forecast:")
for i in range(len(days)):
    print(f"Day: {days[i]}, Temperature: {temperatures[i]}, Condition: {conditions[i]}")

# Find Specific Data
# Highest Temperature
max_temp = max(temperatures, key=lambda x: int(x[:-2]))  # Remove the '°C' and compare the values
max_temp_day = days[temperatures.index(max_temp)]

# "Sunny" condition
sunny_days = [days[i] for i in range(len(conditions)) if conditions[i] == 'Sunny']

# Calculate Average Temperature
temp_values = [int(temp[:-2]) for temp in temperatures]  # Remove '°C' and convert to integers
average_temp = sum(temp_values) / len(temp_values)

# Print the results
print("\nSpecific Data:")
print(f"Day with the highest temperature: {max_temp_day} ({max_temp})")
print(f"Day(s) with 'Sunny' condition: {', '.join(sunny_days)}")
print(f"Average Temperature for the week: {average_temp:.2f}°C")
