import subprocess, pty, sys

# Create new tty to handle ioctl errors in termios
master_fd, slave_fd = pty.openpty()

proc = subprocess.Popen([sys.executable, 'Test.py'], stdin=slave_fd)