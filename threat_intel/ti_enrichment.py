def check_ip_reputation(ip):
    # Mock reputation check (Replace with real API integration)
    mock_scores = {
        "192.168.1.10": 85
    }
    
    return {
        "ip": ip,
        "abuse_score": mock_scores.get(ip, 10)
    }
