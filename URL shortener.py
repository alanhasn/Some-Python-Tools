from pystyle import *  # Importing the pystyle library for styled text and boxes
import pyshorteners as short  # Importing pyshorteners library for URL shortening

# Function to display the banner
def display_banner():
    print(Box.Lines('\n[+] URL Shortener [+]'))  # Display a styled box with the title
    Write.Print('[+] URL shortening \n', Colors.purple_to_red, interval=0.1)  # Print styled text
    print(Box.DoubleCube('\nPython URL Shortener'))  # Display another styled box

# Function to get URL input from the user
def get_url_input():
    return Write.Input('[-] Please enter the URL: ', Colors.blue_to_green, interval=0.1)  # Prompt user for URL input with styled text

# Function to shorten the given URL
def shorten_url(url):
    sh = short.Shortener()  # Create an instance of the Shortener class
    return sh.tinyurl.short(url)  # Use the tinyurl service to shorten the URL

# Main function to execute the program
def main():
    display_banner()  # Display the banner
    url = get_url_input()  # Get the URL input from the user
    shortened_url = shorten_url(url)  # Shorten the URL
    print(f"[+] Shortened URL: {shortened_url}")  # Display the shortened URL
    print(Box.DoubleCube('\n[+] URL Shortener [+]'))  # Display a styled box
    input('\nPress any key to exit')  # Wait for user input before exiting

# Entry point of the program
if __name__ == "__main__":
    main()  # Call the main function
