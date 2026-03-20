# TP Note - Test & Test unitaire

## Description

Ce depot contient le travail du TP note de tests unitaires. Le but est de tester de maniere
exhaustive le module `calculatrice.py` qui contient des fonctions utilitaires (operations
arithmetiques, manipulation de chaines, operations sur les listes).

## Structure du depot

```
.
├── calculatrice.py              # code source a tester
├── test_calculatrice.py         # suite de tests pytest
├── requirements.txt             # dependances
├── setup.cfg                    # config flake8
├── pyproject.toml               # config pytest / black / mypy
├── .github/
│   └── workflows/
│       └── ci.yml               # pipeline CI GitHub Actions
└── docs/
    ├── plan_de_test.md          # plan de test
    └── tracabilite.md           # table de tracabilite
```

## Lancer les tests en local

```bash
pip install -r requirements.txt
pytest -v
```

## Couverture

```bash
pytest --cov=calculatrice --cov-report=html -v
# ouvrir htmlcov/index.html dans un navigateur
```

## Analyse statique

```bash
flake8 calculatrice.py test_calculatrice.py
black --check --line-length 100 calculatrice.py test_calculatrice.py
mypy calculatrice.py --ignore-missing-imports
radon cc calculatrice.py -a
```

## Pipeline CI

Le pipeline GitHub Actions se lance automatiquement au push. Il execute :
1. les tests avec rapport de couverture
2. flake8 (linting)
3. black (formatage)
4. mypy (verification de types)
5. radon (complexite cyclomatique)

Le rapport de couverture HTML est telecharge comme artefact dans l'onglet Actions.
