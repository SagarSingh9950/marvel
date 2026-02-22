# 🔧 QR Session Generation API - Debugging Guide

## Quick Start

### 1. Start Both Servers

First, ensure both backend and frontend servers are running:

**Terminal 1 - Backend:**
```bash
cd "c:\Users\sagar\Downloads\MARVEL PRESENTATION"
python -m backend.main
```

**Terminal 2 - Frontend:**
```bash
cd "c:\Users\sagar\Downloads\MARVEL PRESENTATION"
node frontend\server.js
```

### 2. Test the API

#### Option A: Use the Test Page (Easiest)
Open in browser: `http://localhost:3000/qr-api-test.html`

This provides a visual interface to test all endpoints.

#### Option B: Use Python Script
```bash
python test_qr_api.py
```

#### Option C: Use curl (Windows PowerShell)
```powershell
$data = @{
    faculty_id = "FAC001"
    faculty_name = "Dr. Sharma"
    faculty_email = "test@college.edu"
    subject_code = "CS-302"
    subject_name = "Computer Networks"
    branch = "CS"
    semester = 4
    section = "A"
    lecture_date = "2026-02-22T10:00:00"
    lecture_start_time = "2026-02-22T10:00:00"
    lecture_duration_minutes = 50
    qr_validity_minutes = 3
    center_latitude = 26.8467
    center_longitude = 80.9462
    geo_fence_radius_meters = 50.0
    location_name = "Lab 301"
    total_students_expected = 60
    allow_screenshot_scan = $false
    require_device_verification = $true
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:8000/api/qr-attendance/faculty/generate-qr" `
    -Method POST `
    -Headers @{"Content-Type"="application/json"} `
    -Body $data
```

---

## API Endpoints

### 1. Health Check
**Test if backend is running**

```
GET /api/health
```

Expected Response:
```json
{
  "status": "Marvel Frontend Server Running",
  "port": 3000
}
```

---

### 2. Test QR Generation (Simple)
**Generate QR with hardcoded data - for testing**

```
POST /api/qr-attendance/test/generate-qr-simple
```

No request body needed.

Expected Response:
```json
{
  "status": "success",
  "message": "Test QR session created successfully",
  "session_id": "uuid-string",
  "id": 1
}
```

**Use this to verify:**
- Backend is running
- Database connection works
- QR session creation logic works

---

### 3. Full QR Generation (Production)
**Generate QR with complete data validation**

```
POST /api/qr-attendance/faculty/generate-qr
Content-Type: application/json
```

**Required Fields:**
```json
{
  "faculty_id": "string (min 1 char)",
  "faculty_name": "string (min 2 chars)",
  "faculty_email": "valid-email@example.com (optional)",
  "subject_code": "string (min 2 chars, e.g., 'CS-302')",
  "subject_name": "string (min 3 chars)",
  "branch": "string (min 2 chars, e.g., 'CS', 'EC')",
  "semester": "integer (1-8, required)",
  "section": "string (optional, e.g., 'A')",
  "lecture_date": "ISO datetime (2026-02-22T10:00:00)",
  "lecture_start_time": "ISO datetime (2026-02-22T10:00:00)",
  "lecture_duration_minutes": "integer (30-180 minutes)",
  "qr_validity_minutes": "integer (1-10 minutes)",
  "center_latitude": "float (-90 to 90)",
  "center_longitude": "float (-180 to 180)",
  "geo_fence_radius_meters": "float (10-200 meters)",
  "location_name": "string (optional)",
  "total_students_expected": "integer (0+, optional)",
  "allow_screenshot_scan": "boolean (default false)",
  "require_device_verification": "boolean (default true)"
}
```

---

## Common Errors & Solutions

### Error 1: "Failed to generate QR session" (Frontend Alert)

**Causes:**
1. Backend server not running
2. Invalid form data
3. Database connection failed
4. Validation error

**Solutions:**
```
1. Check if backend is running:
   - Open http://localhost:8000/api/health
   - Should return success response

2. Check form fields:
   - All required fields must be filled
   - semester must be 1-8
   - lecture_duration_minutes must be 30-180
   - qr_validity_minutes must be 1-10
   - geo_fence_radius_meters must be 10-200

