import csv

# Path to your text file with email addresses
input_file_path = 'emails.txt'
# Path where you want to save the CSV file
output_file_path = 'contacts.csv'

# Read email addresses from the text file
with open(input_file_path, 'r') as file:
    emails = file.readlines()

# Strip whitespace characters (like newline) from each email
emails = [email.strip() for email in emails]

# Create a CSV file and write the data
with open(output_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the header row
    csv_writer.writerow(['First Name', 'Last Name', 'Email Address'])
    
    # Write empty first and last names along with the email addresses
    for email in emails:
        csv_writer.writerow(['', '', email])

print(f"CSV file '{output_file_path}' created successfully.")
