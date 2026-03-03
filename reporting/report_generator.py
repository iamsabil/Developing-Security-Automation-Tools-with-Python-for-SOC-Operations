import json
from datetime import datetime

def generate_report(events, filename="security_report.json"):
    report = {
        "generated_at": str(datetime.now()),
        "total_alerts": len(events),
        "events": events
    }
    
    with open(filename, "w") as f:
        json.dump(report, f, indent=4)
    
    print("[INFO] Report generated.")
