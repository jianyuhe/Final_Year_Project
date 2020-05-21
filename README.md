# Final_Year_Project

## Project Name:
Space Checker

## Technologies
Python, JavaScript, HTML ,CSS, Amazon Lightsail, Pycharm, jupyter notebook, django, opencv, tensorflow, keras , VGG16

## Projetct Description
This project is about Machine learning, Classification, Deep learning, Convolutional neural networks,
and image processing.
Space checker is a live web application deployed by Django (Django is a high-level Python Web
framework that encourages rapid development and clean, pragmatic design.). this web, VGG16

application has a login page, register page, and home page. the home page can allow the user to
select a different car park to show statues of space. The home page contains a status map
shows the position of free space and space id.
This application is going to design by OpenCV using Python programming language (Python is a
programming language that's soaring in popularity with web and software developers. OpenCV
(Open Source Computer Vision Library) is an open-source computer vision and machine learning
software library.). OpenCV is helpful for image processing.
The database of application is set on PostgreSQL (PostgreSQL is a general-purpose and
object-relational database management system, the most advanced open-source database
system.).
This application is a 3-tier structure, it has presentation tier, application tier, and data tier.

![alttext](https://github.com/jianyuhe/Final_Year_Project/blob/master/relateImage/1.png)
![alttext](https://github.com/jianyuhe/Final_Year_Project/blob/master/relateImage/2.png)
first use the houghlines function to output the position of each line, then separate all lines
into 4 groups to sort lines by x-axis.

![alttext](https://github.com/jianyuhe/Final_Year_Project/blob/master/relateImage/3.png)
we detect 190 lines on the image, that we have to delete extra lines, we used sort function
to sort each line of each group by y-axis, then find distance of both lines, if distance less than
5, then we delete this line. use a loop to make sure to delete all extra lines.

![alttext](https://github.com/jianyuhe/Final_Year_Project/blob/master/relateImage/4.png)
create space id for each rectangle and change all rectangles to the same size, use imwrite
function to output each rectangle as image

![alttext](https://github.com/jianyuhe/Final_Year_Project/blob/master/relateImage/5.png)

tidy up the train images into different label of folders.

![alttext](https://github.com/jianyuhe/Final_Year_Project/blob/master/relateImage/6.png)
use puttext function to show space id, number of total space and free space, then use
make_prediction function to predict status of space.

![alttext](https://github.com/jianyuhe/Final_Year_Project/blob/master/relateImage/7.png)
save model according as h5 file and start train

![alttext](https://github.com/jianyuhe/Final_Year_Project/blob/master/relateImage/8.png)
 plot diagram shows accuracy and loss
 
![alttext](https://github.com/jianyuhe/Final_Year_Project/blob/master/relateImage/9.png)
use adjango to design web application to contain the video, This is park html, It play a video shows status of car park, and set 2 buttons, one is direct to location of car park and other one direct to feedback page.




