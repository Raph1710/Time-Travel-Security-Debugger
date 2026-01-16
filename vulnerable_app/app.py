from debugger.recorder.tracer import start_tracing, stop_tracing
from debugger.security.taint import TAINTED_VARS

def authenticate(user):
    return user == "admin"

def run_command(cmd):
    print(f"[SIMULATION] Executing: {cmd}")

def main():
    user = input("Enter username: ")
    if authenticate(user):
        cmd = input("Enter command: ")
        run_command(cmd)
    else:
        print("Access denied")

def run():
    main()

if __name__ == "__main__":
    start_tracing()
    run()
    trace = stop_tracing()
    
    print("\nExecution Trace:")
    for e in trace:
        print(e)

    print("\nTainted variables:", TAINTED_VARS)
