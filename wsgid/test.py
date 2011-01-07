import os

def simple_fork(function_to_fork):
    
    pid = os.fork()
    if pid:
        return pid
    # Now we pray to have an infinite loop
    function_to_fork()