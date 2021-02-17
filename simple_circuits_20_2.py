import pennylane as qml

dev = qml.device("default.qubit", wires=2)
@qml.qnode(dev)
def simple_circuits_20(angle):
    qml.RX(angle, wires=0)
    return qml.probs(wires=[0])
    
# Load and process input
    angle_str = sys.stdin.read()
    angle = float(angle_str)

output = simple_circuits_20(angle)
print(output[0])
