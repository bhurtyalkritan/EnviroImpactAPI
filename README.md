# Environmental API for Tracking Pollution, Water Wastage, and Deforestation

This is a FastAPI-based application that provides an API for tracking carbon emissions, water wastage, and deforestation impact. The API allows you to create, read, update, and delete records for each of these environmental issues.

## Features

- **Carbon Emissions**: Track energy usage, miles driven, and other sources of carbon emissions. The API calculates the total emission based on predefined emission factors.
- **Water Wastage**: Monitor daily water usage from showers, dish washing, and other sources. The API calculates the total water wastage based on average usage rates.
- **Deforestation Impact**: Track the weight of products and estimate the number of trees cut and animals displaced based on predefined estimation logic.

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies by running `pip install -r requirements.txt`.

## Usage

1. Start the FastAPI application by running `python main.py`.
2. The API will be accessible at `http://0.0.0.0:8000`.
3. Use an API client or tools like Postman, cURL, or the provided Python script to interact with the API endpoints.

## API Endpoints

### Carbon Emissions

- `GET /carbon_emissions`: Get a list of all carbon emission records.
- `GET /carbon_emissions/{emission_id}`: Get a specific carbon emission record by ID.
- `POST /carbon_emissions`: Create a new carbon emission record.
- `PUT /carbon_emissions/{emission_id}`: Update an existing carbon emission record by ID.
- `DELETE /carbon_emissions/{emission_id}`: Delete a specific carbon emission record by ID.

### Water Wastage

- `GET /water_wastage`: Get a list of all water wastage records.
- `GET /water_wastage/{wastage_id}`: Get a specific water wastage record by ID.
- `POST /water_wastage`: Create a new water wastage record.
- `PUT /water_wastage/{wastage_id}`: Update an existing water wastage record by ID.
- `DELETE /water_wastage/{wastage_id}`: Delete a specific water wastage record by ID.

### Deforestation Impact

- `GET /deforestation_impact`: Get a list of all deforestation impact records.
- `GET /deforestation_impact/{impact_id}`: Get a specific deforestation impact record by ID.
- `POST /deforestation_impact`: Create a new deforestation impact record.
- `PUT /deforestation_impact/{impact_id}`: Update an existing deforestation impact record by ID.
- `DELETE /deforestation_impact/{impact_id}`: Delete a specific deforestation impact record by ID.
