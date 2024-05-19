
Hi this AirBnB_clone in this part of the project we started implementing the side of cmd (command line interface ) </br>.
if you wanna get to know this project and test let's how you can you it </br>.
first you need to get this project to you computer by downloading a zipe file or use command line to download </br>.
for command line clone this project by using</br>.
 `git clone https://github.com/flowSar/AirBnB_clone.git`</br>
 `cd AirBnB_clone`</br>
 `./console.py`</br>
if you wanna see the main command line that you can use type `help` </br>
as you can see there's `quit` you can use this command to quit or you can use `Ctrl^D` </br>
you can create an opbject using `create <class_name>`
there's a different ytpe of class thet you use to create your object there's : User, BaseModel, State, City, Review, Place, Amenity </br>
after you create an object you will see that his id was generated and was printed and this object will be sorted in json file named "file.json".
is you wanna see an print the User that you just created `show User <id>` and if you have created multiple useres you can type `all User` and all useres will be printed</br>
but if you want to print all object that was created and stored on json file you can type `all` </br>
you can delete andupdate all object you created by using `destroy and update ` command </br>
for deleting object from your list you will need to spesify which user or object you will delte by giving its id like this </br>
for example `destroy User 6af95bb6-0317-4df8-b0a9-c7f54afcb2aa` </br>
for updating `update User 6af95bb6-0317-4df8-b0a9-c7f54afcb2aa userName "Khalid"` </br>
you can apply this on all other objects `State BaseModel City Review Place Amenity`

and there's another way you do all what we discuss before . </br>
for printing : `User.show("<id>")` example of id `6af95bb6-0317-4df8-b0a9-c7f54afcb2aa` </br>
for deleting : `User.destroy("<id>")` </br>
for updating : `User.update("<id>", "attribute", "value(string or int or float)")` , you can only update one attribute at a time .</br>
for printing all objects : `User.all()`



