import sys
import threading
import time
from debugger.recorder.state import StateSnapshot
from debugger.security.taint import TAINTED_VARS

events = []
last_locals = {}

def trace_calls(frame, event, arg):
    global last_locals

    # DEBUG CONFIRMATION (temp)
    # print("TRACE EVENT:", event, frame.f_code.co_name)

    if event == "line":
        curr_locals = frame.f_locals.copy()
        prev_locals = last_locals.get(id(frame), {})

        # taint propagation
        if any(var in TAINTED_VARS for var in prev_locals):
            for var in curr_locals:
                TAINTED_VARS.add(var)

        last_locals[id(frame)] = curr_locals


    if event in ("call", "line", "return"):
        snapshot = StateSnapshot(frame)
        events.append({
            "type": event,
            "function": snapshot.function,
            "line": snapshot.line_no,
            "locals": snapshot.locals,
            "timestamp": snapshot.timestamp
        })

    return trace_calls


def start_tracing():
    events.clear()
    last_locals.clear()
    sys.settrace(trace_calls)
    threading.settrace(trace_calls)


def stop_tracing():
    sys.settrace(None)
    threading.settrace(None)
    return events
