#!/usr/bin/env python3

import arguments
import devices
import simctl
import react_native

if __name__ == '__main__':
    args = arguments.parse()
    device = devices.find_by_spec(devices.DeviceSpec(args.simulator, os='iOS'))

    if device:
        simctl.shutdown_all()
        simctl.boot(udid=device.udid)
        react_native.run_ios()
    else:
        print('Device %s not found' % device_spec)

