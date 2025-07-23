temperature = float(input("enter the current temperature in °C: "))

if temperature > 30:
    print("it's hot outside! stay hydrated") 
elif 20 <= temperature <= 30:
    print("weather is pleasent and warm.")
elif 10 <= temperature < 20:
    print("it's a bit cool. you might need a light jacket.")
elif 0 <= temperature < 10:
    print("it's cold. wear warm clothes")
else:
    print("it's freezing! stay indoors if possible.")                