## Logging Labs: Iris Dataset Classification with RandomForest + Python Logging

### Overview

This lab is an extended version of a basic logging example, demonstrating how to use logging in a real machine learning pipeline. Instead of simply printing log messages, it focuses on how logging can be utilized to track the steps in the machine learning workflow, including model training, predictions, and exception handling. The dataset used is the Iris dataset from sklearn.datasets, and the model used is the RandomForestClassifier.

### Key Features of the Lab

## Logging Setup:

Uses the built-in Python logging module.

Configures logging to include timestamps, logger name, level, and message.

Logs both to the console and to a .log file.

### ML Pipeline:

Loads the Iris dataset from sklearn.datasets.

Splits the dataset into training and test sets.

Trains a RandomForestClassifier model and logs the training process.

Makes predictions and logs the model’s accuracy.

### Exception Handling and Logging:

Demonstrates how to log exceptions with full traceback for debugging.

Includes intentional exceptions, such as a ZeroDivisionError and ValueError, to show how errors can be caught and logged.

### Logging Features:

Logs to the console (default behavior).

Uses a custom logger with multiple handlers: StreamHandler for console output and FileHandler for saving logs to a file.

Logs error messages with stack traces for easier debugging.

## Comparison: My Lab vs Professor’s Lab 

| Feature               | Professor’s Lab          | My Lab                               |
| --------------------- | ------------------------ | ------------------------------------ |
| **Dataset**           | None (simple print logs) | Iris dataset (sklearn)               |
| **Model**             | None                     | `RandomForestClassifier`             |
| **Pipeline Logging**  | ❌                        | ✔ Full ML pipeline                   |
| **Exception Logging** | Basic                    | Multiple exceptions + traceback      |
| **File Logging**      | ❌                        | ✔ Saves `.log` file                  |
| **Custom Logger**     | Minimal                  | ✔ Named loggers (`ml_pipeline_iris`) |
| **Handlers**          | None                     | ✔ StreamHandler + FileHandler        |


### How to Run the Lab
Option 1 — Google Colab

Open the notebook in Google Colab.

Select Runtime → Run all.

Logs will appear in the cell outputs.

.log files will be created automatically.

Option 2 — Local Machine


Install required dependencies:
```bash
pip install -r requirements.txt
```

Run the Python script:
```bash
python your_logging_file.py
```

