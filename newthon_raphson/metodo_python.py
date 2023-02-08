def funcao(x):
    return (2*(x**3) + 3*(x**2) - 2)

def de_funcao(x):
    return (6*(x**2) + 6*(x))

def metodo_newton(x, e=0.001, iterations=1):
    f_x = funcao(x)
    df_x = de_funcao(x)
    result = x - (f_x/df_x)
    
    if iterations <= 1:
        return metodo_newton(x=result, e=e, iterations=iterations+1)
    elif abs(x-result) < e:
        return [result, e, iterations]
    else:
        return metodo_newton(x=result, e=e, iterations=iterations+1)
