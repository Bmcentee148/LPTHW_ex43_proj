"""This module holds the basic components of a text adventure game.

Classes:
    Scene - The base class for each scene in the game
    Scene_Map - A map that will hold determine which scene is displayed next
    Engine - A game engine that is responsible for processing a users game
"""

#-- Import Statements --#
from random import randint

#-- Class Definitions --#
class Scene(object) :
    """A base class for each scene in the game."""

    # Abstract method that will be implemented in all subclasses
    def enter(self) :
        """Not implemented. Subclass and provide functionality."""
        raise NotImplementedError

class Death(Scene) :
    """---TODO---"""
    pass


class Central_Corridor(Scene) :
    """---TODO---"""
    pass
    

class Armory(Scene) :
    """---TODO---"""
    pass
    

class Escape_Pod(Scene) :
    """---TODO---"""
    pass
    

class Bridge(Scene) :
    """---TODO---"""
    pass
    

class Scene_Map(object) :
    """A map of the game's scene layout structure."""

    scenes = {
        'death' : Death(),
        'central_corridor' : Central_Corridor(),
        'armory' : Armory(),
        'escape_pod' : Escape_Pod(),
        'bridge' : Bridge()
    }


    def __init__(self, start_scene) :
        self.start_scene = start_scene

    def get_scene(self, scene_name) :
        return Scene_Map.scenes.get(scene_name, None)

    def get_opening_scene(self) :
        return self.get_scene(self.start_scene)