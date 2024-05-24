from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI()

# In-memory data storage (for demonstration purposes)
carbon_data = []
water_data = []
deforestation_data = []

class CarbonEmission(BaseModel):
    id: int
    timestamp: datetime
    energy_usage_kwh: float  # in kilowatt-hours
    miles_driven: float  # in miles
    other_sources: float  # in metric tons
    total_emission: float  # in metric tons

class WaterWastage(BaseModel):
    id: int
    timestamp: datetime
    daily_shower_minutes: float
    daily_dish_washing_minutes: float
    daily_other_usage_minutes: float
    total_wastage: float  # in liters

class DeforestationImpact(BaseModel):
    id: int
    timestamp: datetime
    product_weight: float  # in kg
    estimated_trees_cut: float
    estimated_animals_displaced: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Environmental API for Tracking Pollution, Water Wastage, and Deforestation"}

# Carbon Emissions Endpoints
@app.get("/carbon_emissions", response_model=List[CarbonEmission])
def get_carbon_emissions():
    return carbon_data

@app.get("/carbon_emissions/{emission_id}", response_model=CarbonEmission)
def get_carbon_emission(emission_id: int):
    for emission in carbon_data:
        if emission.id == emission_id:
            return emission
    raise HTTPException(status_code=404, detail="Emission not found")

@app.post("/carbon_emissions", response_model=CarbonEmission)
def create_carbon_emission(emission: CarbonEmission):
    # Example emission factors 
    emission_factor_energy = 0.000233  # metric tons CO2 per kWh
    emission_factor_miles = 0.000404  # metric tons CO2 per mile

    emission.total_emission = (
        emission.energy_usage_kwh * emission_factor_energy +
        emission.miles_driven * emission_factor_miles +
        emission.other_sources
    )
    carbon_data.append(emission)
    return emission

@app.put("/carbon_emissions/{emission_id}", response_model=CarbonEmission)
def update_carbon_emission(emission_id: int, updated_emission: CarbonEmission):
    for index, emission in enumerate(carbon_data):
        if emission.id == emission_id:
            # Example emission factors
            emission_factor_energy = 0.000233  # metric tons CO2 per kWh
            emission_factor_miles = 0.000404  # metric tons CO2 per mile

            updated_emission.total_emission = (
                updated_emission.energy_usage_kwh * emission_factor_energy +
                updated_emission.miles_driven * emission_factor_miles +
                updated_emission.other_sources
            )
            carbon_data[index] = updated_emission
            return updated_emission
    raise HTTPException(status_code=404, detail="Emission not found")

@app.delete("/carbon_emissions/{emission_id}")
def delete_carbon_emission(emission_id: int):
    for index, emission in enumerate(carbon_data):
        if emission.id == emission_id:
            del carbon_data[index]
            return {"message": "Emission deleted"}
    raise HTTPException(status_code=404, detail="Emission not found")
# Water Wastage Endpoints
@app.get("/water_wastage", response_model=List[WaterWastage])
def get_water_wastage():
    return water_data

@app.get("/water_wastage/{wastage_id}", response_model=WaterWastage)
def get_water_wastage_by_id(wastage_id: int):
    for wastage in water_data:
        if wastage.id == wastage_id:
            return wastage
    raise HTTPException(status_code=404, detail="Water wastage not found")

@app.post("/water_wastage", response_model=WaterWastage)
def create_water_wastage(wastage: WaterWastage):
    wastage.total_wastage = (
        wastage.daily_shower_minutes * 9 +  # average 9 liters per minute
        wastage.daily_dish_washing_minutes * 6 +  # average 6 liters per minute
        wastage.daily_other_usage_minutes * 8  # average 8 liters per minute
    )
    water_data.append(wastage)
    return wastage

@app.put("/water_wastage/{wastage_id}", response_model=WaterWastage)
def update_water_wastage(wastage_id: int, updated_wastage: WaterWastage):
    for index, wastage in enumerate(water_data):
        if wastage.id == wastage_id:
            updated_wastage.total_wastage = (
                updated_wastage.daily_shower_minutes * 9 +
                updated_wastage.daily_dish_washing_minutes * 6 +
                updated_wastage.daily_other_usage_minutes * 8
            )
            water_data[index] = updated_wastage
            return updated_wastage
    raise HTTPException(status_code=404, detail="Water wastage not found")

@app.delete("/water_wastage/{wastage_id}")
def delete_water_wastage(wastage_id: int):
    for index, wastage in enumerate(water_data):
        if wastage.id == wastage_id:
            del water_data[index]
            return {"message": "Water wastage deleted"}
    raise HTTPException(status_code=404, detail="Water wastage not found")

# Deforestation Impact Endpoints
@app.get("/deforestation_impact", response_model=List[DeforestationImpact])
def get_deforestation_impact():
    return deforestation_data

@app.get("/deforestation_impact/{impact_id}", response_model=DeforestationImpact)
def get_deforestation_impact_by_id(impact_id: int):
    for impact in deforestation_data:
        if impact.id == impact_id:
            return impact
    raise HTTPException(status_code=404, detail="Deforestation impact not found")

@app.post("/deforestation_impact", response_model=DeforestationImpact)
def create_deforestation_impact(impact: DeforestationImpact):
    # Example estimation logic
    impact.estimated_trees_cut = impact.product_weight * 0.02 
    impact.estimated_animals_displaced = impact.product_weight * 0.01  
    deforestation_data.append(impact)
    return impact

@app.put("/deforestation_impact/{impact_id}", response_model=DeforestationImpact)
def update_deforestation_impact(impact_id: int, updated_impact: DeforestationImpact):
    for index, impact in enumerate(deforestation_data):
        if impact.id == impact_id:
            # Update estimation logic
            updated_impact.estimated_trees_cut = updated_impact.product_weight * 0.02
            updated_impact.estimated_animals_displaced = updated_impact.product_weight * 0.01
            deforestation_data[index] = updated_impact
            return updated_impact
    raise HTTPException(status_code=404, detail="Deforestation impact not found")

@app.delete("/deforestation_impact/{impact_id}")
def delete_deforestation_impact(impact_id: int):
    for index, impact in enumerate(deforestation_data):
        if impact.id == impact_id:
            del deforestation_data[index]
            return {"message": "Deforestation impact deleted"}
    raise HTTPException(status_code=404, detail="Deforestation impact not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
