from matplotlib import pyplot as plt
import warnings
import numpy as np
warnings.simplefilter('ignore')

plt.style.use('ggplot')
h=[57.0, 56.0, 57.0, 56.0, 55.0, 55.0, 54.0, 54.0, 54.0, 53.0, 53.0, 54.0, 53.0, 53.0, 52.0, 52.0, 51.0, 51.0, 51.0]
low=[53.0, 54.0, 54.0, 52.0, 54.0, 51.0, 53.0, 53.0, 50.0, 51.0, 52.0, 53.0, 49.0, 50.0, 50.0, 49.0, 50.0, 47.0, 50.0]
high= [58.0, 60.0, 61.0, 57.0, 56.0, 58.0, 58.0, 57.0, 56.0, 55.0, 54.0, 57.0, 54.0, 56.0, 53.0, 56.0, 53.0, 55.0, 52.0]

#Step 1
samples = []
for i in range(len(h)):
    samples.append(i)

fig = plt.figure(figsize = (8,4))
plt.subplot(1,2,1)
plt.plot(samples,h,color='#6be89d')
plt.plot(samples,low,color='#2e66ff')
plt.plot(samples,high,color='#f59089')


plt.fill_between(samples,high,low,alpha=0.5,linewidth=0, color='#8ecae6')
# Step 3 - Analyze data
plt.subplot(1,2,2)
mean = []
std = []
for i in range(len(h)):
    data = [h[i],low[i],high[i]]
    mean.append(np.mean(data))
    std.append(np.std(data))
plt.fill_between(samples,high,low,alpha=.5,linewidth=0,color="#8ecae6")
plt.errorbar(samples,mean,std,fmt="o")
plt.show()

#m,b = np.polyfit(x,h,1)
#plt.ylabel('Relative Humidity')
#plt.xlabel('Temperature')
#plt.scatter(x,h)
#plt.plot(x,m*x+b)
