#!/usr/bin/env python3
"""
Second Chance - Statistical Agent-Based Society Simulator
Project: Second-Chance (Second Chance Ecosystem)
Based on the Prime Directive: "La libertà di ciascuno inizia e finisce dove inizia e finisce quella dell'altro."
"""

import math
import random
import json
import time

class CitizenAgent:
    """An agent representing a citizen in the Second Chance simulation."""
    def __init__(self, agent_id, freedom_level=0.9, trust_score=0.95):
        self.agent_id = agent_id
        self.freedom = freedom_level      # 0.0 to 1.0 (Freedom of action)
        self.trust = trust_score          # 0.0 to 1.0 (Secp256k1 Cryptographic Trust)
        self.friction = 0.05              # Bureaucratic friction
        self.synergy = 1.0                # Innovation & collaboration output
        self.stress = 0.1                 # Anxiety / Stress level

    def interact(self, neighbor, prime_directive_active=True):
        """Simulate interaction between two agents under Second Chance Prime Directive."""
        if prime_directive_active:
            mutual_respect = min(self.freedom, neighbor.freedom)
            self.friction = max(0.01, self.friction * 0.9)
            self.stress = max(0.05, self.stress * 0.85)
            self.synergy += mutual_respect * self.trust * 0.1
        else:
            self.friction += random.uniform(0.05, 0.2)
            self.stress += random.uniform(0.1, 0.3)
            self.synergy *= 0.95

class SecondChanceSimulation:
    """Second Chance agent-based statistical society simulator."""
    def __init__(self, population_size=100, prime_directive_active=True):
        self.population = [CitizenAgent(i) for i in range(population_size)]
        self.prime_directive_active = prime_directive_active
        self.ticks = 0
        self.history = []

    def step(self):
        """Run 1 simulation tick."""
        self.ticks += 1
        for agent in self.population:
            neighbor = random.choice(self.population)
            if neighbor.agent_id != agent.agent_id:
                agent.interact(neighbor, self.prime_directive_active)

        avg_freedom = sum(a.freedom for a in self.population) / len(self.population)
        avg_trust = sum(a.trust for a in self.population) / len(self.population)
        avg_friction = sum(a.friction for a in self.population) / len(self.population)
        avg_synergy = sum(a.synergy for a in self.population) / len(self.population)
        avg_stress = sum(a.stress for a in self.population) / len(self.population)

        stats = {
            "tick": self.ticks,
            "project": "Second-Chance",
            "mode": "Second Chance Freedom Society" if self.prime_directive_active else "Traditional Bureaucracy",
            "avg_freedom_pct": round(avg_freedom * 100, 2),
            "avg_trust_pct": round(avg_trust * 100, 2),
            "avg_friction": round(avg_friction, 4),
            "avg_synergy": round(avg_synergy, 2),
            "avg_stress_pct": round(avg_stress * 100, 2)
        }
        self.history.append(stats)
        return stats

if __name__ == "__main__":
    sim = SecondChanceSimulation(population_size=100, prime_directive_active=True)
    print("=== Second Chance Simulation Engine (Prime Directive Active) ===")
    for _ in range(10):
        stats = sim.step()
    print(json.dumps(stats, indent=2))
