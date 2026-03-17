"""
****************************************************************************
Additional info
 1. I declare that my work contins no examples of misconduct, such as
 plagiarism, or collusion.
 2. Any code taken from other sources is referenced within my code solution.
 3. Student ID: w2182075 (UOW) / 20250212 (IIT)
 4. Date (of Upload) : 21/11/2025
****************************************************************************

"""
from graphics import *
import csv
import math

data_list = []   # data_list An empty list to load and hold data from csv file


def load_csv(CSV_chosen):
    """
    This function loads any csv file by name (set by the variable 'selected_data_file') into the list "data_list"
    YOU DO NOT NEED TO CHANGE THIS BLOCK OF CODE - and so I have not
    """
    with open(CSV_chosen, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            data_list.append(row)


# ************************************************************************************************************
# EDIT THE CODE BELOW TO COMPLETE YOUR SUBMISSION
try:
    departure_city_code = ""
    year = ""  # didn't save as int here since isdigit wouldn't work/to check for type
    valid_airport_code = {"LHR": "London Heathrow",
                          "MAD": "Madrid Adolfo Suárez-Barajas",
                          # CGD was what was in data set (.csv file)
                          "CDG": "Charles De Gaulle International",
                          "IST": "Istanbul Airport International",
                          "AMS": "Amsterdam Schiphol",
                          "LIS": "Lisbon Portela",
                          "FRA": "Frankfurt Main",
                          "FCO": "Rome Fiumicino",
                          "MUC": "Munich International",
                          # used a dictionary here so that the full name can be accessed/printed
                          "BCN": "Barcelona International"}

    # Used .strip() to strip any whitespace from the filename string and .upper() was used for converting lower case letter input.

    while True:
        departure_city_code = (
            str(input("Enter departure city code: "))).strip().upper()
        if len(departure_city_code) != 3:
            print("Wrong code length - please enter a three-letter city code")
        elif departure_city_code not in valid_airport_code:
            print("Unavailable city code - please enter a valid city code")
        else:
            break  #This is here so the question loops again and again till correct answer is entered

    # No int in the year input line cause isdigit doesn't work with it for when I tested
    while True:
        year = input("Enter valid integer year: ").strip()
        if not year.isdigit() or len(year) != 4:  # To check if the year is an integer and has four numbers
            print("Wrong data type or wrong number of numbers - please enter a four-digit year value")
            continue
        year = int(year)
        if year < 2000 or year > 2025:
            print("Out of range - please enter a value from 2000 to 2025")
            continue
        break  #Same as the break before

    # The following is to actually gather the the year and code together to look for the file
    # f string was used here to include year and city code
    selected_data_file = f"{departure_city_code}{year}.csv"
    # \n was used here to start a newline afterwardsi
    print(f"\nSelected file: {selected_data_file}")
    print(f"Airport: {valid_airport_code[departure_city_code]} ({year})")

    # selected_data_file=filename
    # calls the function "load_csv" sending the variable 'selected_data_file" as a parameter
    load_csv(selected_data_file)

    # Some Example code queries to be replaced with those required by the brief. Compare these outputs to the supplied CSV files

# print (f"The current file name is {selected_data_file}")
# print ("")
# print (f"First row (with non label data inside) of data_list is data_list[0] -> {data_list[0]}")
# print ("")
# print (f"Second item of the first row is flight number, data_list[0][1]      -> {data_list[0][1]}")
# print ("")
# print (f"Third item of the second row is scheduled depature, data_list[1][2] -> {data_list[1][2]}")
##
    count_of_flights = len(data_list)
    print(
        f"The total number of departure flights for the selected file recorded in the 12-hour period was {count_of_flights}")
    # roughly 12 hour period
    print("")  # space

    Terminal2_count = 0
    for row in data_list:
        if float(row[8]) == 2:
            Terminal2_count += 1
    print(
        f"The total number of flights departing from Terminal 2 was {Terminal2_count}")
    print("")

    sixhundred_miles_count = 0
    for row in data_list:
        if float(row[5]) < 600:
            sixhundred_miles_count += 1
    print(
        f"The total number of departures of flights that are under 600 miles was {sixhundred_miles_count}")
    print("")

    AF_count = 0
    for row in data_list:
        if row[1].startswith("AF"):
            AF_count += 1
    print(
        f"The total number of departure flights by Air France aircraft was {AF_count}")
    print("")

    below_temp_count = 0
    for row in data_list:
        num = int(row[10][:2])
        if num < 15:
            below_temp_count += 1
    print(
        f"The The total number of flights departing in temperatures below 15C was {below_temp_count}")
    print("")

    BA_count = 0
    for row in data_list:
        if row[1].startswith("BA"):
            BA_count += 1
    BA_departure_result = round(BA_count / 12, 2)
    print(
        f"The average number of British Airways departures per hour (rounded to two decimal places)was {BA_departure_result}")
    print("")

    BA_total_count = 0
    for row in data_list:
        if row[1].startswith("BA"):
            BA_total_count += 1
    BA_total_precentage_result = round(
        (BA_total_count / count_of_flights)*100, 2)
    print(
        f"The percentage of total departures that are British Airways aircraft (rounded to two decimal places) was {BA_total_precentage_result}")
    print("")

    af_total = 0
    af_diff_count = 0

    for row in data_list:
        if row[1].startswith('AF'):
            af_total += 1
            if row[2] != row[3]:
                af_diff_count += 1
    # a flight will presumablely not leave early but may delay
    AF_late_result = round((af_diff_count / af_total) * 100, 2)
    print(
        f"The percentage of Air France flights with a delayed departure (rounded to two decimal places)was {AF_late_result}")
    print("")

    unique_number_rain_count = 0
    unique_numbers_before_colon = set()  # to not allow duplicates

    for row in data_list:
        if "rain" in row[10]:
            number_before_colon = row[2].split(":")[0]#spilt is used here to break apart the 12:22 time string to a list of substrings like [12,22] and so by using [0] we can check the first element of said list
            if number_before_colon not in unique_numbers_before_colon:
                unique_numbers_before_colon.add(number_before_colon)
                unique_number_rain_count += 1

    print(
        f"The total number of hours of rain in the twelve hours (rain values are recorded once every hour) was {unique_number_rain_count}")
    print("")

    string_counts = {}
    for row in data_list:
        string_value = row[4]
        if string_value in string_counts:
            string_counts[string_value] += 1
        else:
            string_counts[string_value] = 1

    min_count = min(string_counts.values())

    least_frequent_strings = []
    for string, count in string_counts.items():
        if count == min_count:
            least_frequent_strings.append(string)

    for code in least_frequent_strings:
        if code in valid_airport_code:
            print(
                f"The full name of the least common destination (or names if more than one)was {valid_airport_code[code]}")

    full_departure_city_name = valid_airport_code.get(departure_city_code)
    result_lines = [
        f"Airport: {full_departure_city_name}",
        f"Year: {year}",
        "Outcomes:",
        f"  The total number of departure flights for the selected file recorded in the 12-hour period: {count_of_flights}",
        f"  The total number of flights departing from Terminal 2: {Terminal2_count}",
        f"  The total number of departures of flights that are under 600 miles: {sixhundred_miles_count}",
        f"  The total number of departure flights by Air France aircraft: {AF_count}",
        f"  The total number of flights departing in temperatures below 15C: {below_temp_count}",
        f"  The average number of British Airways departures per hour (rounded to two decimal places): {BA_departure_result}",
        f"  The percentage of total departures that are British Airways aircraft (rounded to two decimal places): {BA_total_precentage_result}",
        f"  The percentage of Air France flights with a delayed departure (rounded to two decimal places): {AF_late_result}",
        f"  The total number of hours of rain in the twelve hours (rain values are recorded once every hour):{unique_number_rain_count}",
        f"  The full name of the least common destination (or names if more than one): {valid_airport_code[code]}",
        "-" * 40  # Gives space in between
    ]

    result_text = "\n".join(result_lines) + "\n"
    with open("results.txt", "a") as file:
        file.write(result_text)  # saves the file as a text file

    print("Results saved to results.txt")

    # Part - D

    valid_airline_code = {
        "BA": "British Airways",
        "AF": "Air France",
        "AY": "Finnair",
        "KL": "KLM",
        "SK": "Scandinavian Airlines",
        "TP": "TAP Air Portugal",
        "TK": "Turkish Airlines",
        "W6": "Wizz Air",
        "U2": "easyJet",
        "FR": "Ryanair",
        "A3": "Aegean Airlines",
        "SN": "Brussels Airlines",
        "EK": "Emirates",
        "QR": "Qatar Airways",
        "IB": "Iberia",
        "LH": "Lufthansa"}

# This following section is in code twice cause I used these variables to find count_aircraft_departures_per_hour
# Extracting the relevant columns for each row
    rows = [
        [row[1], row[0], row[3]]
        for row in data_list]

# Getting Departure Airport (assuming all flights in rows are from the same airport)
    departure_airport_code = rows[0][1]
    full_departure_airport_name = valid_airport_code.get(
        departure_airport_code, "Unknown Airport")

# List of Hour Labels (from 0:00 to 12:00)
    hours = ["{:02d}:00".format(h) for h in range(0, 13)] 

    def count_aircraft_departures_per_hour(rows, airline_code):
        """
        Counts departures per hour for aircraft with flight numbers starting with "airline_code"
        """
        hour_counts = [0] * 13  # 0 to 12 hours

        for row in rows:
            if row[0].startswith(airline_code):
                # This considers only the hour and drops the minutes.
                hour = int(row[2].split(":")[0])
                # .split(":") -This splits a string into a list using the colon : as the separator. [0] gets the first part (the hour).
                if 0 <= hour <= 12:
                    hour_counts[hour] += 1
        return hour_counts  # so for each hour from 0 to 12, it counts how many departures there were for the specified airline code

# counts = count_aircraft_departures_per_hour(rows, airline_code)

    def draw_histogram(hours, counts, full_name_of_airline, full_departure_airport_name, year):
        n_hours = len(hours)
        max_count = max(counts)
        bar_height = 30
        gap = 10
        left_margin = 220
        right_margin = 60
        top_margin = 80
        bottom_margin = 60
        width = 900
        height = top_margin + n_hours * (bar_height + gap) + bottom_margin

        win = GraphWin("Flight Departures Histogram", width, height)
        win.setBackground("white")

        title = f"Departures per Hour for {full_name_of_airline}\n{full_departure_airport_name} — {year}"
        title_text = Text(Point(width / 2, top_margin / 2), title)
        title_text.setSize(18)
        title_text.setStyle("bold")
        title_text.setFill("navy")
        title_text.draw(win)

        y_label = Text(Point(left_margin / 2, height / 2), "Hour")
        y_label.setSize(14)
        y_label.setStyle("bold")
        y_label.setFill("darkgreen")
        y_label.draw(win)
        y_label.move(-12, 0)

        x_label = Text(Point(width / 2, height - bottom_margin / 2),
                       "Number of Departing Flights")
        x_label.setSize(14)
        x_label.setStyle("bold")
        x_label.setFill("darkgreen")
        x_label.draw(win)

        usable_width = width - left_margin - right_margin
        scale = usable_width / max_count if max_count > 0 else usable_width

        bar_color = "#4286f4"

        for i, (hour, count) in enumerate(zip(hours, counts)): #The program gets hours from above and below,counts from below
            y = top_margin + i * (bar_height + gap)
            bar_len = int(count * scale)

            bar = Rectangle(Point(left_margin, y), Point(
                left_margin + bar_len, y + bar_height))
            bar.setFill(bar_color)
            bar.setOutline("black")
            bar.draw(win)

            hour_text = Text(
                Point(left_margin - 70, y + bar_height / 2), str(hour))
            hour_text.setSize(12)
            hour_text.setFill("black")
            hour_text.draw(win)

            value_text = Text(Point(left_margin + bar_len +
                              25, y + bar_height / 2), str(count))
            value_text.setSize(12)
            value_text.setFill("black")
            value_text.draw(win)

        win.getMouse()
        win.close()

    # draw_histogram(hours, counts, full_name_of_airline, full_departure_airport_name, year)
    def main():
        while True:  # infite loop till break through typing not y
            # Extract the relevant columns for each row
            rows = [
                [row[1], row[0], row[3]]
                for row in data_list]

            #  User Input for Airline Code
            airline_code = input(
                "Enter a two-character Airline code to plot a histogram: ").strip().upper()
            while airline_code not in valid_airline_code: #valid_airline_code is a dictionary from above
                print("Unavailable Airline code, please try again.")
                airline_code = input(
                    "Enter a two-character Airline code to plot a histogram: ").strip().upper()

            # Getting Full Airline Name
            full_name_of_airline = valid_airline_code.get(
                airline_code, airline_code) #calling the fullnames which are here as values on the above dictionary.

            # Getting Departure Airport (assuming all flights in rows are from the same airport)
            departure_airport_code = rows[0][1] #This is AirportCode on the .csv files
            full_departure_airport_name = valid_airport_code.get(
                # If the code isn’t found in the dictionary, it returns "Unknown Airport" as a default.
                departure_airport_code, "Unknown Airport")

            # List of Hour Labels
            hours = ["{:02d}:00".format(h)
                     for h in range(0, 13)]  # 00:00 to 12:00

            counts = count_aircraft_departures_per_hour(rows, airline_code)#calling user def function from above 

            draw_histogram(hours, counts, full_name_of_airline,
                           full_departure_airport_name, year) #calling user def function from above
            again = input(
                "Do you want to select a new data file? Y/N: ").strip().lower()
            if again != 'y':
                print("Exited program.")
                break

    if __name__ == "__main__":
        main()

except Exception as e:
    print("Error occured", e)
