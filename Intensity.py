

from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from lmfit import minimize,Parameters,Parameter,report_fit,conf_interval,printfuncs
from math import *
from scipy.stats import norm,lognorm
from sklearn.neighbors import KernelDensity
from sklearn.preprocessing import normalize
from scipy import stats


Run7_3_ImageNumber=np.linspace(0,247,247)

Run5_3_ImageNumber=np.linspace(0,219,219)



Run5_3_TimeArray='/home/okoye/Documents/python/Colliods/BCAT1/RUN5-3/TimeArray.dat' 


Run7_3_TimeArray='/home/okoye/Documents/python/Colliods/Run7-3NSP/Run7-3_CellProflier/timearray.dat'



c='/home/okoye/Documents/python/Colliods/BCAT1/New1/ImageGlobalOstu2classes0.5Entropy.csv'

 

j= '/home/okoye/Documents/python/Colliods/BCAT1/New2/Global/ImageBkgrd0.6.csv' #Best





def time_Sec(file):
   time=pd.read_table(file)
   time=np.array(time*3600,float)
   return time[:,0]#converts from 1D array to 2D array
   



def time_hr(file):
    time=pd.read_table(file)
    time=np.array(time,float)
    return time[:,0]




def columns(file):
    blob_Data=pd.read_csv(file)
    blob_Data=blob_Data.fillna(0)
    Tot_Intensity_Corrected_Image=blob_Data[[57]] #OrigGray=Corrected Image
    Tot_Intensity_Original_Image=blob_Data[[58]] #Runxxxxxx=Original Image
    return Tot_Intensity_Corrected_Image,Tot_Intensity_Original_Image
    
    
def Tot_Intensity_Corrected_Image(file): #Intensity of Corrected Image
    a=columns(file)
    Tot_Intensity_Corrected_Image=a[0]
    Tot_Intensity_Corrected_Image=np.array(Tot_Intensity_Corrected_Image,float)
    return Tot_Intensity_Corrected_Image
    
    
def Tot_Intensity_Original_Image(file):    #Intensity of Original Image     
    a=columns(file)
    Tot_Intensity_Original_Image=a[1]
    Tot_Intensity_Original_Image=np.array(Tot_Intensity_Original_Image,float)
    return Tot_Intensity_Original_Image





ax=plt.gcf().subplots_adjust(bottom=0.20,left=0.19)

ax=plt.gca()




ax.plot(Run7_3_ImageNumber, (Tot_Intensity_Original_Image(c)),'g-',label='Run7-3' ) #Threshold of 0.5


ax.plot(Run5_3_ImageNumber, (Tot_Intensity_Original_Image(j)),'r-',label='Run5-3' ) #Threshold of 0.6



ax.set_xscale('linear',subsx=[2, 3, 4, 5, 6, 7,8,9])
ax.set_yscale('linear',subsy=[2, 3, 4, 5, 6, 7,8,9])
plt.xlabel('Image Number ',fontsize=18)
plt.ylabel('Total Intensity',fontsize=18)
plt.xlim(-10,260)
ax.minorticks_on()
ax.tick_params('both',length=10,width=1,which='major',direction='out')
ax.tick_params('both',length=5,width=1,which='minor',direction='out')
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

ticklines = ax.get_xticklines()
ticklines.extend( ax.get_yticklines() )
ticklabels = ax.get_xticklabels()
ticklabels.extend( ax.get_yticklabels() )

for label in ticklabels:
      label.set_color('black')
      label.set_fontsize('15')
plt.suptitle('Intensity',fontsize=18)
plt.grid('on')
plt.legend(loc='best')

plt.show()





ax=plt.gcf().subplots_adjust(bottom=0.20,left=0.19)

ax=plt.gca()




ax.plot(Run7_3_ImageNumber, (Tot_Intensity_Corrected_Image(c)),'g-',label='Run7-3' ) #Threshold of 0.5


ax.plot(Run5_3_ImageNumber, (Tot_Intensity_Corrected_Image(j)),'r-',label='Run5-3' ) #Threshold of 0.6



ax.set_xscale('linear',subsx=[2, 3, 4, 5, 6, 7,8,9])
ax.set_yscale('linear',subsy=[2, 3, 4, 5, 6, 7,8,9])
plt.xlabel('Image Number ',fontsize=18)
plt.ylabel('Total Intensity',fontsize=18)
plt.xlim(-10,260)
ax.minorticks_on()
ax.tick_params('both',length=10,width=1,which='major',direction='out')
ax.tick_params('both',length=5,width=1,which='minor',direction='out')
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

ticklines = ax.get_xticklines()
ticklines.extend( ax.get_yticklines() )
ticklabels = ax.get_xticklabels()
ticklabels.extend( ax.get_yticklabels() )

for label in ticklabels:
      label.set_color('black')
      label.set_fontsize('15')
plt.suptitle('Corrected Intensity',fontsize=18)
plt.grid('on')
plt.legend(loc='best')
#plt.savefig(path0+'RBlobFitBPPThres03')#BPP=BlobPerPixel
plt.show()


















