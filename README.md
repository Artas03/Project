# QA Core Fundemental Project

## **Project Overview**

This project encompasses the creation and deployment of an application that is used by 'AHD Garage' a MOT centre, allowing them to keep a record of their customers and their cars.

### <ins>**Project Aims**</ins>

The aim of this project was to create a functioning application that houses a relationship between two tables, in this case, we explored a one to many relationship. The application should be able to exhibit all aspects of 'CRUD', so it must be able to create, read, update and delete any information. 

In this case, Customers and their vehicles must be able to be added to a database from where they're information can be read, updated and deleted.

### <ins>**Project Planning**</ins>

Initially the project that was intended to be creatd was a lot more complex, it would be had the ability to store data on when the customers' vehicles had last been serviced and had a MOT and would then send them a reminder in the coming year when they're MOT and service would be due. However, this sort of development did not seem to be possible with the time frame of this project, so it was scaled down to storing the information of customers and their vehicles, which could be expanded upon in the future to its originally inteded purpose. 

### **1. Trello Board**

![Trello](https://i.imgur.com/0nmJXpD.png)

Above is the trello board that was constantly used throughout the development of the application. It can be seen that the project plan and risk assessment, which are the most important aspects before beginning development, were completed before anything else so there was clear direction as to the intended purpose of the application and what steps were needed to achieve them. 

### **2. Risk Assessment**

![riskassessment](https://i.imgur.com/bNmJ5RJ.png)

The risk assessment was a vital part of the planning that had to be completed before beginning development, to ensure those potential risks would be addressed accordingly.

### **3. ERD Diagram**

![ERD](https://i.imgur.com/ZLuxNsX.png)

Here is the ERD diagram which shows the customers tables as well as the maintenance tables which have a one to many relationship. This means that one customer can have multiple vehicles, however each vehicle can only belong to one customer.


<br>

## **App Functionality**

![CRF](https://i.imgur.com/bdUVABR.png)
Here we can see the customer registration form, where the customer enters their details and the app creates an entry for that specific customer

<br>

![VRF](https://i.imgur.com/FhsDYjY.png)

Here is the vehicle registration form, where the customer can enter the details for their vehicle which will then create and entry of that vehicle.

<br>

The application also has the ability to read the current entries, update a specific entry based on the 'id' input as well as delete a specific entry which will be demonstrated in the presentation. 

<br>


## **Unit Testing**

![test](https://i.imgur.com/wci0U28.png)

Here we can see the test coverage that was conducted within the app.py which was provided with the expected outputs from the code. Upon comparison the achieved coverage was 54% which will be elaborated upon in the following issus section.

## **Issues while conducting the Project**

There were multiple issues that were encountered in this project, the main one being multiple steps of troubleshooting which eats away at key development time.

Testing and deployment through Jenkins was the only aspects of this project that I was not able to meet the requirements for. The reason for this being, the comlexity of the tasks, had I more time assigned for the project I believe I would have been able to achieve these requirements.

In the future, I plan to overcome issues such as this by doing some extra independent research on those areas of functionality and also do some more practice in the spare time I have so that I am able to improve this application with the implementation of those requirements moving forward.




