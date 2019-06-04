# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:06:24 2019

@author: Sandi Šegota
"""

"""
Fuzzy logic for determining the tip value
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#utjecaj
quality = ctrl.Antecedent(np.arange(0,11,1), 'quality')
service = ctrl.Antecedent(np.arange(0,11,1), 'service')
#izlaz
tip = ctrl.Consequent(np.arange(0,26,1), 'tip')

#binovi za podijelu - lose, dobro, odlicno
quality.automf(3)
service.automf(3)

#dodjeljujemo vrijednost raspona sirovih podataka za svaku od jezično zadanih skupina
#pogledati raspodjelu sa prekopljenim trokutima iz prezentacije ako je nejasno
tip['low'] = fuzz.trimf(tip.universe, [0,0,13])
tip['medium'] = fuzz.trimf(tip.universe, [0,13,25])
tip['high'] = fuzz.trimf(tip.universe, [13,25,25])

#pravila

rule1 = ctrl.Rule(quality['poor'] | service ['poor'], tip['low'])
rule2 = ctrl.Rule(service ['average'], tip['medium'])
rule3 = ctrl.Rule(quality['good'] | service ['good'], tip['high'])

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

#dobivanje izlaza - definiranje ulaza
tipping.input['quality'] = 10.0
tipping.input['service'] = 10.0
tipping.compute()

print(tipping.output['tip'])
tip.view(sim=tipping)