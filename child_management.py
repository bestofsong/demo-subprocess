#!/usr/bin/env python
''' demo showing child process management '''
import signal
import atexit
import subprocess

_ALL_SIGNALS = [signal.SIGCHLD, signal.SIGINT, signal.SIGTERM]

signal.pthread_sigmask(signal.SIG_BLOCK, _ALL_SIGNALS)
def on_signal(_signo, _):
    '''  使用空函数避免SIGCHLD被丢弃或忽略 '''
signal.signal(signal.SIGCHLD, on_signal)

def on_exit():
    ''' clean before exit: terminate child processes '''
    if CHILDS is not None:
        for child in CHILDS:
            try:
                child.terminate()
            except Exception as err:
                print('Failed to terminate child: {}'.format(err))
atexit.register(on_exit)

def process_child():
    ''' 处理已结束的子进程'''
    for child in CHILDS:
        if child.returncode is not None:
            continue
        child.wait()
        print('Child proc({}) returncode: {}'.format(child.pid, child.returncode))

CHILDS = [
        subprocess.Popen('./child.sh child1 1', shell=True),
        subprocess.Popen('./child.sh child2 3', shell=True)
        ]
while True:
    try:
        SIG = signal.sigwait(_ALL_SIGNALS)
        if SIG in (signal.SIGINT, signal.SIGTERM):
            break
        else:
            process_child()
    except Exception as err:
        print('Err while sigwait: %s' % err)
