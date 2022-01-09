import requests
open_weather_token = "c7be47a4c5e3121c3a7c99fa81a0ba56"

id_to_emoji = {
    "temperature": "\U0001F321",
    "pressure": "\U000023F2",
    "wind": "\U0001F4A8",
    "place": "\U0001F3D9",
    "2": "\U0001F329",
    "5": "\U0001F327",
    "3": "\U0001F327",
    "6": "\U0001F328",
    "7": "\U0001F32B",
    "8": "\U00002601",
    "800": "\U00002600"
}


def get_weather(city="nizhny+novgorod", token=open_weather_token):
	r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&appid={token}&units=metric")
	data = r.json()

	city = data["name"]
	temperature = str(data["main"]["temp"])
	weather = data["weather"][0]["description"].title()
	wind = str(data["wind"]["speed"])
	pressure = str(data["main"]["pressure"]*0.75)

	'''
	if data["weather"][0]["id"] == 800:
		icon = id_to_emoji["800"]
	else:
		icon = id_to_emoji(str(data["weather"][0]["id"])[0])

	'''
	total_info = {
		"Место": city , # + " " + id_to_emoji["place"],
		"Температура": temperature + "°C",  # + id_to_emoji["temperature"],
		"Погода": weather,  # + " " + icon,
		"Давление": pressure + " мм.рт.ст.",  # + id_to_emoji["pressure"],
		"Ветер": wind + " м/с "  # + id_to_emoji["wind"]
	}

	return total_info

#=================================================#
def weather_table_output(info=get_weather()):
    from rich.console import Console
    from rich.table import Table

    console = Console()

    table = Table(show_header=True, header_style="bold green", show_edge=True, border_style="bold green")
    table.add_column("Чё", style="dim", width=12)
    table.add_column("Как")

    for i in info.keys():
        table.add_row(i, info[i])

    console.print(table)


weather_table_output()
