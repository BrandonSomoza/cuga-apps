# Crypto 101

A Cuga-powered demo app that explains and provides the latest price for a given
cryptocurrency in a beginner friendly manner.

## Port

**28840**

## Quick start

```bash
# Install dependencies
pip install -r requirements.txt

# Set required env vars (example: Anthropic)
export LLM_PROVIDER=anthropic
export LLM_MODEL=claude-sonnet-4-6
export ANTHROPIC_API_KEY=<your-key>
export AGENT_SETTING_CONFIG=/path/to/settings.toml

# Run
python main.py --port 28840

# Open in browser
open http://127.0.0.1:28840
```

## Environment variables

| Variable | Required | Description |
|---|---|---|
| `LLM_PROVIDER` | Always | `anthropic` \| `openai` \| `rits` \| `watsonx` \| `litellm` \| `ollama` |
| `LLM_MODEL` | Always | Model name for the chosen provider (e.g. `claude-sonnet-4-6`, `gpt-4o`) |
| `AGENT_SETTING_CONFIG` | Always | Path to the agent settings TOML file |
| `ANTHROPIC_API_KEY` | When `LLM_PROVIDER=anthropic` | Anthropic API key |
| `OPENAI_API_KEY` | When `LLM_PROVIDER=openai` | OpenAI API key |
| `RITS_API_KEY` | When `LLM_PROVIDER=rits` | IBM RITS API key |

## Example prompts

1. `What is Bitcoin, and what's its price today?`
2. `Explain Ethereum like I'm new to crypto`
3. `How is Solana different from Bitcoin?`
4. `What is Dogecoin and why does it exist?`
5. `Compare Bitcoin and Ethereum for a beginner`

## Tools

| Tool | Description |
|---|---|
| `get_crypto_price` | Fetch current price + 24h change for a cryptocurrency via CoinGecko |
| `get_stock_quote` | Fetch a real-time stock quote via Alpha Vantage |
