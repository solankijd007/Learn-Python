# Sync vs Async Testing Script

## Problem
`--reload` mode में `--workers 1` काम नहीं करता क्योंकि reload mode automatically multiple processes create करता है।

## Solution: Testing के लिए बिना reload के run करें

### Step 1: Server को Single Worker Mode में Start करें
```bash
# Virtual environment activate करें
source venv/bin/activate

# Bina reload ke, single worker mode
uvicorn main:app --host 127.0.0.1 --port 8000
```

### Step 2: Sync Blocking Test

**Terminal 1:**
```bash
time curl http://localhost:8000/sync-slow
```

**Terminal 2 (तुरंत, 1-2 seconds में):**
```bash
time curl http://localhost:8000/test
```

**Expected Result:**
- Terminal 1: ~10 seconds लगेंगे
- Terminal 2: ~10 seconds लगेंगे (wait करेगा) ❌

### Step 3: Async Non-Blocking Test

**Terminal 1:**
```bash
time curl http://localhost:8000/async-fast
```

**Terminal 2 (तुरंत):**
```bash
time curl http://localhost:8000/test
```

**Expected Result:**
- Terminal 1: ~10 seconds लगेंगे
- Terminal 2: <1 second (तुरंत complete) ✅

---

## Alternative: Browser से Test करें

### Sync Test:
1. Browser tab 1: `http://localhost:8000/sync-slow` खोलें
2. तुरंत browser tab 2: `http://localhost:8000/test` खोलें
3. देखें - दोनों ~10 seconds बाद load होंगे

### Async Test:
1. Browser tab 1: `http://localhost:8000/async-fast` खोलें
2. तुरंत browser tab 2: `http://localhost:8000/test` खोलें
3. देखें - Tab 2 तुरंत load होगा, Tab 1 10 seconds बाद

---

## Better Demo: Load Testing Tool

### Install httpie (optional)
```bash
pip install httpie
```

### Parallel Requests भेजें
```bash
# 5 sync requests parallel में
for i in {1..5}; do
  (time curl http://localhost:8000/sync-slow &)
done

# Total time: ~50 seconds (sequential)
```

```bash
# 5 async requests parallel में
for i in {1..5}; do
  (time curl http://localhost:8000/async-fast &)
done

# Total time: ~10 seconds (parallel)
```

---

## Key Point

**Uvicorn default behavior:**
- Production में multiple workers use होते हैं (performance के लिए)
- इसलिए blocking उतना visible नहीं होता
- लेकिन **high load** पर async का फायदा दिखता है

**Real-world scenario:**
- 100 concurrent users
- Sync: सभी sequential में handle होंगे (slow)
- Async: सभी concurrent में handle होंगे (fast)
