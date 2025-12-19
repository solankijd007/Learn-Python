#!/usr/bin/env python3
"""
Load Testing Script - Sync vs Async Performance Demo
Yeh script sync aur async endpoints ko test karke performance difference dikhata hai
"""

import asyncio
import aiohttp
import time
from datetime import datetime
import sys

# Colors for terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


def print_header(text):
    """Print formatted header"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text.center(60)}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.RESET}\n")


def print_success(text):
    """Print success message"""
    print(f"{Colors.GREEN}✓ {text}{Colors.RESET}")


def print_error(text):
    """Print error message"""
    print(f"{Colors.RED}✗ {text}{Colors.RESET}")


def print_info(text):
    """Print info message"""
    print(f"{Colors.BLUE}ℹ {text}{Colors.RESET}")


def print_warning(text):
    """Print warning message"""
    print(f"{Colors.YELLOW}⚠ {text}{Colors.RESET}")


async def fetch_url(session, url, request_id):
    """Single request ko fetch karna"""
    try:
        async with session.get(url) as response:
            data = await response.json()
            return {"success": True, "request_id": request_id, "data": data}
    except Exception as e:
        return {"success": False, "request_id": request_id, "error": str(e)}


async def load_test_async(base_url, endpoint, num_requests, test_name):
    """
    Async load test - Multiple requests parallel mein
    """
    print_header(f"{test_name}")
    print_info(f"Endpoint: {endpoint}")
    print_info(f"Total Requests: {num_requests}")
    print_info(f"Starting test...")
    
    start_time = time.time()
    
    # Create async HTTP session
    async with aiohttp.ClientSession() as session:
        # Sabhi requests ko parallel mein bhejo
        tasks = []
        for i in range(num_requests):
            url = f"{base_url}{endpoint}/{i}"
            task = fetch_url(session, url, i)
            tasks.append(task)
        
        # Wait for all requests to complete
        results = await asyncio.gather(*tasks, return_exceptions=True)
    
    end_time = time.time()
    total_time = end_time - start_time
    
    # Results analyze karo
    successful = sum(1 for r in results if isinstance(r, dict) and r.get("success"))
    failed = num_requests - successful
    
    # Print results
    print(f"\n{Colors.BOLD}Results:{Colors.RESET}")
    print(f"  Total Time: {Colors.YELLOW}{total_time:.2f} seconds{Colors.RESET}")
    print(f"  Requests/sec: {Colors.CYAN}{num_requests/total_time:.2f}{Colors.RESET}")
    print_success(f"Successful: {successful}/{num_requests}")
    
    if failed > 0:
        print_error(f"Failed: {failed}/{num_requests}")
    
    return {
        "total_time": total_time,
        "successful": successful,
        "failed": failed,
        "requests_per_sec": num_requests/total_time
    }


def print_comparison(sync_result, async_result):
    """
    Dono results ka comparison print karo
    """
    print_header("Performance Comparison")
    
    print(f"{Colors.BOLD}Sync Endpoint:{Colors.RESET}")
    print(f"  Time: {sync_result['total_time']:.2f}s")
    print(f"  Requests/sec: {sync_result['requests_per_sec']:.2f}")
    print(f"  Success Rate: {sync_result['successful']}/{sync_result['successful']+sync_result['failed']}")
    
    print(f"\n{Colors.BOLD}Async Endpoint:{Colors.RESET}")
    print(f"  Time: {async_result['total_time']:.2f}s")
    print(f"  Requests/sec: {async_result['requests_per_sec']:.2f}")
    print(f"  Success Rate: {async_result['successful']}/{async_result['successful']+async_result['failed']}")
    
    # Speed improvement
    speedup = sync_result['total_time'] / async_result['total_time']
    print(f"\n{Colors.BOLD}{Colors.GREEN}Async is {speedup:.2f}x faster!{Colors.RESET}")
    
    # Throughput improvement
    throughput_improvement = (async_result['requests_per_sec'] / sync_result['requests_per_sec'] - 1) * 100
    print(f"{Colors.BOLD}{Colors.GREEN}Async handles {throughput_improvement:.1f}% more requests/sec{Colors.RESET}")


async def main():
    """Main function"""
    base_url = "http://localhost:8000"
    
    print_header("FastAPI Load Testing - Sync vs Async")
    print_info("Yeh script sync aur async endpoints ko test karega")
    print_warning("Make sure FastAPI server chal raha hai (uvicorn main:app)")
    
    # Menu
    print(f"\n{Colors.BOLD}Select Test:{Colors.RESET}")
    print("1. Light Test (100 requests each)")
    print("2. Medium Test (500 requests each)")
    print("3. Heavy Test (1000 requests each)")
    print("4. Extreme Test (Sync: 1000, Async: 10000)")
    print("5. Custom Test")
    
    choice = input(f"\n{Colors.CYAN}Enter choice (1-5): {Colors.RESET}").strip()
    
    if choice == "1":
        sync_count = async_count = 100
    elif choice == "2":
        sync_count = async_count = 500
    elif choice == "3":
        sync_count = async_count = 1000
    elif choice == "4":
        sync_count = 1000
        async_count = 10000
        print_warning("Extreme test! Sync might struggle...")
    elif choice == "5":
        sync_count = int(input("Sync requests: "))
        async_count = int(input("Async requests: "))
    else:
        print_error("Invalid choice!")
        return
    
    print_info(f"\nStarting tests...")
    print_info(f"Sync: {sync_count} requests")
    print_info(f"Async: {async_count} requests")
    
    # Test Sync endpoint
    print("\n" + "="*60)
    sync_result = await load_test_async(base_url, "/demo/sync", sync_count, "Testing SYNC Endpoint")
    
    # Wait a bit
    print_info("\nWaiting 2 seconds before next test...")
    await asyncio.sleep(2)
    
    # Test Async endpoint
    print("\n" + "="*60)
    async_result = await load_test_async(base_url, "/demo/async", async_count, "Testing ASYNC Endpoint")
    
    # Print comparison
    print("\n" + "="*60)
    print_comparison(sync_result, async_result)
    
    print_header("Test Complete!")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print_warning("\n\nTest cancelled by user")
        sys.exit(0)
    except Exception as e:
        print_error(f"\nError: {e}")
        sys.exit(1)