3. Check browser console:
   - F12 → Console tab
   - Look for error messages
   - Check Network tab for request/response details
```

### Error 2: "Invalid input value" (from API)

**Cause:** One or more fields have invalid values

**Check:**
- Email format (if provided)
- Numeric ranges (semester, duration, etc.)
- DateTime format (must be ISO format)
- String field lengths (min/max)

### Error 3: "Failed to create QR session: [database error]"

**Cause:** Database connectivity issue

**Solutions:**
```
1. Restart the backend server
2. Check database file exists at: backend/college.db
3. If database corrupted, delete and recreate:
   - Delete backend/college.db
   - Restart backend (will auto-create)
```

### Error 4: Connection refused / Cannot connect

**Cause:** Backend server not running on port 8000

**Solutions:**
```powershell
# Check if port 8000 is in use
netstat -ano | findstr :8000

# If something is using it, kill the process
Get-Process | Where-Object {$_.Id -eq <PID>} | Stop-Process -Force

# Then restart backend
python -m backend.main
```

---

## Validation Rules

### String Fields
- `faculty_id`: min 1 char ✓
- `faculty_name`: min 2 chars ✓
- `subject_code`: min 2 chars (e.g., "CS-302") ✓
- `subject_name`: min 3 chars ✓
- `branch`: min 2 chars (e.g., "CS", "EC") ✓

### Numeric Fields
- `semester`: must be 1-8 ✓
- `lecture_duration_minutes`: must be 30-180 ✓
- `qr_validity_minutes`: must be 1-10 ✓
- `geo_fence_radius_meters`: must be 10-200 ✓
- `total_students_expected`: must be 0+ ✓
- `center_latitude`: must be -90 to 90 ✓
- `center_longitude`: must be -180 to 180 ✓

### DateTime Fields
- Must be in ISO format: `2026-02-22T10:00:00` ✓
- Can include timezone: `2026-02-22T10:00:00Z` ✓
- Backend converts to UTC automatically ✓

### Email Field
- Must be valid email format (optional)
- Example: `sharma@college.edu` ✓

---

## Testing Workflow

### Step 1: Test Health
```
✓ GET /api/health
→ Confirms backend is running
```

### Step 2: Test Simple QR
```
✓ POST /api/qr-attendance/test/generate-qr-simple
→ Confirms database and QR creation works
```

### Step 3: Test Full QR
```
✓ POST /api/qr-attendance/faculty/generate-qr
→ Confirms validation and production endpoint works
```

### Step 4: Test Frontend
```
✓ http://localhost:3000
→ Open QR Attendance page
→ Fill form and submit
→ Should see QR code displayed
```

---

## Files Added for Debugging

1. **test_qr_api.py** - Python test script
   - Tests backend health
   - Tests QR generation
   - Shows detailed responses

2. **frontend/qr-api-test.html** - Interactive test page
   - Visual interface for testing
   - Test all endpoints
   - See responses in real-time
   - Custom request builder

3. **test_qr_session.md** - This debugging guide

---

## Advanced Debugging

### Check Backend Logs
The backend prints logs to console. Look for:
```
[INFO] QR session created: <session_id>
[ERROR] Failed to create session: <error message>
```

### Check Browser Console
F12 → Console tab shows:
- Network errors
- Validation errors
- JavaScript errors
- Full response data

### Check Network Tab
F12 → Network tab shows:
- Request headers
- Request body
- Response status
- Response body (full error details)

---

## Next Steps After Fixing

Once "Error: Failed to generate QR session" is resolved:

1. ✓ QR code image should display
2. ✓ Live attendance dashboard updates
3. ✓ Students can scan the QR code
4. ✓ Attendance is marked automatically

---

## Support

If issues persist:

1. **Check test_qr_api.py output** for detailed error messages
2. **Use qr-api-test.html** to see exact API responses
3. **Enable browser Network tab** to see request/response details
4. **Check backend console logs** for server-side errors
5. **Restart both servers** if stuck

---

**Last Updated:** February 22, 2026
**Status:** Testing & Debugging Guide Ready ✓
