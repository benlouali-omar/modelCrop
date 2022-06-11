# -*- coding: utf-8 -*-
"""
Created on Fri Mai 06 21:51:19 2022

@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes Crop measurements
class CropData(BaseModel):
    nitrogen: float 
    phosphorius: float 
    potassium: float 
    temperature: float
    humidity:float
    ph:float
    rainfall:float
