# Practical 8B: Solve Tipping Problem Using Fuzzy Logic
# Source: SCT Shortest code with original output.docx

import numpy as np, skfuzzy as fuzz
from skfuzzy import control as c
print("This is Practical 8B")
q=c.Antecedent(np.arange(0,11,1),"quality")
s=c.Antecedent(np.arange(0,11,1),"service")
t=c.Consequent(np.arange(0,26,1),"tip")
q.automf(3); s.automf(3)
t["low"]=fuzz.trimf(t.universe,[0,0,13])
t["medium"]=fuzz.trimf(t.universe,[0,13,25])
t["high"]=fuzz.trimf(t.universe,[13,25,25])
q.view(); s.view(); t.view()
r=[c.Rule(q["poor"]|s["poor"],t["low"]),
   c.Rule(s["average"],t["medium"]),
   c.Rule(s["good"]|q["good"],t["high"])]
tip=c.ControlSystemSimulation(c.ControlSystem(r))
tip.input["quality"]=6.5
tip.input["service"]=9.8
tip.compute()
print("Calculated Tip:",tip.output["tip"])
t.view(sim=tip)
