
from resonator_tools import circuit


port1 = circuit.reflection_port()
# port1.add_fromtxt('S11.txt','dBmagphasedeg',1)
port1.myadd_froms2p(r'data\trap_test\vna-sweep_30mm2025-07-28-09224.csv','S11',fdata_unit=1.0)
port1.GUIfit()
print("Fit results:", port1.fitresults)
port1.plotall()
print("single photon limit:", port1.get_single_photon_limit(), "dBm")
print("done")
