import re

def parse_auth_log(file_path):
    parsed_logs = []
    
    with open(file_path, 'r') as file:
        for line in file:
            ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
            if ip_match:
                parsed_logs.append({
                    "raw": line.strip(),
                    "ip": ip_match.group(1)
                })
    return parsed_logs
