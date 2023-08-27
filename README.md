# VentureMark: Trademark Availability Tool

VentureMark is a Python program and a web application designed to help startup businesses check the availability of trademarks for their company names. The Python program utilizes web scraping techniques through Selenium to interact with the Canadian Intellectual Property Office (CIPO) trademark search page. The web application provides a user-friendly interface for checking trademark availability.

## Python Program (TrademarkScraperBot)

### Features

- Initializes a Chrome webdriver and navigates to the CIPO trademark search page.
- Selects search options for trademark lookup.
- Checks if a trademark name is available.
- Provides suggestions for similar trademark names if the original name is unavailable.
- Allows users to input trademark names and receive availability results.

### Requirements

- Python 3.x
- Selenium
- Webdriver Manager
- BeautifulSoup (for web scraping)
- Chrome Webdriver

### How to Use

1. Install Python: If you don't have Python installed, download and install it from the official website (https://www.python.org/downloads/). Choose a version of Python 3.x.

2. Install Required Packages: Open a terminal or command prompt and install the necessary packages using the following command:

   ```shell
   pip install selenium webdriver_manager beautifulsoup4

3. Download `chromedriver`: Download the `chromedriver` executable suitable for your system and place it in the same directory as the script. You can download it from the official ChromeDriver website: https://sites.google.com/chromium.org/driver/

4. Navigate to Script Directory: Open a terminal or command prompt and navigate to the directory where the Python script is located. Use the `cd` command to change to the appropriate directory.

5. Run the Script: In the terminal, run the Python script using the following command:

   ```shell
   python your_script_name.py

6. Replace `your_script_name.py` with the actual name of your Python script file.

7. Enter Trademark Name: The script will prompt you to enter a trademark name. Enter the desired name and press Enter.

8. View Results: The script will check the availability of the trademark and provide you with results. If the trademark is available, it will display "Trademark is available." If not, it will display "Trademark is not available."

9. Exit the Script: To exit the script, enter `exit` when prompted for a trademark name.

## Web Application (HTML, CSS, JavaScript)

### Features

- Provides a user-friendly interface for checking trademark availability.
- Sends a request to a Flask backend to check trademark availability.
- Displays the availability status of the trademark.

### How to Use

1. Open the `index.html` file in a web browser.
2. Enter a trademark name in the input field.
3. Click the "Check" button.
4. The availability status of the trademark will be displayed.

## Usage Example (Python Program)

```python
from trademark_scraper import TrademarkScraper

def main():
    bot = TrademarkScraper()  # Create an instance of TrademarkScraper
    try:
        while True:
            user_input = input("Enter a trademark name (or 'exit' to end): ")
            if user_input.lower() == "exit":
                break
            
            availability = bot.check_trademark_availability(user_input)  # Check trademark availability
            if availability:
                print("Trademark is available.")
            else:
                print("Trademark is not available.")
    finally:
        bot.cleanup()  # Clean up resources when done

if __name__ == "__main__":
    main()  # Execute the main function
```

## License

VentureMark License

Version 1.0, August 27, 2023

Copyright 2023

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

1. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

2. Commercial use, distribution, sublicensing, or selling of copies of the Software without explicit written permission from the author(s) is strictly prohibited.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

