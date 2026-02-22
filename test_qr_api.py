"""
Test script to diagnose QR generation API issues
Run this to test if the backend is working properly
"""

import requests
import json
from datetime import datetime, timedelta

# Test endpoint URL
BASE_URL = "http://localhost:8000/api"

def test_backend_health():
    """Test if backend is running"""
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"✓ Backend health: {response.status_code}")
        print(f"  Response: {response.json()}")
        return True
    except Exception as e:
        print(f"✗ Backend not running: {e}")
        return False

def test_qr_generation():
    """Test QR generation endpoint"""
    endpoint = f"{BASE_URL}/qr-attendance/faculty/generate-qr"
    
    # Create test data
    now = datetime.utcnow()
    data = {
        "faculty_id": "FAC001",
        "faculty_name": "Dr. Test",
        "faculty_email": "test@college.edu",
        "subject_code": "CS-101",
        "subject_name": "Python Basics",
        "branch": "CS",
        "semester": 1,
        "section": "A",
        "lecture_date": now.isoformat(),
        "lecture_start_time": now.isoformat(),
        "lecture_duration_minutes": 50,
        "qr_validity_minutes": 3,
        "center_latitude": 26.8467,
        "center_longitude": 80.9462,
        "geo_fence_radius_meters": 50.0,
        "location_name": "Lab 101",
        "total_students_expected": 40,
        "allow_screenshot_scan": False,
        "require_device_verification": True
    }
    
    try:
        print("\nTesting QR generation...")
        print(f"Endpoint: {endpoint}")
        print(f"Data: {json.dumps(data, indent=2, default=str)}")
        
        response = requests.post(endpoint, json=data)
        print(f"\nStatus Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 201:
            print("\n✓ QR generation successful!")
            return True
        else:
            print(f"\n✗ QR generation failed with status {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("\n✗ Cannot connect to backend server at http://localhost:8000")
        print("  Make sure to start the backend: python -m backend.main")
        return False
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("QR Attendance API Test")
    print("=" * 60)
    
    if test_backend_health():
        test_qr_generation()
    
    print("\n" + "=" * 60)
