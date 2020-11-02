import numpy as np

def rolling_window(a, window, step_size):
    shape = a.shape[:-1] + (a.shape[-1] - window + 1 - step_size + 1, window)
    strides = a.strides + (a.strides[-1] * step_size,)
    print(strides)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)

if __name__ == "__main__":
    xar = np.random.randint(5,size=(6,6))
    print(xar)
    wind = rolling_window(xar,3,1)
    print(wind)