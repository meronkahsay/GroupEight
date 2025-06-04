let rooms = [
    { number: 101, price: 100, isBooked: false, isPaid: false, guestName: null },
    { number: 102, price: 150, isBooked: false, isPaid: false, guestName: null },
    { number: 103, price: 200, isBooked: false, isPaid: false, guestName: null }
];
let guestName = "Gladwin";
let paymentAmount = 100;
let availableRoom = rooms.find(room => !room.isBooked && room.price === paymentAmount);
if (availableRoom) {
    availableRoom.isBooked = true;
    availableRoom.isPaid = true;
    availableRoom.guestName = guestName;
    console.log("Booking Confirmed");
    console.log(`Room Assigned: ${availableRoom.number}`);
    console.log("Payment Status: Paid");
} else {
    console.log(`Booking Rejected No available room for the payment amount: $${paymentAmount}`);
}