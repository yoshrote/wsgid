#encoding: utf-8



from wsgid.test import simple_fork
import os
import unittest
import time

class SimpleForkTest(unittest.TestCase):
    
    def test_fork_a_function(self):
        def f_to_fork():
            f = file("/tmp/fork.txt", "wa")
            f.write("111")
            f.flush()
            f.close()
            while True:
                time.sleep(1)
        
        pid = simple_fork(f_to_fork)
        self.assertTrue(pid is not None)
        
        time.sleep(1)
        # If we get here the fork was good
        os.kill(pid, 15) # TERM
        
        f = file("/tmp/fork.txt")
        content = f.read()
        
        self.assertTrue(len(content) == 3)
        self.assertEquals("111", content)
            

