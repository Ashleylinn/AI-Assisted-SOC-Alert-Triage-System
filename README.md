# AI-Assisted-SOC-Alert-Triage-System

## Overview

This project simulates a Security Operations Center (SOC) workflow by automating the triage of authentication logs. The system analyzes login events, identifies potentially suspicious activity using simple detection logic, and generates AI-assisted incident summaries to support security analysts in decision-making.

The goal of this project is to demonstrate practical AI automation in information security, focusing on systems thinking rather than advanced machine learning.

## Motivation

In real SOC environments, analysts must review large volumes of alerts and logs under time pressure. Many alerts are repetitive or low risk, making manual triage inefficient and error-prone.

This project explores how AI can assist—not replace—security analysts by:

- Reducing manual log review

- Automatically categorizing alert severity

- Generating clear, human-readable incident summaries

## System Architecture

## Features

- Synthetic authentication log generation

- Detection of suspicious login patterns (e.g. repeated failures, unusual locations)

-- Automated alert severity classification (Low / Medium / High)

- AI-generated incident summaries in natural language

- Structured output suitable for SOC workflows

## Tech Stack

- Language: Python

- Data Format: CSV, JSON

- AI: Large Language Model (for summarization and explanation)

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
