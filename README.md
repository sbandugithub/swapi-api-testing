API Testing Framework for SWAPI (Star Wars API for Planets)

## Description
This is a simple API testing framework for the Star Wars API for Planets (SWAPI). The framework is written in Python and uses the requests library to interact with the API. The framework includes a set of test cases that validate the response from the API for various endpoints.

## Installation
1. Clone the repository

```
git clone https://github.com/sbandugithub/swapi-api-testing.git
```
2. Install the required dependencies using the following command:
```
pip install -r requirements.txt
```
## Running Tests
Run tests using pytest:

```
pytest
```

##Project Structure
```
├── tests/
│   ├── test_planets.py  # Contains all planet-related API tests
├── requirements.txt  # Dependencies
├── pytest.ini  # Pytest settings (log level, etc.)
├── README.md  # Project documentation
```

## Test Cases Overview
The test cases are written in the tests/test_planets.py file. The test cases validate the response from the API for the following endpoints:

1) test_get_planet_details_by_id - Validate planet details by ID.(This test executes for 02 planets which are parameterized).

2) test_response_time - Ensure API response is under acceptable limits.

3) test_invalid_planet - Check response for a non-existent planet.

4) test_get_all_planets - Validate response for fetching all planets.

5) test_get_planet_by_name - Fetch planet by name using search.

6) test_get_length_of_films_for_individual_planets - Verify films count for a planet.

7) test_to_check_films_are_in_list - Ensure films are returned in list format.

8) test_get_the_list_of_residents_from_individual_planet - Validate residents list for a planet.

9) test_pagination_to_check_next_page_link_exist - Check pagination functionality.

10) test_schema_validation - Validate API response schema.

11) test_content_type - Ensure correct content-type (JSON).

## Logging & Reporting

Run tests with logging and HTML report generation:
```
 pytest --log-level=INFO --html=report.html 
 or
 pytest tests/test_planets.py -v --log-level=INFO --html=report.html
```
## Dependencies

pytest
requests
pytest-html

## Install all dependencies using:
`
pip install -r requirements.txt
`

