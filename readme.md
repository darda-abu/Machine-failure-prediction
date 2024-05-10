# Project Name

This project aims to predict machine falures depending on different criteria.

## Usage

- The [`app/main`](app/main) file serves as the main entry point for the application.
- Data-related work is stored in the [`data`](data) directory. The primary file for data processing is [`data/process.ipynb`](data/process.ipynb).
- Model training files are located in the [`model`](model) directory. The main training code resides in [`model/train.ipynb`](model/train.ipynb).

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/darda-abu/Machine-failure-prediction.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Machine-failure-prediction
    ```

3. Ensure Docker is installed on your system.

4. Build the Docker image and run the container using the provided Dockerfile:

    ```bash
    docker compose up --build
    ```

## USAGE

### Model 
#### Performance of DIfferent models
![image](https://github.com/darda-abu/Machine-failure-prediction/assets/167751588/35940227-e331-4269-8be9-b99332a11055)

#### Choosing Light Gradient Boosting Machine as it performs better than the others.
![image](https://github.com/darda-abu/Machine-failure-prediction/assets/167751588/befd5e2a-5581-450a-8249-e47996a36ac5)

### Predicting in postman
![image](https://github.com/darda-abu/Machine-failure-prediction/assets/167751588/56fe203e-957c-4662-a576-cac42e86d2d7)


