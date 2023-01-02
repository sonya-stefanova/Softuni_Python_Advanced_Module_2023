def forecast(*args):
    weather_forecast_dict = {
        'Sunny': [],
        'Cloudy': [],
        'Rainy': [],
    }

    for town, weather in args:
        weather_forecast_dict[weather].append(town)

    result = ''

    for weather, list_of_towns in weather_forecast_dict.items():
        for town in sorted(list_of_towns):
            result += f'{town} - {weather}\n'

    return result


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))