from abc import ABC , abstractmethod
class Car(ABC):
    @abstractmethod
    def breaks(self):
        pass
    @abstractmethod
    def mirror(self):
        pass
    @abstractmethod
    def seats(self):
        pass
    @abstractmethod
    def engine(self):
        pass
    def price(self,model):
        if model=='Aspire':
            return 1000000
        elif model=='EcoSport':
            return 1700000
        elif model=="Endrover":
            return 3500000
        else:
            return 'Please visit the showroom'
class EcoSport(Car):
    def __init__(self,make, my):
        self.make=make
        self.model=my
    def breaks(self):
        self.break_condition="applied"
        return self.break_condition

    def mirror(self):
        self.mirror="fitted"
        return self.mirror
    def seats(self):
        self.capacity="6 seater"
        return self.capacity
    def engine(self):
        self.type="Petrol Engine"
        return self.type
    def waranty(self):
        print("FORD OFFER 3 years FREE Warranty")
es_1=EcoSport('Ford',2022)
es_1.waranty()
print(es_1.engine())
print(es_1.price('EcoSport'))