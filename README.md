# CreditRisk Financial Analyst Tool

> **AI-powered financial analysis using 7 legendary investor perspectives — built with the DRIVER methodology.**

> **Disclaimer:** This tool is for educational and informational purposes only. It does not constitute financial advice, investment recommendations, or professional guidance of any kind. The analyses generated are AI-simulated perspectives and should not be used as the basis for any investment decisions. Always consult a qualified financial advisor before making investment decisions. Use at your own risk.

---

## What This Tool Does

Run a single command and get institutional-grade stock analysis from 7 legendary investor perspectives, including deep credit risk and forensic accounting metrics.

```
/financial-researcher AAPL          # Prompts for mode
/financial-researcher NVDA --full   # Full 7-guru analysis
/financial-researcher TSLA --quick  # Quick metrics only
```

---

## The 7 Investor Analysts

| Investor | Focus |
|----------|-------|
| Warren Buffett | Moats, owner earnings, intrinsic value |
| Ben Graham | Margin of safety, asset-based valuation |
| Peter Lynch | PEG ratio, growth story |
| Cathie Wood | Disruption, TAM, 5-year vision |
| George Soros | Reflexivity, macro regime |
| Ray Dalio | Cycles, debt analysis, stress tests |
| Michael Burry | Forensics, bear case, contrarian signals |

---

## Metrics & Analysis Engine

### Pre-Calculated Composite Scores

The Python processing layer calculates institutional-grade metrics not available from standard APIs:

| Score | What It Measures | Threshold |
|-------|-----------------|-----------|
| **Piotroski F-Score** | Financial strength (0–9) | ≥7 = strong |
| **Altman Z-Score** | Bankruptcy prediction | >2.99 = safe |
| **Ohlson O-Score** | Bankruptcy probability (0–1) | Lower = better |
| **Beneish M-Score** | Earnings manipulation risk | < −2.22 = clean |
| **Sloan Accrual Ratio** | Earnings quality | −10% to +10% = safe |
| **FCF Conversion** | Cash backing of earnings | >80% = healthy |
| **Owner Earnings** | Buffett's true cash to owners | — |
| **EVA** | Value created above cost of capital | Positive = good |
| **DuPont 5-Factor** | ROE decomposition | — |
| **Total Shareholder Yield** | Dividends + buybacks + debt paydown | — |

### Credit Risk Assessment

Integrated credit risk analysis covers:
- **Solvency metrics** — long-term debt sustainability
- **Liquidity ratios** — short-term obligations coverage
- **Default probability** — derived from Altman Z-Score and bond ratings
- **Distress valuation** — explicit failure node following Damodaran's framework:

$$\text{Value} = [\text{DCF}_{Alive} \times (1 - P_{Failure})] + [\text{Distress Sale Value} \times P_{Failure}]$$

---

## Damodaran DCF Framework (Built-In Rules)

This tool enforces Damodaran's discipline for rigorous valuation:

### 1. No Point Estimates — Monte Carlo Mandate
Never use single-number estimates. All key variables (revenue, margins, cost of capital) use probability distributions, outputting a **valuation range** (10th / 50th / 90th percentile).

### 2. Dynamic Cost of Capital (Glide Path)
WACC must evolve over time:
- **Years 1–5 (High Growth):** Higher risk-adjusted WACC
- **Terminal Year:** Converges to Risk-Free Rate + 4.5–5.0% ERP

### 3. R&D and Marketing Capitalization
GAAP treats R&D as an expense — this tool corrects that:
1. Add R&D/Marketing back to Operating Income (Adjusted EBIT)
2. Create a "Research Asset" on the balance sheet (amortized over useful life)
3. Adjust Reinvestment Rate to include capitalized spending

### 4. Narrative Check (Story > Numbers)
Before modeling, the business narrative is stated explicitly:
- **High Growth narrative** → Reinvestment Rate must be high
- **Stable Cash Cow** → Growth capped at risk-free rate
- **Sanity Check:** Terminal market share cannot exceed 100% of TAM

### 5. Explicit Distress Risk
Bankruptcy risk is NOT baked into WACC alone. P(Failure) is estimated from bond ratings or Altman Z-Score and modeled as a separate decision node.

---

## Built With the DRIVER Methodology

This plugin was developed using the **DRIVER** framework — a 6-stage methodology for AI-augmented finance tool development.

| Stage | Purpose | Iron Law |
|-------|---------|----------|
| **D**efine | Research what exists | No building without research first |
| **R**epresent | Plan part by part | Don't reinvent what exists |
| **I**mplement | Build and run | Show don't tell |
| **V**alidate | Verify it works | Evidence before claims |
| **E**volve | Package deliverable | Self-contained export |
| **R**eflect | Capture learnings | Document what didn't work |

### The Philosophy

> **Cognition Mate (认知伙伴)** — 互帮互助，因缘合和，互相成就
> *Mutual help. Interdependent arising. Accomplishing together.*

- **You bring:** vision, domain expertise, judgment
- **AI brings:** patterns, research ability, heavy lifting on code
- **Neither creates alone** — meaning emerges from interaction

### DRIVER Plugin

This tool is published as a Claude Code plugin. To install from GitHub:

```bash
/plugin marketplace add https://github.com/CinderZhang/driver-plugin
/plugin install driver@driver-plugin
```

Or for local development:

```bash
/plugin marketplace add /path/to/driver-plugin
/plugin install driver@driver-dev
```

---

## Installation

1. **Clone this repo**

2. **Configure API keys** in `.mcp.json` and `.env`:
   - `FINANCIAL_DATASETS_API_KEY` — [financialdatasets.ai](https://financialdatasets.ai)
   - `TAVILY_API_KEY` — [tavily.com](https://tavily.com)

3. **Copy `.env.example` → `.env`** and add your keys

---

## Project Structure

```
FAskills/
├── .claude-plugin/              # Marketplace config
├── .mcp.json                    # MCP server definitions
├── CLAUDE.md                    # Project instructions
└── financial-researcher/        # The plugin
    ├── .claude-plugin/          # Plugin config
    ├── SKILL.md                 # Main skill orchestration
    ├── experts/                 # 7 investor prompts
    ├── processing/              # Python metrics layer
    │   ├── orchestrator.py      # Entry point: run_analysis()
    │   ├── data_extractor.py    # Maps API responses to objects
    │   ├── metrics_calculator.py# All composite score calculations
    │   └── financial_metrics.py # Legacy calculations
    ├── references/              # DRIVER methodology docs
    ├── reports/                 # Generated analyses (saved here)
    └── templates/               # Output schemas
```

---

## Testing

```bash
cd financial-researcher
python -m processing.test_pipeline
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| AI Orchestration | Claude Code + DRIVER plugin |
| Data | financialdatasets.ai, Tavily |
| Processing | Python (NumPy, Pandas) |
| Valuation Framework | Damodaran DCF |

---

## Key Chinese Terms (DRIVER Philosophy)

| Term | Pinyin | Meaning |
|------|--------|---------|
| 认知伙伴 | rèn zhī huǒ bàn | Cognition Mate — thinking partner |
| 互帮互助 | hù bāng hù zhù | Mutual help |
| 因缘合和 | yīn yuán hé hé | Interdependent arising |
| 互相成就 | hù xiāng chéng jiù | Accomplishing together |
| 开题调研 | kāi tí diào yán | Open the topic + research (DEFINE) |
| 分头研究 | fēn tóu yán jiū | Parallel research |

---

## License

MIT — See [LICENSE](../LICENSE) file.

---

*Built through the practice it teaches — human vision and AI collaboration, accomplishing together.*
