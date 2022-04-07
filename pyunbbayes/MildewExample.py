import unbbayes.unbbayes as unb

net = unb.createNetworkFromFile("/media/fparadas/HD1/UnB/unbbayes-4.22.18-dist(1)/unbbayes-4.22.18/pyunbbayes/mildew3-2.net")

net = unb.compileNetwork(net)

unb.print_network(net)


print(" ****** Updating Beliefs ****** ")
