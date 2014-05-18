# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
import numpy as np
import matplotlib as plt
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

df["lastupdated"]

# <codecell>


