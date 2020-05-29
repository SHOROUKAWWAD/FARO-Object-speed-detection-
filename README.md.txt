# author : SHOROUK G. AWWAD

the code in this file is still under construction, however this is the last effort invested in it. 


the purpose:

detecting the motion of a close vehicle and determining its velocity and its direction 

hat has been done:
the above mentioned task has been achieved via calculating the difference in the x and y coordinates and divide by the time. 
So, if the difference in X-axis almost less than zero, the vehicle is moving to the east. If the difference is greater
 than zero, the vehicle is moving to west. the same applies for the North and the South directions ith Y axis. 
If the vehicle moves in a composite direction, both speed#s components in X and Y directions will be displayed. 

at the end, the function process_video() returns the average speed of the vehicle regardless the direction. That speed ould be sent to the user 
in a message box after the video ends.
 
the conda environment and all the used libraries have been exported to a yml file ready to be used.

The necessary libraries: 
  - openCV version 4
  - tKinter
  - sys
  - numpy
  - Time

    