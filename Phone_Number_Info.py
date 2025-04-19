# Import the phonenumbers library
import phonenumbers

# Import necessary tools from phonenumbers
from phonenumbers import geocoder, carrier, timezone


def get_phone_number_info(enter_num, region='US'):
    """
    Get information about a phone number.
    
    Args:
        enter_num (str): The phone number entered by the user.
        region (str): The default region for parsing the phone number.
    
    Returns:
        dict: A dictionary containing phone number information.
    """
    try:
        # Parse the entered phone number to create a phone number object
        phone_num = phonenumbers.parse(enter_num, region)
        
        # Check if the phone number is valid
        valid = phonenumbers.is_valid_number(phone_num)
        
        # Get geographical location
        location = geocoder.description_for_number(phone_num, 'en')
        
        # Get carrier (service provider)
        phone_carrier = carrier.name_for_number(phone_num, 'en')
        
        # Get time zone(s)
        time_zones = timezone.time_zones_for_number(phone_num)
        
        return {
            'phone_number': phone_num,
            'valid': valid,
            'location': location,
            'carrier': phone_carrier,
            'time_zones': time_zones
        }
    except phonenumbers.NumberParseException as e:
        return {
            'error': f"Error parsing phone number: {e}"
        }

def main():
    """
    Main function to prompt the user and display phone number information.
    """
    # Prompt the user to enter a phone number
    enter_num = input("Enter a phone number (with country code, e.g., +1234567890): ").strip()
    
    # Get phone number information
    info = get_phone_number_info(enter_num)
    
    # Display the information
    if 'error' in info:
        print(info['error'])
    else:
        print(f"Phone Number: {info['phone_number']}")
        print(f"Valid: {'Yes' if info['valid'] else 'No'}")
        print(f"Geographical Location: {info['location']}")
        print(f"Carrier: {info['carrier']}")
        print(f"Time Zone(s): {', '.join(info['time_zones'])}")

if __name__ == "__main__":
    main()
