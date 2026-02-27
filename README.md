```text
 _____         _     _____               _      ____ _     ___ 
|_   _|_ _ ___| |__ |_   _| __ __ _  ___| | __ / ___| |   |_ _|
  | |/ _` / __| '_ \  | || '__/ _` |/ __| |/ /| |   | |    | | 
  | | (_| \__ \ | | | | || | | (_| | (__|   < | |___| |___ | | 
  |_|\__,_|___/_| |_| |_||_|  \__,_|\___|_|\_\ \____|_____|___|
```

# Task Tracker CLI

A command-line task management tool that stores tasks in a JSON file (`./data/tasks.json`).

This README documents the CLI features and highlights the `create_task` behavior.

Language: English (default)
Other language: French in `README-FR.md`

## 📌 Project Origin

This project is based on the **Task Tracker challenge** from [roadmap.sh](https://roadmap.sh).

You can find the original challenge here:  
https://roadmap.sh/projects/task-tracker

It is part of a series of hands-on projects designed to strengthen backend development fundamentals, including file handling, data persistence, and command-line interface design.

## Features

- Add a task: `task-cli add "Description"`
- Update a task description: `task-cli update <id> "New description"`
- Delete a task: `task-cli delete <id>`
- Mark in progress: `task-cli mark-in-progress <id>`
- Mark done: `task-cli mark-done <id>`
- List tasks: `task-cli list`
- List tasks by status: `task-cli list todo|in-progress|done`

## Example (add)

Input:

```bash
task-cli add "Buy milk"
```

Expected output:

```
Task added successfully (ID: 1)
```

## Example (list)

Input:

```bash
task-cli list
```

Expected output:

```
id  description       status      createdAt           updatedAt
--  ----------------  ----------  ------------------  ------------------
1   marketing         todo        25/02/2026 23:33    25/02/2026 23:34
2   web site          todo        25/02/2026 23:33    -
3   plugin cli        todo        25/02/2026 23:33    -
```

## Exemple (update)

Input:
```bash
task-cli update 1 "Acheter du lait et du pain"
```

Expected output:

```
id  description                 status      createdAt           updatedAt
--  --------------------------  ----------  ------------------  ------------------
1   Acheter du lait et du pain  todo        25/02/2026 23:33    25/02/2026 23:40
```

## Exemple (mark-in-progress)

Input:
```bash
task-cli mark-in-progress 1
```

Expected output:
```
id  description       status         createdAt           updatedAt
--  ----------------  -------------  ------------------  ------------------
1   Acheter du lait   in-progress    25/02/2026 23:33    25/02/2026 23:45
```

## Exemple (mark-done)

Input:
```bash
task-cli mark-done 1
```

Expected output:
```
id  description       status         createdAt           updatedAt
--  ----------------  -------------  ------------------  ------------------
1   Acheter du lait   done           25/02/2026 23:33    25/02/2026 23:45
```

## Exemple (list filtered: todo)

Input:
```bash
task-cli list todo
```

Expected output:
```
id  description       status      createdAt           updatedAt
--  ----------------  ----------  ------------------  ------------------
2   Préparer réunion  todo        25/02/2026 22:10    -
3   Faire sport       todo        25/02/2026 21:00    -
```

## Exemple (list filtered: in-progress)

Input:
```bash
task-cli list in-progress
```

Expected output:
```
id  description         status        createdAt           updatedAt
--  ------------------  ------------  ------------------  ------------------
4   Revoir présentation in-progress  25/02/2026 20:00    25/02/2026 22:00
```

## Exemple (list filtered: done)

Input:
```bash
task-cli list done
```

Expected output:
```
id  description       status      createdAt           updatedAt
--  ----------------  ----------  ------------------  ------------------
5   Envoyer email     done        24/02/2026 18:00    24/02/2026 19:00
```

## Exemple (delete)

Input:
```bash
task-cli delete 1
```

Expected output:
```
id  description                 status      createdAt           updatedAt
--  --------------------------  ----------  ------------------  ------------------
No Task Found
```

## Notes

- The ID is derived from the current number of tasks. If you delete tasks manually from the JSON file, future IDs may be reused.
- Timestamps are saved as strings from `datetime.now()`.
- Task lists are displayed in a simple CLI table with `id`, `description`, `status`, `createdAt`, and `updatedAt`.

## Switch to French

See the French version [here](./README-FR.md).
