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

## 📌 Origine du Projet

Ce projet est basé sur le challenge **Task Tracker** proposé par [roadmap.sh](https://roadmap.sh).

Le challenge original est disponible ici :  
https://roadmap.sh/projects/task-tracker

Il fait partie d'une série de projets pratiques conçus pour renforcer les fondamentaux du développement backend, notamment la manipulation de fichiers, la persistance des données et la conception d'interfaces en ligne de commande.

## Fonctionnalites

- Ajouter une tache : `task-cli add "Description"`
- Mettre a jour une description : `task-cli update <id> "Nouvelle description"`
- Supprimer une tache : `task-cli delete <id>`
- Marquer en cours : `task-cli mark-in-progress <id>`
- Marquer terminee : `task-cli mark-done <id>`
- Lister les taches : `task-cli list`
- Lister par statut : `task-cli list todo|in-progress|done`

## Exemple (add)

Entrée :

```bash
task-cli add "Acheter du lait"
```

Sortie attendue :

```
Task added successfully (ID: 1)

id  description       status      createdAt           updatedAt
--  ----------------  ----------  ------------------  ------------------
1   Acheter du lait         todo  25/02/2026 23:33    -
```

## Exemple (list)

Entrée:
```bash
task-cli list
```

Sortie attendue:

```
id  description       status      createdAt           updatedAt
--  ----------------  ----------  ------------------  ------------------
1   Acheter du lait   todo        25/02/2026 23:33    -
```

## Exemple (update)

Entrée:
```bash
task-cli update 1 "Acheter du lait et du pain"
```

Sortie attendue:

```
id  description                 status      createdAt           updatedAt
--  --------------------------  ----------  ------------------  ------------------
1   Acheter du lait et du pain  todo        25/02/2026 23:33    25/02/2026 23:40
```

## Exemple (mark-in-progress)

Entrée:
```bash
task-cli mark-in-progress 1
```

Sortie attendue:
```
id  description       status         createdAt           updatedAt
--  ----------------  -------------  ------------------  ------------------
1   Acheter du lait   in-progress    25/02/2026 23:33    25/02/2026 23:45
```

## Exemple (mark-done)

Entrée:
```bash
task-cli mark-done 1
```

Sortie attendue:
```
id  description       status         createdAt           updatedAt
--  ----------------  -------------  ------------------  ------------------
1   Acheter du lait   done           25/02/2026 23:33    25/02/2026 23:45
```

## Exemple (list filtered: todo)

Entrée:
```bash
task-cli list todo
```

Sortie attendue:
```
id  description       status      createdAt           updatedAt
--  ----------------  ----------  ------------------  ------------------
2   Préparer réunion  todo        25/02/2026 22:10    -
3   Faire sport       todo        25/02/2026 21:00    -
```

## Exemple (list filtered: in-progress)

Entrée:
```bash
task-cli list in-progress
```

Sortie attendue:
```
id  description         status        createdAt           updatedAt
--  ------------------  ------------  ------------------  ------------------
4   Revoir présentation in-progress  25/02/2026 20:00    25/02/2026 22:00
```

## Exemple (list filtered: done)

Entrée:
```bash
task-cli list done
```

Sortie attendue:
```
id  description       status      createdAt           updatedAt
--  ----------------  ----------  ------------------  ------------------
5   Envoyer email     done        24/02/2026 18:00    24/02/2026 19:00
```

## Exemple (delete)

Entrée:
```bash
task-cli delete 1
```

Sortie attendue:
```
id  description                 status      createdAt           updatedAt
--  --------------------------  ----------  ------------------  ------------------
No Task Found
```

## Notes

- L'ID est calcule a partir du nombre actuel de taches. Si vous supprimez des taches manuellement dans le fichier JSON, des IDs peuvent etre reutilises.
- Les horodatages sont enregistres comme des chaines issues de `datetime.now()`.
- Les listes sont affichees dans un tableau CLI avec `id`, `description`, `status`, `createdAt`, et `updatedAt`.

## Passer a l'anglais

Voir la version anglaise [ici](./README.md).
