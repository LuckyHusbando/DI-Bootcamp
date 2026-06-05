#Exercise XP Ninja - Call History

# Step 1: Create the Phone class
class Phone:
    
    def __init__(self, phone_number):
        """
        Initializes a Phone object with a phone number and empty history lists.
        """
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    # Step 2: Add a method called call
    def call(self, other_phone):
        """
        Simulates a call to another Phone object.
        """
        call_string = f"Calling from {self.phone_number} to {other_phone.phone_number}..."
        print(call_string)
        self.call_history.append(call_string)

    # Step 3: Add a method called show_call_history
    def show_call_history(self):
        """
        Prints the phone's call history.
        """
        print(f"\n--- Call History for {self.phone_number} ---")
        if not self.call_history:
            print("No call history.")
        else:
            for call_log in self.call_history:
                print(call_log)
    
    # Step 4: Implement the send_message method
    def send_message(self, other_phone, content):
        """
        Simulates sending a message to another Phone object.
        The message is saved to both the sender's and receiver's message list.
        """
        message = {
            'to': other_phone.phone_number,
            'from': self.phone_number,
            'content': content
        }
        self.messages.append(message)
        other_phone.messages.append(message)
        print(f"\nMessage sent from {self.phone_number} to {other_phone.phone_number}.")

    # Step 5: Implement show_outgoing_messages(self)
    def show_outgoing_messages(self):
        """
        Prints all messages sent from this phone.
        """
        print(f"\n--- Outgoing Messages from {self.phone_number} ---")
        found_message = False
        for message in self.messages:
            if message['from'] == self.phone_number:
                print(f"To: {message['to']}, Content: {message['content']}")
                found_message = True
        if not found_message:
            print("No outgoing messages.")
    
    # Step 6: Implement show_incoming_messages(self)
    def show_incoming_messages(self):
        """
        Prints all messages received by this phone.
        """
        print(f"\n--- Incoming Messages for {self.phone_number} ---")
        found_message = False
        for message in self.messages:
            if message['to'] == self.phone_number:
                print(f"From: {message['from']}, Content: {message['content']}")
                found_message = True
        if not found_message:
            print("No incoming messages.")
    
    # Step 7: Implement show_messages_from(self, other_phone)
    def show_messages_from(self, other_phone):
        """
        Prints all messages received from a specific other phone.
        """
        print(f"\n--- Messages for {self.phone_number} from {other_phone.phone_number} ---")
        found_message = False
        for message in self.messages:
            if message['from'] == other_phone.phone_number:
                print(f"Content: {message['content']}")
                found_message = True
        if not found_message:
            print(f"No messages from {other_phone.phone_number}.")

# --- Test Code ---

# Create two Phone objects
phone1 = Phone("052-123-4567")
phone2 = Phone("050-987-6543")

# Test the call functionality
phone1.call(phone2)
phone2.call(phone1)
phone1.call(phone2)

# Show call history for each phone
phone1.show_call_history()
phone2.show_call_history()

# Test the message functionality
phone1.send_message(phone2, "Hey, are you free for dinner tonight?")
phone2.send_message(phone1, "I'm busy, sorry! How about tomorrow?")
phone1.send_message(phone2, "Tomorrow works for me!")

# Show messages for phone1
phone1.show_outgoing_messages()
phone1.show_incoming_messages()
phone1.show_messages_from(phone2)

# Show messages for phone2
phone2.show_outgoing_messages()
phone2.show_incoming_messages()
phone2.show_messages_from(phone1)

#end