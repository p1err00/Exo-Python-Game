import Class_TP
import random
import os
import importlib
from os import system

class Game:
    
    a = "o"

    #While user use "o" in inout, reload game
    while a == "o" :

        
        #Launch game
        Class_TP.Launch

        #Instancie nbVictory of each Personnage
        nbVictoryCrs = Class_TP.Crs.nbVictory
        nbVictoryManifestant = Class_TP.Manifestant.nbVictory

        #Print number of victory (but doesn't work )
        print("\t*.*Victoire CRS : " + str(Class_TP.Crs.nbVictory) + " | " + "Victoire Manifestant : " + str(Class_TP.Manifestant.nbVictory) + "*.*\n")
        print("================================================================================\n")
        a = input("\tRecommencer ? [o/n]")
        print("================================================================================\n")


        #Stock victory of each Personnage 
        nbVictoryCrs += nbVictoryCrs
        nbVictoryManifestant += nbVictoryManifestant
        system('cls')

        #Know if reload or not
        if a == "o" :
            importlib.reload(Class_TP)
            
            Class_TP.Launch

            nbVictoryCrs += nbVictoryCrs
            nbVictoryManifestant += nbVictoryManifestant
        else : 
            a = "z"
        
            

        
