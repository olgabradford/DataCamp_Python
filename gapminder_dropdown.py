# -*- coding: utf-8 -*-

#https://github.com/slehkyi/notebooks-for-articles/blob/master/co2_world.py

#doesnt work! check again with above code

# Import the necessary modules
import pandas as pd
import numpy as np
from bokeh.io import curdoc
from bokeh.plotting import figure
#import HooverTool
from bokeh.models import HoverTool, ColumnDataSource, CategoricalColorMapper, Slider
from bokeh.palettes import Spectral6
from bokeh.layouts import widgetbox, row

from bokeh.models import Select


#read final_df to final_dfframe and preprocessing

gapminder = pd.read_csv('gapminder_tidy.csv')
upd_new_df = gapminder.sort_values(by=['Country', 'Year'])
upd_new_df['Year'] = upd_new_df['Year'].astype('int64')
final_df = upd_new_df.dropna()
# Creating visualization app with Bokeh.io
regions_list = final_df.region.unique().tolist()


# Make a color mapper: color_mapper
color_mapper = CategoricalColorMapper(factors=regions_list, palette=Spectral6)
# Make the Columnfinal_dfSource: source
source = ColumnDataSource(data={
    'x'       : final_df.fertility[final_df['Year']==1970],
    'y'       : final_df.life[final_df['Year']==1970],
    'Country'      : final_df.Country[final_df['Year']==1970],
    'pop'      : final_df.population[final_df['Year']==1970],
    'region'      : final_df.region[final_df['Year']==1970],
})



# Save the minimum and maximum values of the fertility column: xmin, xmax
xmin, xmax = min(final_df.fertility), max(final_df.fertility)

# Save the minimum and maximum values of the life expectancy column: ymin, ymax
ymin, ymax = min(final_df.life), max(final_df.life)


# Create the figure: plot_slider
plot = figure(title='gapminder final_df for year 1970', plot_height=600, plot_width=1000,
               x_range=(xmin, xmax), y_range=(ymin, ymax))

# Add the color mapper to the circle glyph
plot.circle(x='x', y='y', fill_alpha=0.8, source=source,
            color=dict(field='region', transform=color_mapper), legend='region')

# Set the legend.location attribute of the plot to 'top_right'
plot.legend.location = 'top_right'

# Set the x-axis label
plot.xaxis.axis_label = 'feritility' 
# Set the y-axis label
plot.yaxis.axis_label = 'life expectancy'

#add hoover tool to plot
hover = HoverTool(tooltips=[('Country', '@Country')])
plot.add_tools(hover)



# Make a slider object: slider
slider = Slider(start=1970, end=2010, step=1, value=1970, title='Year')
# Define the callback function: update_plot

def update_plot(attr, old, new):
    # set the `yr` name to `slider.value` and `source.final_df = new_final_df`
    yr = slider.value
    x=x_select.value
    y=y_select.value
    #label axes of plot
    plot.xaxis.axis_label = x
    plot.yaxis.axis_label = y
    #set new final_df
    new_data = {
            'x'       : final_df.fertility[final_df['Year']==yr],
            'y'       : final_df.life[final_df['Year']==yr],
            'Country'      : final_df.Country[final_df['Year']==yr],
            'pop'      : final_df.population[final_df['Year']==yr],
            'region'      : final_df.region[final_df['Year']==yr],
    }
    #assign new_final_df to source.final_df
    source.data = new_data
        # Set the range of all axes
    plot.x_range.start = min(final_df[x])
    plot.x_range.end = max(final_df[x])
    plot.y_range.start = min(final_df[y])
    plot.y_range.end = max(final_df[y])

        # Add title to figure: plot.title.text
    plot.title.text = 'Gapminder final_df for %d' % yr


# Attach the callback to the 'value' property of slider
slider.on_change('value', update_plot)



# Create a dropdown Select widget for the x data: x_select
x_select = Select(
    options=['fertility', 'life', 'child_mortality', 'gdp'],
    value='fertility',
    title='x-axis data'
)

# Attach the update_plot callback to the
# 'value' property of x_select
x_select.on_change('value', update_plot)

# Create a dropdown Select widget for the y data: y_select
y_select = Select(
    options=['fertility', 'life', 'child_mortality', 'gdp'],
    value='life',
    title='y-axis data'
)

# Attach the update_plot callback to
# the 'value' property of y_select
y_select.on_change('value', update_plot)

# Create layout and add to current document
layout = row(widgetbox(slider, x_select, y_select), plot)
curdoc().add_root(layout)
#

