from twilio.rest import Client

TWILIO_SID = "AC8acc85d0173b132f5d63bd13b1c7643e"
TWILIO_AUTH_TOKEN = "e8220c8d97b4cb9a30a542af36f5a818"
TWILIO_VIRTUAL_NUMBER = "+16264663475"
TWILIO_VERIFIED_NUMBER = "+918766960715"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message=self.client.messages.create(
            body=message,
            from_= TWILIO_VIRTUAL_NUMBER,
            to= TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)

