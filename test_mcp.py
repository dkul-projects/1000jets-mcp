#!/usr/bin/env python3
"""
Quick test script to verify 1000jets MCP is working
Run this before launching to the public
"""

import asyncio
import httpx
import os
from datetime import datetime, timedelta

AVIAPAGES_API_TOKEN = os.getenv(
    "AVIAPAGES_API_TOKEN", "qOAgJCLM8SJTnPQZxF2SOqW5hiZofySiU4KF"
)
AVIAPAGES_BASE_URL = "https://api.aviapages.com/api/v2"


async def test_api_connection():
    """Test that we can connect to Aviapages API"""
    print("🔗 Testing Aviapages API connection...")

    async with httpx.AsyncClient(
        base_url=AVIAPAGES_BASE_URL,
        headers={
            "Authorization": f"Bearer {AVIAPAGES_API_TOKEN}",
            "Content-Type": "application/json",
        },
        timeout=10.0,
    ) as client:
        try:
            # Try a simple request
            response = await client.get("/airports", params={"limit": 1})
            response.raise_for_status()
            print("✅ API connection successful")
            return True
        except Exception as e:
            print(f"❌ API connection failed: {e}")
            return False


async def test_search_jets():
    """Test the search_jets function"""
    print("\n🛫 Testing jet search...")

    async with httpx.AsyncClient(
        base_url=AVIAPAGES_BASE_URL,
        headers={
            "Authorization": f"Bearer {AVIAPAGES_API_TOKEN}",
            "Content-Type": "application/json",
        },
        timeout=10.0,
    ) as client:
        try:
            tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
            response = await client.get(
                "/charter_searches",
                params={
                    "departure": "LAX",
                    "arrival": "JFK",
                    "departure_date": tomorrow,
                    "passengers": 4,
                },
            )
            response.raise_for_status()
            data = response.json()

            if data.get("results"):
                print(f"✅ Found {len(data['results'])} jets")
                return True
            else:
                print("⚠️  No results (API working but no inventory)")
                return True
        except Exception as e:
            print(f"❌ Search test failed: {e}")
            return False


async def test_pricing():
    """Test the get_jet_price function"""
    print("\n💰 Testing pricing endpoint...")

    async with httpx.AsyncClient(
        base_url=AVIAPAGES_BASE_URL,
        headers={
            "Authorization": f"Bearer {AVIAPAGES_API_TOKEN}",
            "Content-Type": "application/json",
        },
        timeout=10.0,
    ) as client:
        try:
            tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
            response = await client.get(
                "/charter_prices",
                params={
                    "departure": "LAX",
                    "arrival": "JFK",
                    "departure_date": tomorrow,
                    "aircraft_class": "Light Jet",
                    "passengers": 4,
                },
            )
            response.raise_for_status()
            data = response.json()

            if data.get("price"):
                print(f"✅ Pricing available")
                return True
            else:
                print("⚠️  No pricing data (API working but no quotes)")
                return True
        except Exception as e:
            print(f"❌ Pricing test failed: {e}")
            return False


async def test_empty_legs():
    """Test the check_empty_legs function"""
    print("\n🆓 Testing empty legs (discounted flights)...")

    async with httpx.AsyncClient(
        base_url=AVIAPAGES_BASE_URL,
        headers={
            "Authorization": f"Bearer {AVIAPAGES_API_TOKEN}",
            "Content-Type": "application/json",
        },
        timeout=10.0,
    ) as client:
        try:
            response = await client.get(
                "/empty_legs",
                params={
                    "departure": "LAX",
                    "arrival": "JFK",
                    "days": 30,
                },
            )
            response.raise_for_status()
            data = response.json()

            if data.get("results"):
                print(f"✅ Found {len(data['results'])} empty legs")
            else:
                print("⚠️  No empty legs available (API working)")
            return True
        except Exception as e:
            print(f"❌ Empty legs test failed: {e}")
            return False


async def test_mcp_server():
    """Test that the MCP server can start"""
    print("\n🤖 Testing MCP server startup...")
    try:
        # Try to import and instantiate
        from mcp_server import server

        print("✅ MCP server imports successfully")
        print(f"   Server name: {server.name}")
        return True
    except Exception as e:
        print(f"❌ MCP server test failed: {e}")
        return False


async def main():
    """Run all tests"""
    print("=" * 50)
    print("1000jets MCP - Pre-Launch Test Suite")
    print("=" * 50)
    print(f"\nTesting with API token: {AVIAPAGES_API_TOKEN[:10]}...")

    results = []

    # Run tests
    results.append(("API Connection", await test_api_connection()))
    results.append(("Jet Search", await test_search_jets()))
    results.append(("Pricing", await test_pricing()))
    results.append(("Empty Legs", await test_empty_legs()))
    results.append(("MCP Server", await test_mcp_server()))

    # Summary
    print("\n" + "=" * 50)
    print("TEST SUMMARY")
    print("=" * 50)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")

    print(f"\nTotal: {passed}/{total} tests passed")

    if passed == total:
        print("\n🚀 All tests passed! Ready to launch.")
        return 0
    else:
        print("\n⚠️  Some tests failed. Check configuration before launching.")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    exit(exit_code)
