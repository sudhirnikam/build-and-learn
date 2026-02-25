# Claude Code CLI Commands

## Commands

| Command | Description |
|---------|-------------|
| `/config` | Browse through existing settings and update them |
| `/model` | Let you choose AI model which you want to use |
| `/clear` | Clears the current session and context window |
| `/context` | Context usage details, token details |
| `/usage` | Status of current usage, if usage is not available you can pay extra, and get more usage |
| `/compact` | Claude will compact previous conversations and store just summary. Some information loss may happen. |
| `/resume` | This will allow to open older sessions |
| `/rewind` | Go back to the specific step, it will undo file changes |
| `/sandbox` | Create sandbox environment without using docker |
| `claude <some question>` | Claude session can be started by asking question |
| `claude -p <some question>` | Runs commands in background |
| `claude --dangerously-skip-permissions` | Skips all permission requests |
| `docker sandbox run claude` | Runs all commands in sandbox env, which reduces risk of affecting local machine |
| `Escape` (twice) | Revert the changes made by claude in the current session |
| `/init` | Analyze the code base to understand it properly |
| `/plan` | Enable plan mode |

## Configuration

You can add a `.claude` directory at project level and add a `settings.json` file in it. It can be used to override global settings mentioned in `~/.claude/settings.json`.

You can also add a `settings.local.json` file for individual's local environment setup. This file will not be committed to repo, it will override settings from `~/.claude/settings.json` and `settings.json` present in repo.

While writing prompts, if you are passing very large text to prompt, write it inside html tags. E.g. while passing error message you can write
<error>
long error message text
</error>

## CLAUDE.md
This file can be created at the root of the project and also at each directory level. Purpose of this file is to store long term memory about the project. 
It is used to store instructions while working with claude. 
CLAUDE.md file create at subdirectory level, is application for that directory.

## Plan Mode
In this mode claude code will gather relevant information before starting working on the task.
It will ask relevant question about the task is clarifications are needed.
It helps to turn your average prompt into good prompts.
In this mode, claude will not change files in your project, it will just explore existing files, and create a plan on how to tackle the task.
It stores the itermediate output in .md files, which can be seen in the output.
