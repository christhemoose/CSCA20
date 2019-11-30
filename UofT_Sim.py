print("This game is rated 19+, if you're under the age \nof 19 play with parent supervison")
print("Welcome to the UofT simulator")
answer = input("To Begin Enter Your Name: ")
if(answer == "Brian"):
        print("Message to Brian:")
        print("Hey Brian, this feature was added just \nin case you were playing \nall inputs must be typed in quotations \nand the answer to the first question is plane departs at 630 \njust in case you get stuck \nrestart the game and type your name with lowercase to start")
        exit()
print("Welcome " + answer)
print("Before we begin please note that this game was designed by students for \nenjoyment purposes and in no way expresses the views and or expressions of UofT as a whole") 
print("your goal of this game is to complete 1 day as a UofT student, \nif at any point your GPA is below 1.2 you will be placed on academic probation \nAlso if your mental health is 0 \nyou will lose")
while(not(answer == "start")):
        print("to begin Simulation write: start")
        answer = input(": ")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("Created by CHRIS & AZAN") 
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
my_GPA = 4.0 
mental_health = 10

print("DAY 1")
print("*alarm sound* ITS 8:00 WAKE UP")
answer = input("select one of the following: \nwake up \nhit snooze \n: ")
if(answer == "wake up"): 
        print("get ready for class and leave the house")
        answer = input("select a mode of transportation: \nuber \nwalk \nTTC \n: ")
        if(answer == "walk"):
                print("You're late for Test you fail")
                exit()
        else: 
                print("Arrive at School: ")
                answer = input("Go to Timmies \nGo to Starbucks \n: ")
                if(answer == "Go to Starbucks"):
                        answer = input("patiently wait in line \ndance in line \n: ")
                        if(answer == "dance in line"):
                                print("bumped someone in front of you")
                                answer = input("apologize \nget into fight \nblame it on someone else \n: ")
                                if(answer == "get into fight"):
                                        print("Go to Dean's Office")
                                        print("You've been expelled for breaking code of conduct line D page 4 of the UofT handbook")
                                        exit()
                                else:
                                        print("Wait in line")
                                        answer = input("What's your order: \nThe Seal Club Sandwich \nCoffee \n: ")
                                        if(answer == "The Seal Club Sandwich"):
                                                print("Animal rights actvists attack you, you've been stabbed")
                                                exit()
                                        else:
                                                Barista_name_1 = input("Give barista your name: ")
                                                import random
                                                list = ["DaKwan","FlaxaWaxon","Jermaine","Tytheritrix"]
                                                Barista_name_2 = random.choice(list)
                                                print("Coffee for " + Barista_name_2)
                                                Death_by_straw = input("Grab straw \nSave turtles \n: ")
                                                print("\n ")
                                                print("\n ")
                                                print("\n ")
                                                print("\n ")
                                                print("\n ")
                                                print("\n ")
                                                print("walk to class")
                                                print("Enter classroom")
                                                if(Death_by_straw == "Grab straw"): 
                                                        print("*a lady approaches you* \nHey I saw you grab a straw from Starbucks")
                                                        Starbucks_response = input(": ") 
                                                        if(Starbucks_response == "I am sorry"):
                                                                print("Its Okay just Don't let it happen again") 
                                                        else:
                                                                print("YOU'VE BEEN BEATEN WITH A CLUB")
                                                                print("Game Over")
                                                                exit()
                        else:
                                print("Wait in line")
                                answer = input("What's your order: \nThe Seal Club Sandwich \nCoffee \n: ")
                                if(answer == "Seal Club Sandwich"):
                                        print("Animal rights actvists attack you, you've been stabbed")
                                        exit()
                                else:
                                        Barista_name_1 = input("Give barista your name: ")
                                        import random
                                        list = ["DaKwan","FlaxaWaxon","Jermaine","Tytheritrix"]
                                        Barista_name_2 = random.choice(list)
                                        print("Coffee for " + Barista_name_2)
                                        Death_by_straw = input("Grab straw \nSave turtles \n: ")
                                        print("\n ")
                                        print("\n ")
                                        print("\n ")
                                        print("\n ")
                                        print("\n ")
                                        print("\n ")
                                        print("walk to class")
                                        print("Enter classroom")
                                        if(Death_by_straw == "Grab straw"): 
                                                print("*a lady approaches you* \nHey I saw you grab a straw from Starbucks")
                                                Starbucks_response = input(": ") 
                                                if(Starbucks_response == "I am sorry"):
                                                        print("Its Okay just Don't let it happen again") 
                                                else:
                                                        print("YOU'VE BEEN BEATEN WITH A CLUB")
                                                        print("Game Over")
                                                        exit()
                       
                else:
                        answer = input("patiently wait in line \ndance in line \n: ")
                        if(answer == "dance in line"):
                                print("bumped someone in front of you")
                                answer = input("apologize \nget into fight \nblame it on someone else \n: ")
                                if(answer == "get into fight"):
                                        print("Go to Dean's Office")
                                        print("You've been expelled for breaking code of conduct line D page 4 of the UofT handbook")
                                        exit()
                                else: 
                                        print("Wait in line")
                                        print("*lady yells* NEXT IN LINE") 
                                        answer = input("NAIZ YOUR BEAK \nComing \ndont say nuthin \n: ")
                                        print(answer) 
                                        answer = input("What do you want? \nIce coffee \nDD \nIce Cap \n: ")
                                        print("Here's your " + answer)
                                        print("Enter classroom")
                        else: 
                                print("Wait in line")
                                print("*lady yells* NEXT IN LINE") 
                                answer = input("NAIZ YOUR BEAK \nComing \ndont say nuthin \n: ")
                                print(answer) 
                                answer = input("What do you want? \nIce coffee \nDD \nIce Cap \n: ")
                                print("Here's your " + answer)
                                print("Enter classroom")





