#!/usr/bin/env python3
"""
1000jets MCP Server - Mock Version (for testing before Aviapages API works)
This version uses fake data so you can test the MCP without real API access.
Once you get the correct Aviapages endpoint, swap this for mcp_server.py
"""

import os
import json
from typing import Any
from datetime import datetime, timedelta
from mcp.server.models import InitializationOptions
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent, ToolResult

# Initialize MCP server
server = Server("1000jets-mcp")

# Mock data
MOCK_JETS = [
    {"type": "Light Jet", "passengers": 6, "price": 5200, "hours": 4.5},
    {"type": "Midsize Jet", "passengers": 8, "price": 7800, "hours": 4.5},
    {"type": "Super Midsize", "passengers": 10, "price": 11500, "hours": 4.5},
    {"type": "Heavy Jet", "passengers": 14, "price": 18900, "hours": 4.5},
]

MOCK_EMPTY_LEGS = [
    {"aircraft": "Midsize", "discount": 45, "date": "2026-09-26"},
    {"aircraft": "Light Jet", "discount": 35, "date": "2026-09-27"},
]


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools for booking private jets"""
    return [
        Tool(
            name="search_jets",
            description="Search available private jets between two airports. Returns aircraft options with pricing estimates.",
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
                        "minimum": 1,
                        "maximum": 20,
                    },
                },
                "required": [
                    "departure_iata",
                    "arrival_iata",
                    "departure_date",
                    "passengers",
                ],
            },
        ),
        Tool(
            name="get_jet_price",
            description="Get detailed pricing for a specific jet charter route.",
            inputSchema={
                "type": "object",
                "properties": {
                    "departure_iata": {
                        "type": "string",
                        "description": "Departure airport IATA code",
                    },
                    "arrival_iata": {
                        "type": "string",
                        "description": "Arrival airport IATA code",
                    },
                    "departure_date": {
                        "type": "string",
                        "description": "Departure date in YYYY-MM-DD format",
                    },
                    "aircraft_type": {
                        "type": "string",
                        "description": "Aircraft type/class (e.g., 'Light Jet', 'Midsize Jet', 'Super Midsize', 'Heavy Jet')",
                    },
                    "passengers": {
                        "type": "integer",
                        "description": "Number of passengers",
                    },
                },
                "required": [
                    "departure_iata",
                    "arrival_iata",
                    "departure_date",
                    "aircraft_type",
                    "passengers",
                ],
            },
        ),
        Tool(
            name="create_booking_request",
            description="Create a booking request for a private jet charter. This initiates the quote and booking process.",
            inputSchema={
                "type": "object",
                "properties": {
                    "departure_iata": {
                        "type": "string",
                        "description": "Departure airport IATA code",
                    },
                    "arrival_iata": {
                        "type": "string",
                        "description": "Arrival airport IATA code",
                    },
                    "departure_date": {
                        "type": "string",
                        "description": "Departure date in YYYY-MM-DD format",
                    },
                    "departure_time": {
                        "type": "string",
                        "description": "Preferred departure time in HH:MM format (24-hour)",
                    },
                    "passengers": {
                        "type": "integer",
                        "description": "Number of passengers",
                    },
                    "aircraft_preference": {
                        "type": "string",
                        "description": "Preferred aircraft class (Light Jet, Midsize, Super Midsize, Heavy Jet, etc.)",
                    },
                    "passenger_name": {
                        "type": "string",
                        "description": "Name of the primary passenger",
                    },
                    "email": {
                        "type": "string",
                        "description": "Contact email for booking confirmation",
                    },
                    "phone": {
                        "type": "string",
                        "description": "Contact phone number",
                    },
                    "special_requests": {
                        "type": "string",
                        "description": "Any special requests (catering, ground transportation, etc.)",
                    },
                },
                "required": [
                    "departure_iata",
                    "arrival_iata",
                    "departure_date",
                    "departure_time",
                    "passengers",
                    "passenger_name",
                    "email",
                ],
            },
        ),
        Tool(
            name="check_empty_legs",
            description="Find available empty leg flights (one-way charter flights at discounted rates) between airports.",
            inputSchema={
                "type": "object",
                "properties": {
                    "departure_iata": {
                        "type": "string",
                        "description": "Departure airport IATA code",
                    },
                    "arrival_iata": {
                        "type": "string",
                        "description": "Arrival airport IATA code",
                    },
                    "date_range_days": {
                        "type": "integer",
                        "description": "Search range in days from today (default 30)",
                        "minimum": 1,
                        "maximum": 90,
                    },
                },
                "required": ["departure_iata", "arrival_iata"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> ToolResult:
    """Handle tool calls from Claude"""
    try:
        if name == "search_jets":
            return await search_jets_tool(arguments)
        elif name == "get_jet_price":
            return await get_jet_price_tool(arguments)
        elif name == "create_booking_request":
            return await create_booking_request_tool(arguments)
        elif name == "check_empty_legs":
            return await check_empty_legs_tool(arguments)
        else:
            return ToolResult(
                content=[
                    TextContent(
                        type="text",
                        text=f"Unknown tool: {name}",
                    )
                ],
                isError=True,
            )
    except Exception as e:
        return ToolResult(
            content=[TextContent(type="text", text=f"Error: {str(e)}")],
            isError=True,
        )


async def search_jets_tool(args: dict) -> ToolResult:
    """Search for available jets (mock data)"""
    results = []
    for jet in MOCK_JETS:
        if jet["passengers"] >= args["passengers"]:
            results.append(
                f"• {jet['type']} - {jet['passengers']} passengers - From ${jet['price']:,}"
            )

    content = f"Found {len(results)} available jets for {args['departure_iata']} → {args['arrival_iata']} on {args['departure_date']}:\n\n" + "\n".join(
        results
    )
    return ToolResult(content=[TextContent(type="text", text=content)])


async def get_jet_price_tool(args: dict) -> ToolResult:
    """Get pricing for specific jet"""
    jet_type = args["aircraft_type"]

    for jet in MOCK_JETS:
        if jet["type"].lower() == jet_type.lower():
            content = f"""**Charter Price Quote**

