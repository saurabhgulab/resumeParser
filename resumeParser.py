import os
from docx import Document
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Paths
BASE_RESUME_PATH = "BaseResume.docx"
UPDATED_RESUME_PATH = "UpdatedResume.docx"
JOB_DESCRIPTION_PATH = "JobDescription.txt"
CHROME_DRIVER_PATH = "path/to/chromedriver"

# Function to extract keywords from job description
def extract_keywords(job_description_file):
    with open(job_description_file, "r") as file:
        text = file.read()
    # Simple keyword extraction logic (customize as needed)
    keywords = [word for word in text.split() if len(word) > 4]
    return keywords

# Function to update resume with extracted keywords
def update_resume(base_resume_path, updated_resume_path, keywords):
    doc = Document(base_resume_path)
    for paragraph in doc.paragraphs:
        # Example: Replace placeholder text with extracted keywords
        if "{SKILLS}" in paragraph.text:
            paragraph.text = paragraph.text.replace("{SKILLS}", ", ".join(keywords))
        if "{SUMMARY}" in paragraph.text:
            paragraph.text = paragraph.text.replace("{SUMMARY}", "Tailored for the role based on the job description.")
    doc.save(updated_resume_path)
    print(f"Updated resume saved at {updated_resume_path}")

# Function to automate resume upload using Selenium
def upload_resume(resume_path):
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    driver.get("https://example.com/login")  # Replace with actual URL

    # Login process
    driver.find_element(By.ID, "username").send_keys("your_username")
    driver.find_element(By.ID, "password").send_keys("your_password")
    driver.find_element(By.ID, "loginButton").click()

    # Navigate to resume upload section
    time.sleep(3)  # Wait for login
    driver.get("https://example.com/resume-upload")  # Replace with actual URL

    # Upload resume
    upload_element = driver.find_element(By.ID, "resumeUpload")  # Replace with actual element ID
    upload_element.send_keys(os.path.abspath(resume_path))
    driver.find_element(By.ID, "submitResume").click()  # Replace with actual element ID

    print("Resume uploaded successfully!")
    driver.quit()

# Main execution
if __name__ == "__main__":
    # Step 1: Extract keywords
    keywords = extract_keywords(JOB_DESCRIPTION_PATH)

    # Step 2: Update resume
    update_resume(BASE_RESUME_PATH, UPDATED_RESUME_PATH, keywords)

    # Step 3: Upload updated resume
    upload_resume(UPDATED_RESUME_PATH)
