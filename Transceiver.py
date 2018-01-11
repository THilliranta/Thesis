from BasePlatform import basePlatform
from Lorawan import LoraWan

import time

def main():
    wapice_test_line_hex = "576170696365204c505741207465737420656e7669726f6e6d656e74"
    tcp_dump_file_name = "Wapice.dat"
    transmit_settings = basePlatform()
    lpwa_interface = LoraWan()
    lpwa_interface.initInterface()
    lpwa_interface.start_gateway_logging()
    time.sleep(10)


    for i in range (0,3):
         time.sleep(transmit_settings.sendInterval)
         lpwa_interface.transmit(wapice_test_line_hex)
    time.sleep(10)
    lpwa_interface.stop_gateway_logging()

if __name__ == "__main__":
    main()