
routes = ["Route A", "Route B"]
passenger_volume = {"peak": 120, "off_peak": 40}
special_event = True
maintenance_time = "02:00 - 04:00"
demand_pattern = {"Route A": 80, "Route B": 100}
def optimize_schedule():
    if passenger_volume["peak"] > 100:
        print("Increase service during peak hours")
    if passenger_volume["off_peak"] < 50:
        print("Reduce service during off-peak hours")
    if special_event:
        print("Add extra trips and modify routes for the event")
    print("Schedule maintenance at:", maintenance_time)
    print("Suggested route: Route B (higher demand)")
optimize_schedule()



