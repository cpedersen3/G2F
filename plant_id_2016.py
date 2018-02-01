plant_id = {}
c = open('Yumou.csv', 'r')
c.readline()
e = {}
for i in c:
	g = i.strip().split(',')
	if len(g) < 3:
		continue
	f = g[2] + '\n'
	f_2 = str(f)
	e[g[1]] = g[2]
	#print e

a = open('exp3_oneday_james_hybridcorns_final.csv', 'r')
a.readline()
d = {}
for x in a:
	y = x.strip().split(',')
	z = y[0].split('-')
	z_2 = str(int(z[2]))
	#z_3 = 'ZL' + z_2
	d[z_2] = y[3:6]
	#print d

r = {}
for akey in e:
	if akey in d:
		vlist = []
		vlist.append(akey)
		vlist.extend(d[akey])
		vlist.append(e[akey])
		vlist.append(float(d[akey][0])/float(d[akey][1]))
		r[e[akey]] = vlist
		#print r


b = open('WIH2_2016.csv', 'r')
b.readline()

k = {}
for i in b:
	l = i.strip().split(',')
	#try:
	m = str(l[0]) + ' ' + str(l[3]) + ' ' + str(l[6]) + '\n'
		#print m
		#1/0
	#except:
		#print l
		#1/0
	if 'WIH2' not in m:
		continue
	if not l[3] in k: k[l[3]] = []
	try: 
		float(l[6])
	except:
		continue
	k[l[3]].append(l[0:8:6])
	#print k

plot_list = []
ratio_list = []
avg_plot_list = []
avg_ratio_list = []
avg_list = []
#ratio_set = set(list(r))
#yield_set = set(list(k))
#print len(ratio_set)
#print ratio_set.difference(yield_set)
#print yield_set.difference(ratio_set)
#1/0
#print len(r), len(k)
for ckey in r:
	if ckey in k:
		ratio_list.append(r[ckey][5])
		#print ckey, ratio_list
		#temp_ratio = []
		#for a in r[ckey]:
			#temp_ratio.append(float(a[1]))
		if len(k[ckey]) < 0.05:
			continue
		#print r[ckey]
		#plot_list.append(str(k[ckey][1]))
		#print plot_list

		temp_plot = []
		for a in k[ckey]:
			temp_plot.append(float(a[1]))
			if 0 in temp_plot:
				continue
		avg_ratio = sum(ratio_list)/float(len(ratio_list))
		avg_ratio_list.append(avg_ratio)
		#print ckey, avg_ratio
		avg_plot = sum(temp_plot)/float(len(temp_plot))
		avg_plot_list.append(avg_plot)
		#print avg_plot_list
		#print ckey, avg_ratio
		#print ckey, avg_plot, avg_ratio

		#avg_list = ckey, avg_test, avg_ratio
		#print avg_list


import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.stats import pearsonr
fig = plt.figure(1)
ax = fig.add_subplot('111')
ax.plot(avg_ratio_list, avg_plot_list, 'o')
ax.set_xlabel('Average Ratio')
ax.set_ylabel('Average Plot Weight')
fig.suptitle('WIH2')
x = avg_ratio_list
y = avg_plot_list
fit = np.polyfit(x,y,1)
fit_fn = np.poly1d(fit)
plt.plot(x,y, 'yo', x, fit_fn(x), '-k')
st = []
pearsonr(x,y)
st = pearsonr(x,y)
plt.text(2.005, 310, r'$R^2 =$' + str(st[0]))
plt.text(2.005, 295, r'$p =$' + str(st[1]))



import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import scipy
plt.figure(2)
mu = avg_ratio_list
sigma = np.std(avg_ratio_list)
num_bins = 20
n, bins, patches = plt.hist(mu, num_bins, normed = 0, facecolor = 'blue', alpha = 0.5)
plt.show()
