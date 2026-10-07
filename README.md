# GRC Risk Assessment Framework

Risk assessment and evaluation framework for enterprise Governance, Risk, and Compliance.

## Features

- Risk identification and categorization
- Probability and impact scoring
- Risk matrix visualization
- Mitigation tracking
- Kenya DPA compliance integration

## Risk Assessment Process

1. **Identify Risks** - List potential security threats
2. **Score Probability** - Likelihood of occurrence (1-5)
3. **Score Impact** - Severity if it occurs (1-5)
4. **Calculate Risk Score** - Probability × Impact
5. **Prioritize** - Focus on highest risks first
6. **Mitigate** - Implement controls

## Risk Categories

- Technical (vulnerabilities, system failures)
- Operational (process failures, human error)
- Compliance (regulatory, audit findings)
- Financial (loss, fraud)
- Reputational (brand damage, customer trust)

## Usage

```python
from risk_framework import RiskAssessment

risk = RiskAssessment(
    name="Data Breach",
    category="Technical",
    probability=3,  # Medium
    impact=5  # Critical
)

print(f"Risk Score: {risk.calculate_score()}")  # 15/25
print(f"Risk Level: {risk.risk_level()}")  # High
```

## Kenya Context

This framework aligns with:
- Kenya Data Protection Act (PDPA) requirements
- Central Bank of Kenya (CBK) guidelines
- Critical Information Infrastructure (CII) mandate
- ISO 27001/27002 standards

## Documentation

See `/docs` for detailed risk assessment methodology and examples.
