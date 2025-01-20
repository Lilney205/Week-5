class Smartphone:
    # Constructor to initialize the smartphone attributes
    def __init__(self, brand, model, color, storage, camera_quality):
        self.brand = brand
        self.model = model
        self.color = color
        self.storage = storage
        self.camera_quality = camera_quality
    
    # Method to display smartphone details
    def display_details(self):
        print(f"Smartphone Details:\nBrand: {self.brand}\nModel: {self.model}\nColor: {self.color}")
        print(f"Storage: {self.storage}GB\nCamera Quality: {self.camera_quality}MP")

    # Method to make a call
    def make_call(self, phone_number):
        print(f"Calling {phone_number}...")

    # Method to send a message
    def send_message(self, phone_number, message):
        print(f"Sending message to {phone_number}: {message}")
    

# Creating an object of the Smartphone class
my_phone = Smartphone("Samsung", "Galaxy S21", "Phantom Gray", 128, 108)
my_phone.display_details()
my_phone.make_call("0724467190")
my_phone.send_message("0724467190", "Hello, this is a test message!")￼Enter
