



import random

countries = [
    "Argentina",
    "Brazil",
    "France",
    "Germany",
    "Spain",
    "Portugal",
    "England",
    "Netherlands",
    "Belgium",
    "Croatia",
    "Italy",
    "Uruguay",
    "Colombia",
    "Mexico",
    "USA",
    "Canada",
    "Japan",
    "South Korea",
    "Australia",
    "Iran",
    "Saudi Arabia",
    "Morocco",
    "Senegal",
    "Egypt",
    "Nigeria",
    "Ghana",
    "Switzerland",
    "Denmark",
    "Sweden",
    "Poland",
    "Turkey",
    "Ecuador"
]

random.shuffle(countries)
for i in range(8):
    print("Group", i+1)
    print(countries[i*4:i*4+4])