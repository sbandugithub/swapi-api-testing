import requests
from os import getenv
import pytest
import logging

logger = logging.getLogger(__name__)


class TestPlanets:

    @pytest.fixture(scope="class")
    def session(self, request):
        """Create a session to be used in all tests within this class."""
        request.cls.session = requests.Session()
        request.cls.base_url = getenv('SWAPI_BASE_URL', 'https://swapi.dev/api/planets')

    @pytest.mark.usefixtures("session")
    class TestWithSession:
        @pytest.mark.parametrize("planet_id, expected_name", [
            (1, 'Tatooine'),
            (2, 'Alderaan'),

        ])
        def test_get_planet_details_by_id(self, planet_id, expected_name):
            # Test fetching details for various planets.
            response = self.session.get(f"{self.base_url}/{planet_id}/")
            data = response.json()
            assert response.status_code == 200, "Expected status code to be 200"
            assert data['name'] == expected_name, f"Expected planet's name to be {expected_name}"
            assert 'population' in data, "Expected response to include the planet's population"
            logger.info(f"The population of the planet is {data['population']}")

        def test_response_time(self):
            # Test that the API response time is within acceptable limits.
            response = self.session.get(f"{self.base_url}/1/")
            assert response.elapsed.total_seconds() < 5, "Response time is too high"
            logger.info(f"The response time is {response.elapsed.total_seconds()}")

        def test_invalid_planet(self):
            """Test fetching details for a non-existent planet to check error handling."""
            response = self.session.get(f"{self.base_url}/999/")
            assert response.status_code == 404, "Expected status code to be 404"

        def test_get_all_planets(self):
            # Test fetching all planets to ensure the endpoint is reachable and returns expected data structure.
            response = self.session.get(f"{self.base_url}/")
            data = response.json()
            assert response.status_code == 200, "Expected status code to be 200"
            assert isinstance(data["results"], list), "'results' should be a list of planets"
            logger.info(f"The total count of the planet is {data['count']}")

        def test_get_planet_by_name(self):
            # Test fetching a planet by name to ensure the endpoint is reachable and returns expected data structure.
            response = self.session.get(f"{self.base_url}/?search=Tatooine")
            data = response.json()
            assert response.status_code == 200, "Expected status code to be 200"
            assert data["results"][0]["name"] == "Tatooine", "Expected planet's name to be Tatooine"
            logger.info(f"The population of the planet is {data['results'][0]}")

        def test_get_length_of_films_for_individual_planets(self):
            # Test fetching a planet by name to ensure the endpoint is reachable and returns expected data structure.
            response = self.session.get(f"{self.base_url}/?search=Tatooine")
            data = response.json()
            assert response.status_code == 200, "Expected status code to be 200"
            assert data["results"][0]["name"] == "Tatooine", "Expected planet's name to be Tatooine"
            logger.info(f"The number of films the planet appears in is  {len(data['results'][0]['films'])}")

        def test_to_check_films_are_in_list(self):
            # This test is to check that a planet has a valid list of residents and isinstance is a function checks
            # If String is added instead of list then the test gets failed
            # By this we can ensure the residents everytime is released in the list format as per the requirement
            response = self.session.get(f"{self.base_url}/1")
            assert response.status_code == 200, "Expected status code 200, but got {response.status_code}"
            data = response.json()
            assert "films" in data, "Response JSON does not contain 'films' key"
            assert isinstance(data["films"], list), "'films' should be a list"
            logger.info(f"The films the planet appears in are {data['films']}")

        def test_get_the_list_of_residents_from_individual_planet(self):
            # Test fetching a planet by name to ensure the endpoint is reachable and returns expected data structure.
            response = self.session.get(f"{self.base_url}/?search=Tatooine")
            data = response.json()
            assert response.status_code == 200, "Expected status code to be 200"
            assert data["results"][0]["name"] == "Tatooine", "Expected planet's name to be Tatooine"
            logger.info(f"The films the planet appears in are {data['results'][0]['films']}")

        def test_pagination_to_check_next_page_link_exist(self):
            # Test fetching a planet by name to ensure the endpoint is reachable and returns expected data structure.
            response = self.session.get(f"{self.base_url}/?page=2")
            data = response.json()
            assert response.status_code == 200, "Expected status code to be 200"
            assert data["next"] == "https://swapi.dev/api/planets/?page=3", "Expected next page link to be present"
            logger.info(f"The next page link is {data['next']}")

        def test_schema_validation(self):
            # Validate that the response structure for a planet contains expected keys.
            response = self.session.get(f"{self.base_url}/1/")
            data = response.json()
            assert response.status_code == 200, "Expected status code to be 200"
            expected_keys = ["name", "rotation_period", "orbital_period", "diameter", "climate", "gravity", "terrain",
                             "surface_water", "population"]
            assert all(key in data for key in expected_keys), "Response does not contain expected keys"
            logger.info(f"The keys present in the response are {data.keys()}")

        def test_content_type(self):
            # Validate that the response content type is JSON.
            response = self.session.get(f"{self.base_url}/3/")
            assert response.headers["Content-Type"] == "application/json", "Expected content type to be JSON"
            logger.info(f"The content type is {response.headers['Content-Type']}")

