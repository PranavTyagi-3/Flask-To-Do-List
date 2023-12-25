# Flask To-Do List Application

This is a simple to-do list web application built with Flask. It allows users to manage their tasks with ease.

## Features

- User authentication
- Add, edit, and delete tasks
- Upload images for tasks

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/PranavTyagi-3/Flask-To-Do-List
   ```
2. Install the required packages:
   ```
   pip install flask
   pip install sqlite3
   ```
3. Initialize the database:
   ```
   python initital_db.py
   ```
4. Run the application:
   ```
   python app.py
   ```

## Usage

After running the application, navigate to `localhost:5000` in your web browser to access the to-do list.

## File Structure

- `app.py`: The main Flask application file.
- `initital_db.py`: Script to initialize the database.
- `users.db`: SQLite database file.
- `templates/`: Contains HTML templates for the application.
- `static/`: Contains static files like CSS, JavaScript, and images.

## Contributions

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
