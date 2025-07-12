
from listener import listen_command, speak, log
from commands import run_command

def main():
    print("🎧 Listening for one command...")
    cmd = listen_command()
    if cmd:
        result = run_command(cmd)
        print("🧠 " + result)
        speak(result)
        log("[Assistant] " + result)

if __name__ == "__main__":
    main()
