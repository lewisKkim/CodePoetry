import random

alive = 27

timbers = 12

print(str(alive) + " men left port")

print("Stalwart, eager, and fresh")

print("Into the howling blue yonder")

print("Casting away their fates")

print()

print("To the far North")

print()

if(random.random() < 0.3):
    print("Inauspicious was the start")
    
    print("For Seaman Dearing")
    
    print("Who dashed his brains")
    
    print("Out with a fall")
    
    print()
    
    alive -= 1
    
if(random.random() < 0.24):
    print("A sudden shock")
    
    print("Three days in")
    
    print("Seaman Briar came to")
    
    print("Buboes pocked his flesh")
    
    print("Shouts, outrage")
    
    print("Terror at infection")
    
    print("The Captain stepped in")
    
    print("Sent him home in a boat")
    
    alive -= 3
    
    print()
    
if(random.random() < 0.18) :
    print("Men tired")
    
    print("Of rations")
    
    print("And looked")
    
    print("To the sky")
    
    print()
    
    print("Saw seagulls, petrels")
    
    print("A white albatross, too")
    
    print("Gaines eyed it hungrily")
    
    print("A pot roast for tonight")
    
    print()
    
    print("With a blast")
    
    print("A bird fell")
    
    print("The men feasted")
    
    print("But one came to regret")
    
    print()
    
    alive -= 1
    
    timbers -= 5
    
print(str(alive) + " men saw their first berg")

print("The mountain of ice")

print("Inspired whoops and yelps")

print("And glares from a few")

print()

if (random.random() < 0.37) :
    print("\"Man overboard!\"")
    
    print("As the midnight storm tore at the sails")
    
    print("One sailor disappeared behind a wave")
    
    alive -= 1
    
    print("And then another")
    
    alive -= 1

if (random.random() < 0.28) :
    print("Dawn saw a sighting")
    
    print("A raft to port")
    
    print("The grateful sailor on board")
    
    print("Promised only treachery ahead")
    
    print()
    
    alive += 1
    
    timbers -= 4
    
if (alive > 24) :
    print("Stores ran dry")
    
    print("Hardtack got harder")
    
    print("Rats disappeared from the deck")
    
    print("As hunger took its grip")
    
    print()
    
    alive -= 6
    
if (random.random() < 0.33) :
    print("Camping on an outcrop")
    
    print("The seal-hunt ended in tears")
    
    print("The white bear tore at the tent")
    
    print("Bloody chunks hanging from its claws")
    
    print()
    
    alive -= 7
    
if (random.random() < 0.16) :
    print("Shrieked Prendergast")
    
    print("\"We must turn back!\"")
    
    print("To no avail")
    
    print("The captain brooked no dissent")
    
    print()
    
    alive -= 1
    
if (timbers < 5) :
    print("The ice closed in")
    
    print("Crushing the little hull")
    
    print("Locked in fast")
    
    print("Nowhere else to go")
    
    print()
    
    print("Edgar led a relief party")
    
    print("Into the empty white")
    
    alive -= 7
    
    print("Mutiny was the watchword")
    
    print("As friends turned into food")
    
    alive -= 3
    
    print()
    
    print("Sunday they found the captain")
    
    alive -= 1
    
    print("The second-to-last bullet in his brain")
    
    print()
    
    if (alive > 2) :
        print("As the last " + str(alive) + "left made their vows")
        
        print("Huddled amidst the furious dark")
        
    elif (alive == 1) :
        print("Lonely and cold")
        
        print("As I scrawl this record")
        
    else:
        print("The last of an ignoble crew")
        
        print("Defiance, arrogance")
        
        print("Leaving the quiet wreckage")
    
else :
    print("It was with four months passed")
    
    print("That finally returned home")
    
    print("That battered, broken vessel")
    
    print("No grand discovery, no celebrated profit")
    
    print("Only " + str(alive) + " hungry, skeletal lads")
    
    print("The look in their eye")
    
    print("Barely human")