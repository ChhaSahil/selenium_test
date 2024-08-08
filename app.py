import streamlit as st
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import transformers
st.title("Selenium with Chrome in Docker")

def create_webdriver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--remote-debugging-port=9222")  # This is crucial for headless mode in Docker

    service = ChromeService(executable_path="/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver
st.write(transformers.__version__)
if st.button("Run Selenium"):
    driver = create_webdriver()
    driver.get("https://www.google.com")
    st.write("Page title:", driver.title)
    driver.quit()
import streamlit as st
import subprocess

def install_chromedriver():
    st.write("Installing ChromeDriver...")

    try:
        # Download ChromeDriver
        subprocess.run(["wget", "-O", "/tmp/chromedriver.zip", 
                        "https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.99/linux64/chromedriver-linux64.zip"], 
                       check=True)
        
        # Unzip ChromeDriver
        subprocess.run(["unzip", "/tmp/chromedriver.zip", "-d", "/tmp/"], check=True)
        
        # Move ChromeDriver to the correct location
        subprocess.run(["mv", "/tmp/chromedriver-linux64/chromedriver", "/usr/local/bin/chromedriver"], check=True)
        
        # Clean up by removing the zip file
        subprocess.run(["rm", "/tmp/chromedriver.zip"], check=True)

        st.success("ChromeDriver installed successfully!")
    except subprocess.CalledProcessError as e:
        st.error(f"An error occurred: {e}")

# Streamlit app code
st.title("ChromeDriver Installer")

if st.button("Install ChromeDriver"):
    install_chromedriver()