import random
#udelat predka bojovniku a pouzit ho pro jeho ruzne typy/specializace, potomky
class Rytir:
    
    def __init__(self, jmeno, HP, ATK, DEF, zbran):
        self.jmeno = jmeno
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.zbran = zbran
    
    def zautoc(self, protivnik):
        return self.ATK + self.zbran.ATK - protivnik.DEF
    
    def __str__(self):
        return f"Jmeno: {self.jmeno}, HP: {self.HP}"
class Negr(Rytir):           #to v zavorce ukazuje ci je potomek jakoze

    def __init__(self, jmeno, HP, ATK, DEF, zbran, bpower):
        super().__init__(jmeno, HP, ATK, DEF, zbran)
        self.bpower = bpower
    def zautoc(self, protivnik):
        return super().zautoc(protivnik) and self.ATK + self.bpower

class Healer(Rytir):

    def __init__(self, jmeno, HP, ATK, DEF, zbran, heal):
        super().__init__(jmeno, HP, ATK, DEF, zbran)
        self.heal = heal
    def zautoc(self,protivnik):
        return super().zautoc(protivnik) and self.HP + self.heal

class Dvojruk(Rytir):

    def __init__(self, jmeno, HP, ATK, DEF, zbran, dr):
        super().__init__(jmeno, HP, ATK, DEF, zbran)
        self.dr = dr
    def zautoc(self, protivnik):
        return super().zautoc(protivnik) and self.ATK+ self.dr.ATK

class Zbran:
    
    def __init__(self, jmeno, ATK):
        self.jmeno = jmeno
        self.ATK = ATK
    
    @property
    def ATK(self):
        return self._ATK
    
    @ATK.setter
    def ATK(self, value):
        self._ATK = int(value)



class Turnaj:
    
    def __init__(self):
        self.seznam_bojovniku = []
    
    def registrace(self, bojovnik):
        self.seznam_bojovniku.append(bojovnik)        

    def duel(self):
        r1 = random.choice(self.seznam_bojovniku)
        r2 = random.choice(self.seznam_bojovniku)
        while r1.HP >= 0 and r2.HP >= 0:
            r2.HP -= r1.zautoc(r2)
            r1.HP -= r2.zautoc(r1)
        if r1.HP <= 0:
            self.seznam_bojovniku.remove(r1)
        if r2.HP <= 0:
            self.seznam_bojovniku.remove(r2)
     

turnaj = Turnaj()
dragon_slayer = Zbran("Dragonslayer", 50)
excalibur = Zbran("Excalibur", 30)
guts = Rytir("Guts", HP=200, ATK=30, DEF=10, zbran=dragon_slayer)
griffith = Rytir("Griffith", HP=180, ATK=25, DEF=25, zbran=excalibur)
nuts = Negr("Nuts", HP=200, ATK=30, DEF=10, zbran=dragon_slayer, bpower = 15)
niffith = Negr("Niffith", HP=180, ATK=25, DEF=25, zbran=excalibur, bpower = 15)
huts = Healer("Huts", HP=200, ATK=30, DEF=10, zbran=dragon_slayer, heal = 9)
hiffith = Healer("hiffith", HP=180, ATK=25, DEF=25, zbran=excalibur, heal = 9)
dvojruk = Dvojruk("Dvojruk",HP=150, ATK=25, DEF=12, zbran=excalibur, dr = random.choice([dragon_slayer, excalibur]))

turnaj.registrace(guts)
turnaj.registrace(nuts)
turnaj.registrace(huts)
turnaj.registrace(griffith)
turnaj.registrace(niffith)
turnaj.registrace(hiffith)
turnaj.registrace(dvojruk)

for bojovnik in turnaj.seznam_bojovniku:
    print(bojovnik)

print()
turnaj.duel()
for bojovnik in turnaj.seznam_bojovniku:
    print(bojovnik)

print()
turnaj.duel()
for bojovnik in turnaj.seznam_bojovniku:
    print(bojovnik)

print()
turnaj.duel()
for bojovnik in turnaj.seznam_bojovniku:
    print(bojovnik)