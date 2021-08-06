class Battle:
    def _init_(pokemon1,pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.actual_turn= 0
        def is_finished (self):
            return self.pokemon.current_hp <= 0 or self.pokemon2.current_hp <= 0
             




class pokemon:
    def _init_(self,name,level.type1,type2):
        self.name=name
        self.level=level
        self.type1=type1
        self.typel=type2
        self.attacks=[] # vector de ataques 
        self.stats={}
        self.current_status= 0
        self.curretn_hp= 0

class Attack:
    def _init_(self,name,t,category,pp,power,accuracy):
        self.name=name
        self.type=t
        self.category=category
        self.pp=pp
        self.power=power
        self.accuracy=accuracy





        