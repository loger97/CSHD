### Contents:
- 4.1 Create simple levels
- 4.2 Import levels into CSHD
- 4.3 All possible features
- 4.4 How to setup complex features

## 4.1 - Creating a simple level
Now when you know everything about 3D editor, you would be able to create your first CSHD  level.
The most important things to set are the:
- Player (and then starting camera parameters)
- Coins
- Platforms
- End (Final crystal)
 
Firstly use `example.chunk` (in SDK/) this is a premade chunk map and when creating new project in the 3D editor, import it as starting chunk map. (You can use your custom chunk map if you really want).

---
First important thing to know is that player will lose if the Y coordinate goes below 0, that means that we must create our platforms above Y=0.
The best is to start with 100, so first set the `Y-lock` to 100. Then create 4 points on the start and be sure that your points don't exceed 400 units of distance from each other per one axis, that means if you have one point at (650,100,1150) the another should not have the X cord. for
example larger than 1050 , and smaller than 250. This is done to prevent visual bugs.
The target result will look like this:
![[Pasted image 20260813000248.png]]

Now enter the fill mode, and select the next color: RGB (127,200,80), color add 1 and brightness -2.
Now select the 4 points (when you select the points when creating a quad always go clockwise or counter-clockwise, which means don't select diagonally)
Fill the quad, and the result should look like this:
![[Pasted image 20260813000341.png]]
The next thing to create are multiple of those platforms. It's up to you how would it look like, but they should be across the whole level, like in the next image:
![[Pasted image 20260813000642.png]]
Now it's time to add player, go to the start of the level. Add a point at the middle of the starting platform, set it's class type to "p" and object type to "gameobject". (p for player)
It will look like this:
![[Pasted image 20260813001237.png]]

--- --- ---
Now you need to set starting camera position and rotation. To do so simply go to desired camera position, and rotate the camera at desired angle, and click the `Set camera` button (it will appear when you enter the focus mode).
The next thing is adding coins, to do so, just add aux. point in the target positions, and set their class type to "c" , and set object type to "sprite" , if you want coins which values 5 coins , set the class type to "bc" instead.
Just be sure that coins are slightly above the platforms, so that they don't clip into the ground. The easiest way to do so is to select the one of the platforms aux. point press "L",  (Y axis must be locked), then enter into place mode, place point in the middle, select new point and hold Q, to move it upwards.
Because you need to have multiple coins, consider using the copy/paste data feature.
The result should look like this:
![[Pasted image 20260813001844.png]]
And the last thing is adding the final crystal, go to the end of the level, and place aux. point at the top of the last platform.
Set it class type to "e" (e is first letter of end), and set the object type to "gameobject". If you didn't managed to do as the previous instructions says, look at the save data of the target result, so it may make things looks more clearer.
 

## 4.2 - Importing level
If you don't want to fork a new project just to play a level. Then it is very simple, just get the 
save data of project of the your custom level (using the divide/subtract save - hold "X") , open Crystal Seeker HD (in turbowarp) and click `Export to CSHD`

The other option is to fork a CSHD, and add new levels with your save data. Then you can choose between different options, like time trial times etc.
 
When you have finished your level, you need to import it into the game. There are two ways to do that.
First is to fork the "Crystal seeker HD" repo, and then go to the sprite named "Data", and then find the custom block named "Scenes" (it is at the very right), you will se this:
![[Pasted image 20260813002514.png]]
You can see "Add attributes to level with next parameters:
- Level Type (1,2,3,4,5), this is deciding what background will be in level (1 regular sky, 2 snowy mountains, 3 jungle, etc...) Also if you choose 2, it will snow in that level
- Music (0-10)
- Light direction (in degrees)
- Moon color (explained later)
 Then at Add scene you can find parameter named "data". Here you need to paste your data.
 ![[Pasted image 20260813002759.png]]
The additional options you can choose from are the ones you will find in the sprite named "LevelSelection", then at the very right, you can find custom block named "Preinit"
There you can find custom blocks "Add level" located in "Preinit".
 There are options for each level:
- Maximum coins
- 3rd, 2nd, 1st award times (for time trial)
- IsBoss (-1 if it isn't , 1,2,3 if it is a boss level)
- Name

## 4.3 - All possible features
Crystal Seeker HD, has much more features, like more than 5 types of platforms, 3 hazards , 3 enemies etc.
They will be arranged in tables so you can have a better look:

| **Platforms**                 |            |             |                                                           |                                                                                                       |
| ----------------------------- | ---------- | ----------- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Name                          | Class type | Object type | Data                                                      | Description                                                                                           |
| Regular                       | 0          | tri/quad    | /                                                         | Normal Platform                                                                                       |
| Slippery                      | s          | tri/quad    | /                                                         | Behaves like ice; can increase your speed the more you walk on it.                                    |
| Circling                      | c          | tri/quad    | Explained at 4.4                                          | Platforms which move in circles, around a 3D line in space.                                           |
| Moving                        | m          | tri/quad    | Explained at 4.4                                          | Moves from one point to another periodically.                                                         |
| Rotating                      | r          | tri/quad    | Explained at 4.4                                          | Rotates around a 3D line in space.                                                                    |
| Bouncy                        | b          | tri/quad    | 1.Bounciness<br>  (Rec. 5-10)                             | Increases player's Y velocity when the player touches it.                                             |
| Falling                       | f          | tri/quad    | 1. If set to -1, platform won't come back.                | The platform starts falling upon contact with the player.                                             |
| Palm tree                     | tree       | other       | 1. Height<br>(Rec. 1-6)                                   | Creates the tree with the bottom at the point where it is placed.                                     |
| Decoration                    | d          | tri/quad    | /                                                         | A triangle, or quad which the player doesn't collide with. Used to increase performance.              |
| Front camera decoration       | d2         | tri/quad    | 1. Distance to be transparent                             | Same as "d", but it becomes transparent when it is very close to the camera.                          |
| Move on trigger to fixed pos. | mtf        | tri/quad    | Explained at 4.4                                          | Platforms which move to target position, which button is activated.                                   |
| Front camera                  | 2          | tri/quad    | 1. Distance to be transparent                             | Becomes transparent, when it is very close to the camera.                                             |
| Regular line                  | 0          | line        | /                                                         | Same as a regular platform, but a line.                                                               |
| Decoration line               | d          | line        | /                                                         | Same as a d platform but a line.                                                                      |
| Balancing platform            | ba         | tri/quad    | Explained at 4.4                                          | Rotates at a specific angle when in contact with the player.                                          |
| Invisable                     | inv        | tri/quad    | Explained at 4.4                                          | Imitates any other triangle/quad class type without data, while invisible.                            |
| **Enemies and Hazards**       |            |             |                                                           |                                                                                                       |
| Enemy Basic                   | eB         | sprite      | Explained at 4.4                                          | An Enemy that, when the player goes within a rectangular border, tries to push you.                   |
| Enemy Shooting                | eS         | sprite      | Explained at 4.4                                          | An enemy that, when the player goes within a rectangular border, tries to hit you with a snowball     |
| Enemy Jumping                 | eJ         | sprite      | Explained at 4.4                                          | An enemy that jumps when the player is near; when it lands, it creates a wave that pushes the player. |
| Axe                           | axe        | line        | Explained at 4.4                                          | It swings left and right and pushes the player upon contact.                                          |
| Boss bull                     | boss1      | game Object | /                                                         | The first boss in Crystal Seeker.                                                                     |
| Boss robot                    | boss 2     | game Object | /                                                         | The second boss in Crystal Seeker.                                                                    |
| Boss frog                     | boss3      | game Object | /                                                         | The third boss in Crystal Seeker                                                                      |
| **Main and Other**            |            |             |                                                           |                                                                                                       |
| Player                        | p          | game Object | /                                                         | The starting position of the player.                                                                  |
| Coin                          | c          | sprite      | /                                                         | Collectable.                                                                                          |
| Big coin                      | bC         | sprite      | /                                                         | Coin with a value of 5 instead of 1.                                                                  |
| Moon                          | moon       | sprite      | Explained at 4.4                                          | Awards the player with 15 coins for exploring or completing a challenge.                              |
| End                           | e          | game Object | /                                                         | The end goal.                                                                                         |
| Rope                          | r          | line        | /                                                         | Used for swinging, important: the first point when creating the line must be upwards.                 |
| Boosting circle               | bc         | game Object | Explained at 4.4                                          | Increases the velocity of the player upon contact with the player.                                    |
| Button                        | button     | game Object | Explained at 4.4                                          | Activates things when activated, such as "mtf" platforms.                                             |
| Checkpoint                    | cp         | other       | Explained at 4.4                                          | Respawns the player when the player falls in a hole.                                                  |
| Sign                          | sign       | other       | 1. sprite name<br>2 .direction (0-360)<br>3. Preview text | Shows you a sprite when you come close.                                                               |
| 3D sprite                     | d          | sprite      | 1.sprite name<br>2. sprite size                           | A non-interactable 3D sprite.                                                                         |
| Lava                          | la         | tri/quad    | /                                                         | Touching this will have the same effect as falling. (changes from red to orange)                      |
| Poison                        | pi         | tri/quad    | /                                                         | Touching this will have the same effect as falling (changes from purple to pink)                      |
| Death Plane                   | die        | tri/quad    | /                                                         | Touching this will have the same effect as falling. (can modify RGBA data)                            |
| Water                         | water      | tri/quad    | /                                                         | Solid water-looking color.                                                                            |

## 4.4 - Setting complex features

There are many complex features; for example, moving platforms require multiple data points, such as the starting point, ending point, speed, and offset.

Before that, you must first learn about vectors. I suggest you search the Internet for vectors so you can more easily set the complex features.

In the Crystal 3D editor, vectors are defined by 2 points, and the 3D engine in-game converts those 2 points into a vector. That vector will be used to determine the angles, positions, etc. Basically, the vector is a set of 3 numbers (X, Y, Z), and it has its direction and magnitude.

The first complex feature you will learn is the moving platform, so create a new empty level so you can test all of the features.

### Moving platforms
The moving platform (class type "m") has 4 data slots:

➣Starting point of moving vector

➣Ending point of moving vector

➣Speed in degrees (to calculate how many seconds it needs to go to the ending point and back, use (360/speed)

➣Offset in degrees (0-360), it represents how far it is from the  
starting point at the beginning of the time.

You can see the structural implementation here:
![](pictures/move.png)
### Circling platforms
Next up is the circling platform.

The circling platform (class type "c") has 4 data slots:

➣Pivot point of the platform (it's the platform's center most of the time)

➣Starting point of the vector around which the platform circles

➣Ending point of the vector around which the platform circles

➣Speed in degrees.

You can see the structural implementation here:
![](pictures/circle.png)

### Rotating platforms
The rotating platforms (class type "r") have 7 data slots:

➣Pivot point (usually located in the center of the platform)

➣Rotating on X axis in degrees per second

➣Rotating on Y axis in degrees per second

➣Rotating on Z axis in degrees per second

➣Offset rotation on X axis (0-360)

➣Offset rotation on Y axis (0-360)

➣Offset rotation on Z axis (0-360)

(offset means how it is already rotated when the game starts)

You can see the structural implementation here:
![](pictures/rotate.png)


### Balancing platforms
The balancing platforms (class type "ba") have 4 data slots:

➣Pivot point, which is also the starting point of the rotate vector and the starting point of the falling vector.

➣Second point of the rotating vector

➣Second point of the falling vector.

➣Maximum fall angle.

**Important**: the second point of the falling vector must be 90 degrees away (CCW) from the second point of the rotating vector relative to the Y axis.

You can see the structural implementation here:
![](pictures/plank.png)


### Enemies
The enemies (class types "eB", "eS", and "eJ") have all the same data meaning, it have two slots:

➣Maximum X distance from starting point

➣Maximum Z distance from starting point

### Boosting ring
The boosting circle (class type "bc") has only one slot:

➣Starting point of direction vector

➣Ending point of direction vector

You can see the structural implementation:
![](pictures/boost.png)


### Swinging axe
The axe (class type "axe") has 5 slots:

➣Button trigger ID (0 for always active)

➣Rotate speed in degrees

➣The second point of blade direction vector

➣The second point of the rotate vector

➣Offset in degrees (0-360)

 **Important**: the first point when filling a line must be upward, the same way it is for swinging rope.

You can see the structural implementation here:
![](pictures/axe.png)


### Buttons & MTF platforms
The button (class type "button"), once triggered, moves the "mtf" platforms to the target position and activates the axes which have the first data slot same as the button trigger ID.

Buttons have 4 data slots:

➣Button trigger ID (1,2,3...)

➣The position where the camera will be when the button is pressed

➣The camera direction relative to the previous point

➣Camera position after cutscene

Platform which will be moved to a fixed position once the button is triggered ("mtf") has 3 data slots

➣Button trigger ID 

➣Starting position point

➣Target position point

You can see the structural implementation here:
![](pictures/buttonMTF.png)


### Checkpoints
The checkpoint (class type "cp") is an AABB (box) collision; when you touch it, it saves you to that point.

Buttons have 3 data slots:

➣The one point of AABB

➣The second point of AABB

➣Angle of checkpoint (0-360)

The AABB is structured so that one point should be at the bottom, and the other at the top, but with different.

X and Z coordinates from the previous point:  
You can see the structural implementation here:
![](checkPoint.png)

### Moons
The Moon is basically a 15-coin; it can be awarded to the player for completing a challenge or exploring the level.  
By default, it is red, but the color can be changed (all moons in the level will change color). You can 
see the recommended moon colors here: 

| Theme       | Color (1-200) | Color (name) |
| ----------- | ------------- | ------------ |
| Grass lands | 30            | Yellow       |
| Snow/ice    | 15            | Oragnge      |
| Jungle      | 125           | Deep blue    |
| Desert      | 70            | Green        |
| Lava        | 100           | Cyan         |
| Clouds      | 0             | Red          |
| Space       | 30            | Yellow       |

Generally you want the color of the moon to contrast with the enviroment.

### Invisible Platforms
The last feature is an invisible platform (class data "inv"); it has only one data slot:

➣The class data will be just invisible; it must be a tri/quad with 0 data slots (most useful are 0 and s)

You must enter "invisible" mode by pressing the key "I" on the keyboard. Notice how the platforms that are overlapping the invisible platforms have class data "d", which means they don't collide with the player, meaning that there are fewer collisions, which means the game will run faster.

