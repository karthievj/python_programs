from pythonds import Stack
import unittest

def reverse_a_Str(string):
    
    myStack  = Stack()
    revStr = ''
    
    for ch in string:
        myStack.push(ch)
        
    while not myStack.isEmpty():
        revStr = revStr + myStack.pop()
    return revStr

class reverse(unittest.TestCase):
    def test(self):
        result = reverse_a_Str("apple")
        self.assertEqual('elppa', result)
        result1 = reverse_a_Str("racecar")
        self.assertEqual("racecar",result1)

if __name__== "__main__":
    unittest.main() 



    

   



