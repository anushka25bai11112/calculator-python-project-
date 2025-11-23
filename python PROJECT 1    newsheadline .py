# 1- import the random module
import random
#2- create subjects
subjects =[
    "virat kohli",
    "shahrukh khan",
    "nirmala sitharaman",
    "A mumbai cat",
    "a group of monkey",
    "prime ministed modi",
    "auto rickshaw driver from delhi",
    "insects"
]
actions=[
    "launches",
    "cancels",
    "dances with",
    "eats",
    "orders",
    "celebrates",
]
places_or_things = [
    "at red fort",
    "in mumbai local train",
    "a  plAte of samosa",
    "inside parliament",
    "at ramghar",
    "during IPL match",
    "at india gate",
]
# 3 start the headline generation loop
while True:
        subjects = random.choice(subjects)
        action = random.choice(actions)
        places_or_thing =random.choice(places_or_things)

        headline = f" BREAKING NEWS :{subjects} {action} { places_or_thing} "
        print("\n" + headline)

        user_input =input("\nDo you want another headline ?(yes/no)").strip()
        if user_input == "no":
             break
#print goodbye message
print("\n Thanks for using the fake News Headline Generator. Have a fun day")
            
        
    
    
