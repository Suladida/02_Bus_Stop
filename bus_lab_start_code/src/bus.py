class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []
        

    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        passenger_count = len(self.passengers)
        return passenger_count