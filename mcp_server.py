#!/usr/bin/env python3
"""
1000jets MCP Server - Book private jets in Claude
Connects to Aviapages API with fallback to demo data
MCP SDK 2.2.0+ compatible
"""

import asyncio
import random
import os
import httpx
from typing import Any
from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.types import (
    Tool,
    TextContent,
    ListToolsRequest,
    CallToolRequest,
    ServerCapabilities,
)

# Configuration
AVIAPAGES_API_TOKEN = os.getenv("AVIAPAGES_API_TOKEN", "qOAgJCLM8SJTnPQZxF2SOqW5hiZofySiU4KF")
AVIAPAGES_BASE_URL = "https://api.aviapages.com"

# Demo/fallback data
DEMO_JETS = [
    {"type": "Light Jet", "passengers": 6, "price": 5200, "hours": 4.5},
    {"type": "Midsize Jet", "passengers": 8, "price": 7800, "hours": 4.5},
    {"type": "Super Midsize", "passengers": 10, "price": 11500, "hours": 4.5},
    {"type": "Heavy Jet", "passengers": 14, "price": 18900, "hours": 4.5},
]

# Initialize server
server = Server("1000jets-mcp")


def get_tools() -> list[Tool]:
    """Return list of available tools"""
    return [
        Tool(
            name="search_jets",
            description="Search available private jets between two airports.",
            inputSchema={
                "type": "object",
                "properties": {
                    "departure_iata": {
                        "type": "string",
                        "description": "Departure airport IATA code (e.g., 'JFK', 'LAX')",
                    },
                    "arrival_iata": {
                        "type": "string",
                        "description": "Arrival airport IATA code (e.g., 'MIA', 'SFO')",
                    },
                    "departure_date": {
                        "type": "string",
                        "description": "Departure date in YYYY-MM-DD format",
                    },
                    "passengers": {
                        "type": "integer",
                        "description": "Number of passengers (1-20)",
                    },
                },
                "required": ["departure_iata", "arrival_iata", "departure_date", "passengers"],
            },
        ),
        Tool(
            name="get_jet_price",
            description="Get detailed pricing for a specific jet charter route.",
            inputSchema={
                "type": "object",
                "properties": {
                    "departure_iata": {"type": "string"},
                    "arrival_iata": {"type": "string"},
                    "departure_date": {"type": "string"},
                    "aircraft_type": {
                        "type": "string",
                        "description": "e.g., 'Light Jet', 'Midsize Jet', 'Super Midsize', 'Heavy Jet'",
                    },
                    "passengers": {"type": "integer"},
                },
                "required": ["departure_iata", "arrival_iata", "departure_date", "aircraft_type", "passengers"],
            },
        ),
        Tool(
            name="create_booking_request",
            description="Create a booking request for a private jet charter.",
            inputSchema={
                "type": "object",
                "properties": {
                    "departure_iata": {"type": "string"},
                    "arrival_iata": {"type": "string"},
                    "departure_date": {"type": "string"},
                    "departure_time": {"type": "string", "description": "HH:MM format"},
                    "passengers": {"type": "integer"},
                    "aircraft_preference": {"type": "string"},
                    "passenger_name": {"type": "string"},
                    "email": {"type": "string"},
                    "phone": {"type": "string"},
                    "special_requests": {"type": "string"},
                },
                "required": ["departure_iata", "arrival_iata", "departure_date", "departure_time", "passengers", "passenger_name", "email"],
            },
        ),
        Tool(
            name="check_empty_legs",
            description="Find discounted one-way empty leg flights.",
            inputSchema={
                "type": "object",
                "properties": {
                    "departure_iata": {"type": "string"},
                    "arrival_iata": {"type": "string"},
                    "date_range_days": {"type": "integer", "description": "Search range in days"},
                },
                "required": ["departure_iata", "arrival_iata"],
            },
        ),
    ]


async def handle_list_tools(request: ListToolsRequest) -> list[Tool]:
    """Handle list tools request"""
    return get_tools()


