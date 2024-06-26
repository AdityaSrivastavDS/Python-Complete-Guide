import requests
import os

# Function to fetch the data from the url and save it to a file
def fetchAndSaveToFile(url, path):
    try:
        # Fetching the data from the url
        r = requests.get(url)
        r.raise_for_status()  # This will raise an exception if the request failed
    except requests.exceptions.RequestException as err:
        print(f"Error occurred while fetching data: {err}")
        return

    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(path), exist_ok=True)
    print(f"Directory {os.path.dirname(path)} created.")

    try:
        # Writing the data to the file
        with open(path, "w", encoding='utf-8') as f:  # Specify encoding here
            f.write(r.text)
        print(f"File {path} written.")
    except IOError as e:
        print(f"Error occurred while writing to file: {e}")

# URL of the website
url = "https://timesofindia.indiatimes.com/city/delhi"

# Path to the file where the content will be written
file_path = "E:\\Aditya\\Notes\\Python\\Web Scraping\\Beautifulsoup Tutorial\\datas/times.html"

# Call the function
fetchAndSaveToFile(url, file_path)



