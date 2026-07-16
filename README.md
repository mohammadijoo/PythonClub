# Python Club

A bilingual Django web platform created to organize and present Python programming projects, introduce important Python libraries and frameworks, manage user consultation requests, and connect Python learners and developers through a unified website.

Python Club was previously deployed at **pythonclub.ir**. The original live website is no longer available, but its Django source code and a video demonstration have been preserved in this repository.

## Project Overview

Python Club was designed as a multi-purpose Python programming portal rather than a simple static portfolio.

The application combines:

* A Persian and English website
* A catalog of Python project categories
* A database-driven project showcase
* A registered-user consultation portal
* User authentication and account management
* Public user profile pages
* Social authentication integrations
* English and Persian contact forms
* Responsive project-category pages
* Django administration
* Static and uploaded media management

The website was intended to provide a central location where users could explore Python technologies, view programming projects, request teaching or development services, and maintain an account for managing their requests.

## Main Capabilities

### Persian and English Interfaces

Python Club provides two dedicated user interfaces:

* Persian, using right-to-left layouts
* English, using left-to-right layouts

The project uses separate templates and URL routes for the two interfaces rather than relying entirely on automatic string translation.

Both language sections provide access to features such as:

* Home and introduction pages
* Python project categories
* Contact forms
* Account registration and login
* User profile management
* Consultation-request management
* Current and completed request pages

This structure demonstrates how a Django project can maintain two parallel user experiences while sharing the same database models and backend logic.

## Python Project Catalog

A major purpose of Python Club is to organize Python projects according to the library, framework, or programming discipline involved.

The project contains dedicated English and Persian pages for the following areas.

### Artificial Intelligence and Computer Vision

* PyTorch
* TensorFlow
* Scikit-learn
* OpenCV

### Data Science and Scientific Computing

* NumPy
* pandas
* SciPy
* Matplotlib

### Web Development

* Django
* Flask

### Desktop User Interfaces

* PyQt
* PySide
* Tkinter
* wxPython
* GTK

### Databases, Games, and Software Design

* SQLite
* Pygame
* Object-oriented programming
* Python design patterns

A central Python Projects page presents these categories as visual cards and routes visitors to a dedicated page for each technology.

The category system was intended to grow as new projects became available. Some category pages contain completed layouts or project content, while others remain prepared as placeholders for future uploads.

## Main Areas of Python Development

The website presents Python projects through several broad application areas.

### Artificial Intelligence

The artificial-intelligence section was designed for projects involving subjects such as:

* Machine learning
* Deep learning
* Neural networks
* Computer vision
* Natural-language processing
* Classification and prediction
* PyTorch
* TensorFlow
* Scikit-learn
* OpenCV

### Data Science

The data-science section covers the Python ecosystem used for:

* Numerical computation
* Data manipulation
* Scientific computing
* Data visualization
* Statistical analysis
* Dataset processing

The principal technologies represented in this section include NumPy, pandas, SciPy, and Matplotlib.

### Desktop Application Development

Python Club also introduces frameworks and libraries used to create graphical desktop applications, including:

* PyQt
* PySide
* Tkinter
* wxPython
* GTK

These sections were intended to contain practical GUI projects and examples of connecting desktop applications to databases.

### Web Development

The website includes dedicated areas for the two major Python web frameworks represented in the project:

* Django
* Flask

Python Club itself is an example of a complete website developed with Django.

### Game Development and Software Architecture

Additional sections cover:

* Pygame projects
* Object-oriented Python practices
* Python design patterns
* SQLite-backed applications

## Database-Driven Project Showcase

The home page is capable of loading project information from the database.

Each project record can contain:

* Title
* Description
* Image
* External URL

This makes it possible to manage featured projects through Django rather than embedding every project permanently into the HTML templates.

Projects can be displayed visually on the home page and linked to:

* Source-code repositories
* Demonstration pages
* Videos
* Documentation
* Download pages
* External websites

The project model and Django administration provide a foundation for expanding the website into a larger Python project directory.

## Consultation and Request Portal

Python Club contains an authenticated request-management system implemented through the `Todo` model.

Although the internal Django application uses task-oriented naming, the website presents these records to users as consultation or project requests.

Registered users can:

* Create a new request
* Add a title
* Add a detailed description
* Mark a request as important
* View their active requests
* Edit an existing request
* Mark a request as completed
* View completed requests
* Delete a request

Each request belongs to a specific user.

