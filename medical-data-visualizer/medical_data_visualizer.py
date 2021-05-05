import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = (df.weight / (df.height / 100) ** 2)

# Normalize data
df['overweight'] = np.where((df.overweight > 25), 1, df.overweight)
df['overweight'] = np.where((df.overweight != 1), 0, df.overweight)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

# gluc
df['gluc'] = np.where((df.gluc == 1), 0, df.gluc)
df['gluc'] = np.where((df.gluc > 1), 1, df.gluc)

# cholesterol
df['cholesterol'] = np.where((df.cholesterol == 1), 0, df.cholesterol)

df['cholesterol'] = np.where((df.cholesterol > 1), 1, df.cholesterol)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
   
    df_cat['total'] = 1   # 1 per row
    
    df_cat = df_cat.groupby(['variable', 'cardio', 'value'], as_index = False).count()

    # Draw the catplot with 'sns.catplot()'
    f = sns.catplot( x = 'variable', y = 'total', col = 'cardio', hue = 'value', kind = 'bar', data = df_cat)
    fig = f.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    # diastolic pressure msut be is lower than systolic
    df_heat = df[
      (df['ap_lo'] <= df['ap_hi'])
      & (df['height'] >= df['height'].quantile(0.025))
      & (df['height'] <= df['height'].quantile(0.975))
      & (df['weight'] >= df['weight'].quantile(0.025))
      & (df['weight'] <= df['weight'].quantile(0.975))
      ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(250, 15, s = 75, l = 40,
                                  n = 9, center = "dark")

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr,
      linewidths=.5,
      annot=True,
      fmt='.1f',
      mask=mask,
      square=True,
      center=0,
      vmin=-0.1,
      vmax=0.25,
      cbar_kws={'shrink':.45, 'format':'%.2f'})


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
