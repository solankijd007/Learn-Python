from fastapi import FastAPI
from typing import Optional
import time
import asyncio
from datetime import datetime

# FastAPI instance create karna
app = FastAPI(
    title="Sync vs Async Demo",
    description="Sync aur Async ka difference samajhne ke liye",
    version="2.0.0"
)

# Root endpoint - GET request
@app.get("/")
def read_root():
    """
    Home page endpoint
    """
    return {
        "message": "FastAPI mein aapka swagat hai!",
        "status": "success",
        "endpoints": {
            "sync_slow": "/sync-slow",
            "async_fast": "/async-fast",
            "sync_fast": "/sync-fast",
            "test": "/test"
        }
    }


# ============================================
# SYNC VERSION (SLOW) - Thread Block Karta Hai
# ============================================
@app.get("/sync-slow")
def sync_slow_api():
    """
    Synchronous API - Yeh thread ko BLOCK kar deta hai
    Jab tak yeh complete nahi hota, koi aur request handle nahi ho sakti
    """
    print(f"[SYNC] Request started at {datetime.now().strftime('%H:%M:%S')}")
    
    # Yeh 10 seconds ke liye PURA THREAD BLOCK kar dega
    time.sleep(10)  # ❌ BAD: Thread blocked for 10 seconds
    
    print(f"[SYNC] Request completed at {datetime.now().strftime('%H:%M:%S')}")
    
    return {
        "type": "SYNC (Slow)",
        "message": "10 seconds wait kiya - Thread BLOCKED tha!",
        "problem": "Is time mein koi aur request handle nahi ho sakti thi"
    }


# ============================================
# ASYNC VERSION (FAST) - Thread Free Rehta Hai
# ============================================
@app.get("/async-fast")
async def async_fast_api():
    """
    Asynchronous API - Thread ko FREE chhod deta hai
    Wait karte time doosri requests handle ho sakti hain
    """
    print(f"[ASYNC] Request started at {datetime.now().strftime('%H:%M:%S')}")
    
    # Yeh 10 seconds wait karega LEKIN thread ko free chhod dega
    await asyncio.sleep(10)  # ✅ GOOD: Thread free, doosre requests handle ho sakte hain
    
    print(f"[ASYNC] Request completed at {datetime.now().strftime('%H:%M:%S')}")
    
    return {
        "type": "ASYNC (Fast)",
        "message": "10 seconds wait kiya - Thread FREE tha!",
        "benefit": "Is time mein doosri requests handle ho sakti thi"
    }


# ============================================
# SYNC VERSION (FAST) - No Blocking
# ============================================
@app.get("/sync-fast")
def sync_fast_api():
    """
    Synchronous lekin fast - Koi blocking operation nahi
    """
    print(f"[SYNC-FAST] Request at {datetime.now().strftime('%H:%M:%S')}")
    
    # Koi blocking operation nahi, turant return
    result = 2 + 2
    
    return {
        "type": "SYNC (Fast - No Blocking)",
        "message": "Turant response - Koi wait nahi",
        "result": result
    }


# ============================================
# TEST ENDPOINT - Quickly test karne ke liye
# ============================================
@app.get("/test")
async def test_endpoint():
    """
    Quick test endpoint
    """
    return {
        "message": "Test successful!",
        "timestamp": datetime.now().strftime('%H:%M:%S')
    }


# ============================================
# MULTIPLE ASYNC OPERATIONS - Parallel Processing
# ============================================
@app.get("/async-parallel")
async def async_parallel():
    """
    Multiple async operations ko PARALLEL mein run karna
    """
    print(f"[PARALLEL] Started at {datetime.now().strftime('%H:%M:%S')}")
    
    # Teen operations ko parallel mein run karenge
    # Agar sync hota to: 3 + 5 + 2 = 10 seconds lagte
    # Async mein: Maximum 5 seconds lagenge (sabse bada operation)
    
    async def task1():
        await asyncio.sleep(3)
        return "Task 1 done (3 sec)"
    
    async def task2():
        await asyncio.sleep(5)
        return "Task 2 done (5 sec)"
    
    async def task3():
        await asyncio.sleep(2)
        return "Task 3 done (2 sec)"
    
    # Sabko parallel mein run karo
    results = await asyncio.gather(task1(), task2(), task3())
    
    print(f"[PARALLEL] Completed at {datetime.now().strftime('%H:%M:%S')}")
    
    return {
        "type": "ASYNC PARALLEL",
        "results": results,
        "total_time": "~5 seconds (not 10!)",
        "explanation": "Teeno tasks parallel mein chale, isliye sirf 5 sec lage"
    }


# ============================================
# DEMONSTRATION: Multiple Requests
# ============================================
@app.get("/demo/sync/{request_id}")
def demo_sync(request_id: int):
    """
    Multiple requests ko test karne ke liye
    """
    start = datetime.now()
    print(f"[DEMO-SYNC-{request_id}] Started at {start.strftime('%H:%M:%S.%f')[:-3]}")
    
    time.sleep(3)  # 3 seconds block
    
    end = datetime.now()
    print(f"[DEMO-SYNC-{request_id}] Completed at {end.strftime('%H:%M:%S.%f')[:-3]}")
    
    return {
        "request_id": request_id,
        "type": "SYNC",
        "start_time": start.strftime('%H:%M:%S.%f')[:-3],
        "end_time": end.strftime('%H:%M:%S.%f')[:-3],
        "duration": "3 seconds"
    }


@app.get("/demo/async/{request_id}")
async def demo_async(request_id: int):
    """
    Multiple requests ko test karne ke liye
    """
    start = datetime.now()
    print(f"[DEMO-ASYNC-{request_id}] Started at {start.strftime('%H:%M:%S.%f')[:-3]}")
    
    await asyncio.sleep(3)  # 3 seconds wait (non-blocking)
    
    end = datetime.now()
    print(f"[DEMO-ASYNC-{request_id}] Completed at {end.strftime('%H:%M:%S.%f')[:-3]}")
    
    return {
        "request_id": request_id,
        "type": "ASYNC",
        "start_time": start.strftime('%H:%M:%S.%f')[:-3],
        "end_time": end.strftime('%H:%M:%S.%f')[:-3],
        "duration": "3 seconds"
    }