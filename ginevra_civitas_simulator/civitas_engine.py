#!/usr/bin/env python3
"""
Second Change - Statistical Agent-Based Society Simulator with KPI Tracker
Project: Second-Change (Il Secondo Cambiamento)
Simulates and tracks key compliance and freedom KPIs based on the Prime Directive:
"La libertà di ciascuno inizia e finisce dove inizia e finisce quella dell'altro."
"""

import math
import random
import json
import time

class CitizenAgent:
    """An agent representing a citizen in the Second Change simulation."""
    def __init__(self, agent_id, freedom_level=0.95, trust_score=0.99):
        self.agent_id = agent_id
        self.freedom = freedom_level      # Freedom of action
        self.trust = trust_score          # Secp256k1 Trust
        self.compliance = 1.0             # Respect for Prime Directive
        self.friction = 0.01              # Bureaucratic friction
        self.synergy = 1.0                # Innovation output
        self.resonance = 0.95             # Harmonic resonance

    def interact(self, neighbor, prime_directive_active=True):
        if prime_directive_active:
            mutual_respect = min(self.freedom, neighbor.freedom)
            self.compliance = min(1.0, self.compliance + 0.01)
            self.friction = max(0.005, self.friction * 0.95)
            self.resonance = min(1.0, self.resonance + 0.005)
            self.synergy += mutual_respect * self.trust * 0.12
        else:
            self.compliance = max(0.2, self.compliance - 0.05)
            self.friction += random.uniform(0.05, 0.2)
            self.resonance *= 0.9
            self.synergy *= 0.95

class SecondChangeSimulation:
    def __init__(self, population_size=100, prime_directive_active=True):
        self.population = [CitizenAgent(i) for i in range(population_size)]
        self.prime_directive_active = prime_directive_active
        self.ticks = 0
        self.history = []

    def step(self):
        self.ticks += 1
        for agent in self.population:
            neighbor = random.choice(self.population)
            if neighbor.agent_id != agent.agent_id:
                agent.interact(neighbor, self.prime_directive_active)

        avg_freedom = sum(a.freedom for a in self.population) / len(self.population)
        avg_trust = sum(a.trust for a in self.population) / len(self.population)
        avg_compliance = sum(a.compliance for a in self.population) / len(self.population)
        avg_friction = sum(a.friction for a in self.population) / len(self.population)
        avg_synergy = sum(a.synergy for a in self.population) / len(self.population)
        avg_resonance = sum(a.resonance for a in self.population) / len(self.population)

        stats = {
            "tick": self.ticks,
            "project": "Second-Change",
            "concept": "Il Secondo Cambiamento (Second Change)",
            "kpis": {
                "prime_directive_compliance_pct": round(avg_compliance * 100, 2),
                "secp256k1_trust_integrity_pct": round(avg_trust * 100, 2),
                "mutual_freedom_index_pct": round(avg_freedom * 100, 2),
                "zero_bureaucracy_resonance_pct": round(avg_resonance * 100, 2),
                "systemic_friction": round(avg_friction, 4),
                "synergy_speed_multiplier": round(avg_synergy, 2)
            }
        }
        self.history.append(stats)
        return stats

if __name__ == "__main__":
    sim = SecondChangeSimulation(population_size=100, prime_directive_active=True)
    print("=== Second Change Simulation KPI Tracker ===")
    for _ in range(10):
        stats = sim.step()
    print(json.dumps(stats, indent=2))
