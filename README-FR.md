```text
 _____         _     _____               _      ____ _     ___ 
|_   _|_ _ ___| |__ |_   _| __ __ _  ___| | __ / ___| |   |_ _|
  | |/ _` / __| '_ \  | || '__/ _` |/ __| |/ /| |   | |    | | 
  | | (_| \__ \ | | | | || | | (_| | (__|   < | |___| |___ | | 
  |_|\__,_|___/_| |_| |_||_|  \__,_|\___|_|\_\ \____|_____|___|
```

# Task Tracker CLI

Un outil de gestion de taches en ligne de commande qui enregistre les taches dans un fichier JSON (`./data/tasks.json`).

Ce README documente les fonctionnalites du CLI et met en avant le comportement de `create_task`.

Langue : Francais (par defaut dans ce fichier)
Autre langue : Anglais dans `README.md`

## Fonctionnalites

- Ajouter une tache : `task-cli add "Description"`
- Mettre a jour une description : `task-cli update <id> "Nouvelle description"`
- Supprimer une tache : `task-cli delete <id>`
- Marquer en cours : `task-cli mark-in-progress <id>`
- Marquer terminee : `task-cli mark-done <id>`
- Lister les taches : `task-cli list`
- Lister par statut : `task-cli list todo|in-progress|done`

## Resume create_task

La fonction `create_task` construit une nouvelle instance de `Task` a partir de la description fournie, assigne un `id` incremental, met le statut a `todo`, et enregistre un horodatage de creation.

## Comment ca marche (create_task)

- Le point d'entree accepte une commande comme : `task-cli add "Votre description"`.
- Le CLI appelle `create_task(description)`.
- `create_task` lit les donnees dans `./data/tasks.json`, puis retourne un nouvel objet `Task` avec :
- `id = len(taches_existantes) + 1`
- `description = description d'entree`
- `status = todo`
- `createdAt = date/heure actuelle`
- La fonction `add_item` enregistre la nouvelle tache dans le JSON.

## Exemple (create_task)

Entree :

```bash
task-cli add "Acheter du lait"
```

Sortie attendue :

```
Task added successfully (ID: 1)
```

## Exemple (list)

Entree:
```bash
task-cli list
```

Sortie attendue:

```
id  description       status      createdAt           updatedAt
--  ----------------  ----------  ------------------  ------------------
1   marketing         todo        25/02/2026 23:33    25/02/2026 23:34
2   web site          todo        25/02/2026 23:33    -
3   plugin cli        todo        25/02/2026 23:33    -
```

## Notes

- L'ID est calcule a partir du nombre actuel de taches. Si vous supprimez des taches manuellement dans le fichier JSON, des IDs peuvent etre reutilises.
- Les horodatages sont enregistres comme des chaines issues de `datetime.now()`.
- Les listes sont affichees dans un tableau CLI avec `id`, `description`, `status`, `createdAt`, et `updatedAt`.

## Passer a l'anglais

Voir la version anglaise [ici](./README.md).
