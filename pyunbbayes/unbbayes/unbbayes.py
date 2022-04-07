from typing import List
from py4j.java_gateway import JavaGateway, is_instance_of

gateway = JavaGateway()
prs = gateway.jvm.unbbayes.prs
io = gateway.jvm.unbbayes.io

class Network:
    def __init__(self, jNet) -> None:
        self.net = jNet
        self.compiled = False

class Node:
    
    def __init__(self, name: str, parents: List[str], states: List[str], probs: List[float]):
        self.name = name
        self.parents = parents
        self.states = states
        self.probs = probs


class UnBBayes:

    def __init__(self):
        self._jvm = JavaGateway()
        self.prs = self._jvm.jvm.unbbayes.prs
        self.io = self._jvm.jvm.unbbayes.io


def createJavaNode( node: Node):
    newNode = prs.bn.ProbabilisticNode()

    newNode.setName(node.name)

    for state in node.states:
        newNode.appendState(state)

    aux_cpt = newNode.getProbabilityFunction()
    aux_cpt.addVariable(newNode)

    for i in range(len(node.probs)):
        aux_cpt.addValueAt(i, float(node.probs[i]))
    
    return newNode

def compileNetwork( network: Network):
    network.compiled = True

    net = network.net

    alg = prs.bn.JunctionTreeAlgorithm()
    alg.setNetwork(net)
    alg.run()

    network.net = net

    return network

def setEvidence( pyNet: Network, evidences):
    if not pyNet.compiled:
        network = compileNetwork(pyNet)
    else:
        network = pyNet

    net = network.net

    for evidence in evidences:
        findingNode = net.getNode(evidence[0])

        for stateIndex in range(findingNode.getStatesSize()):
            if findingNode.getStateAt(stateIndex) == evidence[1]:
                findingNode.addFinding(stateIndex)
                break
    
    return network


def propagateEvidence( pyNet: Network):
    if not pyNet.compiled:
        network = compileNetwork(pyNet)
    else:
        network = pyNet
    
    network.net.updateEvidences()

    return network

def createNetwork( name: str, nodeList: List[Node]):
    net = prs.bn.ProbabilisticNetwork(name)

    for node in nodeList:
        jNode = createJavaNode(node)

        net.addNode(jNode)
    
    for node in nodeList:
        for parent in node.parents:
            jParent = net.getNode(parent)
            jNode = net.getNode(node.name)
            net.addEdge(prs.Edge(jParent, jNode))

    return Network(net)

def createNetworkFromFile(path: str):
    file = gateway.jvm.java.io.File(path)
    net = io.NetIO().load(file)
    return Network(net)

def print_network(network: Network):
    net = network.net

    for node in net.getNodes():
        print(node.getName() + ": " + node.getDescription())

        if is_instance_of(gateway, node, prs.bn.TreeVariable):
            for i in range(node.getStatesSize()):
                print(node.getStateAt(i) + " : " + str(node.getMarginalAt(i)))
        
            print("----")

def addNode(network: Network, node: Node):
    net = network.net
    jNode = createJavaNode(node)

    for parent in node.parents:
        jParent = net.getNode(parent)
        jNode = net.getNode(node.name)
        net.addEdge(prs.Edge(jParent, jNode))

    network.net = net

    return network