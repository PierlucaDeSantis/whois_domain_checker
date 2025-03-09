import dns.resolver
from ipwhois import IPWhois

def ip_info(domain):
    """
    Retrieve ASN and geolocation data for a given domain.
    :param domain: The domain name to analyze.
    :return: Dictionary containing IP, ASN, and geolocation details.
    """
    try:
        ip = dns.resolver.resolve(domain, "A")[0].to_text()
        obj = IPWhois(ip)
        results = obj.lookup_rdap()
        return {
            "IP": ip,
            "ASN": results.get("asn"),
            "ASN Country": results.get("asn_country_code"),
            "ISP": results.get("network", {}).get("name", "Unknown"),
        }
    except Exception as e:
        return {"Error": f"IP lookup failed: {e}"}
