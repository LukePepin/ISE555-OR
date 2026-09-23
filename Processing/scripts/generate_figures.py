"""Reproducible instructional figures; no source-image editing."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyBboxPatch
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'figures'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.size': 11, 'savefig.bbox': 'tight'})

def save(fig, name):
    for ext in ['pdf', 'png']:
        fig.savefig(OUT / f'{name}.{ext}', dpi=180)
    plt.close(fig)

fig, ax = plt.subplots(figsize=(6.7,4.6))
ax.add_patch(Polygon([(0,0),(1,0),(0,1)], color='#cfebea', label='Feasible region'))
x=np.linspace(0,1.2,300)
ax.plot(x,1-x,color='#117c83',lw=2,label=r'$x_1+x_2=1$')
for value in [0.5,1,1.5,2]:
    ax.plot(x,value-2*x,'--',color='#b47942',alpha=.65)
ax.annotate('Larger objective values',xy=(.68,.83),xytext=(.24,.43),
            arrowprops={'arrowstyle':'->','color':'#b47942'},color='#925b26')
for point,label,offset in [((0,0),'C = (0, 0)',(10,8)),((0,1),'B = (0, 1)',(10,5)),((1,0),'A = (1, 0)\noptimum: f = 2',(-36,18))]:
    ax.plot(*point,'o',color='#15324b');ax.annotate(label,point,xytext=offset,textcoords='offset points')
ax.set(xlim=(-.07,1.2),ylim=(-.07,1.2),xlabel=r'$x_1$',ylabel=r'$x_2$',title=r'Maximize $2x_1+x_2$ over the shaded triangle')
ax.set_aspect('equal');ax.grid(alpha=.18);ax.legend(loc='upper right',fontsize=9)
save(fig,'2026-09-14-feasible-region')

fig,ax=plt.subplots(figsize=(8.2,5.2));ax.set(xlim=(0,10),ylim=(-.1,6));ax.axis('off')
ax.text(5,5.65,'Fractional workload allocation: model structure',ha='center',weight='bold',fontsize=14)
for y,label in [(4.5,'P: information requests'),(3,'Q: new policies'),(1.5,'R: claims')]:
    ax.add_patch(FancyBboxPatch((.1,y-.3),2.8,.6,boxstyle='round,pad=.1',facecolor='#cfebea',edgecolor='#117c83'))
    ax.text(1.5,y,label,ha='center',fontsize=10)
    for wy in [4.7,3.8,2.9,2,1.1]:
        ax.annotate('',xy=(5.4,wy),xytext=(3,y),arrowprops={'arrowstyle':'->','color':'#aab9c5','lw':.7},zorder=0)
for i,y in enumerate([4.7,3.8,2.9,2,1.1],1):
    ax.add_patch(FancyBboxPatch((5.45,y-.25),4,.5,boxstyle='round,pad=.06',facecolor='#eef2f6',edgecolor='#486378'))
    ax.text(7.45,y,rf'Worker {i}: $L_{i}=a_{i}P_{i}+b_{i}Q_{i}+c_{i}R_{i}\leq t$',ha='center',fontsize=10)
ax.text(1.5,.35,r'Each workload is fully assigned:'+'\n'+r'$\sum_i P_i=\sum_i Q_i=\sum_i R_i=1$',ha='center',fontsize=10)
ax.text(7.45,.35,r'Minimize $t=\max_i L_i$ at optimum',ha='center',fontsize=11,weight='bold')
save(fig,'2026-09-16-workload-model')
print('Generated two figures, PDF and PNG formats.')
