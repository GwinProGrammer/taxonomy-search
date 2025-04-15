import requests

API_KEY = "a1d3c047-bb5143a8-e66d3a4a-aa59403a"  # Replace with your actual key
API_URL = "https://fortniteapi.io/v1/events/list/active"
# EVENT_ID = "epicgames_S14_FNCS_Qualifier1_EU_PC"

def get_fortnite_event_data():
    headers = {
        "Authorization": API_KEY  # This API uses Authorization header
    }
    
    params = {
        "eventId": EVENT_ID
    }
    
    try:
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()  # Check for HTTP errors
        
        data = response.json()
        
        if data.get("result"):
            # print(data)
            return data
        else:
            print("API returned no data")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None
def format_event_data(event_data):
    """Extracts and formats important event information"""
    if not event_data or not event_data.get('events'):
        return None
        
    event = event_data['events'][0]  # Get first event
    
    # Convert UTC timestamps to readable format
    begin_time = datetime.strptime(event['beginTime'], '%Y-%m-%dT%H:%M:%S.%fZ')
    end_time = datetime.strptime(event['endTime'], '%Y-%m-%dT%H:%M:%S.%fZ')
    
    return {
        'event_id': event['id'],
        'name': f"{event['name_line1']} - {event['name_line2']}",
        'region': event['region'],
        'dates': f"{begin_time.strftime('%b %d, %Y')} to {end_time.strftime('%b %d, %Y')}",
        'description': event['short_description'],
        'requirements': event['long_description'],
        'poster': event['poster'],
        'is_cumulative': event['cumulative'],
        'platforms': event.get('platforms', []),
        'colors': {
            'primary': event['renderData']['primary_color'],
            'secondary': event['renderData']['secondary_color']
        }
    }
# Example usage
if __name__ == "__main__":
    data = get_fortnite_event_data()
    if data:
        formatted = format_event_data(data)
        print("\n=== EVENT DETAILS ===")
        print(f"Name: {formatted['name']}")
        print(f"Region: {formatted['region']}")
        print(f"Dates: {formatted['dates']}")
        print(f"\nDescription: {formatted['description']}")
        print(f"\nRequirements: {formatted['requirements']}")
        print(f"\nPoster URL: {formatted['poster']}")
    else:
        print("No event data found")
    # if event_data:
    #     print("Event Data Retrieved Successfully!")
    #     print(f"Event Name: {event_data.get('name', 'N/A')}")
    #     print(f"Total Participants: {event_data.get('totalTeams', 'N/A')}")
    #     # Add more data processing as needed
    # else:
    #     print("Failed to retrieve event data")



# if __name__ == "__main__":
#     event_id = "epicgames_S14_FNCS_Qualifier1_EU_PC"
#     data = get_event_details(event_id)
    
    