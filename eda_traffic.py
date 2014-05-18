# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib.patches import Polygon
from matplotlib.path import Path
import os, sys
%pylab inline

# <codecell>

del df

path = 'data/'
dirs = os.listdir(path)
dirs = sorted(dirs)

for file in dirs:
    try:
        tempdf = pd.read_csv(path+file)
        df = pd.merge(df,tempdf,how='outer')
    except:
        df = pd.read_csv(path+file)

df.describe()

# <codecell>

df.columns = ['region','id','west','east','south','north','description','currentspeed','lastupdated']
df = df.drop(['description'],1)
df.head()

# <codecell>

def date2int(x):
    m = x[5:7]
    d = x[8:10]
    if m == '05':
        return int(d)-17
    elif m == '06':
        return int(d)+14
    elif m == '07':
        return int(d)+34

df["date"] = [t[0:4] + t[5:7] + t[8:10] for t in df["lastupdated"]]
df["time"] = [t[11:13] + t[14:16] for t in df["lastupdated"]]
df["day"] = [date2int(t) for t in df["lastupdated"]] # day 0 is May 17, 2014
df["dayofwk"] = [(t+6)%7 for t in df["day"]] # 0 indexed Sunday
df.head()

# <codecell>

plt.figure(figsize=(10,15))

im = plt.imread('chicago.png')
implot = plt.imshow(im)

x = (df['west'] - df['west'].min())*477/(df['east'].max() - df['west'].min())
y = 798-(df['north'] - df['south'].min())*798/(df['north'].max() - df['south'].min())
s = df['currentspeed'] / df['currentspeed'].max()
plt.scatter(x,y,c=s,linewidth=0,s=1000,alpha=0.1)

#x0 = (df.ix[0]['west'] - df['west'].min())*477/(df['east'].max() - df['west'].min())
#y0 = 798-(df.ix[0]['north'] - df['south'].min())*798/(df['north'].max() - df['south'].min())
#plt.scatter(x0,y0,c='r',s=2000)
#x0 = (df.ix[0]['east'] - df['west'].min())*477/(df['east'].max() - df['west'].min())
#y0 = 798-(df.ix[0]['south'] - df['south'].min())*798/(df['north'].max() - df['south'].min())
#plt.scatter(x0,y0,c='r',s=2000)
plt.xlim(0,477)
plt.ylim(798,0)
plt.xticks([])
plt.yticks([])
#plt.plot([df['west'],df['west'],df['east'],df['east'],df['west']],[df['south'],df['north'],df['north'],df['south'],df['south']],linewidth=20,alpha=0.2)

# <codecell>

plt.figure(figsize=(15,15))

patches = []
verts = [(df['west'],df['south']),
    (df['west'],df['north']),
    (df['east'],df['north']),
    (df['east'],df['south']),
    (df['west'],df['south'])]

codes = [Path.MOVETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.CLOSEPOLY]

path = Path(verts, codes)

patch = patches.PathPatch(path, facecolor='orange', lw=2)
ax.add_patch(patch)
#ax.set_xlim(-2,2)
#ax.set_ylim(-2,2)
plt.show()
#plt.scatter(df['west'],df['north'],c=df['currentspeed']/df['currentspeed'].max(),linewidth=0,s=200,alpha=0.2)

# <codecell>