Route: {args['departure_iata']} → {args['arrival_iata']}
Date: {args['departure_date']}
Aircraft: {jet_type}
Passengers: {args['passengers']}

Base Price: ${jet['price']:,}
Flight Hours: {jet['hours']}
Estimated Total: ${jet['price']:,}

Ready to book? Use the create_booking_request tool with your details."""
            return ToolResult(content=[TextContent(type="text", text=content)])

    return ToolResult(
        content=[TextContent(type="text", text="Aircraft type not found.")],
        isError=True,
    )


async def create_booking_request_tool(args: dict) -> ToolResult:
    """Create a booking request"""
    import random

    booking_id = f"BR-{random.randint(10000, 99999)}"

    content = f"""✅ **Booking Request Created**

Request ID: {booking_id}
Passenger: {args['passenger_name']}
Email: {args['email']}

Route: {args['departure_iata']} → {args['arrival_iata']}
Date: {args['departure_date']} @ {args.get('departure_time', '12:00')}
Passengers: {args['passengers']}
Aircraft: {args.get('aircraft_preference', 'Any')}

Next Steps:
1. Our team will review your request
2. You'll receive a detailed quote at {args['email']}
3. Confirm and complete payment to finalize booking

You can track your booking at: https://1000jets.com/bookings/{booking_id}"""

    return ToolResult(content=[TextContent(type="text", text=content)])


async def check_empty_legs_tool(args: dict) -> ToolResult:
    """Check for empty leg deals"""
    results = []
    for leg in MOCK_EMPTY_LEGS:
        results.append(
            f"• {leg['aircraft']} - {leg['date']} - {leg['discount']}% off"
        )

    content = (
        f"💰 **Empty Leg Deals Found:**\n\n" + "\n".join(results)
        if results
        else "No empty leg flights available in the next 30 days."
    )
    return ToolResult(content=[TextContent(type="text", text=content)])


async def main():
    """Start the MCP server"""
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            InitializationOptions(
                server_name="1000jets-mcp",
                server_version="1.0.0",
            ),
            read_stream,
            write_stream,
            raise_exceptions=True,
        )


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
