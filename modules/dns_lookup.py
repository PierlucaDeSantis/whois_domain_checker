import dns.resolver

def dns_lookup(domain):
    """
    Perform a DNS lookup for a given domain.
    :param domain: The domain name to query.
    :return: Dictionary containing DNS records.
    """
    records = {}
    dns_records = ["A", "MX", "NS", "TXT", "CNAME"]
    
    for record in dns_records:
        try:
            answers = dns.resolver.resolve(domain, record)
            records[record] = [str(r) for r in answers]
        except Exception as e:
            records[record] = f"Error retrieving {record}: {e}"
    
    return records
