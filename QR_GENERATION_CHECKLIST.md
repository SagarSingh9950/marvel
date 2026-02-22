# ✅ QR Generation Error - Fix Checklist

## Problem: "Error: Failed to generate QR session"

Use this checklist to fix the issue step by step.

---

## STEP 1: Start the Backend Server

- [ ] Open **Terminal 1 (New)**
- [ ] Run: `cd "c:\Users\sagar\Downloads\MARVEL PRESENTATION"`
- [ ] Run: `python -m backend.main`
- [ ] Wait for: `Uvicorn running on http://0.0.0.0:8000`
- [ ] Leave this terminal running

**Expected Output:**
```
Application startup complete
Uvicorn running on http://0.0.0.0:8000
```

---

## STEP 2: Start the Frontend Server

- [ ] Open **Terminal 2 (New)**
- [ ] Run: `cd "c:\Users\sagar\Downloads\MARVEL PRESENTATION"`
- [ ] Run: `node frontend\server.js`
- [ ] Wait for: `🚀 Marvel Frontend Server running on http://localhost:3000`
- [ ] Leave this terminal running

**Expected Output:**
```
🚀 Marvel Frontend Server running on http://localhost:3000
📡 Backend API: http://localhost:8000/api
```

---

## STEP 3: Test Backend Connection

### Option A: Use Test Page (Easiest)
- [ ] Open browser: `http://localhost:3000/qr-api-test.html`
- [ ] Click "Check Backend Health"
- [ ] Should show: ✓ Status 200

### Option B: Use Python Script
- [ ] Open **Terminal 3 (New)**
- [ ] Run: `python test_qr_api.py`
- [ ] Should see: ✓ Health check successful
- [ ] Should see: ✓ QR generation successful

---

## STEP 4: Test QR Generation Form

- [ ] Open browser: `http://localhost:3000`
- [ ] Click **QR Attendance** in sidebar
- [ ] Go to **Faculty Panel** tab
- [ ] Fill in form:
  - Subject Code: `CS-302`
  - Subject Name: `Computer Networks`
  - Branch: `CS`
  - Semester: `4`
  - Lecture Duration: `50`
  - QR Validity: `3 minutes`
  - Geo-fence Radius: `50`
  - Expected Students: `60`
  - Location Name: `Room 301`
- [ ] Check: "Require device verification"
- [ ] Click: "Generate QR Code"
- [ ] Should see: QR code image displayed
- [ ] Should see: Live attendance updates

---

## STEP 5: Troubleshoot If Anything Fails

### Issue: "Cannot connect to backend"
**Solution:**
- [ ] Verify Terminal 1 shows "Uvicorn running on http://0.0.0.0:8000"
- [ ] Check if port 8000 is available: `netstat -ano | findstr :8000`
- [ ] Kill any process using port 8000
- [ ] Restart backend server

### Issue: "Invalid input value" error
**Solution:**
- [ ] Check all form fields are filled
- [ ] Verify semester is between 1-8
- [ ] Verify lecture duration is 30-180 minutes
- [ ] Verify QR validity is 1-10 minutes
- [ ] Verify geo-fence radius is 10-200 meters

### Issue: "Database error"
**Solution:**
- [ ] Stop backend server (Ctrl+C in Terminal 1)
- [ ] Delete file: `backend/college.db`
- [ ] Start backend server again (will recreate database)

### Issue: Still getting error
**Solution:**
- [ ] Check browser F12 → Console for error messages
- [ ] Check browser F12 → Network tab for API response details
- [ ] Check backend Terminal 1 for error logs
- [ ] Run: `python test_qr_api.py` to see detailed errors

---

## STEP 6: Verify Success

When working correctly, you should see:

- [ ] ✅ QR code image displayed on screen
- [ ] ✅ Session ID shown
- [ ] ✅ Timer showing expiry time
- [ ] ✅ Live attendance dashboard with stats
- [ ] ✅ Browser console shows no errors
- [ ] ✅ Backend Terminal 1 shows success logs

---

## Files Created for Debugging

| File | Purpose |
|------|---------|
| `test_qr_api.py` | Python test script to verify API |
| `frontend/qr-api-test.html` | Interactive test page in browser |
| `QR_API_DEBUG_GUIDE.md` | Detailed debugging documentation |
| `QR_GENERATION_CHECKLIST.md` | This file |

---

## Quick Commands

**Terminal 1 - Start Backend:**
```bash
cd "c:\Users\sagar\Downloads\MARVEL PRESENTATION"
python -m backend.main
```

**Terminal 2 - Start Frontend:**
```bash
cd "c:\Users\sagar\Downloads\MARVEL PRESENTATION"
node frontend\server.js
```

**Terminal 3 - Test API:**
```bash
cd "c:\Users\sagar\Downloads\MARVEL PRESENTATION"
python test_qr_api.py
```

**Browser - Access:**
- Main App: `http://localhost:3000`
- Test Page: `http://localhost:3000/qr-api-test.html`
- API Health: `http://localhost:8000/api/health`

---

## Success Indicators ✓

When everything is working:
1. ✓ Both servers running in terminals
2. ✓ API test shows all endpoints working
3. ✓ Form submission generates QR code
4. ✓ QR code image displays
5. ✓ Live dashboard updates
6. ✓ No errors in browser console

---

## If Still Stuck

1. **Check all 3 terminals are running** (Backend, Frontend, and ideally a test terminal)
2. **Verify ports are free** (3000 and 8000)
3. **Use the test page** to pinpoint which endpoint is failing
4. **Check the QR_API_DEBUG_GUIDE.md** for detailed information
5. **Look at error messages** - they now show exact API response details

---

**Status:** 🚀 Ready to test!
**Last Updated:** February 22, 2026
