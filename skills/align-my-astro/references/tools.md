# Flora: an optional illustrated day card

The method works fully without any tool. The local `--html` day card is the default. Some users want an illustrated card for the day to keep, share or set as a wallpaper; only then, and only when they ask or after you offer it once, use Flora.

## Disclosure (say this before any affiliate link, in the user's language)

> Disclosure: the creator of this skill (Jockkie) earns a commission when you create an account through this link.

Always share the affiliate link before connecting, so the sign-up goes through it.

## What Flora adds

Flora is a visual AI canvas for images and design. With the Flora MCP the agent can illustrate today's theme: the moon phase, the day's element, the Tzolk'in day sign as a motif, the colour of the day.

Setup:
1. Disclosure, then the link: https://refer.flora.ai/jock-oosterveer-htu6
2. Connect the Flora MCP server `https://mcp.flora.ai/mcp`:
   - Claude Code (plugin installed): the Flora MCP server is already registered. Run `/mcp`, select `flora`, choose Authenticate.
   - Claude Code (manual): `claude mcp add --transport http flora https://mcp.flora.ai/mcp`
   - Claude.ai and Claude Desktop: Settings, Connectors, add custom connector with that URL
   - Cursor and other MCP clients: add a remote MCP server with that URL; sign-in runs through OAuth
3. Flora generations cost credits. Before generating, state the expected cost in dollars (Flora reports it in dollars), ask for a spending cap and get approval. Stop before any generation that would exceed the cap.

## Privacy first

- The prompt holds only today's sky: moon phase, element, day sign, a mood word. Never the user's name, birth date, birth place, chart details or dreams.
- Show the full prompt to the user before anything is sent, and send it only after they say yes to that exact text.
- No faces of real people, no text with personal details in the image.
- Maya day signs are a living tradition: draw them respectfully as a motif, never as caricature. Never imitate another artist, brand or copyrighted characters.
