"""This module holds the basic components of a text adventure game.

Classes:
    Scene - The base class for each scene in the game
    Scene_Map - A map that will hold determine which scene is displayed next
    GameEngine - A game engine that is responsible for processing a users game
"""

#-- Import Statements --#
from random import randint
import sys

#-- Class Definitions --#
class Scene(object) :
    """A base class for each scene in the game."""

    # Prevent creation of instance objects of type Scene
    def __init__(self) :
        raise NotImplementedError

    # Abstract method that will be implemented in all subclasses
    def enter(self) :
        """Not implemented. Subclass and provide functionality.

        Returns:
            the name of the next scene in the players path 
        """
        pass

    def __eq__(self, other) :
        # Just check if type of Scene are the same.
        return type(self) == type(other)


class Death(Scene) :
    """---TODO---"""
    
    def __init__(self) :
        pass

    def enter(self) :
        pass


class Central_Corridor(Scene) :
    """---TODO---"""
    
    def __init__(self) :
        pass

    def enter(self) :
        pass
    

class Armory(Scene) :
    """---TODO---"""
    
    def __init__(self) :
        pass

    def enter(self) :
        pass
    

class Escape_Pod(Scene) :
    """---TODO---"""
    
    def __init__(self) :
        pass

    def enter(self) :
        pass
    

class Bridge(Scene) :
    """---TODO---"""
    
    def __init__(self) :
        pass
    
    def enter(self) :
        pass

class Scene_Map(object) :
    """A map of the game's scene layout structure.

    Attributes:
        scenes - a map of scene names to scenes
        start_scene - the name of the scene to start from
    """

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
        """Get the scene with the given name.

        Arguments:
            scene_name - the name of scene to retrieve
        Returns:
            a Scene object of given name if the name is in the map, else None 
        """
        return Scene_Map.scenes.get(scene_name, None)

    def get_opening_scene(self) :
        """Get the opening scene.

        Returns:
            the beginning Scene object
        """
        return self.get_scene(self.start_scene)


class GameEngine(object) :


    def __init__(self, scene_map) :
        self.scene_map = scene_map

    def play(self) :
        curr_scene = self.scene_map.get_opening_scene()

        while True :
            print('\n----------------------------')
            next_scene_name = curr_scene.enter()
            current_scene = self.scene_map.get_scene(next_scene_name)
























