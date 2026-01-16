DANGEROUS_SINKS = {
    "run_command": {
        "severity": "HIGH",
        "issue": "Command Injection",
        "fix": (
            "Avoid executing raw user input. "
            "Use an allow-list of permitted commands or sanitize input strictly."
        )
    }
    ,
    "exfiltrate": {
        "severity": "HIGH",
        "issue": "Data Exfiltration",
        "fix": (
            "Do not send untrusted data to external endpoints. "
            "Validate and sanitize data, and restrict plugin capabilities."
        )
    }
}