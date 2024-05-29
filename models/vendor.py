from pydantic import BaseModel
  
class Vendor(BaseModel):
    name: str 
    contact_details: str
    address: str
    vendor_code: str 
    on_time_delivery_rate: float 
    quality_rating_avg: float 
    average_response_time: float 
    fulfillment_rate: float 

