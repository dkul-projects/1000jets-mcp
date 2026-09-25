# 1000jets MCP - Book Private Jets in Claude

The first AI-native jet booking platform. Search, price, and book private jets directly inside Claude, ChatGPT, Gemini, and other LLMs.

## What This Does

Users can now book private jets without leaving their LLM chat interface:

```
User: "I need a jet from JFK to Miami for 4 people tomorrow morning"
Claude: [searches 1000jets MCP] "Found 8 available jets. Here are the options..."
User: "Book the Light Jet for $5,200"
Claude: [creates booking request] "✅ Booking confirmed. Confirmation #XYZ sent to your email"
```

## Features

- **Search Jets** - Real-time availability search across Aviapages network
- **Get Prices** - Instant pricing quotes for specific routes and aircraft
- **Create Bookings** - One-click booking requests (quote → book → pay flow)
- **Empty Legs** - Discounted one-way charter deals
- **Integration** - Works with Claude, ChatGPT, Gemini, Groq, and more

---

## Local Development

### Prerequisites
- Python 3.11+
- `pip` and `venv`
- Aviapages API token (in environment)

### Setup

```bash
# Clone/navigate to the project
cd /Users/yacht/1000jets

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set API token
export AVIAPAGES_API_TOKEN="qOAgJCLM8SJTnPQZxF2SOqW5hiZofySiU4KF"

# Run the MCP server
python mcp_server.py
```

The server will start and wait for MCP client connections (like Claude).

---

## Deploy to Railway (2 minutes)

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial 1000jets MCP commit"
git remote add origin https://github.com/YOUR_USERNAME/1000jets-mcp.git
git push -u origin main
```

### Step 2: Deploy on Railway
1. Go to [railway.app](https://railway.app)
2. Click "New Project" → "Deploy from GitHub"
3. Select your `1000jets-mcp` repository
4. Railway auto-detects the Dockerfile
5. Add environment variable: `AVIAPAGES_API_TOKEN=qOAgJCLM8SJTnPQZxF2SOqW5hiZofySiU4KF`
6. Click "Deploy"
7. Copy the Railway URL from the deployment logs

Your MCP is now live! 🚀

---

## Add to Claude

### Option 1: Claude Code (Built-in MCP Support)

1. Open [Claude Code](https://claude.com/claude-code)
2. Click Settings → MCP Servers
3. Click "Add Server"
4. Configure:
   ```
   Name: 1000jets
   Type: Command
   Command: python /Users/yacht/1000jets/mcp_server.py
   Env: AVIAPAGES_API_TOKEN=qOAgJCLM8SJTnPQZxF2SOqW5hiZofySiU4KF
   ```
5. Reload Claude

### Option 2: Claude.ai (Web)

1. Open [claude.ai](https://claude.ai)
2. Start a conversation
3. Mention: "Add my 1000jets MCP server"
4. Follow the prompt to configure

### Option 3: Claude API (Programmatic)

```python
from anthropic import Anthropic

client = Anthropic(
    mcp_servers={
        "1000jets": {
            "command": "python",
            "args": ["/Users/yacht/1000jets/mcp_server.py"],
            "env": {"AVIAPAGES_API_TOKEN": "qOAgJCLM8SJTnPQZxF2SOqW5hiZofySiU4KF"}
        }
    }
)

response = client.messages.create(
    model="claude-opus-5",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": "Find me a jet from LAX to NYC for 6 people next Friday"
    }]
)
print(response.content[0].text)
```

---

## Publish to MCP Registry

Once tested, publish your MCP for discoverability:

### Step 1: Create GitHub Release
```bash
git tag v1.0.0
git push origin v1.0.0
```

### Step 2: Submit to MCP Registry
1. Go to [mcp.run](https://mcp.run)
2. Click "Submit Server"
3. Fill in:
   - **Name:** 1000jets Jet Booking
   - **Description:** Book private jets in Claude, ChatGPT, Gemini
   - **GitHub URL:** https://github.com/YOUR_USERNAME/1000jets-mcp
   - **Maintainer Email:** your-email@1000jets.com

Done! Users can now find your MCP in the registry.

---

## Expand to ChatGPT, Gemini (Week 2)

### ChatGPT Custom Actions

Convert your MCP tools to OpenAI Actions:

```json
{
  "openapi": "3.0.0",
  "info": {"title": "1000jets Jet Booking", "version": "1.0.0"},
  "servers": [{"url": "https://YOUR_RAILWAY_URL"}],
  "paths": {
    "/search": {
      "post": {
        "operationId": "searchJets",
        "parameters": [
          {"name": "departure", "in": "query", "schema": {"type": "string"}},
          {"name": "arrival", "in": "query", "schema": {"type": "string"}},
          {"name": "date", "in": "query", "schema": {"type": "string"}},
          {"name": "passengers", "in": "query", "schema": {"type": "integer"}}
        ]
      }
    }
  }
}
```

1. Create a web API wrapper (Flask/FastAPI) that exposes your MCP tools as REST endpoints
2. Generate OpenAPI spec
3. Add to ChatGPT via Settings → Custom GPTs

### Gemini Extensions

Similar process: wrap your MCP tools as REST endpoints → add to Gemini Extensions.

---

## Marketing Copy (For Launch)

### Twitter/X
> "Just launched: Book private jets without leaving Claude 🛫 Search, price, and book jets in one conversation. No forms, no calls. The AI-native jet booking platform is here. 1000jets.com + MCP"

### Product Hunt
> "First AI-native jet booking platform - book jets in Claude, ChatGPT & Gemini. Real Aviapages pricing & availability, instant quotes, one-click booking."

### Landing Page
```
HEADLINE: Book Private Jets in Claude AI

COPY:
"Stop switching apps. Book your jet in the LLM you already use.

✈️ Search availability
💰 Get instant prices  
✅ Confirm booking
All inside Claude, ChatGPT, or Gemini.

Powered by 1000 verified jet operators worldwide."

CTA: "Launch the MCP" → https://claude.ai/mcp/1000jets
```

---

## Rate Limits (Aviapages Free Account)

- Charter Quotes: 30/month
- Aircraft: 10/month
- Companies: 10/month
- Search/Prices/Empty Legs: 300/month

**Scaling:** Upgrade to paid Aviapages account for higher limits.

---

## Next Steps

1. ✅ **Local test** - Run `python mcp_server.py` and connect Claude
2. ✅ **Deploy to Railway** - Get live URL
3. ✅ **Publish to registry** - Make discoverable
4. ✅ **Launch marketing** - Tweet, Product Hunt, HN
5. ✅ **Expand to ChatGPT/Gemini** - Week 2

---

## Support

Questions? Check Aviapages docs: https://aviapages.com/api

---

**Built for 1000jets.com - The AI-native jet booking platform**
