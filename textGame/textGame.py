"""This module holds the basic components of a text adventure game.

Classes:
    Scene_Map - A map that will hold determine which scene is displayed next
    GameEngine - A game engine that is responsible for processing a users game
"""

#-- Import Statements --#
import scenes
from random import randint
import sys

#-- Class Definitions --#

class Scene_Map(object) :
    """A map of the game's scene layout structure.

    Attributes:
        scenes - a map of scene names to scenes
        start_scene - the name of the scene to start from
    """

    scenes = {
        'death' : scenes.Death(),
        'central_corridor' : scenes.Central_Corridor(),
        'armory' : scenes.Armory(),
        'escape_pod' : scenes.Escape_Pod(),
        'bridge' : scenes.Bridge(),
        'finished' : scenes.Finished()
    }

    def __init__(self, start_scene) :
        self.start_scene = start_scene

    def __eq__(self, other) :
        return self.start_scene == other.start_scene

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
    """Engine for running the text adventure game.

    Attributes:
        scene_map - A map of the scene names to scenes in the game
    """

    def __init__(self, scene_map) :
        self.scene_map = scene_map

    def play(self) :
        """Run the text adventure game."""

        current_scene = self.scene_map.get_opening_scene()
        last_scene = self.scene_map.get_scene('finished')

        while current_scene != last_scene :
            print('\n----------------------------')
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.get_scene(next_scene_name)

        # run the last scene
        current_scene.enter()

#-- Main Script --#
if __name__ == '__main__' :
    game = GameEngine(Scene_Map('central_corridor'))
    game.play()




















