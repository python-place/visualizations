import bokeh
from bokeh.plotting import figure, show
from bokeh.sampledata.iris import flowers

# Create a ColumnDataSource from the Iris dataset
source = bokeh.plotting.ColumnDataSource(flowers)

# Create a figure with a title and x/y axis labels
p = figure(title="Iris Dataset", x_axis_label="Petal Length",y_axis_label="Petal Width")

# Add glyphs for each type of glyph to the first five rows of the iris dataset
p.circle(x=flowers["sepal_length"][:5], y=flowers["sepal_width"][:5], size=10, color="blue")

show(p)
p.square(x=flowers["sepal_length"][:5], y=flowers["sepal_width"][:5], size=10, color="red")