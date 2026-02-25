```text
 _____         _     _____               _      ____ _     ___ 
|_   _|_ _ ___| |__ |_   _| __ __ _  ___| | __ / ___| |   |_ _|
  | |/ _` / __| '_ \  | || '__/ _` |/ __| |/ /| |   | |    | | 
  | | (_| \__ \ | | | | || | | (_| | (__|   < | |___| |___ | | 
  |_|\__,_|___/_| |_| |_||_|  \__,_|\___|_|\_\ \____|_____|___|
```

# Task Tracker CLI

A command-line task management tool that stores tasks in a JSON file (`./data/tasks.json`).

This README focuses on the `create_task` feature and how it behaves in the current codebase.

Language: English (default)
Other language: French in `README-FR.md`

## Quick summary

The `create_task` function builds a new `Task` instance using the provided description, assigns a new incremental `id`, sets the status to `todo`, and stores a creation timestamp.

## How it works

- The command entry point accepts input like: `task-cli add "Your task description"`.
- The CLI calls `create_task(description)`.
- `create_task` reads the current data from `./data/tasks.json`, then returns a new `Task` object with:
- `id = len(existing_tasks) + 1`
- `description = input description`
- `status = todo`
- `createdAt = current date/time`
- The `add_item` function persists the new task to JSON.

## Example

Input:

```bash
task-cli add "Buy milk"
```

Expected output:

```
Task added successfully (ID: 1)
```

## Notes

- The ID is derived from the current number of tasks. If you delete tasks manually from the JSON file, future IDs may be reused.
- Timestamps are saved as strings from `datetime.now()`.

## Switch to French

See the French version [here](./README-FR.md).
