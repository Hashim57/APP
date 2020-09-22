from timeit import Timer
import app
import timeit
import unittest




# t1 = Timer("""app()""", """from __main__ import app""") 
  

def test_app():
    """Test function"""
    L = []
    for i in range(100):
        L.append(i)

if __name__ == '__main__':
    print(timeit.timeit("test_app()", setup="from __main__ import test_app"))
    unittest.main()

# if __name__=='__main__':
#     unittest.main()


