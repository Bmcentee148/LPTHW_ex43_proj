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
    
    quips = [
        "You died. You kinda suck at this.",
        "This isn't your day kid, you're dead.",
        "I can not believe you managed to die like that.",
        "You should just stop trying."
    ]

    def enter(self) :
        return Death.quips[randint(0,len(Death.quips) - 1)]

class Finished(Scene) :
    """---TODO---"""

    def enter(self) :
        pass

class Central_Corridor(Scene) :
    """---TODO---"""
    
    def enter(self) :
        pass
    

class Armory(Scene) :
    """---TODO---"""
    
    def enter(self) :
        pass
    

class Escape_Pod(Scene) :
    """---TODO---"""
    
    def enter(self) :
        pass
    

class Bridge(Scene) :
    """---TODO---"""
        
    def enter(self) :
        pass