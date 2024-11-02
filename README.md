# CashFlow

CashFlow is a web application designed to help users manage their financial transactions, including incomes and expenses. The application provides a dashboard to view all transactions, track goals, and calculate the balance.

## Features

- Add, edit, and delete income and expense transactions.
- View transactions in a table with alternating row colors for better readability.
- Track financial goals and their progress.
- Calculate total income, total expenses, and balance.
- Download transaction history.

## Technologies Used

- Django: Backend framework
- Bootstrap: Frontend framework for responsive design
- FontAwesome: Icons
- Google Fonts: Material Symbols for icons
- jQuery: JavaScript library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/CashFlow.git
    cd CashFlow
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000/` to access the application.

## Usage

### Adding Transactions

1. Navigate to the dashboard.
2. Use the forms provided to add income or expense transactions.
3. Fill in the details and submit the form.

### Viewing Transactions

1. Transactions are displayed in a table on the dashboard.
2. Rows alternate colors for better readability.
3. Icons indicate whether a transaction is an income or an expense.

### Tracking Goals

1. Add financial goals using the provided form.
2. Track the progress of each goal on the dashboard.
