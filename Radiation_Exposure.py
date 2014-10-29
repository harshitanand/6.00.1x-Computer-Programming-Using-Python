def radiationExposure(start, stop, step):
    tot_radiation = 0.0
    
    while start<=stop:
        tot_radiation = tot_radiation + (f(start)*step)
        start = start+step

    return tot_radiation
