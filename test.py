from graphics import *


def draw_bar_graph_from_list(data, labels=None):
    """
    Draws a bar graph using the graphics.py module, optimized for visibility,
    and removing the unsupported setRotation() method.

    :param data: A list of numbers representing bar heights.
    :param labels: An optional list of strings for x-axis labels.
    """

    # --- Configuration ---
    num_bars = len(data)
    if num_bars == 0:
        print("No data to display for the bar graph.")
        return

    max_value = max(data) if data else 1

    # NEW: Larger window dimensions
    win_width = 800  # Increased width
    win_height = 600  # Increased height

    # NEW: Increased padding for labels and more whitespace
    padding_x = 100  # Padding for left/right sides
    # Padding for top/bottom sides (more space for X-axis labels)
    padding_y = 100

    # Calculate the effective drawing area for the bars
    graph_width = win_width - 2 * padding_x
    graph_height = win_height - 2 * padding_y

    # The width allocated to each bar (including space)
    bar_space_width = graph_width / num_bars
    bar_width = bar_space_width * 0.7  # Bar takes 70% of its allocated space

    # --- Setup Window and Coordinates ---
    win = GraphWin("Simple Bar Graph with Axis Labels", win_width, win_height)

    # Set coordinates: Origin (0,0) is bottom-left of the drawing area for the graph itself.
    # Y-axis range is from 0 to max_value (plus a bit extra for text).
    y_coord_max = max_value * 1.2  # 20% extra space at the top for labels and aesthetics
    win.setCoords(-padding_x, -padding_y, win_width -
                  padding_x, y_coord_max + padding_y)

    # --- Draw Axes and Grid Lines ---

    # X-Axis Line
    x_axis = Line(Point(0, 0), Point(graph_width, 0))
    x_axis.setArrow("last")
    x_axis.draw(win)

    # Y-Axis Line
    y_axis = Line(Point(0, 0), Point(0, y_coord_max * 0.95))
    y_axis.setArrow("last")
    y_axis.draw(win)

    # NEW: Add Axis Titles (Y-axis title is now placed to the left without rotation)
    x_axis_title = Text(Point(graph_width / 2, -padding_y / 2), "Categories")
    x_axis_title.setSize(14)
    x_axis_title.setStyle("bold")
    x_axis_title.draw(win)

    # FIX: Place the Y-axis label horizontally far to the left
    y_axis_title = Text(Point(-padding_x * 0.7, y_coord_max / 2), "Values")
    y_axis_title.setSize(14)
    y_axis_title.setStyle("bold")
    # y_axis_title.setRotation(90) <--- REMOVED
    y_axis_title.draw(win)

    # Add Y-Axis Scale Labels
    # Determines tick mark spacing (e.g., 5, 10, 15...)
    tick_interval = max(1, int(max_value / 5))
    for val in range(0, int(max_value * 1.1), tick_interval):
        if val == 0:
            continue
        tick_label = Text(Point(-10, val), str(val))
        tick_label.setSize(9)
        tick_label.draw(win)
        # Add a small tick mark
        tick_line = Line(Point(-3, val), Point(0, val))
        tick_line.draw(win)

    # --- Draw Bars and Labels ---

    for i in range(num_bars):
        height = data[i]

        # Calculate X-coordinates
        x_start_col = i * bar_space_width
        x_bar_left = x_start_col + (bar_space_width - bar_width) / 2
        x_bar_right = x_bar_left + bar_width

        # 1. Draw the Bar (Rectangle)
        p1 = Point(x_bar_left, 0)
        p2 = Point(x_bar_right, height)
        bar = Rectangle(p1, p2)

        # Simple color cycle
        colors = ["skyblue", "lightcoral", "lightgreen", "gold",
                  "orchid", "darkturquoise", "mediumpurple", "salmon"]
        bar.setFill(colors[i % len(colors)])
        bar.setOutline("black")
        bar.draw(win)

        # 2. Draw the Bar Value (on top of the bar)
        value_text = Text(Point(x_start_col + bar_space_width / 2,
                          height + max_value * 0.03), str(height))
        value_text.setSize(10)
        value_text.setStyle("bold")
        value_text.draw(win)

        # 3. Draw the X-Axis Label (below the x-axis)
        if labels and i < len(labels):
            label_text = Text(
                Point(x_start_col + bar_space_width / 2, -15), labels[i])
            label_text.setSize(10)
            # label_text.setRotation(45) <--- REMOVED
            label_text.draw(win)

    # --- Main Loop and Close ---
    # Draw title
    title = Text(Point(graph_width / 2, y_coord_max +
                 padding_y / 2), "Data Visualization Bar Graph")
    title.setSize(18)
    title.setStyle("bold")
    title.draw(win)

    # Pause until user clicks
    message = Text(Point(graph_width / 2, -padding_y / 2 - 20),
                   "Click anywhere to close.")
    message.setSize(10)
    message.draw(win)
    win.getMouse()
    win.close()


# --- USAGE EXAMPLE ---

# Your list of data (The values determine the bar heights)
data_points = [15, 30, 10, 45, 20, 35, 28]

# Optional list of corresponding labels for the X-axis
category_labels = ["Cat A", "Cat B", "Cat C",
                   "Cat D", "Cat E", "Cat F", "Cat G"]

# Call the function
draw_bar_graph_from_list(data_points, category_labels)
