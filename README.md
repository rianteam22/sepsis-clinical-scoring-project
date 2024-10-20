
# Clinical Score Calculation Project

This project performs clinical score calculations for patients based on infection and sepsis data, providing a comprehensive risk and prognosis analysis. It includes methods for data cleaning, validation, and processing to compute scores such as qSOFA, SOFA, SIRS, APACHE II, MODS, MEWS, SOS, omqSOFA, and omSOFA.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project is designed to help healthcare professionals quickly assess the condition of critically ill patients by using various clinical scores to monitor vital signs and other indicators. The project allows the import of patient data in CSV format, which is then processed to calculate specific scores for infection and sepsis.

## Features

- Calculation of clinical scores:
  - **qSOFA**
  - **SOFA**
  - **SIRS**
  - **APACHE II**
  - **MODS**
  - **MEWS**
  - **SOS**
  - **omqSOFA**
  - **omSOFA**
- Cleaning and validation of clinical data
- Generation of CSV files with calculated scores

## System Requirements

- Python 3.7+
- Pandas

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repository
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Data Cleaning
Use the `clean_data.py` module to clean the input data:
```python
from clean_data import clean_data

data = clean_data(df)
```

### 2. Data Validation
Use the `validate_data.py` module to validate each data row:
```python
from validate_data import validate_data

if validate_data(row):
    # Proceed with processing
```

### 3. Score Calculation
The score calculation is performed by the `calculate_scores.py` module:
```python
from calculate_scores import process_csv

input_file = 'patient_data.csv'
output_file = 'calculated_scores.csv'
process_csv(input_file, output_file)
```

### Example Execution
```bash
python calculate_scores.py --input patient_data.csv --output calculated_scores.csv
```

## Project Structure

```plaintext
.
├── calculate_scores.py     # Module for score calculation
├── clean_data.py           # Module for data cleaning
├── validate_data.py        # Module for data validation
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/feature-name`)
3. Commit your changes (`git commit -m 'Added a new feature'`)
4. Push to the branch (`git push origin feature/feature-name`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
