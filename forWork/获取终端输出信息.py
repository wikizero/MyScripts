import subprocess

command = 'ls /home'


def sh(command, print_msg=True):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    lines = []
    for line in iter(p.stdout.readline, b''):
        line = line.rstrip().decode('utf8')
        if print_msg:
            print(">>>", line)
        lines.append(line)
    return lines
