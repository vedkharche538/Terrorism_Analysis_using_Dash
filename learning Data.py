# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 13:24:17 2020

@author: Vedhas
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('global_terror.csv')
print(df)
sns.heatmap(df)