# Employee Management

A simple Python app to keep track of employees. You can add, remove, search, and display employee records, and everything gets saved in a CSV file for easy access later.

## What It Can Do

- **Add Employees**: Store their name, age, and department.
- **Remove Employees**: Delete them by name.
- **Search Employees**: Look up employees by name and get their details.
- **Display Employees**: See a list of everyone in the system.
- **Save Data**: All changes are saved to a CSV file when you exit.

## Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/7eves/employee-management.git
   ```
2. Move into the project folder:
   ```bash
   cd employee-management
   ```
3. Make sure you've got Python installed. You can check by running:
   ```bash
   python --version
   ```
4. (Optional) Set up a virtual environment:
   ```bash
   python -m venv myenv
   myenv\Scripts\activate  # On Windows
   ```
5. Install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use It

1. Run the script:
   ```bash
   python employee_management.py
   ```
2. Just follow the menu options to manage your employee data—add, remove, search, display, or save.

## What's Inside

```
employee-management/
│
├── employee_management.py  # The main script
├── employee_list.csv       # Where your employee data gets saved
└── README.md               # This file
```

## Contributing

Want to make this better? Fork it, make your changes, and send a pull request.

## License

This project is open-source under the [MIT License](LICENSE).
