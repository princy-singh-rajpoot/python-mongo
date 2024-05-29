from pydantic import BaseModel

class Vendor(BaseModel):
    """
    Represents a vendor with detailed information regarding their performance and contact details.

    Attributes:
        name (str): The name of the vendor.
        contact_details (str): The contact details of the vendor, such as phone number.
        address (str): The physical address of the vendor.
        vendor_code (str): A code assigned to the vendor for identification purposes.
        on_time_delivery_rate (float): The percentage of deliveries made by the vendor on time.
        quality_rating_avg (float): The average quality rating given to the vendor.
        average_response_time (float): The average time (in hours) the vendor takes to respond to inquiries or issues.
        fulfillment_rate (float): The percentage of orders fulfilled completely and accurately by the vendor.
    """
    
    name: str 
    contact_details: str
    address: str
    vendor_code: str 
    on_time_delivery_rate: float 
    quality_rating_avg: float 
    average_response_time: float 
    fulfillment_rate: float 
