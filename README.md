# GradePro Student Marks Calculator

A simple Python desktop application for calculating a student's results from seven subjects. The app uses a Tkinter graphical interface and displays the total marks, average, percentage, and letter grade.

## Features

- Enter marks for Math, English, Computer, Islamiat, Pak Studies, Urdu, and Physics.
- Calculate the total, average, percentage, and grade.
- Clear all entered marks and results.
- Use the app without additional third-party Python packages.

## Requirements

- Python 3
- Tkinter, which is included with most standard Python installations

## Run the Application

From the project directory, run:

```bash
python marks_software.py
```

Enter an integer mark for each subject, then select **Calculate**. Select **Clear** to reset the form.

## Grading Rules

The application calculates the percentage using a total possible score of 550 and applies these grade boundaries:

| Percentage | Grade |
| --- | --- |
| 80% or higher | A+ |
| 70% to 79.99% | A |
| 60% to 69.99% | B |
| 50% to 59.99% | C |
| Below 50% | F |

The project currently calculates marks and percentage; it does not calculate GPA or predict future grades.

## Notes

- Each field must contain a whole number before selecting **Calculate**.
- The current program does not validate empty, non-numeric, or out-of-range input, so invalid input may cause an error.