Backend views use both authentication checks and user-based database filtering, ensuring that users retrieve and modify only their own requests.

### Request Data

Each request stores:

* Title
* Description or memo
* Creation time
* Completion time
* Importance status
* Owning user

Active requests are identified by the absence of a completion date. Completed requests are ordered by their completion time.

### English and Persian Request Pages

The same request data is available through separate English and Persian templates.

This provides language-specific interfaces without duplicating the underlying request records or business logic.

The request-management routes remain present in the project. Depending on the selected base template, the consultation-portal navigation item may need to be re-enabled before a new deployment.

## User Registration and Authentication

Python Club extends Django’s built-in authentication functionality.

Users can:

* Register
* Log in
* Log out
* Edit account information
* Change their password
* Create a public profile
* Edit their public profile
* View profile pages
* Access authenticated consultation features

The custom registration form collects:

* Username
* First name
* Last name
* Email address
* Password
* Password confirmation

Django’s standard password validators are enabled, including:

* Password similarity validation
* Minimum-length validation
* Common-password detection
* Numeric-password detection

## User Profiles

Registered users can create extended profile pages.

A profile can contain:

* Biography
* Profile picture
* Phone number
* Skills
* Hobbies
* Personal website
* LinkedIn profile
* GitHub profile
* Stack Overflow profile
* Instagram profile
* Twitter/X profile

The application includes views for:

* Creating a profile
* Displaying a profile
* Editing a profile
* Editing the associated Django user account

These capabilities provide a foundation for building a community of Python developers, students, instructors, and project contributors.

## Social Authentication

The project includes Python Social Auth configuration for external sign-in providers.

Configured authentication backends include:

* Google
* GitHub
* Twitter/X
* Facebook
* Django username and password authentication

The provider keys and secrets in the repository are placeholders. Developers must create their own OAuth applications and configure the corresponding credentials before social login will operate.

For a secure deployment, OAuth credentials should be loaded through environment variables and must never be committed directly to Git.

## Contact Forms

Python Club contains separate Persian and English contact forms.

Visitors can submit:

* Name
* Email address
* Phone number
* Message

The server uses Django’s email system to forward the submitted information through SMTP.

The original configuration references the historical `pythonclub.ir` email server and website email address. A new deployment must replace these values with an active mail provider and valid credentials.

## Responsive Frontend

The frontend uses Django templates together with a responsive Bootstrap-based design.

Interface components include:

* Fixed responsive navigation
* Mobile navigation controls
* Project-category cards
* Portfolio grids
* Filterable project sections
* Contact forms
* User account menus
* Profile dropdowns
* Responsive images
* English left-to-right layouts
* Persian right-to-left layouts
* Font Awesome and Themify icons
* Custom local and web fonts

The application uses different base templates for Persian and English pages so that layout direction, wording, navigation, and typography can be customized independently.

## Django Administration

Django’s administration interface is enabled at:

```text
/admin/
```

Administrators can use it to manage application data such as:

* Users
* User profiles
* Consultation requests
* Portfolio projects
* Social-authentication records

The administration interface provides a foundation for maintaining the project showcase without directly editing templates or database files.

## Application Architecture

The repository is divided into three principal components.

### `pythonclubir`

The main Django project package contains:

* Global settings
* Root URL configuration
* WSGI configuration
* Deployment configuration

### `todo`

The primary website application contains:

* Home pages
* Project showcase
* Consultation requests
* Contact forms
* Persian and English project-category pages
* Shared project and request models
* Request forms
* Main frontend templates

### `members`

The account-management application contains:

* Custom registration
* Account editing
* Password changes
* Public profile creation
* Public profile editing
* Profile display pages

## Project Structure

```text
PythonClub/
├── manage.py
├── pythonclubir/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── todo/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   ├── migrations/
│   ├── templates/
│   │   ├── todo/
│   │   └── library/
│   └── static/
├── members/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── migrations/
│   └── templates/
├── media/
├── static/
└── .htaccess
```

## Technology Stack

### Backend

* Python
* Django
* Django ORM
* Django authentication
* Python Social Auth
* SQLite
* SMTP email integration

### Frontend

* HTML5
* CSS3
* JavaScript
* Django templates
* Bootstrap-based responsive components
* Font Awesome
* Themify Icons
* Persian right-to-left interface
* English left-to-right interface

### Deployment

* WSGI
* WhiteNoise
* CloudLinux Passenger
* LiteSpeed/Apache rewrite rules
* HTTPS redirection
* Static and media file handling

