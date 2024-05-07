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

### Purchase Order Tracking
Create a purchase order

    $ POST /api/purchase_orders/

List all purchase orders with an option to filter by vendor

    $ GET /api/purchase_orders/

Retrieve details of a specific purchase order

    $ GET /api/purchase_orders/{po_id}/

Update a purchase order

    $ PUT /api/purchase_orders/{po_id}/

Delete a purchase order

    $ DELETE /api/purchase_orders/{po_id}/

### Vendor Performance Evaluation:
Retrieve a vendor's performance metrics

(on_time_delivery_rate, quality_rating_avg, average_response_time, and fulfillment_rate along with th vendor ID)

    $ GET /api/vendors/{vendor_id}/performance

Update Acknowledgment

(This endpoint will update acknowledgment_date and trigger the recalculation of average_response_time.)

    $ POST /api/purchase_orders/{po_id}/acknowledge

# Errors
The GitHub Readme API uses standard HTTP status codes to indicate the success or failure of a request. In case of an error, additional information may be provided in the response body.

#### Common error codes include:

400 Bad Request: Invalid request parameters.

401 Unauthorized: Authentication failure.

404 Not Found: The specified resource does not exist.

403 Forbidden: Access to the requested resource is forbidden.

500 Internal Server Error: An unexpected error occurred on the server.

