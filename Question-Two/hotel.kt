data class Room(
    val number: Int,
    val price: Int,
    var isBooked: Boolean = false,
    var isPaid: Boolean = false,
    var guestName: String
)
fun main() {
    val rooms = mutableListOf(
        Room(101, 100),
        Room(102, 150),
        Room(103, 200)
    )
    val availableRoom = rooms.find { !it.isBooked && it.price == paymentAmount }
    if (availableRoom != null) {
        availableRoom.isBooked = true
        availableRoom.isPaid = true
        availableRoom.guestName = guestName
        println("Booking Confirmed :white_check_mark:")
        println("Room Assigned: ${availableRoom.number}")
        println("Payment Status: Paid")
    } else {
        println("Booking Rejected :x: - No available room for the payment amount: $paymentAmount")
    }
}
val guestName = "Meron"
val paymentAmount = 100