#Q2
import numpy as np
import matplotlib.pyplot as plt
premium_call = 100
premium_put = 183

k = 9000
k1 = 8800
k2 = 9100
interval = 500
ST = np.arange(k - interval,k + interval)
longcall = np.maximum(ST-k1,0) - premium_call
longput = np.maximum(k2-ST,0) - premium_put

plt.axhline(y=0, color='k')
plt.plot(ST,longcall)
plt.plot(ST,longput)
plt.plot(ST,longcall+longput)
plt.show
