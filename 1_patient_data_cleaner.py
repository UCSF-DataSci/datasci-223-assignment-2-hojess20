#!/usr/bin/env python3
"""
Patient Data Cleaner

This script standardizes and filters patient records according to specific rules:

Data Cleaning Rules:
1. Names: Capitalize each word (e.g., "john smith" -> "John Smith")
2. Ages: Convert to integers, set invalid ages to 0
3. Filter: Remove patients under 18 years old
4. Remove any duplicate records

Input JSON format:
    [
        {
            "name": "john smith",
            "age": "32",
            "gender": "male",
            "diagnosis": "hypertension"
        },
        ...
    ]

Output:
- Cleaned list of patient dictionaries
- Each patient should have:
  * Properly capitalized name
  * Integer age (≥ 18)
  * Original gender and diagnosis preserved
- No duplicate records
- Prints cleaned records to console

Example:
    Input: {"name": "john smith", "age": "32", "gender": "male", "diagnosis": "flu"}
    Output: {"name": "John Smith", "age": 32, "gender": "male", "diagnosis": "flu"}

Usage:
    python patient_data_cleaner.py
"""

import json
import os

def load_patient_data(filepath):
    """
    Load patient data from a JSON file.
    
    Args:
        filepath (str): Path to the JSON file
        
    Returns:
        list: List of patient dictionaries
    """
    # BUG: No error handling for file not found
    # FIX: Added try/except FileNotFoundError
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return []


def clean_patient_data(patients):
    """
    Clean patient data by:
    - Capitalizing names
    - Converting ages to integers
    - Filtering out patients under 18
    - Removing duplicates
    
    Args:
        patients (list): List of patient dictionaries
        
    Returns:
        list: Cleaned list of patient dictionaries
    """
    cleaned_patients = []
    seen = set()  # FIX: Added set to track duplicates using patient tuples

    
    for patient in patients:
        # BUG: Typo in key 'nage' instead of 'name'
        # FIX: Corrected typo 'nage' to 'name' and capitalized properly
        patient['name'] = patient.get('name', '').title()
        
        # BUG: Wrong method name (fill_na vs fillna)
        # FIX: Convert age to integer, set to 0 if invalid
        try:
            patient['age'] = int(patient.get('age', 0))
        except (ValueError, TypeError):
            patient['age'] = 0
        
        # # BUG: Wrong method name (drop_duplcates vs drop_duplicates)
        # patient = patient.drop_duplicates()
        # # BUG: Wrong comparison operator (= vs ==)
        # if patient['age'] = 18:
        #     # BUG: Logic error - keeps patients under 18 instead of filtering them out
        #     cleaned_patients.append(patient)
        
        # FIX: Corrected logic to only keep patients age 18 and over
        if patient['age'] >= 18:
            # FIX: Use to track duplicates
            dedup_key = tuple(patient.items())
            if dedup_key not in seen:
                seen.add(dedup_key)
                cleaned_patients.append(patient)
            
    
    # BUG: Missing return statement for empty list
    if not cleaned_patients:
        return None
    
    return cleaned_patients

def main():
    """Main function to run the script."""
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the data file
    data_path = os.path.join(script_dir, 'data', 'raw', 'patients.json')
    
    # BUG: No error handling for load_patient_data failure
    # FIX: Handled potential loading failure
    patients = load_patient_data(data_path)
    if not patients:
        return
    
    # Clean the patient data
    cleaned_patients = clean_patient_data(patients)
    
    # BUG: No check if cleaned_patients is None
    # FIX: Handled case where cleaned_patients is None
    if not cleaned_patients:
        print("No valid patients found.")
        return
    
    # Print the cleaned patient data
    print("Cleaned Patient Data:")
    for patient in cleaned_patients:
        # BUG: Using 'name' key but we changed it to 'nage'
        # FIX: corrected reference to key 'name'
        print(f"Name: {patient['name']}, Age: {patient['age']}, Diagnosis: {patient['diagnosis']}")
    
    # Return the cleaned data (useful for testing)
    return cleaned_patients

if __name__ == "__main__":
    main()