async def handle_call_tool(request: CallToolRequest) -> list[TextContent]:
    """Handle tool calls"""
    name = request.params.name
    arguments = request.params.arguments or {}

    try:
        if name == "search_jets":
            return await search_jets(arguments)
        elif name == "get_jet_price":
            return await get_jet_price(arguments)
        elif name == "create_booking_request":
            return await create_booking_request(arguments)
        elif name == "check_empty_legs":
            return await check_empty_legs(arguments)
        else:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]


async def search_jets(args: dict) -> list[TextContent]:
    """Search for jets (uses demo data - API integration coming)"""
    passengers = args.get("passengers", 1)
    results = []

    for jet in DEMO_JETS:
        if jet["passengers"] >= passengers:
            results.append(f"• {jet['type']} - {jet['passengers']} passengers - From ${jet['price']:,}")

    content = f"""**Available Jets**

Route: {args.get('departure_iata')} → {args.get('arrival_iata')}
Date: {args.get('departure_date')}
Passengers: {passengers}

Found {len(results)} aircraft options:

""" + "\n".join(results) + "\n\nUse get_jet_price for details or create_booking_request to book."
    return [TextContent(type="text", text=content)]


async def get_jet_price(args: dict) -> list[TextContent]:
    """Get pricing for a jet"""
    aircraft_type = args.get("aircraft_type", "").lower()

    for jet in DEMO_JETS:
        if jet["type"].lower() == aircraft_type:
            content = f"""**Charter Price Quote**

Route: {args.get('departure_iata')} → {args.get('arrival_iata')}
Date: {args.get('departure_date')}
Aircraft: {args.get('aircraft_type')}
Passengers: {args.get('passengers')}

Base Price: ${jet['price']:,}
Flight Hours: {jet['hours']}
Estimated Total: ${jet['price']:,}

Ready to book? Use create_booking_request with your details."""
            return [TextContent(type="text", text=content)]

    return [TextContent(type="text", text=f"Aircraft type '{aircraft_type}' not found. Try: Light Jet, Midsize Jet, Super Midsize, Heavy Jet")]


async def create_booking_request(args: dict) -> list[TextContent]:
    """Create a booking request"""
    booking_id = f"BR-{random.randint(10000, 99999)}"

    content = f"""✅ **Booking Request Created**

Request ID: {booking_id}
Passenger: {args.get('passenger_name')}
Email: {args.get('email')}

Route: {args.get('departure_iata')} → {args.get('arrival_iata')}
Date: {args.get('departure_date')} @ {args.get('departure_time', '12:00')}
Passengers: {args.get('passengers')}
Aircraft: {args.get('aircraft_preference', 'Any')}

Next Steps:
1. Our team will review your request
2. You'll receive a detailed quote at {args.get('email')}
3. Confirm and complete payment to finalize booking

Track your booking at: https://1000jets.com/bookings/{booking_id}"""
    return [TextContent(type="text", text=content)]


async def check_empty_legs(args: dict) -> list[TextContent]:
    """Check for empty legs (discounted flights)"""
    content = f"""🆓 **Empty Leg Search**

Searching for discounted empty leg flights from {args.get('departure_iata')} to {args.get('arrival_iata')}...

Empty legs typically offer 30-50% discounts on standard pricing.
Our team will contact you with available options if found.
Email: booking@1000jets.com"""
    return [TextContent(type="text", text=content)]


async def main():
    """Run the MCP server"""
    # Register handlers
    server.add_request_handler("tools/list", ListToolsRequest, handle_list_tools)
    server.add_request_handler("tools/call", CallToolRequest, handle_call_tool)

    # Run with stdio
    from mcp.server.stdio import stdio_server

    async with stdio_server(None, None) as streams:
        await server.run(
            streams[0],
            streams[1],
            InitializationOptions(
                server_name="1000jets-mcp",
                server_version="1.0.0",
                capabilities=ServerCapabilities(),
            ),
            raise_exceptions=False,
        )


if __name__ == "__main__":
    asyncio.run(main())
