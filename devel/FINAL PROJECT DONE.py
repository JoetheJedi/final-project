from selenium import webdriver


print("Pick a Genre of games by typing one of the three genres below and ill show you a list of games from that genre you might enjoy!")
print("Horror")
print("Adventure")
print("Mystery")


    



################################HORROR CODE######################################
def HORRORCODE():
    print('Here are three of my favorite horror games! Pick one of the games to see the trailer for it!')
    print('A.)Silent Hills: psychological horror')
    print('B.)Resident evil: survival horror based around zombies')
    print('C.)Allison road: Haunting!')
    print('D.)The Evil Within: psychological survival horror')
    while True:
        GameChoice=input()
        if GameChoice=="A" or GameChoice=="a" or GameChoice=="B" or GameChoice=="b" or GameChoice=="C" or GameChoice=="c" or GameChoice=="D" or GameChoice=="d":
            break
        print('Invalid choice, please choose either A B C OR D')
    if GameChoice=="A" or GameChoice=="a":
        webdriver.Firefox().get('https://www.youtube.com/watch?v=LrL8ybvDSkA')
    elif GameChoice=="B" or GameChoice=="b":
        webdriver.Firefox().get('https://www.youtube.com/watch?v=AwcU7E1TprM')
    elif GameChoice=="C" or GameChoice=="c":
        webdriver.Firefox().get('https://www.youtube.com/watch?v=Ot1-xyvE_8A')
    elif GameChoice=="D" or GameChoice=="d":
        webdriver.Firefox().get('https://www.youtube.com/watch?v=PvR7-pZh_0M')
exit

######################################ADVENTURE CODE#########################################
def ADVENTURECODE():
      print('Here are some of my favorite adventure games! Pick one that sounds interesting to see the trailer for it!')
      print('A.)Kerbal space program: Travel into space using your own selfmade spacecraft!')
      print('B.)Witcher 3: Open world Fantacy')
      print('C.)Metal Gear Solid V: Action adventure based around stealth')
      print('D.)Fallout 4: Post nuclear survival')
      while True:
          GameChoice1=input()
          if GameChoice1=="A" or GameChoice1=="a" or GameChoice1=="B" or GameChoice1=="b" or GameChoice1=="C" or GameChoice1=="c" or GameChoice1=="D" or GameChoice1=="d":
              break
          print('Invalid choice, please choose either A B C OR D')
      if GameChoice1=="A" or GameChoice1=="a":
          webdriver.Firefox().get('https://www.youtube.com/watch?v=7kTbo1wmN-w')
      elif GameChoice1=="B" or GameChoice1=="b":
          webdriver.Firefox().get('https://www.youtube.com/watch?v=c0i88t0Kacs')
      elif GameChoice1=="C" or GameChoice1=="c":
          webdriver.Firefox().get('https://www.youtube.com/watch?v=A9JV0EvCkMI')
      elif GameChoice1=="D" or GameChoice1=="d":
          webdriver.Firefox().get('https://www.youtube.com/watch?v=X5aJfebzkrM')
exit

####################################MYSTERY CODE###################################################
def MYSTERYCODE():
    print('Here are some of my favorite mystery games! Pick one that sounds interesting to see the trailer for it!')
    print('A.)La Noire: detective work')
    print('B.)Heavy Rain: Looking for you kidnapped son')
    print('C.)Murdered: Soul Suspect')
    print('D.)FireWatch: Linear mystery')
    while True:
        GameChoice2=input()
        if GameChoice2=="A" or GameChoice2=="a" or GameChoice2=="B" or GameChoice2=="b" or GameChoice2=="C" or GameChoice2=="c" or GameChoice2=="D" or GameChoice2=="d":
            break
        print('Invalid choice, please choose either A B C OR D')
    if GameChoice2=="A" or GameChoice2=="a":
        webdriver.Firefox().get('https://www.youtube.com/watch?v=skAkfQr3e-4')
    elif GameChoice2=="B" or GameChoice2=="b":
        webdriver.Firefox().get('https://www.youtube.com/watch?v=YVYiJ3VSp60')
    elif GameChoice2=="C" or GameChoice2=="c":
        webdriver.Firefox().get('https://www.youtube.com/watch?v=5CeWsTEOZYo')
    elif GameChoice2=="D" or GameChoice2=="d":
        webdriver.Firefox().get('https://www.youtube.com/watch?v=kZX3MgsRb0A')
exit
    

    
        

#################################STARTING PROGRAM##################################################




while True:
    GenreChoice=input()
    if GenreChoice=="Horror" or GenreChoice=="horror" or GenreChoice=="HORROR" or GenreChoice=="Adventure" or GenreChoice=="ADVENTURE" or GenreChoice=="adventure" or GenreChoice=="Mystery" or GenreChoice=="mystery" or GenreChoice=="MYSTERY":
        break
    print('Please choose one of the three provided Genres')

    
if GenreChoice=="Horror" or GenreChoice=="horror" or GenreChoice=="HORROR":
    HORRORCODE()
elif GenreChoice=="Adventure" or GenreChoice=="adventure" or GenreChoice=="ADVENTURE":
    ADVENTURECODE()
elif GenreChoice=="Mystery" or GenreChoice=="mystery" or GenreChoice=="MYSTERY":
    MYSTERYCODE()

    

