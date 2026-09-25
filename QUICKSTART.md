# 1000jets MCP - Quick Start (30 seconds)

## Run Locally

```bash
cd /Users/yacht/1000jets

# One-time setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Every time you want to run
export AVIAPAGES_API_TOKEN="qOAgJCLM8SJTnPQZxF2SOqW5hiZofySiU4KF"
python mcp_server.py
```

The server is now running and ready for Claude to connect.

---

## Connect Claude (Local)

### Via Claude Code Settings:
1. Open Claude Code
2. Settings → MCP Servers → Add Server
3. Name: `1000jets`
4. Command: `python /Users/yacht/1000jets/mcp_server.py`
5. Env vars: `AVIAPAGES_API_TOKEN=qOAgJCLM8SJTnPQZxF2SOqW5hiZofySiU4KF`

### Or use API:
```python
import anthropic
import subprocess

client = anthropic.Anthropic()

# Start MCP server in background
proc = subprocess.Popen(
    ["python", "/Users/yacht/1000jets/mcp_server.py"],
    env={"AVIAPAGES_API_TOKEN": "qOAgJCLM8SJTnPQZxF2SOqW5hiZofySiU4KF"}
)

# Use Claude with MCP
response = client.messages.create(
    model="claude-opus-5",
    max_tokens=1024,
    tools=[
        {
            "type": "mcp_tool",
            "mcp_server_name": "1000jets",
            "tool_name": "search_jets"
        }
    ],
    messages=[{
        "role": "user",
        "content": "Find me a jet from JFK to Miami tomorrow for 4 passengers"
    }]
)

print(response.content[0].text)
proc.terminate()
```

---

## Deploy to Railway (2 minutes)

### Prerequisites:
- GitHub account
- Railway account (free tier)

### Steps:

1. **Initialize Git** (if not already done)
```bash
cd /Users/yacht/1000jets
git init
git add .
git commit -m "Add 1000jets MCP server"
git remote add origin https://github.com/YOUR_USERNAME/1000jets-mcp.git
git push -u origin main
```

2. **Deploy on Railway**
   - Go to railway.app
   - Click "New Project"
   - Select "Deploy from GitHub"
   - Connect your account and select the 1000jets-mcp repo
   - Railway auto-detects Dockerfile
   - Add env var: `AVIAPAGES_API_TOKEN=qOAgJCLM8SJTnPQZxF2SOqW5hiZofySiU4KF`
   - Click "Deploy"

3. **Get your live URL**
   - Once deployed, Railway gives you a public URL (like `1000jets-mcp.railway.app`)
   - This is where your MCP is now hosted

---

## Test the MCP

### Example 1: Search Jets
```
You: "I need a jet from LAX to NYC for 6 people on 2026-10-15"

Claude: [uses search_jets tool]

Output: "Found 8 available jets:
• Light Jet - From $8,500
• Midsize Jet - From $12,000
• Super Midsize - From $15,500
..."
```

### Example 2: Get Price Quote
```
You: "How much for a Heavy Jet from JFK to Miami for 8 people on 2026-10-20?"

Claude: [uses get_jet_price tool]

Output: "**Charter Price Quote**
Route: JFK → MIA
Aircraft: Heavy Jet
Passengers: 8
Base Price: $28,000
Flight Hours: 3.5
Total: $31,500"
```

### Example 3: Create Booking
```
You: "Book me the Midsize Jet from JFK to Miami for 4 people. My name is John Smith, email john@example.com"

Claude: [uses create_booking_request tool]

Output: "✅ **Booking Request Created**
Request ID: BR-12345
Passenger: John Smith
Email: john@example.com

Next Steps:
1. Our team will review your request
2. You'll receive a detailed quote
3. Confirm and complete payment"
```

---

## Your Next Moves

**Day 1 (Today):**
- ✅ Test locally (`python mcp_server.py`)
- ✅ Connect to Claude Code
- ✅ Try a few test searches

**Day 2:**
- Push to GitHub
- Deploy to Railway
- Get live URL

**Day 3:**
- Publish to MCP registry (mcp.run)
- Tweet announcement
- Start ChatGPT/Gemini expansion

---

## Troubleshooting

**"ModuleNotFoundError: mcp"**
```bash
pip install mcp
```

**"AVIAPAGES_API_TOKEN not set"**
```bash
export AVIAPAGES_API_TOKEN="qOAgJCLM8SJTnPQZxF2SOqW5hiZofySiU4KF"
```

**"Connection refused"**
- Make sure the server is running (`python mcp_server.py`)
- Check that Claude is configured to use the right path

**"API Rate Limited"**
- You're hitting Aviapages limits (300/month for searches/prices)
- Upgrade your Aviapages plan for higher limits

---

## Support

- Aviapages API docs: https://aviapages.com/api
- MCP docs: https://modelcontextprotocol.io
- Questions? See MCP_README.md

---

**Ready? Run:** `python mcp_server.py`
