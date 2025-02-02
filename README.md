# Student Progression Outcome Calculator

## Description

This Python program determines the progression outcome of students based on their pass, defer, and fail credits. It checks whether a student progresses, is excluded, or needs to retrieve modules. The program stores results in a text file and displays a histogram graph of the outcomes using the `graphics` module.

## Features

- Takes user input for pass, defer, and fail credits.
- Validates input values to ensure they are within the correct range.
- Calculates and displays progression outcomes.
- Stores results in a text file (`Progression data.txt`).
- Generates a histogram graph to visualize the distribution of outcomes.

## Technologies Used

- Python
- `graphics.py` module (for histogram visualization)

## Installation & Usage

### Prerequisites

- Install Python (if not already installed)
- Ensure you have the `graphics.py` module installed. You can install it using:
  ```bash
  pip install graphics.py
  ```

### Running the Program

1. Clone or download the script.
2. Run the script using:
   ```bash
   python progression_calculator.py
   ```
3. Follow the prompts to enter student credits.
4. View the progression results and histogram graph.

## Example Usage

```
Please enter your credits at pass: 100
Please enter your credits at defer: 20
Please enter your credits at fail: 0
Your result is: Progress (Module Trailer)
Do you want to continue? (q/y): y
```

## Output

- **Text File (`Progression data.txt`)**: Stores all progression results.
- **Graphical Histogram**: Displays a bar chart of progression outcomes.

## Author

- **Name**: Meepe Gamage Binuk Yehan Dias
- **Student ID**: 2052783
- **Date**: 13/12/2023

## License

This project is for educational purposes only.
