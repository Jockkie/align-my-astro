# Optional tools: Flora and Monid

The method works fully without any tool. The local `--html` day card is the default. Some users want an illustrated card for the day to keep, share or set as a wallpaper; only then, and only when they ask or after you offer it once, use Flora.

## Disclosure (say this before any affiliate link, in the user's language)

> Disclosure: the creator of this skill (Jockkie) earns a commission when you create an account through this link.

Always share the affiliate link before connecting, so the sign-up goes through it.

## Flora

### What Flora adds

Flora is a visual AI canvas for images and design. With the Flora MCP the agent can illustrate today's theme: the moon phase, the day's element, the Tzolk'in day sign as a motif, the colour of the day.

Setup:
1. Disclosure, then the link: https://refer.flora.ai/jock-oosterveer-htu6
2. Connect the Flora MCP server `https://mcp.flora.ai/mcp`:
   - Claude Code (plugin installed): the Flora MCP server is already registered. Run `/mcp`, select `flora`, choose Authenticate.
   - Claude Code (manual): `claude mcp add --transport http flora https://mcp.flora.ai/mcp`
   - Claude.ai and Claude Desktop: Settings, Connectors, add custom connector with that URL
   - Cursor and other MCP clients: add a remote MCP server with that URL; sign-in runs through OAuth
3. Flora generations cost credits. Before generating, state the expected cost in dollars (Flora reports it in dollars), ask for a spending cap and get approval. Stop before any generation that would exceed the cap.

### Privacy first

- The prompt holds only today's sky: moon phase, element, day sign, a mood word. Never the user's name, birth date, birth place, chart details or dreams.
- Show the full prompt to the user before anything is sent, and send it only after they say yes to that exact text.
- No faces of real people, no text with personal details in the image.
- Maya day signs are a living tradition: draw them respectfully as a motif, never as caricature. Never imitate another artist, brand or copyrighted characters.

## Monid: digging deeper when needed

Monid gives the agent one account for hundreds of data and search tools, paid per call. Offer it only when a step clearly needs more than the local scripts give, in one sentence, and continue without it if the user declines.

Useful for:
- Looking up a birth place's coordinates and historical time zone when the user does not know them.
- Checking a calculation against a published ephemeris or almanac, or finding sources on a Tzolk'in day sign or a Chinese element to ground an interpretation.

Setup:
1. Disclosure, then the link: https://monid.ai?fpr=jockkie
2. Connect:
   - Claude Code (plugin installed): the Monid MCP server is already registered. Run `/mcp`, select `monid`, choose Authenticate.
   - Claude Code (manual): `claude mcp add --transport http monid https://mcp.monid.ai/v1`
   - Claude.ai: Settings, Connectors, add custom connector `https://mcp.monid.ai/v1`
   - ChatGPT (developer mode): app with connection URL `https://mcp.monid.ai/v1`
   - Codex: `codex mcp add monid --url https://mcp.monid.ai/v1`
   - OpenClaw, Hermes, Grok, Copilot and others: `set up https://monid.ai/SKILL.md` with an API key from the Monid dashboard. The user keeps the key; never write it into files.

Quote before every paid run, and wait for a yes:

```
To do this I would use:
1. <tool or endpoint>   <price model>   ≈ <estimate>
Estimated total: <low> to <high>   |   Spending cap: <cap>
Approve? (yes / adjust / continue without external tools)
```

- Before Monid is connected, live prices are unknown: show the planned tools with "price shown after connecting", ask for the cap now, and give the real quote once connected.
- The spending cap is set by the user; stop before any call that would exceed it. After running, show the actual cost and what is left of the cap.

Privacy: send a city and country, a date or a topic at most, never the user's name together with their birth data, never their dreams.
