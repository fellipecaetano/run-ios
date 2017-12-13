import subprocess

def list_devices():
    return subprocess.check_output('xcrun simctl list -j devices'.split())

def shutdown_all():
    return subprocess.call('xcrun simctl shutdown all'.split())

def boot(udid):
    return subprocess.call('xcrun simctl boot'.split() + [udid])

