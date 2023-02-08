# test_cython
Testing Cython speed.

During my first month of learning programming, I heard Python was a slow language. How could be that? I click the run button and immediately receive the output, Java on the other side usually takes several seconds to run, so Python is faster than Java, isn't it? In summary, I was a layman.

Some months later I found out why I was wrong. Now I can see clearly, especially after applying numerical methods that python is slow indeed (at least until now). So during the course "Economia Computacional 2" at "UFRGS" I learned about Cython, another language based on python that enables C extensions for the Python language to run Python code faster.

So this repository is made to test the speed of Cython compared to standard Python.  Initially, this only applies the test on the Newton–Raphson method, but I intend to expand the testing to discover the weaknesses and strengths of Cython.

