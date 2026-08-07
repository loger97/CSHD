# About Scenes
In CSHD, scenes are the 3D data Crystal3D (the engine of CSHD) uses to draw an environment.
Levels can contain many scenes, and scenes might not have a level. What you need to know is all levels have at least one scene, but not all scenes need to have a level. 
## Making a Scene into a Level
To make a scene a level, you must declare that scene, then under "levelSelect/LevelSelection/" add the level data using this format: `MaximumCoins=[INT]` `3rdAwardTime=[TimeInSeconds]` `2ndAwardTime=[TimeInSeconds]` `1stAwardTime=[TimeInSeconds]` `IsBoss=[1,2,3] (use -1 if not boss)` `Name=[NameOfLevel]`. After that, add its map parts to the level select with this format: `MapCordX` `MapCordY` `Costume=[LevelSelectIconID]` `LevelID=[SceneID]` `levelTransition=[LevelIDNext]` (not super important; you can set this to the same as the scene ID)
