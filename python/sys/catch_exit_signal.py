"""
Example of catching the interrupt signals
Author: Hao Chen (chen960216@gmail.com)
Created: 20230622osaka

Note:
SIGINT (signal interrupt) is sent when the user types the interrupt character (usually Ctrl-C) in the terminal. It is intended to gracefully terminate a process.
SIGTERM (signal terminate) is sent to request that a process terminate. It is intended to allow a process to perform cleanup operations before exiting.

Reference:
[Implementation of Signals under Linux and Windows?](https://stackoverflow.com/questions/12671741/implementation-of-signals-under-linux-and-windows)

"""
import sys
import signal


def handle_exit_signal():
    """Listen to exit signal like ctrl-c or kill from os and try to exit the process forcefully."""

    def shutdown(signal_code, frame):
        del frame
        print(
            f'Received signal {signal_code}: terminating process...',
        )
        sys.exit(signal_code)

        # # Listen to signals to exit process.

    if sys.platform.startswith('linux'):
        signal.signal(signal.SIGHUP, shutdown)
    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)


if __name__ == "__main__":
    while 1:
        handle_exit_signal()
