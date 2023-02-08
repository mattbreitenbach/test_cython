import cython

def funcao(x: cython.double):
    result: cython.double
    result = (2*(x**3) + 3*(x**2) - 2)
    return result

def de_funcao(x: cython.double):
    result: cython.double
    result = (6*(x**2) + 6*(x))
    return result

def metodo_newton(x: cython.double, e: cython.double=0.001, iterations: cython.int=1):
    f_x: cython.double = funcao(x)
    df_x: cython.double = de_funcao(x)
    result: cython.double = x - (f_x/df_x)
    
    if iterations <= 1:
        return metodo_newton(x=result, e=e, iterations=iterations+1)
    elif abs(x-result) < e:
        return [result, e, iterations]
    else:
        return metodo_newton(x=result, e=e, iterations=iterations+1)
   
