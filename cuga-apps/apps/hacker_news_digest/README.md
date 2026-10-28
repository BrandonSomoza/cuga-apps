# Hacker News Digest

A Cuga-powered app for a concise, developer-focused digest of Hacker News stories.
It fetches current feed items, links to the articles and discussions, and can
summarize a story in four bullets.

## Run

```bash
pip install -r requirements.txt
python main.py --port 28841
```

Configure `LLM_PROVIDER`, `LLM_MODEL`, and `AGENT_SETTING_CONFIG` as for other
Cuga apps. Open <http://127.0.0.1:28841>.

## Example prompts

- What's on Hacker News today?
- Top 5 Hacker News stories, one line each
- Anything about Python on Hacker News?
- Show me interesting Show HN projects
- Summarize the #1 story on Hacker News

## Tools

Uses the existing `web` MCP tools `fetch_feed` and `fetch_webpage`.
