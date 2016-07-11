"""Module that holds Scene classes for use in the text adventure game.
    
    Classes:
        Scene - The base class for each scene in the game
        Death - Scene for when player dies
        Finished - Scene for when game is completed
        Central_Corridor - Scene we typically start in
        Armory - Scene in the laser weapon armory
        Escape_Pod - Scene where player escapes
        Bridge -  Scene where bridge is taken
"""

#-- Import Statements --#
import sys
from random import randint

#-- Class Definitions --#
class Scene(object) :
    """A base class for each scene in the game."""

    # Abstract method that will be implemented in all subclasses
    def enter(self) :
        """Not implemented. Subclass and provide functionality.

        Returns:
            the name of the next scene in the players path 
        """
        raise NotImplementedError

    def __eq__(self, other) :
        # Just check if type of Scene are the same.
        return type(self) == type(other)


class Death(Scene) :
    """Class for death scenes in the text adventure game."""

    quips = [
        "You died. You kinda suck at this.",
        "This isn't your day kid, you're dead.",
        "I can not believe you managed to die like that.",
        "You should just stop trying."
    ]

    def enter(self) :
        print Death.quips[randint(0,len(Death.quips) - 1)]
        sys.exit(0)

class Finished(Scene) :
    """Class for final scene when user wins and ends the game."""

    def enter(self) :
        print "You have won! Good job!"
        return "finished"

class Central_Corridor(Scene) :
    """Class for scene that takes place in the central corridor."""

    def enter(self) :
        print 'The Gothons of planet Percal #25 have invaded your ship and destroyed'
        print 'your entire crew. You are the last surviving member and your last'
        print 'mission is to get the neutron destruct bomb from the Weapons Armory,'
        print 'put it in the Bridge, and blow the ship up after getting into an '
        print 'escape pod.'
        print '\n'
        print 'You\'re running down the central corridor to the armory when a'
        print 'Gothon jumps out. He\'s blocking the door to the armory and'
        print 'about to pull a weapon to blast you with.'

        action = raw_input('>')

        if action == 'shoot!' :
            print "Quick on the draw you yank out your blaster and fire it at the Gothon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "off your aim.  Your laser hits his costume but misses him entirely.  This"
            print "completely ruins his brand new costume his mother bought him, which"
            print "makes him fly into an insane rage and blast you repeatedly in the face until"
            print "you are dead. Then he eats you."
            return 'death'
        elif action == 'dodge!' :
            print "Like a world class boxer you dodge, weave, slip and slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Gothon stomps on"
            print "your head and eats you."
            return 'death'
        elif action == 'tell a joke' :
            print "Lucky for you they made you learn Gothon insults in the academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
            print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
            print "While he's laughing you run up and shoot him square in the head"
            print "putting him down, then jump through the Weapon Armory door."
            return 'armory'
        else :
            print 'DOES NOT COMPUTE'
            return 'central_corridor'
    

class Armory(Scene) :
    """---TODO---"""
    
    def enter(self) :
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding.  It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its container.  There's a keypad lock on the box"
        print "and you need the code to get the bomb out.  If you get the code"
        print "wrong 10 times then the lock closes forever and you can't"
        print "get the bomb.  The code is 3 digits."

        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        print "Code: %s" % code
        guess = raw_input('[keypad]>')
        num_guesses = 1

        while guess != code and num_guesses < 10 :
            print "BZZZZEEDD!"
            guess = raw_input('[keypad]>')
            num_guesses += 1

        if guess == code :
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return "bridge"
        else :
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."
            return "death"
    

class Escape_Pod(Scene) :
    """Class for scene that takes place on the escape pod."""
    
    def enter(self) :
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes.  It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference.  You get to the chamber with the escape pods, and"
        print "now need to pick one to take.  Some of them could be damaged"
        print "but you don't have time to look.  There's 5 pods, which one"
        print "do you take?"

        working_pod = randint(1,5)
        print "Working pod #: %s" % working_pod
        pod_choice = raw_input('[pod #]>')

        if int(pod_choice) == working_pod :
            print "You jump into pod %s and hit the eject button." % pod_choice
            print "The pod easily slides out into space heading to"
            print "the planet below.  As it flies to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the Gothon ship at the same"
            print "time.  You won!"
            return 'finished'
        else :
            print "You jump into pod %s and hit the eject button." % pod_choice
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'death'

    

class Bridge(Scene) :
    """Class for scene that takes place on the bridge."""
        
    def enter(self) :
        print "You burst onto the Bridge with the netron destruct bomb"
        print "under your arm and surprise 5 Gothons who are trying to"
        print "take control of the ship.  Each of them has an even uglier"
        print "clown costume than the last.  They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."

        action = raw_input('>')

        if action == "throw the bomb" :
            print "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door.  Right as you drop it a"
            print "Gothon shoots you right in the back killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off."
            return 'death'
        elif action == "slowly place the bomb" :
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock so the Gothons can't get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off this tin can."
            return 'escape_pod'
        else :
            print "DOES NOT COMPUTE!"
            return 'bridge'