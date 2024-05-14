# To-Do List API

This repository contains a simple To-Do List API implemented in Python with the Flask framework. The API provides endpoints for managing tasks in a to-do list, including creating, retrieving, updating, and deleting tasks.

## Getting Started

To run the API locally, follow these steps:

1. Clone this repository to your local machine:
`git clone https://github.com/mohamad-jamil/automated-api-testing.git`

2. Navigate to the project directory:
`cd automated-api-testing`

3. Install the required dependencies:
`pip install -r requirements.txt`

4. Run the Flask application:
`python todo_api.py`

The API will be accessible at `http://localhost:5000`.

## Endpoints

- `POST /tasks`: Create a new task.
- `GET /tasks`: Retrieve all tasks.
- `GET /tasks/<task_id>`: Retrieve a specific task by its ID.
- `PUT /tasks/<task_id>`: Update an existing task.
- `DELETE /tasks/<task_id>`: Delete a specific task by its ID.

For more details on each endpoint, see the API documentation.

## API Documentation

The API documentation is dynamically generated and can be accessed by visiting the root URL (`http://localhost:5000`). It lists all available endpoints along with their descriptions.

## Automated Testing with Postman

Automated testing of the API can be performed using Postman. Follow these steps to set up and run automated tests:

1. Install Postman from [postman.com](https://www.postman.com/downloads/).

2. Import the Postman collection provided in the `tests` directory.

3. Set up environment variables such as base URL and authentication tokens if required.

4. Run the collection in the Postman Runner or integrate it into your CI/CD pipeline using Newman.

For detailed instructions on running automated tests with Postman, refer to the Postman documentation.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.