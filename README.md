# Point Transaction API
This Flask application provides a RESTful API to manage point transactions, allowing you to add points, spend points, and retrieve point balances for users.

## Features
Add Points: Submit a transaction to add points for a specific user.
Spend Points: Request to spend a specified number of points.
Get Balance: Retrieve the current point balance for all users.
## Requirements
Python 3
Flask
## Installation
Clone the repository:

git clone <repository-url>
cd <repository-directory>

Install Flask: You can use pip to install Flask:

pip install Flask

## Running the Application
Run the application:

python pointsAPI.py
The application will start on port 8000 by default. 

## 1. Add Points
URL: /add
Method: POST
Request Body:
{
  "payer": "string", // Name of the company adding points
  "points": number,   // Number of points to add
  "timestamp": "string" // Timestamp of the transaction in ISO 8601 format
}
Response: HTTP 200 on success, HTTP 400 on invalid request.

## 2. Spend Points
URL: /spend
Method: POST
Request Body:
{
  "points": number // Number of points to spend
}
Response:
HTTP 200 with JSON array of companies and points spent on success.
HTTP 400 if insufficient points are available or if the request is invalid.

## 3. Get Balance
URL: /balance
Method: GET
Response: HTTP 200 with a JSON object representing the current balance of each company.

## Troubleshooting
Ensure you have Python and Flask installed correctly.
Check the console for any error messages when running the application.
Make sure you send requests to the correct URL and port.
