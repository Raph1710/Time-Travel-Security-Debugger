TAINT_SOURCES = set()
TAINTED_VARS = set()

def mark_taint(var_name):
    TAINTED_VARS.add(var_name)

def is_tainted(var_name):
    return var_name in TAINTED_VARS
