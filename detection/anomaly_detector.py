from collections import defaultdict

def detect_brute_force(logs, threshold=5):
    ip_counter = defaultdict(int)
    
    for log in logs:
        ip_counter[log["ip"]] += 1
    
    suspicious_ips = []
    
    for ip, count in ip_counter.items():
        if count >= threshold:
            suspicious_ips.append({
                "ip": ip,
                "attempts": count,
                "reason": "Possible Brute Force"
            })
    
    return suspicious_ips