else:
        print("*One hour later*")
        print("You dash to school in the whipski")
        answer = input("Run to class \nWalk to class \n: ")
        if(answer == "Run to class"):
                print("You arrive on time")
                
        else:
                print("You're 20 minutes late")
                mental_health -= 1
                print("you feel anxious for being late \nand suffer a minor anxeity attack \nMental Health = " + str(mental_health))
                print("Enter classroom")
right_answer = "plane departs at 630"
print("OK class lets get started, my apologies for being late, \nWelcome to DecrpytionA10")
attention_class = input("Pay attention \ngo on phone \nTalk to friends \n: ")
if(attention_class == "Pay attention"):
        print("the answer is 3 words all lower case followed by the integer given")
if(attention_class == "Talk to friends"):
        import random
        list = ["Samir: nice shirt", "Trisha: How was your weekend?", "Cris: Hey man you seen the new Riverdale"]
        Friend_comment = random.choice(list)
        print(Friend_comment)
while(not(attention_class == "Pay attention")):
        attention_class = input("Pay attention \nTalk to friends \n: ")
        if(attention_class == "Talk to friends"):
                import random
                list = ["Samir: nice shirt", "Trisha: How was your weekend?", "Cris: Hey man you seen the new Riverdale"]
                Friend_comment = random.choice(list)
                print(Friend_comment)
print("Now its time for some class participation!")
print("If question is unknown select: \nI Don't Know ")
Q_1 = input("decrypt the code: (1a1b1c1d1e1f2a2b2c2d2e2f3a3b3c.... = 630) \n: ")
if(Q_1 == right_answer): 
        print("Correct")
while(not(Q_1 == right_answer)):
        if(Q_1 == "I Don't Know"):
                break
        print("Wrong answer")
        my_GPA -= 0.2 
        mental_health -= 1
        print("Mental Health: " + str(mental_health))
        print(my_GPA) 
        Q_1 = input("decrypt the code: (1a1b1c1d1e1f2a2b2c2d2e2f3a3b3c.... = 630) \n: ")
        if(mental_health == 0):
                print("you find your self on the roof of HL feeling empty inside")
                print("\n")
                endgame = input("endgame \nseek help \n: ")
                if(endgame == "endgame"):
                        print("later that day your outlook recived an email: \nTo UofT Students: \nUnfortunatley we suffered a great tragedy today \nfor mental health options please find help \nYour Friend, \nDesmond Pouyat")
                        exit()
                else:
                        print("you saught out help from peers and family \nAnd decided its best to take a year off")
                        exit()

