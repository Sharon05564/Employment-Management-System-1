=========================================
Employee Management System (EMS)
==========================================
Description

The Employee Management System (EMS) is a Python desktop application developed using customtkinter for the GUI and MySQL as the database to manage employee records. It allows users to add, update, delete, search, and display employees' details such as ID, name, phone number, role, gender, and salary. This system is intended for small to medium-sized organizations that need a straightforward and easy-to-use tool to manage their employee data.

Features

Login Page: User authentication with a username and password.

Add Employee: Allows you to add new employees with details like ID, name, phone number, role, gender, and salary.

Update Employee: Update existing employee records.

Delete Employee: Delete individual employee records or all records at once.

Search Employee: Search employees by ID, name, phone, role, gender, or salary.

Display Employees: View all employees in a table format with scrollable content.

Database Integration: All employee records are stored and managed in a MySQL database.

Technologies Used

Python: Core programming language.

CustomTkinter: For building the modern GUI interface.

PIL (Pillow): Used for handling image assets.

Tkinter: Base library for GUI components.

MySQL: Relational database to store employee data.

pymysql: Python library for MySQL database connectivity.

Project Structure

bash

Copy code

├── main.py              # Main application file (EMS GUI)

├── database.py          # Database connection and queries

├── back2.jpg             # Background image for login page

├── background_ems3.jpg  # Banner image for EMS page

└── README.md            # Documentation for the project

Installation Guide

Prerequisites

Before running the project, ensure that the following are installed on your machine:

Python: Download and install Python

MySQL: Download and install MySQL

Pip Packages:

customtkinter

pillow

pymysql

You can install the required Python packages by running:

bash

Copy code

pip install customtkinter pillow pymysql

Setting up the MySQL Database

Start your MySQL server and log in with the correct credentials.

Make sure the MySQL service is running before executing the project.

The script will automatically create a database named employee_data if it doesn't already exist.

Running the Project

Clone the repository or download the project files to your machine.

Open a terminal or command prompt in the project directory.

Run the following command to start the application:
bash

Copy code

python main.py

A login window will appear. Use the following credentials to log in:

Username: Deezy

Password: 1234

Upon successful login, the Employee Management System interface will open, allowing you to manage employees.

Usage

Login: Enter the provided credentials on the login page to access the system.

Add Employee: Fill in the form fields and click Add Employee to insert new employee records.

Update Employee: Select an employee from the table, modify the details in the form, and click Update Employee.

Delete Employee: Select an employee and click Delete Employee or click Delete All to remove all records.

Search Employee: Use the search box to filter employees by the specified criteria.

Show All: Click the Show All button to reset the search and display all employees.


License

This project is open-source.

Author

Owusu Sharon Addai

Feel free to reach out for any further questions or contributions to the project.
