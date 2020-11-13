class Band:
    previous_bands=[]
    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.previous_bands += [name]
        
    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        solos=[]
        for member in self.members:
            individual_solo = member.solo
            solos += [individual_solo]
        return solos
    @classmethod
    def to_list(cls):
        return cls.previous_bands
        

class Musician:
    def __init__(self,name,instrument,solo="unknown solo"):
        self.name=name
        self.instrument=instrument
        if solo != "unknown solo":
            self.solo=solo
    def play_solo(self):
        return self.solo
    def get_instrument(self):
        return self.instrument
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

class Guitarist(Musician):
    def __init__(self,name):
        super().__init__(name,"guitar","face melting guitar solo")
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    pass

class Bassist(Musician):
    def __init__(self,name):
        super().__init__(name,"bass","bom bom buh bom")
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    pass

class Drummer(Musician):
    def __init__(self,name):
        super().__init__(name,"drums","rattle boom crash")
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    pass