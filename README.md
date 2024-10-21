# NetPortAudit

This project consists of a Bash script that performs port scanning on a list of IP addresses using Nmap and then generates a summary report in an Excel file using Python. The script captures open ports for each IP and formats the results for easy analysis.

## Features

- Scans specified IP addresses for open ports using Nmap.
- Outputs results to a text file.
- Generates an Excel report summarizing the findings.
- Supports customizable IP-to-hostname mapping.

## Prerequisites

- **Bash**: A Unix shell for running the script.
- **Nmap**: A network scanning tool to perform the port scans.
- **Python**: For generating the Excel report.
- **XlsxWriter**: A Python library for creating Excel files.

## Installation

1. **Install Nmap**:
   - On Ubuntu/Debian: 
     ```bash
     sudo apt-get install nmap
     ```
   - On macOS: 
     ```bash
     brew install nmap
     ```

2. **Install Python and XlsxWriter**:
   ```bash
   pip install XlsxWriter

## Usage

### Modify the Script

1. **Edit the Bash script**: Include the list of IP addresses you wish to scan in the script.
2. **Update the Python section**: Modify the `ip_hostname_map` dictionary with your IP-to-hostname mappings.

### Run the Bash Script

```bash
chmod +x NetPortAudit.sh
./NetPortAudit.sh
```

3. **Generate the Excel Report:

After running the Bash script, the Python section will automatically create an Excel file named nmap_scan_results.xlsx.

## Output
- Text File: nmap_scan_results.txt will contain detailed scan results for each IP address.
- Excel File: nmap_scan_results.xlsx will provide a summary with columns for:
  - IP Address
  - Hostname
  - Open Ports



