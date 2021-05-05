import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates = ['date'],  index_col = 'date')

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot

    # parameters
    y = df['value']
    fig, ax = plt.subplots(1,1, figsize = (12, 6))

    # display
    ax.plot(y, color = 'r')

    # Use mdates to detect hours
    locator = mdates.MonthLocator(bymonth = [1, 7])
    ax.xaxis.set_major_locator(locator)

    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    ax.set_ylim(bottom = 0, top = 180000)
    ax.grid(True) 

    # Save image and return fig 
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
 
    # extract year and month
    df_bar = df.reset_index().drop(['date'], axis = 1)
    df_bar['year'] = df.reset_index().date.dt.year
    df_bar['month'] = df.reset_index().date.dt.month_name()

    # draw bar plot
    # parameters
    # parameters
    g = sns.catplot(x = 'year', y = 'value', data = df_bar, kind = 'bar',
                    hue = 'month', aspect = 1.55, ci = None, 
                    hue_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
                    legend_out = False, palette = 'tab10').set(title = 'Average Page Views') 

    # display
    g.set(xlabel = 'Years')
    g.set(ylabel = 'Average Page Views') 
    g.add_legend(title = 'Months')
    plt.grid() 

    # Save image and return fig 
    fig = g.fig
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots 
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize = (16, 6))
    sns.set_style("whitegrid")

    # --figure (1)
    sns.boxplot(x = 'year', y = 'value', data = df_box, palette = 'tab10', ax = ax[0]).set(
        title = 'Year-wise Box Plot (Trend)',  xlabel='Year',  ylabel='Page Views') 


    # --figure (2)
    sns.boxplot(x = 'month', y = 'value', data = df_box, order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                    palette = 'tab10', ax = ax[1]).set(title = 'Month-wise Box Plot (Seasonality)',  xlabel='Month',  ylabel='Page Views') 


    fig.show()
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
