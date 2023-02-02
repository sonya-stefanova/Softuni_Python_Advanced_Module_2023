def forecast(*args):

    dict_of_forecasts = {
        'Sunny': [],
        'Cloudy': [],
        'Rainy': []
    }

    for location, forecast in args: #tuple
        dict_of_forecasts[forecast].append(location)

    result = ''
    for forecast, list_of_locations in dict_of_forecasts.items():
        for location in sorted(list_of_locations):
            result += f'{location} - {forecast}\n'

    return result




print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
