import math

PI = 3.14159

def power_grid_forecast(consumption_data):
    f = [val-(10 * math.sin((2*PI*i)/10)) for i, val in enumerate(consumption_data, 1)]
    X = [i for i in range(1, len(consumption_data)+1)]
    Xx = sum([i*i for i in X])
    Xy = sum([x*y for x,y in zip(X,f)])
    xsum = sum(X)
    ysum = sum(f)
    m = (len(X)* Xy - xsum * ysum) / (len(X)* Xx - (xsum)**2)
    b = (ysum - m * xsum)/ len(X)

    ba = m * 15 + b
    pred = (10 * math.sin((2*PI*15)/10)) + ba
    return math.ceil(1.05 * round(pred))

