import requests
from datetime import datetime

BASE_URL = "http://0.0.0.0:8000"


def print_response(response):
    print(response.status_code)
    print(response.json())


def example_carbon_emissions():
    print("Carbon Emissions Example:")

    # Create a new carbon emission record
    carbon_emission_data = {
        "id": 1,
        "timestamp": datetime.now().isoformat(),
        "energy_usage_kwh": 500,
        "miles_driven": 1000,
        "other_sources": 1.0,
        "total_emission": 0  # Will be calculated by the API
    }
    response = requests.post(f"{BASE_URL}/carbon_emissions", json=carbon_emission_data)
    print("POST /carbon_emissions")
    print_response(response)

    # Get all carbon emission records
    response = requests.get(f"{BASE_URL}/carbon_emissions")
    print("GET /carbon_emissions")
    print_response(response)

    # Get a specific carbon emission record by ID
    response = requests.get(f"{BASE_URL}/carbon_emissions/1")
    print("GET /carbon_emissions/1")
    print_response(response)

    # Update an existing carbon emission record
    updated_carbon_emission_data = {
        "id": 1,
        "timestamp": datetime.now().isoformat(),
        "energy_usage_kwh": 600,
        "miles_driven": 1200,
        "other_sources": 1.5,
        "total_emission": 0  # Will be calculated by the API
    }
    response = requests.put(f"{BASE_URL}/carbon_emissions/1", json=updated_carbon_emission_data)
    print("PUT /carbon_emissions/1")
    print_response(response)

    # Delete a specific carbon emission record by ID
    response = requests.delete(f"{BASE_URL}/carbon_emissions/1")
    print("DELETE /carbon_emissions/1")
    print_response(response)


example_carbon_emissions()
