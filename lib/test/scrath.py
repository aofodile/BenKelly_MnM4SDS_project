import numpy as np

xar = np.array(np.zeros([6,9],dtype=int))

def findcp(xar):
    hx = xar.shape[0] // 2
    wx = xar.shape[1] // 2
    xar[hx,wx] = 1
    print(xar)











        

if __name__ == "__main__":
    findcp(xar)
'''
    hc = xar.shape[0]/2
    print(hc)
    if hc % 2 != 0:
        if len(xar[hc,:]) %2 != 0:
            mid = (xar.shape[1] % 2) + 1
            xar[hc,mid] = 1
        else:
            mid = [(xar.shape[1] % 2) + 1,(xar.shape[1] % 2) - 1]
            for i in mid:
                xar[hc,i] = 1
    print(xar)
'''