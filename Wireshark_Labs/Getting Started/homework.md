### What to hand in 

The goal of this first lab was primarily to introduce you to Wireshark. The following questions will demonstrate that you’ve been able to get Wireshark up and running, and have explored some of its capabilities. Answer the following questions, based on your Wireshark experimentation: 

1. List 3 different protocols that appear in the protocol column in the unfiltered packet-listing window in step 7 above. 
2. How long did it take from when the HTTP GET message was sent until the HTTP OK reply was received? (By default, the value of the Time column in the packetlisting window is the amount of time, in seconds, since Wireshark tracing began. To display the Time field in time-of-day format, select the Wireshark View pull down menu, then select Time Display Format, then select Time-of-day.) 
3. What is the Internet address of the gaia.cs.umass.edu (also known as wwwnet.cs.umass.edu)? What is the Internet address of your computer?
4. Print the two HTTP messages (GET and OK) referred to in question 2 above. To do so, select Print from the Wireshark File command menu, and select the “Selected Packet Only” and “Print as displayed” radial buttons, and then click OK.



1. different protocols：

   ARP, EAP, ICMPv6, TCP, UDP

<img src="C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816003328073.png" alt="image-20200816003328073" style="zoom: 33%;" />

<img src="C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816003553632.png" alt="image-20200816003553632" style="zoom:33%;" />



2. the  time between HTTP GET message was sent and the HTTP OK reply was received

<img src="C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816005136687.png" alt="image-20200816005136687" style="zoom:50%;" />

<img src="C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816005024349.png" alt="image-20200816005024349" style="zoom:33%;" />



3. the Internet address of the school library

<img src="C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816011048327.png" alt="image-20200816011048327" style="zoom:33%;" />



4. content just like above