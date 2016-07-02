# Tests for components of the testGame module

from nose.tools import *
from textGame.textGame import *
from textGame.scenes import *

def test_scene_base() :
    # We are not able to directly create an object of type Scene
    assert_raises(NotImplementedError, Scene)

def test_subclassing() :
    # Test we can create an object from subclass of Scene and call its methods
    d = Death()
    assert_equal(d.enter(), None)
    e = Escape_Pod()
    assert_equal(e.enter(), None)

def test_scene_map() :
    scene_map = Scene_Map('armory')
    assert_equal(scene_map.start_scene, 'armory')
    assert_equal(Scene_Map(None).start_scene, None)
    assert_not_equal(scene_map.start_scene, 'central_corridor')
    assert_equal(scene_map.get_scene('vacant'), None)
    assert_equal(Scene_Map(None).get_opening_scene(), None)

    assert_equal(scene_map.get_opening_scene(), Armory())
    assert_equal(scene_map.get_scene('death'), Death())

def test_gameEngine() :
    scene_map = Scene_Map('bridge')
    game = GameEngine(scene_map)
    assert_equal(game.scene_map, scene_map)
    assert_not_equal(game.scene_map, Scene_Map('armory'))
    assert_equal(game.scene_map, Scene_Map('bridge'))



