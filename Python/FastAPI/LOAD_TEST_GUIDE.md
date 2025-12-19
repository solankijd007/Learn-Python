# 🚀 Load Testing Guide - Sync vs Async Performance

## 📋 Setup

### 1. Install Required Package
```bash
source venv/bin/activate
pip install aiohttp
```

### 2. Make Script Executable
```bash
chmod +x load_test.py
```

---

## ▶️ How to Run

### Step 1: Start FastAPI Server
```bash
# Terminal 1
source venv/bin/activate
uvicorn main:app --reload
```

### Step 2: Run Load Test
```bash
# Terminal 2
source venv/bin/activate
python load_test.py
```

---

## 🎯 Test Options

### 1. Light Test (100 requests each)
- **Good for:** Quick testing
- **Expected:** Both complete quickly

### 2. Medium Test (500 requests each)
- **Good for:** Seeing performance difference
- **Expected:** Async noticeably faster

### 3. Heavy Test (1000 requests each)
- **Good for:** Real-world simulation
- **Expected:** Clear async advantage

### 4. Extreme Test (Sync: 1000, Async: 10000)
- **Good for:** Demonstrating scalability
- **Expected:** 
  - Sync: ~3000 seconds (50 minutes) or crash
  - Async: ~30 seconds

### 5. Custom Test
- **Good for:** Your own experiments

---

## 📊 Expected Results

### Light Test (100 requests):
```
Sync:   ~300 seconds (5 minutes)
Async:  ~3 seconds
Speedup: 100x faster
```

### Medium Test (500 requests):
```
Sync:   ~1500 seconds (25 minutes)
Async:  ~3 seconds
Speedup: 500x faster
```

### Heavy Test (1000 requests):
```
Sync:   ~3000 seconds (50 minutes)
Async:  ~3 seconds
Speedup: 1000x faster
```

### Extreme Test:
```
Sync (1000):    ~3000 seconds or CRASH ❌
Async (10000):  ~30 seconds ✅
```

---

## 🎨 Output Explanation

### Colors:
- 🟢 **Green:** Success messages
- 🔴 **Red:** Errors
- 🟡 **Yellow:** Warnings/Time
- 🔵 **Blue:** Info
- 🔷 **Cyan:** Headers/Requests per second

### Metrics:
- **Total Time:** Test complete hone mein kitna time laga
- **Requests/sec:** Per second kitne requests handle hue
- **Success Rate:** Kitne requests successful rahe

---

## 💡 What You'll Learn

### 1. **Concurrency Difference**
Async endpoint 1000x zyada requests handle kar sakta hai same time mein

### 2. **Resource Efficiency**
Async kam memory aur CPU use karta hai

### 3. **Scalability**
High load par async ka real advantage dikhta hai

---

## ⚠️ Important Notes

### Server Might Crash!
Agar aap heavy test (1000+) sync endpoint par run karenge:
- Server slow ho jayega
- Memory usage badh jayega
- Possible crash

**Solution:** Test ke baad server restart karein:
```bash
Ctrl+C
uvicorn main:app --reload
```

### System Resources
Monitor your system:
```bash
# CPU and Memory usage dekhne ke liye
htop

# या
top
```

---

## 🧪 Sample Run

```bash
$ python load_test.py

============================================================
        FastAPI Load Testing - Sync vs Async
============================================================

ℹ Yeh script sync aur async endpoints ko test karega
⚠ Make sure FastAPI server chal raha hai

Select Test:
1. Light Test (100 requests each)
2. Medium Test (500 requests each)
3. Heavy Test (1000 requests each)
4. Extreme Test (Sync: 1000, Async: 10000)
5. Custom Test

Enter choice (1-5): 1

============================================================
              Testing SYNC Endpoint
============================================================

ℹ Endpoint: /demo/sync
ℹ Total Requests: 100
ℹ Starting test...

Results:
  Total Time: 300.45 seconds
  Requests/sec: 0.33
✓ Successful: 100/100

============================================================
              Testing ASYNC Endpoint
============================================================

ℹ Endpoint: /demo/async
ℹ Total Requests: 100
ℹ Starting test...

Results:
  Total Time: 3.12 seconds
  Requests/sec: 32.05
✓ Successful: 100/100

============================================================
            Performance Comparison
============================================================

Sync Endpoint:
  Time: 300.45s
  Requests/sec: 0.33
  Success Rate: 100/100

Async Endpoint:
  Time: 3.12s
  Requests/sec: 32.05
  Success Rate: 100/100

Async is 96.29x faster!
Async handles 9609.1% more requests/sec
```

---

## 🎯 Recommended Tests

### For Beginners:
Start with **Light Test (Option 1)**

### To See Real Difference:
Run **Medium Test (Option 2)**

### For Maximum Impact:
Run **Extreme Test (Option 4)** - यह सबसे impressive होगा!

---

## 🚀 Next Steps

After testing, you'll understand:
- ✅ Why async is important
- ✅ When to use async vs sync
- ✅ How to handle high concurrency
- ✅ Production-ready API design

---

**Happy Testing! 🎉**
