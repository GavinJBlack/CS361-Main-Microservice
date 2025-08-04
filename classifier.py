# classifier.py

def classify_command(command: str) -> str:
    command = command.strip().lower()

    known_commands = {
        "git": "git",
        "docker": "docker",
        "kubectl": "kubectl",
        "npm": "npm",
        "npx": "npm",
        "yarn": "yarn",
        "python": "python",
        "pip": "python",
        "java": "java",
        "javac": "java",
        "node": "node",
        "bash": "bash",
        "zsh": "zsh",
        "sh": "bash",
        "ssh": "ssh",
        "scp": "ssh",
        "curl": "http",
        "wget": "http",
        "make": "build",
        "cmake": "build",
        "gradle": "build",
        "mvn": "build",
        "ls": "filesystem",
        "cd": "filesystem",
        "rm": "filesystem",
        "mkdir": "filesystem",
        "cp": "filesystem",
        "mv": "filesystem",
        "cat": "filesystem",
        "touch": "filesystem",
        "top": "system",
        "htop": "system",
        "ps": "system",
        "kill": "system",
        "man": "help",
        "help": "help",
        "exit": "shell",
        "clear": "shell"
    }

    for prefix, tool in known_commands.items():
        if command.startswith(prefix + " "):
            return tool

    return "unknown"
