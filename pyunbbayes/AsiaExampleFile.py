import unbbayes.unbbayes as unb

net = unb.createNetworkFromFile("/media/fparadas/HD1/UnB/unbbayes-4.22.18-dist(1)/unbbayes-4.22.18/pyunbbayes/asia.net")

net = unb.compileNetwork(net)

unb.print_network(net)


print(" ****** Updating Beliefs ****** ")

net = unb.propagateEvidence(unb.setEvidence(net, [("D", "yes"), ("S", "no")]))

unb.print_network(net)