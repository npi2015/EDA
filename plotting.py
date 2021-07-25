from parsing_data import df, planets_discovered_RV, planets_discovered_ima, planets_discovered_ast, planets_discovered_etv, planets_discovered_obm, planets_discovered_micro, planets_discovered_dkin,planets_discovered_pulsar, planets_discovered_ptv, planets_discovered_PT
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('dark_background')

# Read in the dataset from the csv



fig, axes = plt.subplots(3, 1, sharex=False, sharey=False)
fig.subplots_adjust(hspace=0.05)

ax1 = sns.countplot(x=df["discoverymethod"], ax=axes[0])
ax2 = sns.countplot(x=df["discoverymethod"], ax=axes[1])
ax3 = sns.countplot(x=df["discoverymethod"], ax=axes[2])

ax1.set_ylim(2500, )
ax2.set_ylim(800, 900)
ax3.set_ylim(0,83)

ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)
ax2.spines.bottom.set_visible(False)
ax3.spines.top.set_visible(False)
ax2.set_xticks(ax2.get_xticks())
ax1.set_xlabel(None)
ax1.set_ylabel(None)
ax2.set_xlabel(None)
ax2.set_ylabel(None)
ax3.set_ylabel(None)

ax1.tick_params(labeltop=False)  # don't put tick labels at the top
ax2.xaxis.tick_bottom()
ax2.tick_params(labeltop=False)  # don't put tick labels at the top
ax3.xaxis.tick_bottom()

d = .5
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='w', mec='w', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)
ax2.plot([0,1], [0,0], transform=ax2.transAxes, **kwargs)
ax3.plot([0, 1], [1, 1], transform=ax3.transAxes, **kwargs)


plt.xlabel("Discovery method")
fig.text(0.015, .67, 'Count', ha='center', va='center', rotation='vertical')
ax2.set_ylabel(None)
ax1.set_xticks([])
ax2.set_xticks([])
ax3.set_xticklabels(ax3.get_xticklabels(), rotation = 40, ha = 'right')
plt.tight_layout()
plt.savefig("Bar plot discovery methods")
# Drop all the planets whose existance is disputed
plt.close()

sns.scatterplot(x = planets_discovered_RV['pl_masse'],y =  planets_discovered_RV['pl_rade'], alpha = 0.5)
sns.scatterplot(x = planets_discovered_PT['pl_masse'], y =  planets_discovered_PT['pl_rade'], alpha = 0.5)
sns.scatterplot(x = planets_discovered_ptv['pl_masse'], y =  planets_discovered_ptv['pl_rade'])
plt.xlabel("Mass $M_{\\bigoplus}$")
plt.xlim(0, 5000)
plt.savefig("test.png")
plt.close()
plt.ylim(0,12000)

plot = sns.scatterplot(data = df, y = 'pl_massj', x = 'pl_orbper', hue = 'discoverymethod', style = 'discoverymethod', alpha = 0.5)
plot.set(xscale = 'log')

plt.show()


# TODO: Correlacion entre distintos metodos de deteccion y masa, añadir barras de error
# TODO: Cuantos Jupiter calientes hay?
# TODO: En que metodo de descubrimiento se descubren mas jupiters calientes
# TODO: Cuantos sistemas binarios hay? Hay algun trinario?