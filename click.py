from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import random
import time

class UniqueVisitorSimulator:
    def __init__(self, url):
        self.url = url
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 Edge/91.0.864.64",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        ]
        self.driver = None

    def create_driver(self, user_agent):
        """Create a new WebDriver instance with a specified user agent"""
        chrome_options = Options()
        chrome_options.add_argument(f"user-agent={user_agent}")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def visit_link(self):
        """Open the URL with a unique user agent"""
        user_agent = random.choice(self.user_agents)
        self.create_driver(user_agent)
        self.driver.get(self.url)
        print(f"Visited: {self.url} with User Agent: {user_agent}")
        self.driver.quit()

    def run_simulation(self, num_visits):
        """Run the simulation for a specified number of visits"""
        for _ in range(num_visits):
            self.visit_link()
            time.sleep(random.uniform(1, 3))  # Simulate delay between visits

if __name__ == "__main__":
    url = "https://learn.microsoft.com/en-gb/users/adityasrivastav-6032/?wt.mc_id=studentamb_306330"  # Replace with your URL
    simulator = UniqueVisitorSimulator(url)
    simulator.run_simulation(132)  # Simulate 130 unique visits
