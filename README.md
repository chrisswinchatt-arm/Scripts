# Scripts

Helpful scripts

* `hci.py` - decode HCI packets in 0A:1B:2C... format into human-readable strings (WIP - describes most BLE CMD/EVT packets but doesn't decode params)
* `hci-mbed.py` - mbed OS adapter for `hci.py` (use like `./hci-mbed.py <mbed-raw.log | ./hci.py >mbed-cooked.log`)
* `mount-boards.sh` - functions and variables that help with mounting boards (currently just NRF52) - source with '.' instead of executing
