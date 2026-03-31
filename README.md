# Lexical Repetition

This repository contains a small experimental dataset and analysis scripts for studying **lexical repetition behavior** in LLM outputs under different prompting conditions.

The current material focuses on a character-style prompt family (primarily a *knight* persona) and compares how output length and prompt style influence:

- **Synonymous repetition** in responses.
- **Prompt-overlap repetition** (model reusing prompt phrasing).

## Repository Layout

```text
.
├── prompts.txt
├── intra_turn_test/
│   ├── no_prompt-intro/
│   ├── short_prompt-intro/
│   ├── long-prompt-intro/
│   └── anti-rep intro/
└── data/
    ├── synonymous/
    │   ├── occurrence.py
    │   └── rate.py
    └── overlap/
        ├── overlap-count
        └── overlap-rate
```

### Key files

- `prompts.txt`: Prompt templates used for the tested personas and variants (no persona, light persona, long persona, and anti-repetition instruction).  
- `intra_turn_test/...`: Collected trial outputs at different target lengths (25, 50, 100, 200, 400 words) for each prompt variant.  
- `data/synonymous/occurrence.py`: Plots synonymous repetition **occurrence counts** vs. response length with error bars and power-law fits.  
- `data/synonymous/rate.py`: Plots synonymous repetition **rates** (occurrences normalized by output length) with power-law fits.  
- `data/overlap/overlap-count`: Plots prompt-overlap **occurrence counts** vs. response length.  
- `data/overlap/overlap-rate`: Plots prompt-overlap **rates** (occurrences normalized by output length), including trial-level scatter, mean trends, and power-law fits.

## Setup

### Requirements

- Python 3.9+
- `numpy`
- `matplotlib`

Install dependencies:

```bash
pip install numpy matplotlib
```

## Running the analysis

From the repository root:

```bash
python data/synonymous/occurrence.py
python data/synonymous/rate.py
python data/overlap/overlap-count
python data/overlap/overlap-rate
```
Each script opens a `matplotlib` visualization window.

## Data notes

- Trial data appears to be manually curated in the scripts and text files.
- Most analyses are based on three trials per length bucket.
- Length buckets currently used: **25, 50, 100, 200, 400** words.
