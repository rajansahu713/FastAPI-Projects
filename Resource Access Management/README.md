# FastAPI Role-Based Resource Access Management
This repository contains a FastAPI application for role-based access control (RBAC) to manage resources. It provides endpoints for user authentication and authorization, allowing different roles to access resources with specific permissions.

Features
Role-based authentication and authorization.
Dynamic configuration of resource access control.
User management for registration and authentication.
Endpoint to manage resources with different permissions.
Easy-to-understand code structure and documentation.
Installation
Clone the repository:

```bash
git clone https://github.com/rajansahu713/FastAPI-Projects.git
```
Navigate to the Role Base Resource Access Management directory:

```bash
cd FastAPI-Projects/Role\ Base\ Resource\ Access\ Management
```
Install dependencies:

```bash
pip install -r requirements.txt
```
## Usage

Run the FastAPI application:

```bash
uvicorn main:app --reload
```
Access the FastAPI interactive documentation at http://localhost:8000/docs to explore available endpoints and interact with the API.

## Configuration
Role-based access control configuration is defined in the RESOURCES_FOR_ROLES dictionary within the application code (main.py).
User data and authentication logic are managed in the USERS dictionary and authentication functions (authenticate_user, get_password_hash) in the application code.
Optionally, excluded paths from permission checks can be configured in the EXCLUDED_PATHS list within the application code.
Contributing
Contributions to this project are welcome. Feel free to open issues for bug reports, feature requests, or suggestions, and submit pull requests to contribute improvements.


Creditional for Generating Token

```json
# 1
{
    "username": "user1",
    "password": "password"
}

# 2

{
    "username": "admin1",
    "password": "password"
}

```
