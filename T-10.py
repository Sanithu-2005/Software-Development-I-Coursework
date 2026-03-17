from graphics import *

def draw_histogram(hours, counts, airline, airport, year):
    n_hours = len(hours)
    max_count = max(counts)
    bar_height = 30
    gap = 10
    left_margin = 120
    right_margin = 60
    top_margin = 80
    bottom_margin = 60
    width = 800
    height = top_margin + n_hours * (bar_height + gap) + bottom_margin

    win = GraphWin("Flight Departures Histogram", width, height)
    win.setBackground("white")

    # Title
    title = f"Departures per Hour for {airline}\n{airport} — {year}"
    title_text = Text(Point(width/2, top_margin/2), title)
    title_text.setSize(18)
    title_text.setStyle("bold")
    title_text.setFill("navy")
    title_text.draw(win)

    # Y-axis label
    y_label = Text(Point(left_margin/2, height/2), "Hour")
    y_label.setSize(14)
    y_label.setStyle("bold")
    y_label.setFill("darkgreen")
    y_label.draw(win)

    # X-axis label
    x_label = Text(Point(width/2, height - bottom_margin/2), "Number of Departing Flights")
    x_label.setSize(14)
    x_label.setStyle("bold")
    x_label.setFill("darkgreen")
    x_label.draw(win)

    # Scale bars
    usable_width = width - left_margin - right_margin
    scale = usable_width / max_count if max_count > 0 else usable_width

    # Colors for bars
    bar_colors = [
        "#4e79a7", "#f28e2b", "#e15759", "#76b7b2",
        "#59a14f", "#edc948", "#b07aa1", "#ff9da7",
        "#9c755f", "#bab0ab", "#2b7a78", "#3aafa9"
    ]

    # Draw bars and labels
    for i, (hour, count) in enumerate(zip(hours, counts)):
        y = top_margin + i * (bar_height + gap)
        bar_len = int(count * scale)

        bar = Rectangle(Point(left_margin, y), Point(left_margin + bar_len, y + bar_height))
        bar.setFill(bar_colors[i % len(bar_colors)])
        bar.setOutline("black")
        bar.draw(win)

        hour_text = Text(Point(left_margin - 50, y + bar_height/2), str(hour))
        hour_text.setSize(12)
        hour_text.setFill("black")
        hour_text.draw(win)

        value_text = Text(Point(left_margin + bar_len + 25, y + bar_height/2), str(count))
        value_text.setSize(12)
        value_text.setFill("black")
        value_text.draw(win)

    win.getMouse()  # Wait for click to close
    win.close()

# Example data to show the histogram
if __name__ == "__main__":
    hours = ["06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
    counts = [7, 12, 18, 15, 10, 8, 16, 9, 14, 11, 13, 6]
    airline = "Air Example"
    airport = "Example International Airport"
    year = 2024
    draw_histogram(hours, counts, airline, airport, year)
