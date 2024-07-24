from matplotlib import pyplot as plt
import warnings
import numpy as np
warnings.simplefilter('ignore')

sensorA = [16,24,24,9,23,26,26,23,25,14]
sensorB = [2,19,25,10,11,24,17,7,24,17]
sensorC = [15,11,24,21,6,2,18,27,1,16]
sensorD = [9,19,29,11,13,20,7,13,20,14]

# Mean and Standard Deviation
mean,std,max2,min2 = [],[],[],[]
samples = np.arange(1,11)
#ERROR BARS
for i in range(10):
    data = [sensorA[i],sensorB[i],sensorC[i]]
    mean.append(np.mean(data))
    std.append(np.std(data))
    max2.append(max(data))
    min2.append(min(data))

plt.errorbar(samples,mean,std,fmt="o")
#PLOT - ERROR BARS & FILL
plt.fill_between(samples,max2,min2,alpha=0.5,linewidth=0, color='#8ecae6')
plt.ylabel('Relative Humidity')
plt.xlabel('Hour')
plt.title('Humidity')
plt.show()