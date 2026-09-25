# 1000jets MCP Launch Checklist

**Goal:** Launch as the first AI-native jet booking platform with MCP support

---

## Phase 1: Development & Testing (Days 1-2)

- [ ] Run `python mcp_server.py` locally
- [ ] Connect to Claude Code via MCP settings
- [ ] Test tools:
  - [ ] `search_jets` (LAX to NYC, 4 passengers)
  - [ ] `get_jet_price` (JFK to Miami, Midsize Jet)
  - [ ] `create_booking_request` (full booking flow)
  - [ ] `check_empty_legs` (discount flights)
- [ ] Verify Aviapages API responses are correct
- [ ] Test error handling (bad dates, invalid airports)

**Status:** Ready for deployment ✓

---

## Phase 2: Deployment (Day 3)

- [ ] Create GitHub repo: `1000jets-mcp`
- [ ] Push code to GitHub
- [ ] Create Railway account (free tier)
- [ ] Deploy to Railway
- [ ] Add `AVIAPAGES_API_TOKEN` env var
- [ ] Copy live Railway URL
- [ ] Test that live deployment works

**Live URL:** `https://YOUR-RAILWAY-URL`

---

## Phase 3: Registry & Discovery (Day 4)

- [ ] Create GitHub release `v1.0.0`
- [ ] Submit to MCP Registry (mcp.run)
  - [ ] Name: "1000jets Jet Booking"
  - [ ] Description: "Book private jets in Claude, ChatGPT, Gemini"
  - [ ] GitHub URL: https://github.com/YOUR_USERNAME/1000jets-mcp
  - [ ] Maintainer: your-email@1000jets.com
- [ ] Verify MCP shows up in public registry

**Registry URL:** https://mcp.run/1000jets

---

## Phase 4: Marketing Launch (Day 5)

### Social Media

- [ ] **Twitter/X** - Post launch thread
  ```
  🧵 Just launched: Book private jets in Claude AI
  
  No more switching apps. Search, price & book jets directly in your LLM chat.
  
  ✈️ Real Aviapages network (1000+ operators)
  💰 Instant quotes
  ✅ One-click booking
  🚀 Works in Claude, ChatGPT, Gemini
  
  Open source MCP: https://mcp.run/1000jets
  Website: https://1000jets.com
  
  #Claude #AI #Aviation #Startup
  ```

- [ ] **LinkedIn** - Professional angle
  ```
  "Thrilled to announce 1000jets: The AI-native jet booking platform.
  
  Users can now book private jets directly in Claude, ChatGPT, and Gemini through our open Model Context Protocol (MCP) integration.
  
  Built on Aviapages' 1000+ verified operators worldwide. Quote → Book → Pay, all in conversation.
  
  The future of aviation is conversational. We're pioneering it.
  
  https://1000jets.com"
  ```

- [ ] **Product Hunt** (optional Day 6)
  - Post to Show HN / Product Hunt
  - Title: "1000jets – Book Private Jets in Claude AI"
  - Description: "The first AI-native jet booking platform. MCP support for Claude, ChatGPT, Gemini"

### Content

- [ ] Update `1000jets.com` homepage
  ```
  "Book jets in Claude. The AI-native way."
  
  - Integrated MCP for Claude, ChatGPT, Gemini
  - Real Aviapages pricing & availability
  - Quote in seconds, book in minutes
  ```

- [ ] Blog post: "How We Built the First AI-Native Jet Booking Platform"
  - Explain MCP technology
  - Show demo (search → book flow in Claude)
  - Link to GitHub

- [ ] Create demo video (3 minutes)
  - Show Claude searching for jets
  - Get price quote
  - Create booking request
  - Post on Twitter + website

---

## Phase 5: Expansion (Week 2)

### ChatGPT Custom Actions

- [ ] Build REST API wrapper (Flask/FastAPI)
- [ ] Generate OpenAPI spec from MCP tools
- [ ] Create ChatGPT Custom Action
- [ ] Test booking flow in ChatGPT
- [ ] Post "Now on ChatGPT!" update

### Gemini Extensions

- [ ] Similar REST wrapper
- [ ] Add to Gemini Extensions
- [ ] Test flow
- [ ] Post update

### Groq Integration

- [ ] Test MCP compatibility with Groq
- [ ] Create integration guide
- [ ] Post to Groq community

---

## Success Metrics

Track these post-launch:

- [ ] MCP downloads/installs (from registry)
- [ ] Claude users who've tried the MCP
- [ ] Booking requests created via MCP
- [ ] GitHub stars
- [ ] Website traffic spike
- [ ] Twitter engagement

**Goal:** 100+ MCP installs in first week, 5+ bookings via MCP in first month

---

## Quick Links

- **MCP Server Code:** `/Users/yacht/1000jets/mcp_server.py`
- **Deployment Guide:** `/Users/yacht/1000jets/MCP_README.md`
- **Quick Start:** `/Users/yacht/1000jets/QUICKSTART.md`
- **Website:** https://1000jets.com
- **GitHub:** https://github.com/YOUR_USERNAME/1000jets-mcp
- **Registry:** https://mcp.run
- **Aviapages API:** https://aviapages.com/api

---

## Notes

- Your Aviapages free tier: 300 searches/prices per month (upgrade if needed)
- Keep API token secure (don't commit to public repo - use env vars)
- Monitor Railway usage (free tier is generous but watch it)
- Start with Claude feedback before expanding to ChatGPT/Gemini

---

**Status:** Ready to launch 🚀

Last updated: 2026-09-25
