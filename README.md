# Vendor-Management-System

# Introduction

This is a Vendor Management System using Django and Django REST Framework. This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics


### Main features

* Vendor Profile Management

* Purchase Order Tracking

* Vendor Performance Evaluation

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd {{ project_name }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

And navigate to http://127.0.0.1:8000/

# Creating SuperUser

First clone the repository from Github and switch to the new directory:

    $ python manage.py createsupruser
    
Then enter the Username.
    
Then Enter the e-mail Address, Password and the Confirm Password.

# Admin Pannel

Run the server:

    $ python manage.py runserver

And navigate to http://127.0.0.1:8000/admin/

# API Endpoints

### Vendor Profile Management:
Create a new vendor

    $ POST /api/vendors/
    
List all vendors

    $ GET /api/vendors/
    
Retrieve a specific vendor's details

    $ GET /api/vendors/{vendor_id}/

Update a vendor's details

    $ PUT /api/vendors/{vendor_id}/
    
Delete a vendor
    $ DELETE /api/vendors/{vendor_id}/
