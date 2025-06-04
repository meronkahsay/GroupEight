let routes = ["Route A", "Route B"];
let passengerVolume = { peak: 120, offPeak: 40 };
let specialEvent = true;
let maintenanceTime = "02:00 - 04:00";
let demandPattern = { "Route A": 80, "Route B": 100 };
function optimizeSchedule() {
    if (passengerVolume.peak > 100) {
        console.log("Increase service during peak hours");
    }
    if (passengerVolume.offPeak < 50) {
        console.log("Reduce service during off-peak hours");
    }
    if (specialEvent) {
        console.log("Add extra trips and modify routes for the event");
    }
    console.log("Schedule maintenance at: " + maintenanceTime);
    console.log("Suggested route: Route B (higher demand)");
}
optimizeSchedule();






