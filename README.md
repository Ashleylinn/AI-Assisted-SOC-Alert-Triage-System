# AI-Assisted-SOC-Alert-Triage-System

## Overview

This project simulates a Security Operations Center (SOC) workflow by automating the triage of authentication logs. The system analyzes login events, identifies potentially suspicious activity using simple detection logic, and generates AI-assisted, analyst-readable incident summaries to support security analysts in decision-making.

The goal of this project is to demonstrate practical AI automation in information security, focusing on systems thinking rather than advanced machine learning.

## AI Component

This project uses an AI-ready design for incident summarization.
Incident explanations and recommended actions are generated using
structured, LLM-style prompts.

To ensure transparency and explainability, the current implementation
simulates AI output using deterministic logic. This allows the alert
triage and automation workflow to be validated before integrating an
external AI API.

This mirrors real-world engineering practice, where automation logic
and safety controls are established prior to introducing AI services.

## Motivation

In real SOC environments, analysts must review large volumes of alerts and logs under time pressure. Many alerts are repetitive or low risk, making manual triage inefficient and error-prone.

This project explores how AI can assist—not replace—security analysts by:

- Reducing manual log review

- Automatically categorizing alert severity

- Generating clear, human-readable incident summaries

## System Architecture

## Workflow

1. Synthetic authentication logs are generated using a Python script (`generate_logs.py`)
2. Logs are analyzed using rule-based detection logic to identify suspicious activity (`detect_alerts.py`)
3. Alerts are classified into Low / Medium / High risk levels based on explainable rules
4. AI-assisted logic generates incident summaries and recommended actions (`ai_summary.py`)
5. Final structured incident reports are saved as JSON for further analysis (`generate_reports.py`)

## Features

- Synthetic authentication log generation

- Detection of suspicious login patterns (e.g. repeated failures, unusual locations)

- Automated alert severity classification (Low / Medium / High)

- AI-assisted incident summarization using structured prompts (LLM-ready design)

- Structured output suitable for SOC workflows

## Tech Stack

- Language: Python

- Data Format: CSV, JSON

- AI: LLM-ready prompt design for summarization and explanation

- Environment: Local development

## Project Scope

This project focuses on one realistic SOC task:

- Alert triage and incident summarization

It intentionally avoids:

- Full SIEM implementation

- Malware detection

- Network packet inspection

- Custom ML model training

## Example Use Case

1. Authentication logs are ingested from a CSV file

2. The system detects multiple failed login attempts from a new IP address

3. An alert is automatically flagged as High Risk

4. AI generates a concise incident summary with recommended next steps

## What I Learned

- How SOC-style alert triage workflows operate in practice
- Designing explainable, rule-based security detection logic
- Integrating AI-assisted summaries into automated pipelines
- Building end-to-end automation from raw logs to incident reports