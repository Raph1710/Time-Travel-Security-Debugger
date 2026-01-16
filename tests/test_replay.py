from debugger.recorder.tracer import start_tracing, stop_tracing
from debugger.replay.replayer import Replayer

def vulnerable():
    x = 1
    x = x + 1
    x = x * 10
    return x

def main():
    start_tracing()
    vulnerable()
    trace = stop_tracing()

    replayer = Replayer(trace)

    print("\nStepping forward:")
    while replayer.step_forward():
        print(replayer.step_forward())

    print("\nStepping backward:")
    while replayer.step_backward():
        print(replayer.step_backward())

if __name__ == "__main__":
    main()