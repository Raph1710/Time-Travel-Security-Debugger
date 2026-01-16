from debugger.security.sinks import DANGEROUS_SINKS
from debugger.security.taint import TAINTED_VARS

def find_exploits(trace, tainted_vars):
    issues = []
    taint_origins = {}

    # Detect taint introduction
    for event in trace:
        if event["type"] == "line":
            for var in event.get("locals", {}):
                if var in tainted_vars and var not in taint_origins:
                    taint_origins[var] = {
                        "function": event["function"],
                        "line": event["line"],
                        "timestamp": event["timestamp"]
                    }

    # Detect tainted sinks
    for event in trace:
        if event["type"] != "call":
            continue

        func = event["function"]
        locals_ = event.get("locals", {})

        if func in DANGEROUS_SINKS:
            for var in locals_:
                if var in tainted_vars:
                    sink_info = DANGEROUS_SINKS[func]

                    issues.append({
                        "variable": var,
                        "origin": taint_origins.get(var),
                        "sink": func,
                        "line": event["line"],
                        "severity": sink_info["severity"],
                        "issue": sink_info["issue"],
                        "fix": sink_info["fix"],
                        "timestamp": event["timestamp"]
                    })

    return issues