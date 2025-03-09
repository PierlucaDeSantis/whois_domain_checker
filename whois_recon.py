import argparse
import json
from modules.whois_lookup import whois_lookup
from modules.dns_lookup import dns_lookup
from modules.ip_info import ip_info
from modules.blacklist_check import check_blacklist

def generate_html_report(report_data, output_file):
    """
    Generate an HTML report from the analysis results.
    :param report_data: Dictionary containing analysis results.
    :param output_file: Output HTML file name.
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>WHOIS & DNS Recon Report</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h1>WHOIS & DNS Recon Report</h1>
    """
    
    for section, data in report_data.items():
        html_content += f"<h2>{section}</h2><table>"
        if isinstance(data, dict):
            html_content += "<tr><th>Key</th><th>Value</th></tr>"
            for key, value in data.items():
                html_content += f"<tr><td>{key}</td><td>{value}</td></tr>"
        else:
            html_content += f"<tr><td>{data}</td></tr>"
        html_content += "</table>"
    
    html_content += """
    </body>
    </html>
    """
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"HTML report generated: {output_file}")

# Main function
def main():
    parser = argparse.ArgumentParser(description="WHOIS & DNS Recon Tool")
    parser.add_argument("domain", help="Domain name to analyze")
    parser.add_argument("--output", help="Output file name (JSON)", default="report.json")
    args = parser.parse_args()
    
    report = {
        "WHOIS Data": whois_lookup(args.domain),
        "DNS Records": dns_lookup(args.domain),
        "IP Information": ip_info(args.domain),
        "Blacklist Status": check_blacklist(args.domain)
    }
    
    with open(args.output, "w") as f:
        json.dump(report, f, indent=4)
    
    print(f"JSON report generated: {args.output}")
    
    # Generate HTML Report
    html_output = args.output.replace(".json", ".html")
    generate_html_report(report, html_output)

if __name__ == "__main__":
    main()
