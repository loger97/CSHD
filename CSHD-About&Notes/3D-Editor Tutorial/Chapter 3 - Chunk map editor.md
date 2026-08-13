### Contents:
- 3.1 Place chunks
- 3.2 Connect chunks
- 3.3 Orientate, use options
- 3.4 Save/load and import chunk maps


## 3.1 Placing chunks
Before this, you have to know what chunks are. Imagine you're at the start of a level, you don't need to see and update the end part.
Let's simplify things, let the level have 3 parts, starting
part, two middle parts and an ending part. If you're at the start you only need to see the starting part, and the first middle part, when you are in middle part you  need to
see only the previous part, and the next part and so on. Thanks to chunks this is possible, each object has it's own chunk, and the chunk is determined by the position at the moment when object is placed. And you wouldn't be able to see object in inactive chunks. You will get it over time.

---
To create chunk maps you will need to open `ChunkMapEditor.sb3`.
When you start the editor you will see this:
![[chunkMapEditor.png]]

Let stick with our previous example (with 4 parts), each part will be determined by a number 1,2,3,4. The default selected chunk is "1".
To place simply click the on a light gray tile:
The result should look like this:
 ![[one dot.png]]
Now you can do that multiple times, and it should look like this:
![[manydots.png]]

**Tip: always start level from the bottom left corner.**

---
The next part would be changing chunk that will be placed. There are two ways do to so:
First is by clicking`Selected Type`, and then typing the desired chunk number (0-99).
The next is the quick way, by pressing keys from 0-9 on your keyboard.
Keep in mind, that if you press 2, and your current chunks is 1, it won't select 2 , but 12, because of that you must press 2 twice, that way it will select.
Also you can press "C" to select chunk 0, which is empty
chunk (object on it will be counted as global i.e. they will be chunk independent).
 
Now select chunk number 2, and place chunks in way something like this:
![[connected dots.png]]
Now repeat this process for 3 and 4, and it should look like this:
![[connectedlotsofdots.png]]


## 3.2 - Connecting chunks
Now when you have placed the desired chunk, we now have to define which chunks you can see when you are in specific chunk. The easiest way to do is by simply clicking `Auto Connect`, this way, all neighboring chunks will be selected.
Now to see what actually happened, you have to select all of the chunks. There are two ways to do so: First is holding "X" key , and then clicking a chunk on the chunk map. That way the selected type will be equal to the chunk value you have clicked. Keep in mind this will also change the type of newly created chunks. 
 
The next way is by switching modes, there are two ways to do so , first is simply by clicking `Replace Mode`, (click again) to return back to the select mode.
The other way is simply by pressing "Z" key , it will switch between replace/select modes that way.
When you are in select mode, you can select tiles just by clicking on them. When you select a chunk the black dots represent what chunks you can see from the select chunks.

For example if you select chunk number 3, it will look like this:
![[connectingThem.png]]
From this image we can conclude that currently you can see chunk number 2 and chunk
number 4 from the chunk 3. (Also the chunk which is selected is automatically included as visible).

But what if we don't want to use auto connect or we want to upgrade the existing connections?
For example we want chunk number 1, to see chunk number 3 (but not see 1 from 3).
Repeat next steps:
- Select number 1 chunk
- Enter "connection" mode by clicking `Add Connection` or by pressing "space" on keyboard.
- Click on chunk number 3
- Leave "connection" mode by clicking `Select tile to connect` or by pressing "space" on keyboard.
 By this, you now can see chunk 3 from chunk 1.
 The result will look like this: (before leaving connection mode)
 ![[fullScreen shot.png]]
On this list , you can see which chunks are currently connected to the chunk which is selected.
Here's the tip for easier adding connections: When you're in selection mode, you can still hold "X" and when you click on the chunk, there won't be any connections added, but it will select chunk instead. This way you don't have to switch between modes, when you are adding connections.


## 3.3 - Orientating, using options
The first important thing you need to learn is to change size of the chunk map:
You can do so simply by clicking `sizeX` or `sizeZ`. For this example change sizeX to 15 and sizeZ to 12.
The result should look like this:
![[seeMap.png]]
This way you can have a larger chunk map.
Feel free to make your own custom chunk map.
**Tip: always have at least 2 chunk tiles empty from the black border**.

---
The next is about moving through the chunk map. You can do that simply by using WASD or arrow
keys on your keyboard. The another option is to use `xPos` or `zPos` to change the x or z position respectively. To zoom or un-zoom the map use the `ChunkRate` slider located in top left corner.

`Chunk size` the best values for this are 100-1000, and the default value is 400 , which
is the best for Crystal Seeker (and CSHD). It represents the size in units of the chunk tile.
`startX` and `startZ` represents the starting coordinates of first (bottom-left) chunk. These
currently have no particular use, so keep them at 0,0.


## 3.4 - Saving/loading, importing
When you have finished creating your chunk map, you need to save it. You do that simply by clicking the `Save` button and copying, the .chunk file to safe place, so you
don't lose it. Then when you want to edit your chunk map again, simply
press the load button, and select your .chunk file. The most important of this load features is changing the existing connections. You wouldn't want to remove existing
chunks if you have already placed something there with the 3D editor.

To import the chunk map into the 3D editor, when creating new project in 3D editor, instead of leaving the import field empty (which will give you a default chunk map), use your .chunk file insted.
Here's the result:
![[result.png]]

[[Chapter 4 - CSHD levels]]