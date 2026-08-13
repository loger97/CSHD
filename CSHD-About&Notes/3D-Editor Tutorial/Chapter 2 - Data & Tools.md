### Contents:
- 2.1 Use Data
- 2.2 Copy/paste data and appearance
- 2.3 Use certain tools
- 2.4 Fix known glitches

## 2.1 - Using data
In Crystal Seeker HD, each object has the option to save a certain number of data items.
The role of the data in Crystal Seeker is fixed, for example a moving platform has, the starting point, ending point, speed and the offset. Each of them we will learn about later. 
 
Now create and focus a point.
![[data1.png]]
The first thing that needs to be explained is the Object Type
There are 4 object types:
- Other 
- GameObject 
- Sprite3D 
- Text3D
 
There are **NO DIFFERENCES** between them and how they work. You can watch them as a number, and each number represents a different section.
To change the object type simple click on the `Object Type` button keep clicking to cycle through the 4 types.
The rule will be that GameObject you will be using for the 3D meshes, Sprite3D for sprites, Text3D for text in 3d space, and other for combinations or invisible collisions.
It may look complicated now, but you will get it over time.

The next most important thing is the class type. To change the class type simply press the `Class Type` button, and type the target class type.
The examples for class type can be "button", "p"
"eB", "tree" , "mtf" etc. The "non value" is 0, those will be deleted in lossy save, but the triangle and quads with 0 as class data won't.

The next things is the actual data. For example if you want to your enemy to have 100 health and
20 attack for example, you want to set the first data field to 100 and second to 20.

So to do that, firstly for health in this case, click the `Set data`, button, then enter the INDEX (1 in this case) of the actual data field you want to add/change, and then the editor will ask you once again, now type the **VALUE** (100 in this case). Repeat process for the attack, just now index will
be 2 and value will be 20.

In this image you can see the target result.
![[dataShowcase.png]]

The next example will be how to create set data for moving platform. The moving object has this data:
- PointStart
- PointEnd
- Move speed
- Starting offset
 
As you can see you can't save one point as a single value, but instead you would save the ID of the point. Now be sure you have at least 3 aux. points.
 
To do so click `Set Point`, now you have to chose the index of the data slot you want to change, so type 1 in this case and select another point. Do the same for the other slot, but with the other point. And last add the move speed and the offset.
The results should look like this:
![[dataShowcase2.png]]
You can also do the same thing for triangles and quads.


## 2.2 - Copying/pasting data & appearance
If you want to have multiple objects with the same data, but you don't want to type each manually, luckily there is copy, paste option.
To copy the data, go to the object you want to copy data from and click the `Copy data` button. The keyboard shortcut for this is "C".
In order to paste data, firstly go to the target object and click the `Paste data` button.
The keyboard shortcut for this is "V".

The process is almost the same for appearance (appearance is color of line/face, style of face, and
the thickness of the line).
You have `Copy apperence` and `Paste apperence` buttons.
Keyboards shortcuts for these are "B" and "N".
The only difference that those buttons will also appear in "Fill" mode, so you can set that every new
object will have the appearance of a previously  existing object. Or if you want to change the color of the triangle without creating a new face, you can simply
change the fill options, copy appearance, then focus the face, and paste appearance.


## 2.3 - Using certain tools

| Mode/tool           | Key                             | Description                                                                                                                                                                                                                                          |
| ------------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lock data move      | "L"                             | Moves lock data coordinates to focused points location.                                                                                                                                                                                              |
| Y chunk help fields | "P"                             | Change the Y coordinate of the chunk helping fields. (They're the already existing quads at the beginning)                                                                                                                                           |
| Chunk rendering     | "o"                             | Enable/disable chunk rendering, but keep in mind, that you won't be able to select objects which aren't in an active chunk.                                                                                                                          |
| Fast mode           | "u"                             | Enable/disable fast mode, this way you can move much faster.                                                                                                                                                                                         |
| Light angle         | "y" (kinda)                     | Change **Level editor** light angle                                                                                                                                                                                                                  |
| Invis. Mode         | "i"                             | Enable/disiable invisible mode, in this mode every triangle/quad with class type "inv" will be visible, and every other will become invisible. Useful when you need to have overlaping triangles/quads (visaul and collision platforms for example). |
| Render points       | `Point`, `Tri`,`Line` buttons   | Enable/disable rendering of points, triangles(quads), and lines respectively (Useful when you have points inside the blocks of quads for example).                                                                                                   |
| Default class type  | `Set Default class type` button | Setting the default class type, which would be the starting class type of the new created triangle or line. Useful when you need to place multiple triangles with same class type.                                                                   |
| Set camera          | `Set camera` button             | When you press this button, the starting position and rotation of the camera, will be set to the current position and rotation of camera.                                                                                                            |
| Set music type      | `Set music type` button         | Let's you change the music that plays when you preview the level (explained later)                                                                                                                                                                   |
| Set skybox type     | `Set skybox type` button        | Let's you change the skybox when you preview the level (explained later)                                                                                                                                                                             |
| Set snow in level   | `Set snow` button               | Enter a value 0-1, 0 meaning no snow, 1 meaning snow in level preview (explained later)                                                                                                                                                              |
| Set light angle     | `Set light angle` button        | Change **Level editor** and level preview light angle                                                                                                                                                                                                |
| Set moon hue        | `Set moon hue` button           | Change level preview moon hue.                                                                                                                                                                                                                       |

## 2.4 - Fixing known glitches
There are two known glitches:
![[Pasted image 20260812033727.png]]
If you see (A) there, and there is not an ask bar below, that is a glitch, simply press
"space", and everything will work.
The second is very rare, which happens when deleting triangles and quads, you would see that some of quads have lost their pair of triangle, so the quads become the triangles, to solve that, simply save the level using regular save, and load the project again.

[[Chapter 3 - Chunk map editor]]