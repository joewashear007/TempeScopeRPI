
def GetCloudSchedule(weather):
	if weather['clouds']  <= 0.25:
		return (10,20 )
	if weather['clouds'] > 0.25 and weather['clouds'] <= 0.50:
		return (10,15)
	if weather['clouds'] > 0.50 and weather['clouds'] <= 0.75:
		return (10,10)
	if weather['clouds'] > 0.75:
		return (10,5)

def GetWindSchedule(weather):
	if weather['wind']['speed'] <= 1:
		return (1, 5)
	if weather['wind']['speed'] <= 2:
		return (2,4)
	if weather['wind']['speed'] <= 3:
		return (3,3)
	if weather['wind']['speed'] > 3:
		return (4,2)


def GetRainSchedule(weather):
    if len(weather['rain']) < 1:
        return (0, 30)
	if weather['rain']['3h'] <= 1:
		return (1, 5)
	if weather['rain']['3h'] <= 2:
		return (2,4)
	if weather['rain']['3h'] <= 3:
		return (3,3)
	if weather['rain']['3h'] > 3:
		return (4,2)
