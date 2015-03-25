import random
import time
#GAME CLASS
class game:
        
#SET
    def CreateHero(self,hero):
        self.hero=hero
    def CreateEnemy(self,enemy):
        self.enemy=enemy
    def CreatePlayer(self,player):
        self.player=player
#FUNCTIONS
    def PrintStatus(self):
        print "hero level: "+str(self.hero.GetLevel())
        print "hero damage: "+str(self.hero.GetDamage())
        print "gold: "+str(self.player.GetGold())
        print "hero power: "+str(self.hero.GetPower())
        print "------------------"
        print "enter 1 to attack, 2 to upgrade, 3 to regenerate, 4 to quit"
    def Upgrade(self):
        print "hero level: "+str(self.hero.GetLevel())
        print "upgrade cost: "+str(self.hero.GetUpgradeCost())
        print "enter number of levels to upgrade"
        u_input=raw_input()
        for i in range(int(u_input)):
            if (self.player.GetGold()>self.hero.GetUpgradeCost()):
                self.player.IncreaseGold(-self.hero.GetUpgradeCost())
                self.hero.IncreaseLevel(1)
            else:
                print "hero level: "+str(self.hero.GetLevel())
                break
    
    def Attack(self):
        print "enter level of enemy you wish to attack"
        el_input=raw_input()
        self.enemy.SetLevel(int(el_input))
        enemy_life=self.enemy.GetLife()
        hero_damage=self.hero.GetDamage()
        self.hero.SetAttackSpeed(1)
        while(enemy_life>0):
            print  "\renemy life: "+str(enemy_life)+" hero power: "+str(self.hero.GetPower())+" hero damage: "+str(self.hero.GetDamage())+"     ",
            enemy_life=enemy_life-self.hero.GetDamage()
            if (self.hero.GetLevel()<self.enemy.GetLevel):
                self.hero.SetPower(self.hero.GetPower()-(self.enemy.GetLevel()-self.hero.GetLevel()+1))
            time.sleep(1./self.hero.GetAttackSpeed())
        print  "\renemy life: "+str(enemy_life)+" hero power: "+str(self.hero.GetPower())+" hero damage: "+str(self.hero.GetDamage())+"     ",
        print ""
        print "enemy defeated"
        print "gold earned: "+str(self.enemy.GetGoldWorth())
        self.player.IncreaseGold(self.enemy.GetGoldWorth())
    
    def Regenerate(self):
        print "how many hours to sleep? regenerates 1 hero power per hour"
        r_input=raw_input()
        for i in range(int(r_input)):
            self.hero.SetPower(self.hero.GetPower()+1)
            print "\rhero power: "+str(self.hero.GetPower())+"     ",
            if (self.hero.GetPower()>=100):
                self.hero.SetPower(100)
                print "\rhero power: "+str(self.hero.GetPower())+"     ",
                break
            time.sleep(1)


#PLAYER CLASS
class player:
    def __init__(self,name):
        self.name=name
        self.gold=0
    def IncreaseGold(self,increase):
        self.gold=self.gold+increase 
    def GetGold(self):
        return self.gold
#DAMAGE CLASS
class damage:
	def __init__(self,element):
		self.element=element
		

#ENEMY CLASS 
class enemy:
    def __init__(self,level,element):
        self.level=level
        self.element=element
        self.MakeName()
        self.InitLife()
        self.life=self.level*100
        self.goldworth=self.level*2
    def MakeName(self):
        firstnames=["hans","hubert","dominik"]
        surnames=["meier","schmitt","stransky"]
        self.name=firstnames[random.randint(0,len(firstnames)-1)]+" "+surnames[random.randint(0,len(surnames)-1)]
    def InitLife(self):
        self.life=self.level*100
        
    def InitGoldWorth(self):
        self.InitLife()
        self.goldworth=self.level*2
#SET
    def SetLevel(self,level):
        self.level=level
        self.InitLife()
        self.InitGoldWorth()

#GET
    def GetLevel(self):
        return self.level
    def GetLife(self):
        self.InitLife()
        return self.life
    def GetGoldWorth(self):
        self.InitLife()
        self.InitGoldWorth()
        return self.goldworth



#HERO CLASS
class hero:
    def __init__(self,name,element):
        self.level=1
        self.name=name
        self.element=element
        self.basedamage=self.level*10
        self.extradamage=0
        self.damage=self.basedamage+self.extradamage
        self.attackspeed=1
        self.power=100
        
    def InitDamage(self):
        self.basedamage=self.level*10
        self.damage=int((self.basedamage+self.extradamage)*self.power/100.)+1
    def IncreaseLevel(self,increase):
        self.level=self.level+increase
        self.InitDamage()
    def Upgrade(self):
        self.IncreaseLevel(1)
    def Upgrade(self,n):
        for i in range(n):
            self.Upgrade()        
#SET
    def SetLevel(self,level):
        self.level=level
        self.InitDamage()  
    def SetExtradamage(self,extradamage):
        self.extradamage=extradamage
        self.InitDamage()
    def SetAttackSpeed(self,attackspeed):
        self.attackspeed=attackspeed
    def SetPower(self,power):
        if (power<0):
            power=0
        self.power=power
        self.InitDamage()        
#GET    
    def GetLevel(self):
        return self.level
    def GetElement(self):
        return self.element
    def GetName(self):
        return self.name
    def GetDamage(self):
        self.InitDamage()
        return self.damage
    def GetAttackSpeed(self):
        return self.attackspeed
    def GetUpgradeCost(self):
        return self.level*10
    def GetPower(self):
        return self.power



        
