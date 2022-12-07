# The laws of a country state that an adult can drive
# if they have a license to do so, and to qualify for
# a driver's license, you must be 18 years of age or older.

# Create a conditional structure to check if a 16-year-old
# without a license can drive, and display the corresponding
# result on the screen:

# "You can drive"
# "You can't drive yet. You must be 18 years old and have a license"
# "You can't drive. You need to have a license"


age = 16
has_license = False
if has_license == True:
    print("You can drive")
elif age < 17:
    print("You can't drive yet. You must be 18 and have a license")
else:
    print("You can't drive. You need to have a license")