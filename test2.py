from graphics import *

# Create a larger window
win = GraphWin("Bar Graph with Full Axis Labels", 900, 600)
win.setBackground("white")

# Add more padding on the left side
# Now x starts from -1 (extra space for "Values")
# y from -2 to 12 leaves room for labels and title
win.setCoords(-2, -2, 12, 12)
#win.setCoords(x_min, y_min, x_max, y_max)

# Data and labels
data = [3, 7, 5, 9, 4]
labels = ["A", "B", "C", "D", "E"]

# Draw Y-axis clearly visible at x=0
y_axis = Line(Point(0, 0), Point(0, 10))
y_axis.setWidth(2)
y_axis.draw(win)

# Draw X-axis across chart
x_axis = Line(Point(0, 0), Point(11, 0))
x_axis.setWidth(2)
x_axis.draw(win)

# Axis labels
x_label = Text(Point(5.5, -1.4), "Categories")
x_label.setSize(12)
x_label.draw(win)

# Moved farther left so "Values" is fully visible
y_label = Text(Point(-0.6, 5), "Values")
y_label.setSize(12)
y_label.setStyle("bold")
y_label.draw(win)

# Title
title = Text(Point(5.5, 11), "Bar Graph Example")
title.setSize(14)
title.setStyle("bold")
title.draw(win)

# Draw bars starting to the right of y-axis
bar_width = 1.5
gap = 0.5
x_start = 0.5  # starts right after y-axis

for i in range(len(data)):
    x1 = x_start + i * (bar_width + gap)
    x2 = x1 + bar_width
    height = data[i]

    # Create and draw bar
    bar = Rectangle(Point(x1, 0), Point(x2, height))
    bar.setFill("skyblue")
    bar.setOutline("black")
    bar.draw(win)

    # Category label
    label = Text(Point((x1 + x2) / 2, -0.5), labels[i])
    label.setSize(10)
    label.draw(win)

    # Value label
    value = Text(Point((x1 + x2) / 2, height + 0.3), str(height))
    value.setSize(10)
    value.draw(win)

# Instruction
msg = Text(Point(5.5, -1.8), "Click anywhere to close")
msg.setSize(10)
msg.draw(win)

win.getMouse()
win.close()
