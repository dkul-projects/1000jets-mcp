# Test Your MCP in Claude Code - Right Now

## Step 1: Start the Server

In your terminal:
```bash
cd /Users/yacht/1000jets
source venv/bin/activate
export AVIAPAGES_API_TOKEN="qOAgJCLM8SJTnPQZxF2SOqW5hiZofySiU4KF"
python mcp_server.py
```

You should see:
```
# (server starts silently, ready for connections)
```

**Leave this running** - it's waiting for Claude to connect.

---

## Step 2: Configure Claude Code

1. **Open Claude Code** (or go to claude.com/claude-code)
2. **Click Settings** (⚙️ in top right)
3. **Find "MCP Servers"** section
4. **Click "Add Server"**
5. **Fill in:**
   - **Name:** `1000jets`
   - **Type:** Command
   - **Command:** `python`
   - **Args:** `/Users/yacht/1000jets/mcp_server.py`
   - **Environment:** `AVIAPAGES_API_TOKEN=qOAgJCLM8SJTnPQZxF2SOqW5hiZofySiU4KF`
6. **Click "Save"**
7. **Reload Claude Code**

---

## Step 3: Test in Claude

Start a new chat and try these:

### Test 1: Search for Jets
```
Search for jets from LAX to NYC for 4 passengers tomorrow
```

Claude should respond with:
```
Found 4 available jets for LAX → NYC on 2026-09-26:

• Light Jet - 6 passengers - From $5,200
• Midsize Jet - 8 passengers - From $7,800
• Super Midsize - 10 passengers - From $11,500
• Heavy Jet - 14 passengers - From $18,900
```

### Test 2: Get Price Quote
```
What's the price for a Midsize Jet from JFK to Miami for 4 people?
```

Claude should return pricing details.

### Test 3: Create a Booking
```
Book me a jet from JFK to Miami tomorrow at 9am for 4 people. 
Name: John Smith
Email: john@example.com
Aircraft: Midsize
```

Claude should create a booking request with an ID.

### Test 4: Check Deals
```
Show me empty leg flights between LAX and JFK
```

Claude should show discounted empty leg options.

---

## What to Expect

✅ **When it works:**
- Claude responds with jet options
- Bookings get confirmation IDs
- Pricing displays correctly
- Empty legs show discounts

❌ **If it doesn't work:**
- Check the terminal where you ran `python mcp_server.py`
- Look for error messages
- Verify the path is correct: `/Users/yacht/1000jets/mcp_server.py`
- Make sure you set `AVIAPAGES_API_TOKEN` env var
- Try reloading Claude Code

---

## Troubleshooting

### "Tool not found"
- Make sure MCP server is still running in terminal
- Check the terminal for errors
- Restart: stop the server (Ctrl+C), run again

### "Connection refused"
- Verify server is running: `python mcp_server.py` in terminal
- Check the path is exactly right
- Env var must be set: `export AVIAPAGES_API_TOKEN="qOAgJCLM8SJTnPQZxF2SOqW5hiZofySiU4KF"`

### Claude says "No tools available"
- Reload Claude Code (F5 or Cmd+R)
- Check Settings → MCP Servers that it's listed
- Try stopping and restarting the server

---

## What This Proves

Once you see Claude booking jets ✅

You've proved:
- ✅ MCP server works
- ✅ Claude can call your tools
- ✅ The tool framework is solid
- ✅ You're ready to deploy

---

## Next: Deploy to Railway

Once this works locally, deploy to Railway in 3 steps:

```bash
# 1. Commit everything
git add .
git commit -m "Working 1000jets MCP - tested locally"

# 2. Push to GitHub
git push

# 3. Deploy to Railway
# (go to railway.app, select your repo, deploy)
```

That's it. You're live.

---

**Have fun! Go book a jet in Claude.** ✈️
