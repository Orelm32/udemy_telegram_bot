import datetime

class ReminderData:

    def __init__(self, row):
        self.reminder_id = row[0]
        self.chat_id = row[1]
        self.message = row[2]
        self.time = row[3]
        self.fired = row[4]
    def __repr__(self):
        return 'Message: {0};At time: {1}'.format(self.message, self.time.strftime('%d/%m/%Y %H:%M'))


    def should_be_fired(self):
        return self.fired is False and datetime.datetime.today() >=self.time

