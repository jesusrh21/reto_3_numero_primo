import unittest
import reto_3_es_numero_primo as ep

class Test_numero_primo(unittest.TestCase):
    def test_es_primo(self):
        self.assertEquals(ep.es_primo(2,3,4,8,9,17),True,True,False,False,False,True)
        
    
if __name__ == '__main__':
    unittest.main()