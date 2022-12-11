class Alarm:
    def postponed(self, amount_minute):
        print(f"the alarm has been postponed {amount_minute} minutes")

lazy = Alarm()
lazy.postponed(15)