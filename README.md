We all know how painful Python imports can be. 
I made this repository to show the simplest way to make Python imports work.

It is very much inspired with this discussion:
https://stackoverflow.com/questions/4383571/importing-files-from-different-folder

Generally you need to control: 
1) where you are executing the script from
2) where is the relevant other package located (is it same level, level above, level below)... 
  - in case it is in the same level but different folder and in the case of folder above, you have to append to the system path
  - in case the module is in a subdirectory, you can easily just import from there 
  
Overall the imports in Python are very messy and feel hackish ie. you won't get any code completion in your IDE if you use this trick. 
I especially hate the imports when you compare it to a language like Java.
