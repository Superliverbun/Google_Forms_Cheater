import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import random
import time

# Set stdout encoding to utf-8
sys.stdout.reconfigure(encoding='utf-8')

def fill_form(url, num_submissions):
    driver = webdriver.Chrome()
    
    for submission in range(num_submissions):
        driver.get(url)
        
        try:
            # Wait for the form to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "form"))
            )
            
            # Find all questions
            questions = driver.find_elements(By.CSS_SELECTOR, ".geS5n")
            
            for question in questions:
                # Find all options for the question
                options = question.find_elements(By.CSS_SELECTOR, ".Od2TWd")
                
                if options:
                    # Randomly select an option
                    random.choice(options).click()
                    time.sleep(0)  # Brief pause to simulate human action
            
            # Try to find and click the submit button
            submit_button = None
            possible_submit_selectors = [
                "div[role='button'][jsname='M2UYVd']",
                ".uArJ5e.UQuaGc.Y5sE8d.VkkpIf",
                "div[jscontroller='soHxf'][jsaction]",
                "[type='submit']"
            ]
            
            for selector in possible_submit_selectors:
                try:
                    submit_button = driver.find_element(By.CSS_SELECTOR, selector)
                    break
                except NoSuchElementException:
                    continue
            
            if submit_button:
                submit_button.click()
                print(f"Form {submission + 1} was randomly filled and submitted")
            else:
                print(f"Form {submission + 1} could not find a submit button")
            
            # Wait a few seconds to ensure the form is submitted
            time.sleep(3)
        
        except TimeoutException:
            print(f"Form {submission + 1} timed out during loading")
        except Exception as e:
            print(f"An error occurred while filling form {submission + 1}: {str(e)}")
    
    driver.quit()

# Example usage
form_url = "YOUR_LINK_HERE"
number_of_submissions = 1
fill_form(form_url, number_of_submissions)
