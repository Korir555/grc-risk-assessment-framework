"""
Risk Assessment Framework

GRC risk identification, assessment, and tracking system.
Aligned with Kenya DPA and CBK requirements.
"""

from enum import Enum
from dataclasses import dataclass
from datetime import datetime
import json


class RiskCategory(Enum):
    TECHNICAL = "Technical"
    OPERATIONAL = "Operational"
    COMPLIANCE = "Compliance"
    FINANCIAL = "Financial"
    REPUTATIONAL = "Reputational"


class RiskLevel(Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    NEGLIGIBLE = "Negligible"


@dataclass
class Risk:
    """Risk assessment object"""
    
    id: str
    name: str
    description: str
    category: RiskCategory
    probability: int  # 1-5
    impact: int  # 1-5
    owner: str
    created_date: datetime
    mitigation_strategy: str = None
    status: str = "Open"  # Open, In Progress, Mitigated, Accepted
    
    def calculate_score(self) -> int:
        """Calculate risk score (probability × impact)"""
        return self.probability * self.impact
    
    def get_risk_level(self) -> RiskLevel:
        """Determine risk level from score"""
        score = self.calculate_score()
        if score >= 20:
            return RiskLevel.CRITICAL
        elif score >= 12:
            return RiskLevel.HIGH
        elif score >= 6:
            return RiskLevel.MEDIUM
        elif score >= 2:
            return RiskLevel.LOW
        else:
            return RiskLevel.NEGLIGIBLE
    
    def to_dict(self):
        """Convert to dictionary for storage"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "category": self.category.value,
            "probability": self.probability,
            "impact": self.impact,
            "score": self.calculate_score(),
            "level": self.get_risk_level().value,
            "owner": self.owner,
            "created_date": self.created_date.isoformat(),
            "mitigation_strategy": self.mitigation_strategy,
            "status": self.status
        }


class RiskRegister:
    """Register and track risks"""
    
    def __init__(self):
        self.risks = []
    
    def add_risk(self, risk: Risk):
        """Add risk to register"""
        self.risks.append(risk)
        return risk.id
    
    def get_risks_by_level(self, level: RiskLevel):
        """Get all risks at specific level"""
        return [r for r in self.risks if r.get_risk_level() == level]
    
    def get_critical_risks(self):
        """Get all critical risks"""
        return self.get_risks_by_level(RiskLevel.CRITICAL)
    
    def get_risks_by_category(self, category: RiskCategory):
        """Get risks by category"""
        return [r for r in self.risks if r.category == category]
    
    def export_to_json(self, filename="risk_register.json"):
        """Export risk register to JSON"""
        data = [r.to_dict() for r in self.risks]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def get_summary(self):
        """Get risk summary statistics"""
        return {
            "total_risks": len(self.risks),
            "critical": len(self.get_critical_risks()),
            "high": len(self.get_risks_by_level(RiskLevel.HIGH)),
            "medium": len(self.get_risks_by_level(RiskLevel.MEDIUM)),
            "low": len(self.get_risks_by_level(RiskLevel.LOW))
        }


# Example usage
if __name__ == "__main__":
    register = RiskRegister()
    
    # Add sample risks
    risk1 = Risk(
        id="RISK-001",
        name="Data Breach",
        description="Unauthorized access to customer data",
        category=RiskCategory.TECHNICAL,
        probability=3,
        impact=5,
        owner="Security Team",
        created_date=datetime.now(),
        mitigation_strategy="Implement encryption, access controls"
    )
    
    risk2 = Risk(
        id="RISK-002",
        name="Non-compliance with DPA",
        description="Failure to meet Kenya DPA requirements",
        category=RiskCategory.COMPLIANCE,
        probability=2,
        impact=4,
        owner="Compliance Officer",
        created_date=datetime.now(),
        mitigation_strategy="Audit compliance, update policies"
    )
    
    register.add_risk(risk1)
    register.add_risk(risk2)
    
    print("Risk Register Summary:")
    print(register.get_summary())
    
    print("\nCritical Risks:")
    for risk in register.get_critical_risks():
        print(f"  - {risk.name} (Score: {risk.calculate_score()}/25)")
