# Opening File and Write Anything
file= open("youtube.txt", "w")

# Method 1
try:
    file.write("Youtube playlist is there")
finally:
    file.close()

# Method 2
with open("youtube.txt", "w") as file:
    file.write("Youtube playlist is there")