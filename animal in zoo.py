class Animal :
    zoo_name = "Animal world"
    def __init__(self, name ,species , age , sound):

        

        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def info(self):
        info_Animal = f"*zoo name : {Animal.zoo_name} \n name : {self.name} \
        \n species : {self.species} \n age : {self.age} \n sound : {self.sound} "
        return info_Animal 
    

    def __str__(self):
        s = (f" name : {self.name} , species : {self.species} , age : {self.age} , sound : {self.sound}")
        return s
    
    def make_sound(self):
        sound_Animal = f" {self.name} say: {self.sound}"
        return sound_Animal

class Bird(Animal):
    def __init__(self , name ,species , age , sound , wing_span ):
        super().__init__( name ,species , age , sound )

        self.wing_span = wing_span

    def info(self):
        info_Animal = f"*zoo name : {Animal.zoo_name} \n name : {self.name} \n species : {self.species} \
        \n age : {self.age} \n sound : {self.sound} \n wing span : {self.wing_span} "
        return info_Animal 
    

lion = Animal("lion" , "felin" , "20" , "mioooooo"  )
quail = Bird("quail" , "Bird" , "2" , "jik jik" , "43" )