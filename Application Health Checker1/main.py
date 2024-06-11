import requests
import time

def check_app_health(url, expected_status_code=200):

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == expected_status_code:
            return "up"
        else:
            return "down"
    except requests.ConnectionError:
        return "down"
    except requests.Timeout:
        return "down"
    except requests.RequestException:
        return "down"

def main():
    url = "https://example.com"  # Replace with the URL of the application to check
    while True:
        status = check_app_health(url)
        print(f"Application status: {status}")
        time.sleep(60)  # Check every 1 minute

if __name__ == "__main__":
    main()