import random
import time
from os import system


#Create global class Personnage with attribute
class Personnage:
    pv=100
    pa=10
    name = "Personnage"
    def attack(self):
        return self.pa * random.randint(0, 4)
    
    #Gette/Setter
    def getPv(self):
        return self.pv
    def getPa(self):
        return self.pa

#Create Manifestant class with Personnage attribute
class Manifestant(Personnage):

    print("-->Manifestant s'avance<--\n")
    name = "Manifestant"
    pa = Personnage.pa + 20
    nbPotion = 5
    nbVictory = 0

    #Crete function to heal Manifestant
    def potion(self):
        pot = random.randint(0, 1)
        print("\t*.* Manifestant utilise 8.6 *.*\n")
        if pot == 1 and self.nbPotion > 0:

            print("\tLe manifestant boit une 8.6\n")
            self.nbPotion -= self.nbPotion
            print("\tIl lui reste " + str(self.pv + 15) + " PV\n")
            self.pv += 15
            return self.pv

        else :
            print("\tCa n'a pas marché\n")
            return self.pv

    #Create function to attack with Manifestant
    def atk(self):

        if(self.pa>=5):

            print("\tXxX " + self.name + " lance un pavé XxX\n")
            self.pa -= 5
            atk = self.attack()
            print("\tIl fait " + str(atk) + " point de degats\n")
            return atk
        else:
            print("\t --Pas assez de mana--\n")
            return 0

#Create Crs class with Personnage attribute
class Crs(Personnage):

    print("-->CRS s'avance<--\n")
    name = "CRS"
    pv = Personnage.pv + 20
    pa = Personnage.pa + 10
    nbVictory = 0

    #Create function to know if Crs can be attack Manifestant or himself
    def fail(self):

        print("\tXxX Le CRS attaque... \n")
        randFail = random.randint(0, 4)
        if randFail == 0:
            atk = self.attack()
            print("\t ...et se fait " + str(atk) + " points de degats XxX\n")
            self.pv -= atk
            print("\tIl lui reste " + str(self.pv) + " PV\n")
            return 0

        else:
            print("\t ...et reussit son coup XxX\n")
            atk = self.attack()
            print("\t Il fait " + str(atk) + " point de degasts\n")
            return atk

# Create class to count Victory by Personnage
# But doesn't function because I reimplement my class after each reload and change the number of vicotry by the default value ( 0 ),
#  
# but if I try to import game class to put new value into game class
# my program bug because he initialize my import in loop 

# And with other ideas juste Manifestant win victory points

class Victory(Personnage):
    def victory(self):

        #He can't understand if my Personnage is CRS or Manifestant
        print(Personnage.name)
        if Personnage.name == Crs.name :
            Crs.nbVictory += 1
        else :
            Manifestant.nbVictory += 1
        input()

# Create function to launch program (To make fight)
class Launch(Manifestant, Crs):

    rand = random.randint(0,1)
    first = False

    # Random number to know who is Joueur1 and Joueur2
    if rand == 0:

        j1 = Manifestant()
        j2 = Crs()
        first = True

    else :  

        j1 = Crs()
        j2 = Manifestant()

    # While no Personnage have pv under or equal 0, continue fight
    while j1.pv > 0 and j2.pv > 0 :
        system('cls')
        print("================================================================================\n")
        print(j1.name + " : " + str(j1.pv) + "PV | " + j2.name + " : " + str(j2.pv) + " PV\n")
        print("================================================================================\n")

        #If Manifestant begin
        if first == True :

            #Stop loop if pv's Personnage have under 0
            if j1.pv <= 0 or j2.pv <= 0 :
                break
            print("*** C'est au tour de " + j1.name + " ***\n")
            j1.potion()
            atk = j1.atk()
            print("\t" + j1.name + " attaque et fait " + str(atk) + " point de degats")
            j2.pv -= atk
            print("\tIl reste " + str(j2.pv) + " à " + j2.name + "\n")
            print("------------------------------------------------------------\n")
            #Stop loop if pv's Personnage have under 0
            if j1.pv <= 0 or j2.pv <= 0 :
                break
            print("*** C'est au tour de " + j2.name + " ***\n")
            atk = j2.fail()
            j1.pv -= atk
            print("\tIl reste " + str(j1.pv) + " PV à " + j1.name + "\n")
            print("------------------------------------------------------------\n")
            input()
            system('cls')
            
        #If Crs begin
        else :

            #Stop loop if pv's Personnage have under 0
            if j1.pv <= 0 or j2.pv <= 0 :
                break
            print("*** C'est au tour de " + j1.name + " ***\n")
            atk = j1.fail()
            j2.pv -= atk
            print("Il reste " + str(j2.pv) + " PV à " + j2.name + "\n")
            print("------------------------------------------------------------")
            #Stop loop if pv's Personnage have under 0
            if j1.pv <= 0 or j2.pv <= 0 :
                break
            print("C'est au tour de " + j2.name + "\n")
            j2.potion()
            atk = j2.atk()
            j1.pv -= atk
            print("Il reste " + str(j1.pv) + " PV à " + j1.name + "\n")
            print("------------------------------------------------------------")
            input()
            system('cls')
            
            
    #When one Personnage have pv under 0
    #If j1 is dead, j2 win 
    if j1.pv <= 0 :
        print("\t*.* " + j2.name + " gagne le combat *.*\n")

        #Add one victory
        j2.nbVictory += 1
    
    elif j2.pv <= 0 :
        print("\t*.* " + j1.name + " gagne le combat *.*\n")

        #Add one victory
        j1.nbVictory += 1
    else : 
        print("Bizzare...")
    
    


