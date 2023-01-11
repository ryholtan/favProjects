print("""


""")
print("""Hello, thank you for playing this 'game'. In order to play choose
one of the options in all caps after every statement. 

I think you will find that your decisions become your reality.
Please, be warned, you may never stop playing.""")
print()
#################### Does the user join the adventure? if not, they can have the option again
while input("If you dare, please enter 'yes', otherwise please go away. ").lower() != "yes":
    print("You have two choices my friend.")
    print()
else:
    print()
    print("""You hear men yelling, waves crashing, and you smell salt in the air.
You see a man standing over you wearing a ring in his nose and a red jacket with a
sword at his waist sharp enough to cut with a brush. You seem to be lying on your 
back looking up at him. He's shouting something at you. 'Roberts! Get off your caboose
and pick up your swab! Get back to work you scallywag!' """)
print()
####################### Scene A1 TRIP OR SORRY
scene_a_1 = None
while scene_a_1 != "trip" and scene_a_1 != "sorry":
    scene_a_1 = input("""Two ideas come to your mind: Reach over and TRIP the man yelling at you or 
get up and grab the swab while you say SORRY. Which do you choose? """).lower()
    print("""

    """)
else:
    ####scene a1 // TRIP
    if scene_a_1 == "trip":
        print("""You reach out and grab his foot as he looks away. He stumbles back and falls
hitting his head hard on the way down. He is out cold and no one seems to have
noticed you are the culprit.""")
        print()
        ########### Scene A //trip> SWABBING OR TELL OR JUMP
        scene_a = None
        while scene_a != "swabbing" and scene_a != "tell" and scene_a != "jump":
            scene_a = input("""Do you: get up and start SWABBING, go TELL someone, or run to the edge
of the ship and JUMP off? """).lower()
            print("""
            
            """)
        else:
            #####scene a //trip> SWABBING
            if scene_a == "swabbing":
                print("""You start swabbing as if nothing has happened. After dinner you start to 
wonder about the man.""")
                print()
                ######## Scene B //trip>swabbing> ASK OR GO
                scene_b = None
                while scene_b != "ask" and scene_b != "go":
                    scene_b = input("Do you ASK your bunkmate about the situation or GO looking for information? ").lower()
                    print("""
                    
                    """)
                else:
                    #####scene b //trip>swabbing> ASK
                    if scene_b == "ask":
                        print("""You ask your bunkmate Jack for his insight to the situation, careful
to leave out the part that you tripped the man. Jack tells you that the man that
'fell' today was the first mate and some say he has lost his memories.""")
                        print("""
                        
                        """)
                    #####scene b //trip>swabbing> GO
                    elif scene_b == "go":
                        print("""As you walk around, you happen by the infirmatory while the Dr. is
talking. You learn that the man you tripped earlier today is the first mate
and he doesn't remember who he is.""")
                        print("""
                        
                        """)
            #####scene a //trip> TELL
            elif scene_a == "tell":
                print("""You run over to the next person you see and explain the situation. After many
'why's and 'how's, the person you tell finally decides to get some help. You help carry the 
unconcious man to the infirmitory.""")
                print()
                ######### SCENE B //trip>tell> WAIT OR GO
                scene_b = None
                while scene_b != "wait" and scene_b != "go":
                    scene_b = input("Do you: WAIT for the man to wake or GO eat dinner? ").lower()
                    print("""
                        
                        """)
                else:
                    #####scene b //trip>tell> WAIT
                    if scene_b == "wait":
                        print("""The man wakes up and looks at you. 'Where am I?' he says.""")
                        print()
                        ###### SCENE C //trip>tell>wait> TELL OR BASH
                        scene_c = None
                        while scene_c != "tell" and scene_c != "bash":
                            scene_c = input("""Do you TELL him what you know or pick up something heavy and BASH 
him to see if he will go back to sleep? """).lower()
                            print("""
                            
                            """)
                        else:
                            #####scene c //trip>tell>wait> TELL
                            if scene_c == "tell":
                                print("You tell the man what you know.")
                                print("""
                            
                                """)
                            #####scene c //trip>tell>wait> BASH
                            elif scene_c == "bash":
                                print("You pick up the lantern beside the bed and hit him over the head.")
                                print("""
                            
                                """) 
                    #####scene b //trip>tell> GO                       
                    elif scene_b == "go":
                        print("""As you walk out of the room, you hear mumblings from the man.""")
                        print()
                        ##### SCENE C //trip>tell>go> SMILE OR ACT
                        scene_c = None
                        while scene_c != "smile" and scene_c != "act":
                            scene_c = input("""You find where you can grab some dinner, everyone is talking about
the incident today. As you walk into the chow hall everyone goes quiet. Do you: SMILE 
and wave, wondering why you ever decided to play this game. Or do you ACT like you forgot 
something and run back out of the room? """).lower()
                            print("""
                            
                            """)
                        #####scene c //trip>tell>go> SMILE
                        else:
                            if scene_c == "smile":
                                print("You smile and wave like a weirdo.")
                                print("""
                            
                                """)
                            ####scene c //trip>tell>go> ACT
                            elif scene_c == "act":
                                print("You run from the room holding your head with one hand.")
                                print("""
                            
                                """)
            #####scene a //trip> JUMP
            elif scene_a == "jump":
                print("""You get up and sprint to the edge of the ship while others stare at you like you're
mad. As you place your last step and look down while all of your momentum is carrying you forward
you remember you don't know how to swim....""")
                print("""
                    
                    """)
    #####scene a1 // SORRY
    elif scene_a_1 == "sorry":
        print("""As you grab your swab and bucket, you realize your head is throbbing. The man tells you
how he saw you slip as the ship summited a large swell. As you get back to work, a loud bell rings
in your ears, exaspirating your head pain. 'Grog and grub!' is being hollared by a thick accent just
below deck. Your stomach starts to rumble.""")
        print()
        ##### SCENE 1 //sorry> FOLLOW OR WAIT OR JUMP
        scene_1 = None
        while scene_1 != "follow" and scene_1 != "wait" and scene_1 != "jump":
            scene_1 = input("""Do you: FOLLOW everyone else below deck, WAIT for everyone to leave
so yo can explore, or run to the edge of the ship and JUMP off? """).lower()
            print("""
                    
                    """)
        else:
            #####scene 1 //sorry> FOLLOW
            if scene_1 == "follow":
                print("""You follow everyone else downstairs and, amongst the frenzy, you realize the guy that
was standing above you is the first mate and that means he is pretty much in charge of everyone
except the captain.""")
                print()
                #### SCENE 2 //sorry>follow> FAMILIAR OR ALONE
                scene_2 = None
                while scene_2 != "familiar" and scene_2 != "alone":
                    scene_2 = input("Do you: sit by a FAMILIAR face or sit ALONE? ").lower()
                    print("""
                        
                        """)
                else:
                    #####scene 2 //sorry>follow> FAMILIAR
                    if scene_2 == "familiar":
                        print("""You take a seat next to one of the crew that looks most familiar to you
you realize he is your bunkmate Jack. You two share some laughs and stories.""")
                        print("""
                        
                        """)
                    #####scene 2 //sorry>follow> ALONE
                    elif scene_2 == "alone":
                        print("""You take your seat at the least crowded table. As you eat, you notice some of 
the crew pointing at you and whispering. It seems they know something you don't.""")
                        print("""
                        
                        """)
            #####scene 1 //sorry> WAIT
            elif scene_1 == "wait":
                print("""You wait for all the others to meander down the wooden stairs, as you look around
you see everything you would expect to see on a ship in the middle of the ocean, except 
you realize there are no electronics anywhere.""")
                print()
                ###### SCENE 2 //sorry>wait> GO OR SIT
                scene_2 = None
                while scene_2 != "go" and scene_2 != "sit":
                    scene_2 = input("""Do you: GO below deck to see what is on the menu or SIT topside and 
watch the sunset? """).lower()
                    print("""
                        
                        """)
                else:
                    ######scene 2 //sorry>wait> GO
                    if scene_2 == "go":
                        print("""You head down and on the way you pass the man from before. He asks you why you took
so long to go below.""")
                        print("""
                        
                        """)
                    #####scene 2 //sorry>wait> SIT
                    elif scene_2 == "sit":
                        print("""The captain sees you while doing his rounds. He says ''Ya'd bettah get down thare
bafore yah lose yer chance ta eat''.""")
                        print("""
                        
                        """)
            ###### scene 1 //sorry> JUMP
            elif scene_1 == "jump":
                print("""You get up and sprint to the edge of the ship while others stare at you like you're
mad. As you place your last step and look down, while all of your momentum is carrying you forward,
you see sharp triangular fins breaking the top of the water.""")
                print()
                ####SCENE 2 //sorry>jump> REACH OR PLUNGE
                scene_2 = None
                while scene_2 != "reach" and scene_2 != "plunge":
                    scene_2 = input("Do you: REACH for a rope hanging off the side of the hull or PLUNGE into the water full force? ").lower()
                    print()
                else:
                    #####scene 2 //sorry>jump> REACH
                    if scene_2 == "reach":
                        print("""You reach your arm out and grab the first thing you touch, your gravitational
force coupled with the strength of your grip causes your left shoulder to pull from its
socket, you keep falling to the water and now it seems even harder to swim.""")
                        print()
                    ####scene 2 //sorry>jump> PLUNGE
                    elif scene_2 == "plunge":
                        print("""You hit the water hard, right next to one of the fins you saw. You notice these
creatures are huge but they have no interest in you right now. As you look under the water
you see a pack of about 5 dolphins attacking the large shark-like creatures you
identified above the water.""")
                        print()
                print("""
                    
                    """)