print("\n ")
print("\n ")
print("\n ")
print("\n ")
print("\n ")
print("\n ")
print("\n ")
print("It is now 11 am")
lunch_option = input("Go out for lunch \nHangout with friends \n: ")
if(lunch_option == "Hangout with friends"):
        mental_health += 2 
        print("talked about how dumb, Marco's bow tie looks")
        print("Mental Health = " + str(mental_health))
else:
        choose_food = input("KFC \nSubway \n: ") 
        print("Got " + choose_food)
        lunch_scenery = input("eat in SC \neat in BV \neat in library \n: ") 
        if(lunch_scenery == "eat in library"):
                print("approach library with food")
                lib_sneak = input("hide food in jacket \ndon't hide it \n: ")
                if(lib_sneak == "don't hide it"):
                        print("Walked in the library \nLIKE A BOSS")
                        print("*Librarian sees you* \nShe kicks you out of the Library")
                        print("You ate your lunch alone in the hallway")
                        mental_health -= 2
                        print("Your Mental Health is " + str(mental_health))
                        if(mental_health == 0):
                                print("you find your self on the roof of HL feeling empty inside")
                                print("\n")
                                endgame = input("endgame \nseek help \n: ")
                                if(endgame == "endgame"):
                                        print("later that day your outlook recived an email: \nTo UofT Students: \nUnfortunatley we suffered a great tragedy today \nfor mental health options please find help \nYour Friend, \nDesmond Pouyat")
                                        exit()
                                else:
                                        print("you saught out help from peers and family \nAnd decided its best to take a year off")
                                        exit()
                else:
                        print("Entered the Library Study room enjoyied lunch with friends")
                        mental_health += 1
                        print("Mental Health: " + str(mental_health))
        else:
                print("ate lunch")
print("\n ")
print("\n ")
print("\n ")
print("*Its 1:00pm class starts in 10min*")
print("Friends ask you to skip class")
skip_class = input("Go to class \nSkip class with friends \n: ")
if(skip_class == "Skip class with friends"):
        print("Friend 1: Sweet lets go walk around. \nFriend 2: Ya lets see if anyones around")
        print("*Walked around for 20 min, ended up in the valley*")
        print("*Seen a shady man lurking in the bush*")
        shady_man = input("Talk to shady man \nRun back to school \n: ")
        if(shady_man == "Talk to shady man"):
                print("Shady man: Hey kids, they call me Scratch, but thats not me. \nFriend 1: That's cool man, what are you doing out here? \nScratch?: Oh you know, chillin with my buds *Hysterical laughter* you want to join me. \nPhone: *Ringing*")
                print("*You're mom is calling*")
                phone_call = input("Answer phone \nPress ignore \n: ")
                if(phone_call == "Press ignore"): 
                        print("Scratch: so you guys in or out")
                        print("Friends: Um that's not for us we're children of Allah")
                        accept_drugs = input("Take the drugs \nDon't take drugs \n: ")
                        if(accept_drugs == "Take the drugs"):
                                print("*friends off it*")
                                print("*You Take A Fat Toke*")
                                mental_health += 5
                                print("Scratch: Aight man EZ")
                                print("*You head back to school Feeling good*")
                                print("*Two hours later, High wore off you feel like trash*")
                                mental_health -= 8
                                print("Mental Health: " + str(mental_health))
                                if(mental_health == 0):
                                        print("you find your self on the roof of HL feeling empty inside")
                                        print("\n")
                                        endgame = input("endgame \nseek help \n: ")
                                        if(endgame == "endgame"):
                                                print("later that day your outlook recived an email: \nTo UofT Students: \nUnfortunatley we suffered a great tragedy today \nfor mental health options please find help \nYour Friend, \nDesmond Pouyat")
                                                exit()
                                        else:
                                                print("you saught out help from peers and family \nAnd decided its best to take a year off")
                                                exit()
                        else:
                                print("Sorry man not for me")
                                print("*Walked back to school with friends*")
                else:
                        print("*talk to Mom about school*")
                        print("*Scratch walks away*")
                        print("*Walked back to school with friends*")
        else:
                print("*You ran back to school with friends away from Shady man*")
