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

## create_task summary

The `create_task` function builds a new `Task` instance using the provided description, assigns a new incremental `id`, sets the status to `todo`, and stores a creation timestamp.

## How it works (create_task)

- The command entry point accepts input like: `task-cli add "Your task description"`.
- The CLI calls `create_task(description)`.
- `create_task` reads the current data from `./data/tasks.json`, then returns a new `Task` object with:
- `id = len(existing_tasks) + 1`
- `description = input description`
- `status = todo`
- `createdAt = current date/time`
- The `add_item` function persists the new task to JSON.

## Example (create_task)

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

## Notes

- The ID is derived from the current number of tasks. If you delete tasks manually from the JSON file, future IDs may be reused.
- Timestamps are saved as strings from `datetime.now()`.
- Task lists are displayed in a simple CLI table with `id`, `description`, `status`, `createdAt`, and `updatedAt`.

## Switch to French

See the French version [here](./README-FR.md).
