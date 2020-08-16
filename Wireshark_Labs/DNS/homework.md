### 1. nslookup

1. Run nslookup to obtain the IP address of a Web server in Asia. What is the IP address of that server? 

**Answer: My school's web server's IP address is 202.38.193.28**

<img src="C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816182147833.png" alt="image-20200816182147833" style="zoom:50%;" />



2. Run nslookup to determine the authoritative DNS servers for a university in Europe. 

<img src="C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816182807068.png" alt="image-20200816182807068" style="zoom:50%;" />



3. Run nslookup so that one of the DNS servers obtained in Question 2 is queried for the mail servers for Yahoo! mail. What is its IP address?

<img src="C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816183507821.png" alt="image-20200816183507821" style="zoom:50%;" />



### 2. ipconfig

- `ipconfig \all`

<img src="C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816183715871.png" alt="image-20200816183715871" style="zoom: 50%;" />



***



### 3. Tracing DNS with Wireshark

4. Locate the DNS query and response messages. Are then sent over UDP or TCP? 

**Answer: Both UDP**

<img src="C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816185019485.png" alt="image-20200816185019485" style="zoom:50%;" />

<img src="C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816185057870.png" alt="image-20200816185057870" style="zoom:50%;" />



5. What is the destination port for the DNS query message? What is the source port of DNS response message?

**Answer: As can see in the picture above, both port are 53**



6. To what IP address is the DNS query message sent? Use ipconfig to determine the IP address of your local DNS server. Are these two IP addresses the same? 

   **Answer: They are the same.**

![image-20200816185548555](C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816185548555.png)

![image-20200816185715236](C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816185715236.png)



7. Examine the DNS query message. What “Type” of DNS query is it? Does the query message contain any “answers”?

**Answer: Type is A, means query for IP address, it doesn't contain any answers.**

![image-20200816185904507](C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816185904507.png)



8. Examine the DNS response message. How many “answers” are provided? What do each of these answers contain?

![image-20200816190231407](C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816190231407.png)



9. Consider the subsequent TCP SYN packet sent by your host. Does the destination IP address of the SYN packet correspond to any of the IP addresses provided in the DNS response message?

**Answer: Yes, there is.**

10. This web page contains images. Before retrieving each image, does your host issue new DNS queries? 

**Answer: No, it already have local DNS cache.**



***



11. What is the destination port for the DNS query message? What is the source port of DNS response message?

<img src="C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816192059064.png" alt="image-20200816192059064" style="zoom:50%;" />

12. To what IP address is the DNS query message sent? Is this the IP address of your default local DNS server?

**Answer: Yes, it is.**

13. Examine the DNS query message. What “Type” of DNS query is it? Does the query message contain any “answers”?

**Answer: there are three DNS queries,  type of which are PTR, A, AAAA. doesn't contain any answers.**

14. Examine the DNS response message. How many “answers” are provided? What do each of these answers contain? 

<img src="C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816192255068.png" alt="image-20200816192255068" style="zoom:50%;" />

15. Provide a screenshot. **Answer: as above.**



***



16. To what IP address is the DNS query message sent? Is this the IP address of your default local DNS server? 

**Answer: YES**

![image-20200816192649089](C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816192649089.png)



17. Examine the DNS query message. What “Type” of DNS query is it? Does the query message contain any “answers”? 

**Answer: type is NS, no answers.**

![image-20200816193140201](C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816193140201.png)



18. Exmine the DNS response message. What MIT nameservers does the response message provide? Does this response message also provide the IP addresses of the MIT namesers? 

**Answer: the type=NS**

•**name** is domain

•**value** is hostname of authoritative name server for this domain

![image-20200816192949509](C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816192949509.png)

19. Provide a screenshot. **Answer:** **As above.**



***



20. To what IP address is the DNS query message sent? Is this the IP address of your default local DNS server? If not, what does the IP address correspond to? 

![image-20200816193654967](C:\Users\13896\AppData\Roaming\Typora\typora-user-images\image-20200816193654967.png)



21. Examine the DNS query message. What “Type” of DNS query is it? Does the query message contain any “answers”?

22. Examine the DNS response message. How many “answers” are provided? What does each of these answers contain? 

23. Provide a screenshot.

### *the last 4 questions got a time out