## Running the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/mohammadijoo/PythonClub.git
cd PythonClub
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

### 3. Install the Required Packages

The project was created with a Django 3.1-era stack and does not currently contain a complete dependency lock file.

A starting installation command is:

```bash
pip install Django Pillow social-auth-app-django whitenoise
```

For reliable reproduction, identify the original package versions or modernize the application and create a new `requirements.txt` or `pyproject.toml`.

### 4. Configure Local Settings

The original settings allow only the historical production hosts:

```python
ALLOWED_HOSTS = ["pythonclub.ir", "www.pythonclub.ir"]
```

For local development, add:

```python
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
```

A better long-term approach is to read allowed hosts from environment variables.

### 5. Configure Sensitive Values

Provide secure values for:

* Django secret key
* Debug setting
* Allowed hosts
* Email server
* Email username
* Email password
* Google OAuth client ID and secret
* GitHub OAuth client ID and secret
* Twitter/X OAuth keys
* Facebook OAuth keys

Do not commit production secrets to the repository.

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create an Administrator

```bash
python manage.py createsuperuser
```

### 8. Collect Static Files

```bash
python manage.py collectstatic
```

This is usually required for production deployment and may not be necessary for a basic development-server run.

### 9. Start the Development Server

```bash
python manage.py runserver
```

Open the Persian home page:

```text
http://127.0.0.1:8000/
```

Open the English home page:

```text
http://127.0.0.1:8000/en/
```

## Production Configuration

The repository includes historical CloudLinux Passenger and HTTPS rewrite configuration.

The original deployment used:

* CloudLinux
* Passenger
* Python 3.9 virtual environment
* LiteSpeed or Apache-compatible rewrite rules
* Forced HTTPS
* The `pythonclub.ir` domain

These paths are specific to the former server and must be replaced before deploying the application elsewhere.

## Current Repository Status

This repository preserves the source code of a formerly deployed website. It should currently be treated as a legacy Django project and technical reference rather than a production-ready package.

Important considerations include:

* The original `pythonclub.ir` deployment is offline.
* Django 3.1 is no longer a current supported release.
* `DEBUG` is enabled in the preserved settings.
* Allowed hosts reference only the former domain.
* OAuth credentials are placeholders.
* SMTP settings reference the former domain.
* Some external links may no longer be active.
* Some Python project-category pages are placeholders.
* A complete dependency file is not included.
* Automated tests are minimal or absent.
* Some bilingual views and templates contain repeated logic.
* Historical server paths remain in `.htaccess`.

## Recommended Modernization

Before deploying the project again, consider:

* Upgrading Django to a currently supported version
* Using a supported Python release
* Creating a complete dependency lock file
* Moving configuration to environment variables
* Setting `DEBUG=False` in production
* Rotating the Django secret key
* Replacing historical SMTP configuration
* Recreating OAuth applications
* Replacing obsolete domain links
* Reviewing all uploaded media
* Adding automated tests
* Adding GitHub Actions
* Adding form-level validation
* Adding permission tests for request access
* Re-enabling the consultation navigation where required
* Reducing duplicated English and Persian view logic
* Using reusable template components
* Adding project search and filtering
* Adding project detail pages
* Adding pagination to large project collections
* Migrating from SQLite to PostgreSQL for a larger deployment
* Adding Docker and Docker Compose support
* Conducting accessibility and security reviews

Run Django’s deployment checks with:

```bash
python manage.py check --deploy
```

## Potential Uses

This repository can be useful as:

* A bilingual Django website example
* A Persian right-to-left Django interface reference
* A Django authentication example
* A Python Social Auth integration reference
* A per-user request-management example
* A database-driven project portfolio
* A Python library catalog
* A starting point for a programming education portal
* A reference for deploying Django with CloudLinux Passenger
* A legacy Django modernization project

## Historical Website

The original website was formerly available at:

```text
https://pythonclub.ir
```

The domain is no longer serving this Django application. The source code remains available here as an archive of the platform and as a reference for Django developers.

## Website Demonstration

The following video presents the original Python Club website and demonstrates its interface and major capabilities.

<a href="https://www.youtube.com/watch?v=LENnMkPYLq8" target="_blank" rel="noopener noreferrer">
  <img src="https://mohammadijoo.ir/image/Python_Club.jpg" alt="Python Club website demonstration">
</a>

## Author

Created by [Abolfazl Mohammadijoo](https://github.com/mohammadijoo).
