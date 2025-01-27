
# Open the file in read mode
with open('src/trams/toyama/7000/toyama7000.pnml', 'r') as file:
    lines = file.readlines()

# Define the string to find and the new line content
search_string = "speed:"
ignore_string = "loading_speed:"
new_line_content = "\t\tspeed:\t\t\t\t\t\t\t50 km/h;"

# Replace the entire line if the search string is found
new_lines = []
for line in lines:
    if search_string in line and ignore_string not in line:
        new_lines.append(new_line_content + '\n')
    else:
        new_lines.append(line)

# Overwrite the original file with the modified content
with open('src/trams/toyama/7000/toyama7000.pnml', 'w') as file:
    file.writelines(new_lines)