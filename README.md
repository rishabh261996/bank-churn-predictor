![image](https://github.com/user-attachments/assets/a4960206-4250-43cb-a1cf-1a3ca3dda8d9)

# Bank Churn Prediction Website

![Bank Churn Prediction](https://your-link-to-image.com/banner.png)

## Overview

The **Bank Churn Prediction Website** is a Flask-based web application that predicts whether a bank customer will churn (leave the bank) based on various features such as credit score, balance, age, and tenure. The website uses a pre-trained machine learning model that was trained on customer data, and it provides users with an easy-to-use interface to input customer data and receive predictions.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [How to Run](#how-to-run)
- [Usage](#usage)
- [Demo](#demo)
- [Contributing](#contributing)
- [License](#license)

## Features

- Predicts customer churn using machine learning.
- User-friendly interface to input customer data.
- Provides instant feedback on the prediction.
- Uses Flask for the backend and Gunicorn for production deployment.

## Technologies Used

- **Python** (Flask, scikit-learn)
- **Gunicorn** (for production server)
- **HTML/CSS** (for frontend)
- **scikit-learn** (for machine learning model)
- **StandardScaler** (for scaling input data)

## How to Run

### Prerequisites

- Python 3.x
- `pip` for installing required Python packages
- Git for cloning the repository

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/bank-churn-predictor.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd bank-churn-predictor
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application using Gunicorn:
   ```bash
   gunicorn app:app
   ```

   By default, the app will be accessible at `http://127.0.0.1:8000`.

### Run in Development Mode

If you want to run the application in development mode (using Flask’s built-in server):

```bash
python app.py
```

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:8000`.
2. You will see a form to input customer data such as **credit score**, **age**, **tenure**, etc.
3. Fill out the form and click on the **Predict** button.
4. The website will display the prediction (whether the customer is likely to churn or not).

## Demo

You can access the live demo of the project:

https://bank-churn-predictor-3o97.onrender.com/




## Machine Learning Model

The machine learning model is trained using the following features from the dataset:

- **credit_score**
- **country**
- **gender**
- **age**
- **tenure**
- **balance**
- **products_number**
- **credit_card**
- **active_member**
- **estimated_salary**

The model is trained using `scikit-learn` and saved using `pickle`.

## Contributing

Contributions are welcome! Here’s how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

```

### Explanation:
- **Overview**: Provides a summary of what the project does.
- **Technologies Used**: Lists the technologies (Flask, Gunicorn, scikit-learn) used in the project.
- **How to Run**: Explains how users can set up and run the project on their own machines.
- **Usage**: Guides users on how to interact with the web app.
- **Demo**: Place a link to your live deployment here if you have deployed the app (e.g., on Heroku, Render, or any hosting service).
- **Screenshots**: Place images of your app, such as the homepage or results page.
- **Machine Learning Model**: Explains the features used for the prediction and the model.
- **Contributing**: Instructions for other developers who might want to contribute to the project.
- **License**: Information about the project’s license.

### Images and Links:
- Replace the placeholders like `https://your-link-to-image.com/banner.png` with actual links to images (either hosted or stored in your repo).
- Replace `https://github.com/rishabh261996/bank-churn-predictor.git` with your actual GitHub repo URL.
- Replace `https://bank-churn-predictor-3o97.onrender.com/predict` with the live demo URL if you've deployed the project.

Let me know if you need any more details or adjustments!
