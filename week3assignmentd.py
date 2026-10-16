months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
date_input=input("Date: ").strip()

if "/" in date_input:
    month,day,year=date_input.split("/")

elif "," in date_input:
    month,day,year=date_input.split(" ")
    day.replace(",","")

if month.title() in months:
    month=months.index(month.title())+1

else:
    pass

print(f"{year}--,{month:02d}--{day:02d}")