else:
        right_answer_2 = "Quartz"
        print("OK class lets get started, \nWelcome to EESB15")
        attention_class = input("Pay attention \ngo on phone \nTalk to friends \n: ")
        if(attention_class == "Pay attention"):
                print("the answer is: Quartz")
        while(not(attention_class == "Pay attention")):
                attention_class = input("Pay attention \ngo on phone \nTalk to friends \n: ")
                if(attention_class == "Talk to friends"):
                        import random
                        list = ["Samir: nice shirt", "Trisha: How was your weekend?", "Cris: Hey man you seen the new Riverdale"]
                        Friend_comment = random.choice(list)
                        print(Friend_comment)
        print("Now its time for some class participation!")
        print("If question is unknown select: \nI Don't Know ")
        Q_2 = input("Which of the following is the most felsic: \nBasalt \nRhyolite \nQuartz \n: ")
        if(Q_2 == right_answer_2): 
                print("Correct")
        while(not(Q_2 == right_answer_2)):
                if(Q_2 == right_answer_2): 
                        print("Correct")
                        break
                if(Q_2 == "I Don't Know"):
                        break
                print("Wrong answer")
                my_GPA -= 0.2 
                mental_health -= 1
                print(my_GPA) 
                Q_2 = input("Which of the following is the most felsic: \nBasalt \nRhyolite \nQuartz \n: ")
                if(mental_health == 0): 
                        print("you find your self on the roof of HL feeling empty inside")
                        print("\n")
                        endgame = input("endgame \nseek help \n: ")
                        if(endgame == "endgame"):
                                print("later that day your outlook recived an email: \nTo UofT Students: \nUnfortunatley we suffered a great tragedy today \nfor mental health options please find help \nYour Friend, \nDesmond Pouyat")
                                exit()
                        else:
                                print("you saught out help from peers and family \nAnd decided its best to take a year off")
                                exit()
                if(my_GPA == 1.2):
                        print("You have been placed on academic probation")
                        exit()

print("\n ")

print("Class over")
gym_1 = input("Go home \nGo to Panam \n: ")
if(gym_1 == "Go to Panam"):
        print("Arrived at Panam")
        change_room = input("Leave phone in locker \nBring phone with you \n: ")
        if(change_room == "Bring phone with you"):
                print("walked into weights room") 
                print("while working out, your phone was found \ncrushed under a 45LBS dumbell. ")
                print("*went home*") 
        else: 
                print("*left phone in locker*")
                workout_setting = input("Go to weights room \nGo to pool \n: ")
                if(workout_setting == "Go to weights room"):
                        print("Paul: Hey man, have a good workout")
                        workout_1 = input("chest day \nleg day \nback day \n: ")
                        if(workout_1 == "chest day"):
                                print("had a awesome bench set, chest is poppin")
                        if(workout_1 == "back day"):
                                print("Murdered some deadlifts, and rows")
                        if(workout_1 == "leg day"):
                                print("Squats where on point today")
                        print("*you feel exhausted*")
                        print("*You Called Eman for a ride home*")
                        
                else:
                        print("hit lane swim for an hour \nthen packed up")
else:
        print("decided to go home its been a long day")
        ride_home = input("ask mom for a ride home \nTTC \nUBER \n: ")
        if(ride_home == "TTC"):
                print("Had a nice bus ride home")
        else: 
                print("had a nice drive home")
final_GPA = my_GPA
print("My final GPA is: " + str(final_GPA)) 
my_health = mental_health
print("My Mental Health: " + str(my_health))
print("Congratulations, \nYou have completed Part 1 of 7, of The UofT Simulator \nStay tuned for other games by us like, *What Really Happened to epstien*") 