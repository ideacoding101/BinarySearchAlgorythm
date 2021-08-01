# BinarySearchAlgorythm
This is the source code for an instagram post I made where we discuss how the Binary Search Algorythm works. You can acces it by clicking [here :D](https://www.instagram.com/p/CEmW6CzF_gO/)

<p align="center">
  <img src="https://github.com/ideacoding101/images/blob/master/large_logo.png" width="461" height="291" alt="ideacoding">
</p>
  
<p align="center">
 <a href="https://www.fiverr.com/ideacoding">
    <img src="https://img.shields.io/uptimerobot/status/m778918918-3e92c097147760ee39d02d36?color=%231DBF73&label=WANNA%20LEARN%20PYTHON%3F&logo=Fiverr&style=for-the-badge"
        alt="Fiverr">
 </a>

 <a href="https://www.instagram.com/ideacoding101/">
    <img src="https://img.shields.io/uptimerobot/status/m778918918-3e92c097147760ee39d02d36?color=%23E4405F&label=DAILY%20PYTHON%20CONTENT&logo=Instagram&style=for-the-badge"
        alt="Instagram">
 </a>

 <a href="https://www.youtube.com/channel/UCwF2neCernMKopJHCWAt2aQ">
    <img src="https://img.shields.io/uptimerobot/status/m778918918-3e92c097147760ee39d02d36?color=%23FF0000&label=my%20youtube&logo=yOUTUBE&logoColor=%23FF0000&style=for-the-badge"
        alt="Youtube">
  </a>

 <a href="mailto:ideacoding.contact@gmail.com">
    <img src="https://img.shields.io/uptimerobot/status/m778918918-3e92c097147760ee39d02d36?color=%23D14836&label=contact%20me&logo=gmail&logoColor=%23D14836&style=for-the-badge"
        alt="Gmail">
  </a>

</p>


# HOW DOES IT WORK?
In my instagram post we also discuss the way this algorythm functions, here's a more in depth explanation. So basically, we'll follow the same procces the function follows and we'll explain everything from that point. At the bottom of the file, we call the function and we store the value it outputs into a variable, later we print the variable. When we call the function, we pass a few parameters: the list that contains the element we want to look for(the list need to be sorted), the target we are looking for, the index of the first item (or the item in the left) which is going to be 0 and finally the index of the item in the right which is gonna be the list' lenght minus one because we start counting from zero.

Now, we do a while loop that checks if the right is bigger than the left index, which always should unless they overlap, that would mean that we found the number we were looking for. In order to find that number, we select the center of the list and we check if this is the number we were looking for, if it's not, we check if it's bigger or smaller. Depending on that last condition, we'll discard the elements of the left or the elements of the right. For example, imagine our target is 20 and the center of the array is 40, when we do that last check, we realize 20 is smaller than 40 so we discard the elements of the right as no bigger numbers than 40 will be the target, therefore, we set the right variable value to 40 and we loop again. Each loop round will discard half of the list by checking if it's bigger or smaller than the taget. By repeatedly calling the fucntion with new values we use a technique called recrusion.

That's it! It's a quite simple and effective algorythm, however, it also has some cons, you can check my post on instagram [here](https://www.instagram.com/p/CEmW6CzF_gO/) to discover the weak points of the Binary Search Algorythm.
