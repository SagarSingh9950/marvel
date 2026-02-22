#!/bin/bash
# Quick test script for QR API
# Run this to diagnose QR generation issues

echo "==========================================="
echo "QR Attendance API - Quick Test"
echo "==========================================="
echo ""

# Test 1: Health Check
echo "1️⃣  Testing Backend Health..."
curl -s http://localhost:8000/api/health | python -m json.tool || echo "❌ Backend not running"
echo ""

# Test 2: Simple QR
echo "2️⃣  Testing Simple QR Generation..."
curl -s -X POST http://localhost:8000/api/qr-attendance/test/generate-qr-simple \
  -H "Content-Type: application/json" | python -m json.tool
echo ""

# Test 3: Full QR with Sample Data
echo "3️⃣  Testing Full QR Generation..."
curl -s -X POST http://localhost:8000/api/qr-attendance/faculty/generate-qr \
  -H "Content-Type: application/json" \
  -d '{
    "faculty_id": "FAC001",
    "faculty_name": "Dr. Sharma",
    "faculty_email": "sharma@college.edu",
    "subject_code": "CS-302",
    "subject_name": "Computer Networks",
    "branch": "CS",
    "semester": 4,
    "section": "A",
    "lecture_date": "2026-02-22T10:00:00",
    "lecture_start_time": "2026-02-22T10:00:00",
    "lecture_duration_minutes": 50,
    "qr_validity_minutes": 3,
    "center_latitude": 26.8467,
    "center_longitude": 80.9462,
    "geo_fence_radius_meters": 50.0,
    "location_name": "Lab 301",
    "total_students_expected": 60,
    "allow_screenshot_scan": false,
    "require_device_verification": true
  }' | python -m json.tool
echo ""

echo "==========================================="
echo "Test Complete!"
echo "==========================================="
