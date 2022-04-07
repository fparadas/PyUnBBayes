import unbbayes.unbbayes as unb

nodeList = [
    unb.Node(name="asia", parents=[], states=["yes", "no"], probs=[0.01, 0.99]),
    unb.Node(name="tub", parents=["asia"], states=["yes", "no"], probs=[0.05, 0.95, 0.01, 0.99]),
    unb.Node(name="smoke", parents=[], states=["yes", "no"], probs=[0.5,0.5]),
    unb.Node(name="lung", parents=["smoke"], states=["yes", "no"], probs=[0.1, 0.9, 0.01, 0.99]),
    unb.Node(name="bronc", parents=["smoke"], states=["yes", "no"], probs=[0.6, 0.4, 0.3, 0.7]),
    unb.Node(name="either", parents=["lung", "tub"], states=["yes", "no"], probs=[1,0,1,0,1,0,0,1]),
    unb.Node(name="xray", parents=["either"], states=["yes", "no"], probs=[0.98, 0.02, 0.05, 0.95]),
    unb.Node(name="dysp", parents=["bronc", "either"], states=["yes", "no"], probs=[0.9, 0.1, 0.7, 0.3, 0.8, 0.2, 0.1, 0.9]),
]

net = unb.createNetwork("Asia.net", nodeList)

net = unb.compileNetwork(net)

unb.print_network(net)

net = unb.propagateEvidence(unb.setEvidence(net, [("dysp", "yes"), ("smoke", "no")]))

print(" ****** Updating Beliefs ****** ")
unb.print_network(net)