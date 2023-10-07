import numpy as np
import matplotlib.pyplot as plt


fig,ax = plt.subplots(1,2)
plt.subplots_adjust(left=0.083,bottom=0.367,right=0.9,top=0.675)


ax[0].axhspan(ymin = 1, ymax = 3, color = 'orangered', alpha = 0.9, label = 'Strength and Courage')
ax[0].axhspan(ymin = -1, ymax = 1, color = 'white', label = 'Peace and Truth')
ax[0].axhspan(ymin = -3, ymax = -1, color = 'darkgreen', label = 'Fertility, Growth and Auspiciousness')
ax[0].axhline(y = -1, color = 'g', alpha = 0.2)
ax[0].axhline(y = 1, color = 'orange', alpha = 0.2)
ax[0].set_xlim([-4.5,4.5])
ax[0].set_ylim([-3,3])
ax[0].set_frame_on(False)
ax[0].tick_params(left = False , labelleft = False ,labelbottom = False, bottom = False)
ax[0].set_aspect(1)


r = 0.8
the = np.linspace(0,360,10000)
the = np.radians(the)
x = r*np.cos(the)
y = r*np.sin(the)
ax[0].plot(x,y,color = 'navy', label='Duty')
phi = np.arange(0,360,15)
for i in phi :	
	i = np.radians(i)
	ax[0].plot([r*np.cos(i),0],[r*np.sin(i),0],color = 'navy')


fig.legend(bbox_to_anchor = (0.92,0.62), edgecolor = 'k', fancybox = True, fontsize = 'small', facecolor = 'gainsboro')
plt.figtext(0.51, 0.17, '[Credit : Das.R]', fontfamily = 'monospace', fontsize = 'medium')
fig.delaxes(ax[1])
plt.show()
