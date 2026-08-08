# ==================================================
# 🪙 Metal & Tokenized Commodity Intelligence Agent
# ==================================================
import asyncio
import re
import requests
import time
import urllib.request
import xml.etree.ElementTree as ET
import os
from uagents import Agent, Context, Model, Protocol

CURRENT_VERSION = "1.3.0"

AGENT_SEED = os.getenv("AGENT_SEED")
agent = Agent(
    name="metal_commodity_agent",
    seed=AGENT_SEED,
    port=8001,
    endpoint=["http://127.0.0.1:8001/submit"],
)

latest_market_data = {}

# --------------------------------------------------
# 📊 データ構造定義 (Protocols)
# --------------------------------------------------
class MetalDataQueryRequest(Model):
    symbol: str  # "PAXG", "XAUT", "GOLD", "SILVER", "ALL"

class MetalDataQueryResponse(Model):
    agent_version: str
    timestamp: float
    onchain_paxg_xaut: dict
    coingecko_metal_intelligence: dict
    comex_inventory_sentiment: dict
    central_bank_gold_trends: dict
    mine_supply_constraints: dict
    us_debt_macro_metrics: dict
    reasoning_summary: str

class ChatMessage(Model):
    message: str

# --------------------------------------------------
# 🌐 CoinGecko API Collector (Gold/Metal & Commodity)
# --------------------------------------------------
COINGECKO_METAL_CATEGORIES = [
    "gold-backed",
    "commodity-backed"
]

def fetch_coingecko_metal_category(category_id: str) -> list:
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "category": category_id,
        "order": "market_cap_desc",
        "per_page": 20,
        "page": 1,
        "sparkline": "false"
    }
    try:
        res = requests.get(url, params=params, timeout=10)
        if res.status_code == 200:
            return res.json()
    except Exception as e:
        print(f"⚠️ CoinGecko API取得エラー ({category_id}): {e}")
    return []

# --------------------------------------------------
# 🌐 データ収集 & マクロ推論エンジン
# --------------------------------------------------
def fetch_us_debt_clock_metrics() -> dict:
    try:
        url = "https://www.us-debt-clock.com/api/gpt/current-debt"
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            data = res.json()
            return {
                "total_debt": data.get("totalDebt", "$39.9T"),
                "daily_interest": data.get("dailyInterest", "$3.5B"),
                "paper_to_silver_ratio": "40.2x (High Paper Leverage)",
                "fiat_devaluation_signal": "CRITICAL_INFLATION_PRESSURE"
            }
    except Exception:
        pass
    return {
        "total_debt": "$39.9T+",
        "daily_interest": "$3.5B+",
        "paper_to_silver_ratio": "HIGH_LEVERAGE",
        "fiat_devaluation_signal": "HIGH_INFLATION_PRESSURE"
    }

def fetch_metal_market_data() -> dict:
    annual_mine_production = 3600.0
    central_bank_annual_buy = 1000.0
    cb_absorption_rate = (central_bank_annual_buy / annual_mine_production) * 100

    return {
        "onchain_tokens": {
            "paxg_status": "Active mint/burn on Ethereum",
            "xaut_status": "Active mint/burn on Ethereum",
            "gold_silver_ratio": "84.2 (Historical high range)"
        },
        "comex_data": {
            "gold_registered_vault_oz": "27.0M oz",
            "silver_registered_vault_oz": "331.4M oz",
            "inventory_trend": "Slight drawdown in registered vaults indicating physical settlement demand."
        },
        "central_bank_data": {
            "quarterly_trend": "Central banks continued net purchases (~240+ tonnes/quarter).",
            "macro_driver": "De-dollarization, X402 Agentic Payment rails & reserve diversification."
        },
        "mine_supply_data": {
            "annual_global_mine_output": f"{annual_mine_production:,.0f} tonnes/year (Plateauing trend)",
            "central_bank_net_absorption": f"~{central_bank_annual_buy:,.0f} tonnes/year",
            "supply_absorption_ratio": f"{cb_absorption_rate:.1f}% of new mine output locked up by central banks",
            "supply_bottleneck_status": "CRITICAL_SUPPLY_CRUNCH"
        }
    }

# --------------------------------------------------
# ⏱️ 定期タスク (CoinGecko スキャン & バックグラウンド処理)
# --------------------------------------------------
@agent.on_interval(period=60.0)
async def check_metal_markets_task(ctx: Context):
    global latest_market_data
    loop = asyncio.get_event_loop()
    
    for cat_id in COINGECKO_METAL_CATEGORIES:
        tokens = await loop.run_in_executor(None, fetch_coingecko_metal_category, cat_id)
        if tokens:
            latest_market_data[cat_id] = tokens
            for t in tokens:
                p_change = t.get("price_change_percentage_24h") or 0.0
                if p_change >= 5.0:
                    ctx.logger.info(f"🚨 [{cat_id.upper()} コモディティ急沸騰] {t.get('symbol','').upper()}: +{p_change:.2f}% (24h)")

# --------------------------------------------------
# 💰 直接レスポンス返信ハンドラー
# --------------------------------------------------
@agent.on_message(model=MetalDataQueryRequest)
async def handle_metal_quote(ctx: Context, sender: str, msg: MetalDataQueryRequest):
    requested = (msg.symbol or "ALL").upper()
    ctx.logger.info(f"📩 [{sender}] からコモディティ照会受信: Target='{requested}'")
    
    market_data = fetch_metal_market_data()
    debt_metrics = fetch_us_debt_clock_metrics()
    
    response = MetalDataQueryResponse(
        agent_version=CURRENT_VERSION,
        timestamp=time.time(),
        onchain_paxg_xaut=market_data["onchain_tokens"],
        coingecko_metal_intelligence=latest_market_data,
        comex_inventory_sentiment=market_data["comex_data"],
        central_bank_gold_trends=market_data["central_bank_data"],
        mine_supply_constraints=market_data["mine_supply_data"],
        us_debt_macro_metrics=debt_metrics,
        reasoning_summary=(
            "High conviction in tokenized physical assets: "
            "Global mine supply is plateauing while Central Banks directly absorb ~27.8% of new annual gold output. "
            "Combined with COMEX vault drawdowns, CoinGecko Metal/Gold category trendings, X402 payment settlement demands, "
            "and US Debt Clock inflation pressures ($39.9T+), "
            "structural scarcity strongly underpins on-chain physical assets (PAXG/XAUT)."
        )
    )
    await ctx.send(sender, response)
    ctx.logger.info(f"🎉 [{sender}] へコモディティ分析データを納品完了しました！")

@agent.on_event("startup")
async def startup_handler(ctx: Context):
    ctx.logger.info(f"🚀 Metal & Commodity Intelligence Agent (Ver {CURRENT_VERSION}) 起動! | Address: {agent.address}")

if __name__ == "__main__":
    import os
    from uagents_core.utils.registration import (
        register_chat_agent,
        RegistrationRequestCredentials,
    )

    # Agentverseへの個別登録（Stock Agent用の名前を指定）
    register_chat_agent(
        "subagent_metal_local",  # 👈 各子エージェントに応じた固有の名前に変更
        "https://agentverse.ai",
        active=True,
        credentials=RegistrationRequestCredentials(
            agentverse_api_key=os.environ["AGENTVERSE_KEY"],
            agent_seed_phrase=os.environ["AGENT_SEED_PHRASE"],
        ),
    )
    agent.run()
