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

4. Build the Docker image using the provided Dockerfile:

    ```bash
    docker build -t Machine-failure-prediction .
    ```

5. Run the Docker container:

    ```bash
    docker run -it Machine-failure-prediction
    ```

## License

This project is licensed under the [nothing] - see the [LICENSE.md](LICENSE.md) file for details.

