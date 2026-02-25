```text
 _____         _     _____               _      ____ _     ___ 
|_   _|_ _ ___| |__ |_   _| __ __ _  ___| | __ / ___| |   |_ _|
  | |/ _` / __| '_ \  | || '__/ _` |/ __| |/ /| |   | |    | | 
  | | (_| \__ \ | | | | || | | (_| | (__|   < | |___| |___ | | 
  |_|\__,_|___/_| |_| |_||_|  \__,_|\___|_|\_\ \____|_____|___|
```

# Task Tracker CLI

Un outil de gestion de taches en ligne de commande qui enregistre les taches dans un fichier JSON (`./data/tasks.json`).

Ce README se concentre sur la fonctionnalite `create_task` et son comportement dans le code actuel.

Langue : Francais (par defaut dans ce fichier)
Autre langue : Anglais dans `README.md`

## Resume rapide

La fonction `create_task` construit une nouvelle instance de `Task` a partir de la description fournie, assigne un `id` incremental, met le statut a `todo`, et enregistre un horodatage de creation.

## Comment ca marche

- Le point d'entree accepte une commande comme : `task-cli add "Votre description"`.
- Le CLI appelle `create_task(description)`.
- `create_task` lit les donnees dans `./data/tasks.json`, puis retourne un nouvel objet `Task` avec :
- `id = len(taches_existantes) + 1`
- `description = description d'entree`
- `status = todo`
- `createdAt = date/heure actuelle`
- La fonction `add_item` enregistre la nouvelle tache dans le JSON.

## Exemple

Entree :

```bash
task-cli add "Acheter du lait"
```

Sortie attendue :

```
Task added successfully (ID: 1)
```

## Notes

- L'ID est calcule a partir du nombre actuel de taches. Si vous supprimez des taches manuellement dans le fichier JSON, des IDs peuvent etre reutilises.
- Les horodatages sont enregistres comme des chaines issues de `datetime.now()`.

## Passer a l'anglais

Voir la version anglaise [ici](./README.md).
