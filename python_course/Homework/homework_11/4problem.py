# create a class to turn seconds into minutes
class Time:
    def __init__(self,t):
        self.secs = t
    def convert_to_minutes(self):
        minutes = (self.secs-(self.secs%60))/60
        print(f'{int(minutes)}:{int(self.secs%60)}')
    def convert_to_hours(self):
        hours = ((self.secs-(self.secs%3600))/3600)
        minutes = ((self.secs%3600)-((self.secs%3600)%60))/60
        print(f'{int(hours)}:{int(minutes)}:{int((self.secs%3600)%60)}')



if __name__ == "__main__":
    secs = eval(input("how many seconds? "))
    neater = Time(t = secs)
    if secs < 3600:
        neater.convert_to_minutes()
    else:
        neater.convert_to_hours()
