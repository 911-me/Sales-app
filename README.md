# Daily Sales Recorder

A simple web application that lets a small shop owner record daily sales
(product, quantity, selling price) and automatically see the total sales
amount, built with Python (Flask) and HTML/CSS.

## How to run locally

1. Install Python 3.9+.
2. Open a terminal in this folder and install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the application:

   ```
   python app.py
   ```

4. Open your browser and go to:

   ```
   http://127.0.0.1:5000
   ```

## Project structure

```
sales_app/
├── app.py              # Python backend (Flask routes, sales logic)
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # Main user interface
└── static/
    └── style.css         # Styling
```

## Features

- Add a sale (product, quantity, selling price)
- Automatic calculation of each sale's total and the grand total
- View all sales entered during the session
- Delete a single sale record
- Clear all records to start a new day
