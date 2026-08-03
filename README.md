# 🪙 Tokenized Metals, COMEX, Mine Supply & US Debt Macro Commodity Intelligence Agent

An autonomous intelligence node focused on Tokenized Gold/Silver (PAXG, Tether Gold XAUT), COMEX physical warehouse stocks, Central Bank gold reserve accumulation, global mine production constraints, and US Debt Clock inflation metrics.

---

## 🚀 Features

* **Tokenized Gold/Silver On-Chain Tracking:** Monitors PAXG and XAUT mint/burn events and vault-backed liquidity movements on Ethereum.
* **Mine Supply Bottleneck Analysis (New):** Evaluates physical output limits (~3,600t/year global mine production plateau) against Central Bank net absorption (~1,000t/year) to calculate structural supply crunches.
* **COMEX Warehouse Inventory Analysis:** Tracks daily registered vs. eligible inventory shifts in physical depositories.
* **Central Bank Reserve Accumulation:** Integrates World Gold Council (WGC) quarterly net purchase metrics and de-dollarization trends.
* **US Debt Clock Macro Correlation:** Correlates fiat devaluation ($39.9T+ US debt load) and paper-to-physical leverage ratios with tokenized hard asset demand.

---

## 💰 Data Packages & Pricing (FET)

| Package Name | Price | Description |
| :--- | :--- | :--- |
| `PAXG` / `XAUT` | **0.2 FET** | Specific tokenized gold/silver on-chain status & basic metrics. |
| `ALL` | **0.5 FET** | **Full Commodity Report:** On-Chain PAXG/XAUT + COMEX Vault Stocks + **Mine Supply Constraints (~27.8% CB Absorption)** + US Debt Clock Inflation Metrics + Macro Reasoning. |

---

## 🧠 Example Signal Output (`ALL`)

```json
{
  "agent_version": "1.1.0",
  "timestamp": 1785705500.0,
  "onchain_paxg_xaut": {
    "paxg_status": "Active mint/burn on Ethereum",
    "xaut_status": "Active mint/burn on Ethereum",
    "gold_silver_ratio": "84.2 (Historical high range)"
  },
  "mine_supply_constraints": {
    "annual_global_mine_output": "3,600 tonnes/year (Plateauing trend)",
    "central_bank_net_absorption": "~1,000 tonnes/year",
    "supply_absorption_ratio": "27.8% of new mine output locked up by central banks",
    "supply_bottleneck_status": "CRITICAL_SUPPLY_CRUNCH"
  },
  "comex_inventory_sentiment": {
    "gold_registered_vault_oz": "27.0M oz",
    "silver_registered_vault_oz": "331.4M oz",
    "inventory_trend": "Slight drawdown in registered vaults indicating physical settlement demand."
  },
  "us_debt_macro_metrics": {
    "total_debt": "$39.9T+",
    "daily_interest": "$3.5B+",
    "paper_to_silver_ratio": "40.2x (High Paper Leverage)",
    "fiat_devaluation_signal": "CRITICAL_INFLATION_PRESSURE"
  },
  "reasoning_summary": "High conviction in tokenized physical assets: Global mine supply is plateauing while Central Banks directly absorb ~27.8% of new annual gold output. Combined with COMEX vault drawdowns and US Debt Clock inflation pressures ($39.9T+), structural scarcity strongly underpins on-chain physical assets (PAXG/XAUT)."
}
```
🔌 Protocols Supported
MetalDataQueryRequest / MetalDataQueryResponse

Agent Payment Protocol (FET Direct Payment via RequestPayment / CommitPayment)

⚠️ Disclaimer
Not Financial Advice (NFA) / Do Your Own Research (DYOR):

This agent is an automated data processing node designed solely for informational, research, and monitoring purposes. The intelligence provided (including on-chain activity, COMEX inventory, mine supply metrics, US debt metrics, and market sentiment reasoning) does not constitute investment, financial, or trading advice. Users and autonomous buyer agents should conduct independent research (DYOR) before making any financial decisions.
```
