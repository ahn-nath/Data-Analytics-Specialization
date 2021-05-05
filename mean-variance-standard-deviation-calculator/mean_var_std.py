import numpy as np

def calculate(lista):
    # arr must have 9 digits
    if len(lista) != 9:
     raise ValueError("List must contain nine numbers.")

    # convert to numpy arr
    arr = np.array(lista).reshape(3, 3)
    
    # var preparations
    calculations = dict()
    args = [0, 1, None]

    # lists
    mean = list()
    var = list()
    std = list()
    max_val = list() 
    min_val = list()
    sum_val = list()

    # get values
    for axis in args:
        var.append(np.var(arr, axis = axis).tolist())
        mean.append(np.mean(arr, axis = axis).tolist())
        std.append(np.std(arr, axis = axis).tolist())
        max_val.append(np.max(arr, axis = axis).tolist())
        min_val.append(np.min(arr, axis = axis).tolist())
        sum_val.append(np.sum(arr, axis = axis).tolist()) 

        
    # out   
    calculations["mean"] = mean
    calculations["variance"] = var
    calculations["standard deviation"] = std
    calculations["max"] = max_val
    calculations["min"] = min_val
    calculations["sum"] = sum_val


    return calculations

