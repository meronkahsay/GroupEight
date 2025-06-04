class Room:
    def __init__(self, room_id, room_type, price_per_night):
        self.room_id = room_id
        self.room_type = room_type
        self.price_per_night = price_per_night
class Reservation:
    def __init__(self, room_id, guest_name, check_in_day, check_out_day):
        self.room_id = room_id
        self.guest_name = guest_name
        self.check_in_day = check_in_day
        self.check_out_day = check_out_day
        self.is_paid = False
class Payment:

    def __init__(self, guest_name, room_id, amount):
        self.guest_name = guest_name
        self.room_id = room_id
        self.amount = amount

class HotelSystem:
    def __init__(self):
        self.rooms = {} 
        self.reservations = {}  
        self.payments = [] 

    def add_room(self, room_id, room_type, price_per_night):
        room = Room(room_id, room_type, price_per_night)
        self.rooms[room_id] = room
        self.reservations[room_id] = []
        print(f"Room {room_id} added.")

    def is_available(self, room_id, check_in, check_out):
        for res in self.reservations[room_id]:
            if check_in < res.check_out_day and check_out > res.check_in_day:
                return False
        return True

    def book_room(self, guest_name, check_in, check_out):
        for room_id in self.rooms:
            if self.is_available(room_id, check_in, check_out):
                new_res = Reservation(room_id, guest_name, check_in, check_out)
                self.reservations[room_id].append(new_res)
                print(f"{guest_name} booked Room {room_id} from Day {check_in} to Day {check_out}.")
                return new_res
        print("No available rooms for those days.")
        return None

    def calculate_price(self, room_id, check_in, check_out):
        nights = check_out - check_in
        return self.rooms[room_id].price_per_night * nights

    def make_payment(self, guest_name, room_id, amount):
        for res in self.reservations[room_id]:
            if res.guest_name == guest_name and not res.is_paid:
                expected_amount = self.calculate_price(room_id, res.check_in_day, res.check_out_day)
                if amount == expected_amount:
                    res.is_paid = True
                    payment = Payment(guest_name, room_id, amount)
                    self.payments.append(payment)
                    print("Payment successful.")
                else:
                    print(f"Payment failed. Expected: {expected_amount}, but got: {amount}")
                return
        print("Reservation not found or already paid.")

    def check_in(self, guest_name, room_id):
        for res in self.reservations[room_id]:
            if res.guest_name == guest_name:
                if res.is_paid:
                    print("Check-in successful.")
                else:
                    print("Check-in failed: Payment not done.")
                return
        print("Reservation not found.")
        
    def check_out(self, guest_name, room_id):
        for res in self.reservations[room_id]:
            if res.guest_name == guest_name:
                print("Check-out successful.")
                return
        print("Reservation not found.")
