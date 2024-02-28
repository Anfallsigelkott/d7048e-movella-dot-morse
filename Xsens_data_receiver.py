import xdpchandler
import movelladot_pc_sdk
from sig2bin import Databank
import sys

from pynput import keyboard


class Xsens_data_receiver:

    def __init__(self):
        # TODO: make variables private
        self.xdpcHandler = xdpchandler.XdpcHandler()
        self.device = None
        self.db = None

        # initialize
        if not self.xdpcHandler.initialize():
            print("No Movella DOT device(s) found. Aborting.")
            # TODO: specific error
            self.xdpcHandler.cleanup()
            raise Exception('Aborted')
        
        self.xdpcHandler.scanForDots()
        if len(self.xdpcHandler.detectedDots()) == 0:
            print("Could not connect to any Movella DOT device(s). Aborting.")
            self.xdpcHandler.cleanup()
            raise Exception('Aborted')

        self.xdpcHandler.connectDots()
        self.device = self.xdpcHandler.connectedDots()
        if len(self.device) >= 1:
            self.device = self.device[0]
        else:
            raise Exception('No device found')
        
        print(f"Current profile: {self.device.onboardFilterProfile().label()}")
        if self.device.onboardFilterProfile().label() != 'Dynamic':
            if not self.device.setOnboardFilterProfile("Dynamic"):
                print("Setting filter profile failed!")
            
    def run(self, db:Databank, log_file:bool=True):
        self.db = db
        if log_file:
            self.device.setLogOptions(movelladot_pc_sdk.XsLogOptions_Euler)
            logFileName = "logfile_" + self.device.bluetoothAddress().replace(':', '-') + ".csv"
            if not self.device.enableLogging(logFileName):
                print(f"Failed to enable logging. Reason: {self.device.lastResultText()}")

        # enable measurement mode
        if not self.device.startMeasurement(movelladot_pc_sdk.XsPayloadMode_OrientationEuler):
            print(f"Could not put device into measurement mode. Reason: {self.device.lastResultText()}")
            raise Exception('Aborting')
        
        # start measuring
        self.run = True
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

        print("\nRunning (q=quit) (r=clear)")
        while self.run:
            if self.xdpcHandler.packetsAvailable():
                # Retrieve a packet
                packet = self.xdpcHandler.getNextPacket(self.device.portInfo().bluetoothAddress())

                if packet.containsOrientation():
                    euler = packet.orientationEuler()
                    db.sigToBin(euler.y())
        
        # disabling measurement
        if not self.device.stopMeasurement():
            print("Failed to stop measurement.")
        if log_file and not self.device.disableLogging():
            print("Failed to disable logging.")


                
    def reset_orientation(self) -> bool:
        """
        Resets the orientation of the device. 

        :return: True if reset was successful, otherwise false
        """
        return self.device.resetOrientation(movelladot_pc_sdk.XRM_Heading)


    def on_press(self, key) -> None:
        try:
            k = key.char
        except:
            k = key.name
        if key == keyboard.Key.esc or k == 'q':
            self.run = False
        if k == 'r':
            self.db.reset_string()


    def __del__(self):
        self.xdpcHandler.cleanup()
        self.device = None


if __name__ == '__main__':
    args = sys.argv
    if len(args) >= 2:
        db = Databank(int(args[1]))
    else:
        db = Databank()

    obj = Xsens_data_receiver()

    obj.reset_orientation()
    obj.run(db)