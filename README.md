<h1 align="center"><i><b> ~ Feu de circulation intelligent ~ </i></b></h1>

## Plan du feu de circulation intelligent
  >Remerciement à **Sacha Blanc-Richard** pour le modèle et l'impression du feu de circulation.

<img src="feuIntel_plan.png" alt="feuIntelPlan" width="900">

## Impression 3D du feu de circulation
<img src="feuIntel_3d.jpeg" alt="feuIntel3D" width="900">

## Modélisation
<img src="modelisation.png" alt="model" width="900">

## Installation:
Pour installer le code clonez le dépôt, lancez le processus pigpiod.
```
git clone https://github.com/MaximeGazze/feu-intel.git 
cd feu-intel
sudo pigpiod
```

>Vous pouvez optionnellement exécuter pigpiod après chaque démarrage avec
`sudo systemctl enable pigpiod`

Puis vous pouvez exécuter le code avec:
```
python3 main.py
```
