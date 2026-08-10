# CSHD

CSHD, or Crystal Seeker HD, is a mod of [Crystal Seeker](https://scratch.mit.edu/projects/463553665/fullscreen/) that makes modding easier.

## Weird files
In this repository, you will find uncompiled code in the form of .sb3 files; in order to edit them, use [Turbowarp](https://desktop.turbowarp.org/).
Save data will be in .sav files and, as of right now, can only be read by CSHD.
Level data is in two places; the first is in the `Crystal Seeker HD.sb3` file, spesificly under the "root/data" path, the second place you can find level data is in the SDK directory each "scene" is in it's own .lvl file named after it's scene ID (you can look them up here: [[Scene States]])

**NOTE** Large files are split into 10mb files; use 7zip (or similar) to recombine them

## About Scenes
In CSHD, scenes are the 3D data Crystal3D (the engine of CSHD) uses to draw an environment.
Levels can contain many scenes, and scenes might not have a level. What you need to know is all levels have at least one scene, but not all scenes need to have a level. 
### Making a Scene into a Level
To make a scene a level, you must declare that scene, then under "levelSelect/LevelSelection/" add the level data using this format: `MaximumCoins=[INT]` `3rdAwardTime=[TimeInSeconds]` `2ndAwardTime=[TimeInSeconds]` `1stAwardTime=[TimeInSeconds]` `IsBoss=[1,2,3] (use -1 if not boss)` `Name=[NameOfLevel]`. After that, add its map parts to the level select with this format: `MapCordX` `MapCordY` `Costume=[LevelSelectIconID]` `LevelID=[SceneID]` `levelTransition=[LevelIDNext]` (not super important; you can set this to the same as the scene ID)

Help with complex editor/Crystal3D Topics:
[[4.2 - All possible features]]
[[4.3 - Setting up complex features]]
[[Scene States]]
