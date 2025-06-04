val routes = listOf("Route A", "Route B")
val passengerVolume = mapOf("peak" to 120, "off_peak" to 40)
val specialEvent = true
val maintenanceTime = "02:00 - 04:00"
val demandPattern = mapOf("Route A" to 80, "Route B" to 100)
fun optimizeSchedule() {
    if (passengerVolume["peak"]!! > 100) {
        println("Increase service during peak hours")
    }
    if (passengerVolume["off_peak"]!! < 50) {
        println("Reduce service during off-peak hours")
    }
    if (specialEvent) {
        println("Add extra trips and modify routes for the event")
    }
    println("Schedule maintenance at: $maintenanceTime")
    println("Suggested route: Route B (higher demand)")
}
fun main() {
    optimizeSchedule()
}