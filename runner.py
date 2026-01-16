from debugger.recorder.tracer import start_tracing, stop_tracing
from debugger.security.analyzer import find_exploits
from debugger.security.taint import TAINTED_VARS
import mock_app.app as app

# 1️⃣ Start tracing
start_tracing()

# 2️⃣ Run mock application (with simulated virus)
app.main()

# 3️⃣ Stop tracing
trace = stop_tracing()

# 4️⃣ Analyze trace WITH taint info
exploits = find_exploits(trace, TAINTED_VARS)

# 5️⃣ Print condensed execution trace
print("\n🕒 Execution Trace (Condensed):")
for e in trace:
    if e["function"] in ("run_plugin", "exfiltrate"):
        print(e)

# 6️⃣ Print security findings
print("\n🚨 Security Analysis:")
if not exploits:
    print("No security issues detected.")
else:
    for ex in exploits:
        print(f"🔴 Variable '{ex['variable']}'")
        print(f"   Introduced in {ex['origin']['function']} "
            f"(line {ex['origin']['line']})")
        print(f"   Reached sink '{ex['sink']}' "
            f"at line {ex['line']}")
        print(f"   Severity: {ex['severity']}")
        print(f"   Issue: {ex['issue']}")
        print(f"   Suggested Fix: {ex['fix']}\n")
