import whois

def whois_lookup(domain):
    """
    Perform a WHOIS lookup for a given domain.
    :param domain: The domain name to query.
    :return: Dictionary containing WHOIS information.
    """
    try:
        w = whois.whois(domain)
        return {
            "Domain": w.domain_name,
            "Registrar": w.registrar,
            "Creation Date": str(w.creation_date),
            "Expiration Date": str(w.expiration_date),
            "Updated Date": str(w.updated_date),
            "Name Servers": w.name_servers,
            "Status": w.status,
        }
    except Exception as e:
        return {"Error": f"WHOIS lookup failed: {e}"}
