import threading

def timout_input(seconds=10):
    print("Enter the correct option a/b/c/d:")
    timer = threading.Timer(seconds, print, ["Time's up!\n"])
    timer.start()
    try:
            user_input = input(f"You have {seconds} seconds: \n")
    except Exception as e:
            print(f"Error: {e}")
            user_input = None
    finally:
            timer.cancel()  

    return user_input


Questions= [
    [   "What is the unit of electric current?", "a.Volt","b.Watt","c.Ampere","d.Ohm","c" ],
    [   "Which gas is produced when hydrochloric acid reacts with zinc?", "a.Oxygen", "b.Hydrogen", "c.Carbon dioxide", "d.Nitrogen", "b"],
    [   "What is the basic unit of the nervous system?", "a.Cell", "b.Tissue", "c.Neuron", "d.Organ", "c"],
    [   "The pH of a neutral solution at 25°C is:", "a.7", "b.0", "c.14", "d.10", "a"],
    [   "Mendel is known for his work on which plant?", "a.Maize", "b.Pea", "c.Wheat", "d.Rice", "b"],
    [   "Which of the following is true about concave lenses?", "a.They converge light rays.", "b.They diverge light rays.", "c.They form only real images.", "d.They magnify images.", "b"],
    [   "Which of the following organisms can perform photosynthesis?", "a.Fungi", "b.Algae", "c.Viruses", "d.Animals", "b"],
    [   "In a parallel circuit, the total resistance is:", "a.Equal to the sum of individual resistances.", "b.More than the largest resistance.", "c.Less than the smallest resistance.", "d.Equal to the average of all resistances.", "c"],
    [   "Which of the following is a strong acid?", "a.HCl (Hydrochloric acid)", "b.CH3COOH (Acetic acid)", "c.H2CO3 (Carbonic acid)", "d.NH4OH (Ammonium hydroxide)", "a"],
    [   "Which of the following is not a part of the human digestive system?", "a.Stomach", "b.Lungs", "c.Small intestine", "d.Liver", "b"],
    [   "What is the primary gas found in the Earth's atmosphere?", "a.Oxygen", "b.Nitrogen", "c.Carbon dioxide", "d.Argon", "b"],
    [   "Which of the following is an example of a chemical change?", "a.Melting of ice", "b.Rusting of iron", "c.Boiling of water", "d.Crushing of a can", "b"],
    [   "What is the function of red blood cells?", "a.Transporting oxygen", "b.Fighting infections", "c.Clotting blood", "d.Transmitting nerve impulses", "a"],
    [   "Which type of energy is stored in a stretched rubber band?", "a.Kinetic energy", "b.Thermal energy", "c.Potential energy", "d.Sound energy", "c"],
    [   "Which planet is known as the 'Red Planet'?", "a.Venus", "b.Mars", "c.Jupiter", "d.Saturn", "b"]
]
while(1):
    x=input("Welcome to KBC!! You wish to recieve 1 crore TK by answering 15 questions?\nPress Y for yes and N for No\n\n(NOTE: If you answer a question correctly, you will earn money and the game will continue. However, if your answer is incorrect, the game will end. There are certain safe points where, even if you answer incorrectly, you will still receive the money you have earned up to that point.)\n")
    if x=="Y":
        money=0
        user_input=""
        for i in range(len(Questions)):
            print( i+1,f"{Questions[i][0],Questions[i][1],Questions[i][2],Questions[i][3],Questions[i][4]}\n")

            user_input= timout_input()

            if user_input==Questions[i][5]:
                print("Congratulations. Correct Answer.")
                if i == 2 or i==0:
                    money=money+1000
                
                elif i==3:
                    money=money+2000

                elif i==11:
                    money=money+610000

                else:
                    money=money*2
                
                if i==4 or i==9:
                    print("\nYou are at Safe Point")
                    
                print("You recieved: Tk.",money,"\n")

            else:
                print("Wrong Answer.\n")
                if i>=4:
                    print("\n\nBy playing this game you recieved: Tk.",money,"\n\n")
                break
    else:
        break
  