# Time Travel Debugger

The **Time Travel Debugger** is a simulated security-focused debugging environment designed to demonstrate how untrusted code, plugins, and data flows can be traced, analyzed, and “rewound” during execution. It mimics real-world attack scenarios such as malicious plugins, data exfiltration, and tainted variables—making it ideal for learning about secure systems, sandboxing, and runtime inspection.

This project blends concepts from:

* Secure execution environments
* Taint tracking
* Plugin isolation
* Execution tracing
* Incident simulation

It’s not just a debugger—it’s a *CyberSecurity Forensic Analyst* for code execution.

---

## Features

* Simulated secure application runtime
* Plugin-based architecture (trusted vs untrusted plugins)
* Taint tracking for sensitive variables
* Execution trace logging
* Malicious behavior simulation (e.g., data exfiltration)
* “Time travel” concept to inspect and replay execution paths

---

## Project Structure

```
time_travel_debugger/
├── debugger/
│   ├── runner.py          # Entry point for the debugger runtime
│   ├── core.py            # Execution engine & trace manager
│   └── taint.py           # Taint tracking utilities
├── plugins/
│   ├── safe_plugin.py
│   └── virus.py           # Simulated malicious plugin
└── README.md
```

---

## Running the Debugger

From the project root:

```bash
python3 -m debugger.runner
```

You’ll be prompted to upload a plugin name:

```
🔐 Secure Application Started
Upload plugin name: virus
```

Example output:

```
Processing plugin: virus
⚠️ Untrusted plugin executed
[SIMULATION] Exfiltrating data: {'token': 'SECRET_API_KEY'}

🕒 Execution Trace (Condensed)
...
```

This demonstrates:

* Detection of untrusted code
* Tracking of sensitive data
* Logging of suspicious behavior
* A trace you can “rewind” and analyze

---

## Purpose

This project is meant to:

* Teach how security tools reason about code execution
* Show how tainted data propagates
* Simulate real-world plugin abuse
* Provide a foundation for building:

  * Sandboxes
  * Secure plugin systems
  * Runtime analyzers
  * Educational security tools

It’s perfect for:

* Students learning cybersecurity
* Developers exploring secure runtimes
* Hackathon demos
* Portfolio projects

---

## Future Ideas

* Step-by-step time rewind of execution
* Visual execution timeline
* Plugin permission system
* Real AST-level tracing
* Web-based UI for inspection

---

**Time Travel Debugger** turns security debugging into a narrative experience—where every line of code leaves a footprint in time.
