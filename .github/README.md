# CSHD

CSHD, or Crystal Seeker HD, is a mod of [Crystal Seeker](https://scratch.mit.edu/projects/463553665/fullscreen/) that makes modding easier.

## Weird files
In this repository, you will find uncompiled code in the form of .sb3 files or in the scr directory; in order to edit them, use [Turbowarp](https://desktop.turbowarp.org/).
Save data will be in .sav files and, as of right now, can only be read by CSHD.
Level data is in two places; the first is in the `Crystal Seeker HD.sb3` file, specifically under the "root/data" path. The second place you can find level data is in the SDK directory; each "scene" is in its own .lvl file named after its scene ID (you can look them up here: [[Scene States]])

**NOTE** Large files are split into 10mb files; use 7zip (or similar) to recombine them

**Also**, you can make CSHD launch and run from an external drive with [loger's SecureAutorun](https://github.com/loger97/SecureAutorun)
## About Scenes
In CSHD, scenes are the 3D data Crystal3D (the engine of CSHD) uses to draw an environment.
Levels can contain many scenes, and scenes might not have a level. What you need to know is all levels have at least one scene, but not all scenes need to have a level. To learn more go to [[Chapter 4 - CSHD levels]]

Help with complex editor/Crystal3D Topics:
[[Chapter 1 - Basics]]
[[Scene States]]
