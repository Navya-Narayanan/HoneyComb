def draw_hexagon():
    return (" ___\n" +
            "/   \\\n" +
            "\\___/")

def draw_pattern(rows, columns):
    pattern = ""
    for row in range(rows):
        if row % 2 != 0:
            pattern += "  "  # Add extra space at the beginning for odd rows
        for column in range(columns):
            pattern += draw_hexagon()
            if column < columns - 1:
                pattern += " "
        pattern += "\n"
    return pattern
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

pattern = draw_pattern(rows, columns)
print(pattern)
