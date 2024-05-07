# RE WOW PETS

This application has been developed using Python, Flask, SQLAlchemy (ORM), HTML, Jinja2, CSS, and Bootstrap. The database used is PostgreSQL, and deployment has been done on Supabase.

## ER MODEL
![RE-WOW DIAGRAM ER](https://github.com/cristiancastano852/Re_Wow_Pets/assets/44209773/bea25ce5-2388-4f37-869e-7ed6c3ac65c5)

## Current Views

- **Login**: This view provides the user interface for logging into the application. Currently, only the interface has been developed, and the login functionality is not yet implemented.

- **Create Pet**: In this view, users can add a new pet to their profile. Data such as name, species, breed, etc., is collected and stored in the database.

- **Medical History**: Here users can view the medical history of their pets. Details such as previous vet visits, administered vaccines, treatments, etc., are displayed.

- **Create Appointments**: This view allows users to schedule new appointments for their pets. Details such as date, time, reason for the appointment, etc., are collected.

## Installation

1. Clone this repository to your local machine.
2. Install project dependencies by running `pip install -r requirements.txt`.
3. Set up the PostgreSQL database and update the application configuration in `config.py`.
4. Run the application by executing `flask run` in your terminal.
