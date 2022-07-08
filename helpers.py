from datetime import date

weekdayDict = {
    0 : "Monday",
    1 : "Tuesday",
    2 : "Wednesday",
    3 : "Thursday",
    4 : "Friday",
    5 : "Saturday",
    6 : "Sunday"
}

mediaDict = {
    "Monday" : "assets/MondayVideo.mp4",
    "Wednesday" : "assets/WednesdayPicture.jpg",
    "Friday" : "assets/FridayVideo.mp4"
}

class Day:
    def __init__(self, dayInt):
        self.dayInt = dayInt
        self.dayStr = weekdayDict[dayInt]
        self.media = mediaDict[self.dayStr] if (self.dayStr in ("Monday", "Wednesday", "Friday")) else None
        self.postDay = (self.dayStr in ("Monday", "Wednesday", "Friday"))

def get_weekday():
    return Day(date.today().weekday())

def format_time(total):
    min = str(int(total/60))
    temp = (total%60)
    sec = "0"+str(temp) if temp<10 else str(temp)
    return (f"{min}:{sec}")
