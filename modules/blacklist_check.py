import requests

def check_blacklist(domain):
    """
    Check if a domain is blacklisted using external APIs.
    :param domain: The domain name to analyze.
    :return: Dictionary containing blacklist status.
    """
    blacklist_providers = [
        "https://api.abuseipdb.com/api/v2/check?ipAddress=",
        "https://threatintelligenceplatform.com/check?domain="
    ]
    status = {}
    
    for provider in blacklist_providers:
        try:
            response = requests.get(provider + domain, timeout=5)
            if response.status_code == 200:
                status[provider] = "Potential threat detected"
            else:
                status[provider] = "Clean"
        except Exception as e:
            status[provider] = f"Error checking blacklist: {e}"
    
    return status
