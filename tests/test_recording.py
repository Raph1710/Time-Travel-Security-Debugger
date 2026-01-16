from debugger.recorder.tracer import start_tracing, stop_tracing

def add(a, b):
    return a + b

# def add(a, b):
#     result = a + b
#     result *= 2
#     return result


def main():
    start_tracing()
    x = add(2, 3)
    trace = stop_tracing()
    return trace

if __name__ == "__main__":
    trace = main()
    print("\nRecorded Events:")
    for e in trace:
        print(e)
