# recorder/state.py
import copy
import time

def safe_copy_locals(locals_dict):
    safe_locals = {}
    for key, value in locals_dict.items():
        try:
            safe_locals[key] = copy.deepcopy(value)
        except Exception:
            safe_locals[key] = repr(value)
    return safe_locals


class StateSnapshot:
    def __init__(self, frame):
        self.function = frame.f_code.co_name
        self.line_no = frame.f_lineno
        self.locals = safe_copy_locals(dict(frame.f_locals))
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())