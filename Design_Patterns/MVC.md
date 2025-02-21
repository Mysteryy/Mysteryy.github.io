---
layout: default
title: MVC
---
# MVC (Model View Controller)

## **What is MVC?**

The Model-View-Controller (MVC) framework is an architectural/design pattern that separates an application into three main logical components Model, View, and Controller. 

## **Features of MVC**

* It provides a clear separation of business logic, UI logic, and input logic.  
* It offers full control over your HTML and URLs which makes it easy to design web application architecture.  
* It is a powerful URL-mapping component using which we can build applications that have comprehensible and searchable URLs.  
* It supports Test Driven Development (TDD).

## **Components Defined**

### Model:

The Model component corresponds to all the data-related logic that the user works with. This can represent either the data that is being transferred between the View and Controller components or any other business logic-related data. It can add or retrieve data from the database. It responds to the controller’s request because the controller can’t interact with the database by itself. The model interacts with the database and gives the required data back to the controller.

#### Responsibilities:

Managing data: CRUD (Create, Read, Update, Delete) operations.  
Enforcing business rules.  
Notifying the View and Controller of state changes.

#### Example:
In a bookstore application, the Model would handle data related to books, such as the book title, author, price, and stock level.

### View:

The View component is used for all the UI logic of the application. It generates a user interface for the user. Views are created by the data which is collected by the model component but these data aren’t taken directly but through the controller. It only interacts with the controller.

#### Responsibilities:

Rendering data to the user in a specific format.  
Displaying the user interface elements.  
Updating the display when the Model changes.  

#### Example:
In a bookstore application, the View would display the list of books, book details, and provide input fields for searching or filtering books.

### Controller:

The controller is the component that enables the interconnection between the views and the model so it acts as an intermediary. The controller doesn’t have to worry about handling data logic, it just tells the model what to do. It processes all the business logic and incoming requests, manipulates data using the Model component, and interact with the View to render the final output.

#### Responsibilities:

Receiving user input and interpreting it.  
Updating the Model based on user actions.  
Selecting and displaying the appropriate View.  

#### Example:
In a bookstore application, the Controller would handle actions such as searching for a book, adding a book to the cart, or checking out.