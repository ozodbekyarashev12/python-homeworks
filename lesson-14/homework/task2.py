import sqlite3
import requests
from bs4 import BeautifulSoup
import csv

# Define SQLite Database
DB_NAME = 'jobs.db'

# Create and connect to SQLite database
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Create the jobs table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS jobs (
    job_title TEXT,
    company_name TEXT,
    location TEXT,
    job_description TEXT,
    application_link TEXT,
    UNIQUE(job_title, company_name, location)
)
''')

# Function to scrape job listings
def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    job_listings = []
    for job in soup.find_all('div', class_='card'):
        try:
            job_title = job.find('h2').text.strip()
            company_name = job.find('h3').text.strip()
            location = job.find('p', class_='location').text.strip()
            job_description = job.find('p', class_='description').text.strip()
            application_link = job.find('a')['href']
            
            job_listings.append((job_title, company_name, location, job_description, application_link))
        except AttributeError:
            # If any of the required elements are missing, skip the job entry
            continue

    return job_listings

# Function to insert or update job listings in the database
def load_jobs(job_listings):
    for job in job_listings:
        try:
            cursor.execute('''
            INSERT INTO jobs (job_title, company_name, location, job_description, application_link)
            VALUES (?, ?, ?, ?, ?)
            ''', job)
            conn.commit()
        except sqlite3.IntegrityError:
            # If the job already exists, update the existing record
            cursor.execute('''
            UPDATE jobs
            SET job_description = ?, application_link = ?
            WHERE job_title = ? AND company_name = ? AND location = ?
            ''', (job[3], job[4], job[0], job[1], job[2]))
            conn.commit()

# Function to filter jobs by location or company
def filter_jobs(location=None, company_name=None):
    query = "SELECT * FROM jobs WHERE 1=1"
    params = []

    if location:
        query += " AND location = ?"
        params.append(location)
    if company_name:
        query += " AND company_name = ?"
        params.append(company_name)

    cursor.execute(query, params)
    return cursor.fetchall()

# Function to export filtered jobs to a CSV file
def export_to_csv(jobs, filename='filtered_jobs.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Job Title', 'Company Name', 'Location', 'Job Description', 'Application Link'])
        writer.writerows(jobs)

# Main function to perform the tasks
def main():
    # Step 1: Scrape new job listings
    print("Scraping new job listings...")
    job_listings = scrape_jobs()

    # Step 2: Load job listings into the database (insert new jobs, update existing ones)
    print("Loading job listings into the database...")
    load_jobs(job_listings)

    # Step 3: Example of filtering jobs by location or company and exporting them
    print("Filter jobs by location or company:")
    location = input("Enter location to filter (or press Enter to skip): ")
    company_name = input("Enter company name to filter (or press Enter to skip): ")

    filtered_jobs = filter_jobs(location=location or None, company_name=company_name or None)

    # Step 4: Export filtered jobs to a CSV file
    if filtered_jobs:
        print(f"Exporting {len(filtered_jobs)} filtered jobs to CSV...")
        export_to_csv(filtered_jobs)
        print(f"Filtered jobs exported to 'filtered_jobs.csv'.")
    else:
        print("No jobs found with the given filter criteria.")

# Run the main function
if __name__ == '__main__':
    main()

    # Close the database connection
    conn.close()
