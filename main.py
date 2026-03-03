from parsers.log_parser import parse_auth_log
from detection.anomaly_detector import detect_brute_force
from threat_intel.ti_enrichment import check_ip_reputation
from response.auto_response import block_ip
from reporting.report_generator import generate_report

def main():
    logs = parse_auth_log("logs/sample_auth.log")
    
    suspicious = detect_brute_force(logs)
    
    enriched_events = []
    
    for event in suspicious:
        reputation = check_ip_reputation(event["ip"])
        event.update(reputation)
        
        if event["abuse_score"] > 70:
            block_ip(event["ip"])
        
        enriched_events.append(event)
    
    generate_report(enriched_events)

if __name__ == "__main__":
    main()
