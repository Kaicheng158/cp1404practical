"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

COLOUR_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                "aquamarine4": "#458b74", "azure1": "#f0ffff",
                "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b",
                "beige": "#f5f5dc", "bisque1": "#ffe4c4"}
print(COLOUR_CODES)

colour_name = input("Enter a colour name: ")
while colour_name != "":
    if colour_name in COLOUR_CODES:
        print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ")
