
import csv
import os

# ==========================================
# 1. CREATE A CSV FILE
# ==========================================

people = [
    {'first_name': 'John', 'last_name': 'Smith', 'country': 'USA'},
    {'first_name': 'David', 'last_name': 'Perera', 'country': 'Sri Lanka'},
    {'first_name': 'Sarah', 'last_name': 'Johnson', 'country': 'UK'},
    {'first_name': 'Amal', 'last_name': 'Silva', 'country': 'Sri Lanka'},
    {'first_name': 'Michael', 'last_name': 'Brown', 'country': 'Canada'}
]

with open('people.csv', 'w', newline='') as csv_file:

    fieldnames = ['first_name', 'last_name', 'country']

    csv_writer = csv.DictWriter(
        csv_file,
        fieldnames=fieldnames
    )

    csv_writer.writeheader()
    csv_writer.writerows(people)


# ==========================================
# 2. READ AND PARSE THE CSV FILE
# ==========================================

html_output = ''

with open('people.csv', 'r') as csv_file:

    csv_reader = csv.DictReader(csv_file)

    # Start HTML document
    html_output += """
    <!DOCTYPE html>
    <html>
    <head>
        <title>People Directory</title>
        <style>
            body {
                font-family: Arial;
                background-color: #f4f4f4;
                padding: 30px;
            }

            li {
                background: white;
                padding: 12px;
                margin: 10px;
                border-radius: 8px;
            }

            h1 {
                color: #333;
            }
        </style>
    </head>
    <body>
        <h1>People Directory</h1>
        <ul>
    """

    # Process every row
    for line in csv_reader:

        first_name = line['first_name']
        last_name = line['last_name']
        country = line['country']

        # Combine names
        full_name = f'{first_name} {last_name}'

        # Generate HTML list item
        html_output += (
            f'<li><strong>{full_name}</strong> '
            f'- {country}</li>\n'
        )

    # Close HTML tags
    html_output += """
        </ul>
    </body>
    </html>
    """


# ==========================================
# 3. WRITE THE HTML FILE
# ==========================================

with open('people.html', 'w') as html_file:

    html_file.write(html_output)


# ==========================================
# 4. DISPLAY RESULTS
# ==========================================

print('=' * 40)
print('CSV TO HTML CONVERTER')
print('=' * 40)

print('\nCSV file created: people.csv')
print('HTML file created: people.html')

print('\nGenerated HTML:')
print(html_output)

# Open HTML file in default browser
file_path = os.path.abspath('people.html')

os.startfile(file_path)

print('\nProject completed successfully!')
