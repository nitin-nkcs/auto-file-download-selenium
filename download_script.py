import os
import time
import glob
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import config  # Import the config module

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get(config.URL)

# Function to select options from a dropdown
def select_dropdown_options(dropdown_id, ignore_values):
    dropdown = Select(driver.find_element(By.ID, dropdown_id))
    options = [option for option in dropdown.options if option.get_attribute('value') not in ignore_values]
    return options

# Function to select options containing specific text
def select_options_containing_text(dropdown_id, text):
    dropdown = Select(driver.find_element(By.ID, dropdown_id))
    options = [option for option in dropdown.options if text in option.text]
    return options

# Function to rename the downloaded file
def rename_downloaded_file(session, exam, subject):
    new_name = f"{session}_{exam}_{subject}.pdf"
    downloads_path = config.DOWNLOADS_PATH
    
    # Get list of all files in the Downloads folder
    list_of_files = glob.glob(os.path.join(downloads_path, "*"))
    
    # Find the most recently downloaded file
    latest_file = max(list_of_files, key=os.path.getctime)
    
    # Construct the new file path
    new_file_path = os.path.join(downloads_path, new_name)
    
    # Check if a file with the new name already exists and remove it
    if os.path.exists(new_file_path):
        os.remove(new_file_path)
    
    # Rename the file
    os.rename(latest_file, new_file_path)

# Ignore values
ignore_values = config.IGNORE_VALUES
# Text to search in Exam dropdown
exam_search_text = config.EXAM_SEARCH_TEXT

# Get all session options
session_options = select_dropdown_options('ContentPlaceHolder1_DropDownList1', ignore_values)

for session_option in session_options:
    session_text = session_option.text
    session_option.click()
    WebDriverWait(driver, 10).until(EC.staleness_of(session_option))  # Wait for the page to reload

    # Re-locate the session dropdown and select the current session again
    session_dropdown = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_DropDownList1'))
    session_dropdown.select_by_visible_text(session_text)

    # Get all exam options containing the specified text
    exam_options = select_options_containing_text('ContentPlaceHolder1_ddlexam', exam_search_text)

    for exam_option in exam_options:
        exam_text = exam_option.text
        exam_option.click()
        WebDriverWait(driver, 10).until(EC.staleness_of(exam_option))  # Wait for the page to reload

        # Re-locate the exam dropdown and select the current exam again
        exam_dropdown = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_ddlexam'))
        exam_dropdown.select_by_visible_text(exam_text)

        # Get all subject options
        subject_options = select_dropdown_options('ContentPlaceHolder1_ddlSub', ignore_values)

        for subject_option in subject_options:
            subject_text = subject_option.text
            subject_option.click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'ContentPlaceHolder1_btnDownload')))  # Wait for the download button to be clickable

            # Click the download button
            download_button = driver.find_element(By.ID, 'ContentPlaceHolder1_btnDownload')
            download_button.click()
            time.sleep(5)  # Wait for the download action to complete

            # Rename the downloaded file
            rename_downloaded_file(session_text, exam_text, subject_text)

driver.quit()
