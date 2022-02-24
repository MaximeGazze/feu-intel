<h1 align="center"> <i><b> ~ Feu de circulation intelligent ~ </i></b></h1>
# Plan de la lumière intelligent
  >Rermerciment à **Sacha Blanc-Richard** pour le modèle et l'impression du feu de circulation.

<img src="feuIntel_plan.png" alt="feuIntelPlan" width="900">

# Impression 3D du feu
<img src="feuIntel_3d.jpeg" alt="feuIntel3D" width="900">

# Modélisation
<img src="modelisation.png" alt="model" width="900">

Installation:
```
git clone https://github.com/MaximeGazze/feu-intel.git && cd feu-intel
```

Lancer (si le service ne roule pas déjà):
```
sudo pigpiod
```

>Vous pouvez optionnellement exécuter le code après chaque démarrage avec:
```
sudo systemctl enable pigpiod
```

Puis vous pouvez exécutant le code avec:
```
python3 main.py
```
