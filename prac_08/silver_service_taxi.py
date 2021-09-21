from prac_08.taxi import Taxi

class Silver_taxi(Taxi):
    flagfall = 4.5
    def __init__(self,name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness
    def __str__(self):
        return "{}, fuel={}, odo={}, {}km on current fare, ${}/km plus flagfall of ${}".format(self.name, self.fuel,
                                                                                               self.odometer,
                                                                                               self.current_fare_distance,
                                                                                               self.price_per_km,self.flagfall)
    def get_new_fare(self):
        return self.flagfall + super().get_fare()