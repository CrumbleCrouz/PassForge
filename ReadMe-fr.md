# Documentation de PassForge
Dans un premier temps, télécharger les modules présents dans le fichier [requirements.txt](requirements.txt) avec la commande `pip install -r requirements.txt`

## Utilisation du CLI :
Ouvrez le fichier [main.py](main.py).

### - Navigation:

- ⬆️ Naviguer vers le bas
- ⬇️ Naviguer vers le haut
- ⬅️ Décrémenter de 1, changer vers la gauche
- ➡️ Incrémenter de 1, changer vers la droite

---

## Utilisation par console python :

### Génération avec les paramètres par défauts
Ouvrez un terminal python là ou vous avez téléchargé le programme, et importez [core.py](core.py).
Créer une instance de la classe Password avec la taille du mot de passe souhaité dans une variable comme ci:
```python
import core

mot_de_passe = core.Password(10)
```
Le mot de passe est construit privilégiant les lettres, puis les chiffres, et en dernier les caractères spéciaux.
La génération du mot de passe, au-dessus de 3 caractères, contiendra en moyenne 60% de lettres, 20% de chiffres et 20% de caractères spéciaux.

Utilisez désormais la méthode `generate()` pour générer votre mot de passe. Vous pouvez utiliser la fonction `print()` pour l'afficher.

```python
import core

mot_de_passe = core.Password(10)
print(mot_de_passe.generate())
```
Vous avez généré votre mot de passe de 10 caractères !

### Génération avec les paramètres personnalisés :
Vous pouvez générer votre mot de passe comme vous le souhaiter en utilisants les paramètres ci dessous:

**n_numb** (int) : le nombre de chiffres

**n_alpha** (int) : le nombre de lettres 

**n_char** (int) : le nombre de lettres

**not_numb** (list[int]) : une liste contenant les chiffres qui ne seront pas présent dans le mot de passe généré

**not_alpha** (list[str]) : une liste contenant les lettres qui ne seront pas présentes dans le mot de passe généré

**not_char** (list[str]) : une liste contenant les caractères qui ne seront pas présent dans le mot de passe généré

**alpha_type** (str) : le types de lettres (majuscules, minuscules, ou les 2.)

#### ⚠️ le types de variable doit être respecté !

Vous pouvez donc générer votre mot de passe comme ci :
```python
import core

mot_de_passe = core.Password(n_numb=5, n_alpha=8, n_char=2, alpha_type="uppercase", not_numb=[6])
print(mot_de_passe.generate())
```
Dans le cas présent, le mot de passe aura 5 chiffres sans le 6, 8 lettres majuscules, et 2 caractères.
