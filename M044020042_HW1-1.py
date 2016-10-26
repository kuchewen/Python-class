import numpy as np
import matplotlib.pyplot as plt

#Q1
k = 9000
premium_call = 179
premium_put = 183
interval = 500
ST = np.arange(k - interval,k + interval)
payoff_longcall = np.maximum(ST-k,0)-premium_call
payoff_shortcall = -payoff_longcall
payoff_longput = np.maximum(k-ST,0) - premium_put
payoff_shortput = -payoff_longput

#Long & Short call
plt.figure(1)
plt.title('Long & Short Call')
plt.axvline(x = k + premium_call,color='red')
plt.axhline(y=0, color='k')
plt.plot(ST,payoff_longcall)
plt.plot(ST,payoff_shortcall)

#Long & Short put
plt.figure(2)
plt.title('Long & Short Put')
plt.axvline(x = k - premium_put,color='red')
plt.axhline(y=0, color='k')
plt.plot(ST,payoff_longput)
plt.plot(ST,payoff_shortput)

plt.show


