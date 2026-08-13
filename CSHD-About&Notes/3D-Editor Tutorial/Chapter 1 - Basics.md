### Contents:
- 1.1 Create a project
- 1.2 Orientate through space
- 1.3 Create auxiliary points
- 1.4 Modify auxiliary points
- 1.5 Fill 3D lines/faces
- 1.6 Save/load projects

## 1.1 Creating a project

The first things you will see then you start the editor are four buttons:
- New project
- Load project
- Load Code
- Change Chunk map
Click the New project button. The editor will ask for a chunk map, for now we can leave that blank.


## 1.2 Orientate through space

The controls are the same as free-cam mode:

| Key         | What it dose          |
| ----------- | --------------------- |
| W           | Go forward            |
| A           | Go left               |
| S           | Go backwards          |
| D           | Go right              |
| Q           | Go up                 |
| E           | Go down               |
| Left arrow  | Yaw rotate left (CCW) |
| Right arrow | Yaw rotate right (CW) |
| Up arrow    | Pitch up              |
| Down arrow  | Pitch down            |
You can also hold "R" and rotate the camera with your mouse.

![[editorBlowout-chuncks.png]]
Here you can see what chunk you are in with a map and `X` and `Z` coordinates.

--------------------------------------------------------------------------
This is the mini-map of the chunk map, it's an 11x11 grid, while the chunk map is much bigger. Each shade/color represents something.
![[miniMap.png]]

| Color                | Meaning                                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------------------------------ |
| Black (-1)           | Out of bounds, you shouldn't put anything here                                                               |
| White (0)            | Undefined, you still shouldn't put anything here, but if you do it will be considered global (always active) |
| Color (1,2,3..98,99) | You should place things here.                                                                                |

--------------------------------------------------------------------------
![[chunkCords.png]]
This shows your current chunk coordinates.

When you click either the "chunkX" or "chunkZ" buttons, you can enter the coordinates you want to go to and the editor will teleport you there. 

![[miniMapCords.png]]
In this image you can see how this system works.

![[full3DRep.png]]
Here you can see a 3D representation of the chunk map.



## 1.3 Creating auxiliary points

The auxiliary points or points are points in 3D space used in this engine, which helps you create 3D polygons.
To be able to create them you must be in `Place` mode. To enter `Place` mode press "1" on your keyboard.

On the bottom of your screen you can see this: ![[auxCords.png]]
Those represent 3D XYZ coordinates of the potential new point.

The center of those axis lines are representing the actual position of the potential point. You can press +/- to change the distance of the axis lines from the camera.

But what if you want to place 10 points with the same Y coordinate, "100" for example. It can be frustrating to nail all of those points. But luckily there is option to lock an axis. In this case we will
be locking Y axis.

Find and press this button `Y lock` then the set button will appear, when you press set the editor will ask you to enter a number, that number will represent the locked y value. Type 100 and place new points to see what happens.
When you are done, press that Y lock button again to 
unlock it. 
You can try locking other axis's, even multiple axis's at once.

----------------------------------------
As you can see by the button `snap`, the magnet snapping is turned on. Which means any new potential points will have all 3 coordinates divisible with the snap value (50 in this case).
It's not recommended ever turning it off (you can try to see what happens).
The real use is when you want snapping to be on a different number, 25 for example. To do it click `set snap` and type 25, now you can see that all new potential points will have their coordinates aligned with a 25 units grid. 
To return back it to 50, simply do it again, but now with 50.


## 1.4 Modifying auxiliary points

You have placed a point on wrong position? Or you don't even want a new point?
No problem, there is a way to modify/delete it.
Enter into `Focus` mode by pressing "2" on keyboard. Now when you're in `Focus` mode you can focus on a single point simply by clicking on it.
Pressing "space" or clicking on empty space will un-focus the point.

Now when you have focused a point, try moving and rotating the camera. You can see that now
controls are different. Instead of moving camera, the point will be what is actually moving, and the camera will just follow it. And instead of rotating the camera, the camera will
rotate around the point. Use +/- once again, but now to change distance from focus point.

Since now you are in a Focus of an aux. point, you can see some new options have appeared.
Currently important are: 
`Delete` - Delete a point
There is also a keyboard shortcut for deleting. It's "~", you don't even need to focus a point to delete it. Just hold "~" and click the point.
![[pointCords.png]]
When you click X,Y,Z respectively, you can change that coordinate.


## 1.5 Filling 3D lines/faces

Now since you have all your points at proper positions, now you can create lines, triangles or quads (rectangles or squares) using them. The first thing you need to do is to enter `Fill`
mode by pressing "3" on keyboard. Now you need to select 2,3,4 points to create
a line, triangle or quad respectively. You select/unselect a point by clicking on it.
Press space to unselect all points.

When you press any of these buttons the editor will ask you to enter a value which will represent that option. Red, Green, Blue and Alpha, is the RGBA value of the filled line or face.
![[RGBACBT.png]]
**What this is:**
RGBA is a way of representing color. 
**Red, Green, Blue:** Mix together to make light-based colors. Value `0` means no light, and `255` means full power.
**Alpha**: Sets how see-through a face will be. Value `0` is invisible, and Value `255` is opaque.
**Thickness**: only works for lines, and it controls line thickness.
**Color add** and **brightness**: represents the change of color/brightness per triangle fill algorithm.

------------------------------------------------------------------------
In this example we will create a triangle, first select three points (you need to create them first). When you select them press "F" on your keyboard. And the triangle will be filled.
![[fillDemo.png]]
Now return back to focus mode (key "2"). Now try selecting a line, triangle or quad.
You can see that it behaves the same way as the points, expect now you can't move the object.
That means you can delete it by pressing delete button or key "~", the same way as for aux. point.

## 1.6 Saving/loading projects

Assume you have finished your level, or you didn't finish but you must turn off the editor, then all progress will be lost. But luckily there is save/load option. There is a save button at the top of the
3D editor screen, and a load button at startup of the editor.
Firstly in order to save, you must choose the right save choice. You have 2 choices:
- Regular save (yellow)
- Divide subtract save (also known as "Export to Crystal Seeker") (this button will appear when you hold "X" key on your keyboard)
**The regular save**, is save which you want to use the when
you want everything to be the same as when you were
saving it. (Save to .lvl file)
**The divide/compress save** (Export to CSHD), it will divide every coordinate with 50 , and subtract some certain values from each color, so the save data occupy less space. "Crystal seeker" uses this way of saving data for its levels. (level data will be copied to your clipboard)

To load your data simply start the 3D editor again, and press the Load project  button.
Then just select your levels `.lvl` file and then everything will be same as you saved it.
But there is still lot to learn until you will know how to create a level for Crystal Seeker HD.

[[Chapter 2 - Data & Tools]]