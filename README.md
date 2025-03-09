# WHOIS & DNS Recon Tool

##  Description
This tool performs **WHOIS and DNS recon** on a given domain, providing insights about:
- **WHOIS Information** (Registrar, Creation & Expiry Date, Name Servers, etc.)
- **DNS Records** (A, MX, NS, TXT, CNAME, etc.)
- **Blacklist Status** (Check if a domain is flagged as malicious)
- **Reports** in both **JSON and HTML** formats

---

##  Installation
### **1 Clone the repository**
```bash
git clone https://github.com/yourusername/whois_recon_tool.git
cd whois_recon_tool
```

### **2 Install dependencies**
```bash
pip install -r requirements.txt
```

---

##  Usage
Run the tool using:
```bash
python whois_recon.py example.com --output report.json
```

### **Options:**
- `example.com` → The domain to analyze
- `--output report.json` → Output report file (default: `report.json`)

The script generates:
 **JSON Report** (`report.json`)
 **HTML Report** (`report.html`)

---

## 🛠 Modules Overview
- **`whois_lookup.py`** → Performs WHOIS lookup on domains
- **`dns_lookup.py`** → Retrieves DNS records
- **`blacklist_check.py`** → Checks if the domain is blacklisted
- **`whois_recon.py`** → Main script managing execution and reporting

---

##  Example Output
### **JSON Output (report.json)**
```json
{
    "WHOIS Data": {"Registrar": "NameCheap", "Expiration Date": "2026-10-15"},
    "DNS Records": {"A": "192.168.1.1", "MX": "mail.example.com"},
    "Blacklist Status": "Clean"
}
```

### **HTML Report Preview**
The tool also generates an HTML report for better readability.

---

##  License
This project is licensed under the **MIT License**.

---

##  Contributing
Feel free to **fork** this project and submit pull requests! 🚀
