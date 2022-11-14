# %% [markdown]
# # **Data Visualization with SeaBorn library**

# %% [markdown]
# ## **1. Importing Liberaries**

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# %% [markdown]
# ## **2. Import Iris dataset**

# %%
iris = sns.load_dataset('iris')
iris.head()

# %% [markdown]
# ## **3. plotting line plot**

# %%
sns.lineplot(x='sepal_length', y='sepal_width', data=iris, hue='species', style='species', markers=True, dashes=False, 
                palette='Set1', legend='full')
plt.show()

# %% [markdown]
# ## **4.boxplot**

# %%
sns.boxplot(x='species', y='sepal_length', data=iris, palette='Set1', hue='species', linewidth=2.5, fliersize=5)
sns.color_palette('Set1', 3)
plt.show()
plt.savefig('boxplot.png')

# %% [markdown]
# ## **5. Scatter plot**

# %%
sns.scatterplot(x='sepal_length', y='sepal_width', data=iris, hue='species', style='species', s=100, alpha=1, palette='Set1',
                 edgecolor='black', linewidth=1, markers=['o', 's', 'D'])
plt.savefig('scatterplot.png', dpi=300)
plt.show()

# %% [markdown]
# ## **7. Pairplot**

# %%
sns.pairplot(iris, hue='species', palette='Set1', 
             markers=['o', 's', 'D'], diag_kind='hist', diag_kws={'edgecolor':'black', 'linewidth':1})

# %% [markdown]
# ## **8. Violin Plot**

# %%
sns.violinplot(x='species', y='sepal_length', data=iris, inner='quartile', palette='Set1', scale='count',   
               scale_hue=False, bw=.2, cut=1, linewidth=1, edgecolor='black', gridsize=100)

# %% [markdown]
# ## **9. Heatmap**

# %%
sns.heatmap(iris.corr(), annot=True, cmap='RdYlGn', linewidths=.5, fmt='.2f', annot_kws={'size':15}, cbar=False)
plt.show()

# %% [markdown]
# ## **10. Histplot**

# %%
sns.histplot(iris['sepal_length'], kde=True, edgecolor='black', linewidth=1, color='red', alpha=1, bins=20, stat='density', 
                cumulative=False, common_norm=False, common_bins=False, multiple='layer', shrink=.8, line_kws={'linewidth':2},)


