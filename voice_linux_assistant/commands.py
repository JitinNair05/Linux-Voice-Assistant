
import subprocess
import os

def run_command(command):
    if "cpu" in command or "memory" in command:
        subprocess.run(["lscpu"])
        subprocess.run(["free", "-h"])
        return "Displayed system information."

    elif "create file" in command:
        name = command.split("create file")[-1].strip()
        open(name, 'w').close()
        return f"File '{name}' created."

    elif "delete file" in command:
        name = command.split("delete file")[-1].strip()
        if os.path.exists(name):
            os.remove(name)
            return f"File '{name}' deleted."
        return "File not found."

    elif "create folder" in command:
        folder = command.split("create folder")[-1].strip()
        os.makedirs(folder, exist_ok=True)
        return f"Folder '{folder}' created."

    elif "delete folder" in command:
        folder = command.split("delete folder")[-1].strip()
        if os.path.exists(folder):
            os.rmdir(folder)
            return f"Folder '{folder}' deleted."
        return "Folder not found."

    elif "git clone" in command:
        url = command.split("git clone")[-1].strip()
        subprocess.run(["git", "clone", url])
        return f"Repository cloned: {url}"

    elif "git pull" in command:
        subprocess.run(["git", "pull"])
        return "Git pull complete."

    elif "install package" in command:
        package = command.split("install package")[-1].strip()
        subprocess.run(["pip", "install", "--user", package])
        return f"Installed package: {package}"

    elif "remove package" in command:
        package = command.split("remove package")[-1].strip()
        subprocess.run(["pip", "uninstall", package, "-y"])
        return f"Removed package: {package}"

    elif "exit" in command or "quit" in command:
        return "Exiting."

    return "Command not recognized."
