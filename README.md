# Django REST API for Admin and User App Management

## Overview
This Django-based web application provides a platform where admins can add Android apps along with the points users can earn by downloading them. Users can view these apps, track their earned points, and submit screenshots for verification of completed tasks.

## Features
- **Admin Facing:**
  - Admin can add Android apps.
  - Admin assigns points to users for downloading apps.
  
- **User Facing:**
  - Users can sign up, log in, and manage their profile.
  - Users can view the list of available apps along with the associated points.
  - Users can track their earned points and completed tasks.
  - Users can upload a screenshot to verify that they have downloaded a particular app.
  
## Requirements
- Python 3.9+
- Django 3.x or higher
- Django REST Framework
- Django Allauth (for authentication)
- Pillow (for handling image uploads)
  
## Installation

1. Clone the repository

    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Install the dependencies

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations

    ```bash
    python manage.py migrate
    ```

4. Create a superuser (for Admin)

    ```bash
    python manage.py createsuperuser
    ```

5. Run the server

    ```bash
    python manage.py runserver
    ```

    Visit the application at `http://127.0.0.1:8000/`.

## API Documentation

### Endpoints

#### User Authentication
- **POST** `/auth/signup/`: User registration endpoint.
- **POST** `/auth/login/`: User login endpoint.

#### Admin APIs
- **POST** `/admin/app/`: Admin can add an Android app and assign points to users.
- **GET** `/admin/apps/`: Admin can see the list of apps added.

#### User APIs
- **GET** `/apps/`: Users can view the list of available apps and the points they can earn.
- **GET** `/user/profile/`: Users can view their profile, earned points, and completed tasks.
- **POST** `/user/upload-screenshot/`: Users can upload screenshots for task completion verification.

### Authentication & Permissions
- **JWT Authentication** is used for securing the endpoints.
- Admins have special permissions to add apps and view all user activity.
- Users can only access their own profile, apps, and uploaded screenshots.

### Permissions
- **Admin:**
  - `IsAdminUser` permission for all admin-related endpoints.
  
- **User:**
  - `IsAuthenticated` permission for user-facing endpoints.

### Example Response for User Profile

```json
{
    "name": "John Doe",
    "profile": "https://example.com/user-profile.jpg",
    "points_earned": 150,
    "tasks_completed": [
        {
            "task_name": "Download XYZ App",
            "task_completed": true,
            "screenshot_url": "https://example.com/screenshot.jpg"
        }
    ]
}
