import socket

def get_domain_ip():
    """Get the IP address of a given domain."""
    try:
        url_name = input('Enter the Domain URL(e,g google.com): ').strip()
        if not url_name:
            print("Error: Domain URL cannot be empty.")
            return
        
        ip = socket.gethostbyname(url_name)
        print(f"The IP address of {url_name} is: {ip}")
    except socket.gaierror:
        print("Error: Unable to resolve the domain. Please check the URL.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    get_domain_ip()