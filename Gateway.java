import java.io.File;

import py4j.GatewayServer;
import unbbayes.prs.Node;
import unbbayes.prs.Edge;
import unbbayes.prs.bn.*;
import unbbayes.io.*;

public class Gateway {
  
  public static void main(String[] args) throws Exception  {
    // ProbabilisticNetwork net = (ProbabilisticNetwork) new NetIO().load(
    //     new File("./examples/bn/net/asia.net")
    // );

    // ProbabilisticNode newNode = new ProbabilisticNode();

    // newNode.setName("K");
    // newNode.setDescription("A test node");
    // newNode.appendState("yes");
    // newNode.appendState("no");
    // PotentialTable auxCPT = newNode.getProbabilityFunction();
    // auxCPT.addVariable(newNode);
    // net.addNode(newNode);
    // ProbabilisticNode asiaNode = (ProbabilisticNode) net.getNodes().get(0);
    // Edge edg = new Edge(asiaNode, newNode);
    // net.addEdge(edg);

    // auxCPT.addValueAt (0 , 0.99f); auxCPT.addValueAt (1 , 0.01f);
    // auxCPT.addValueAt (2 , 0.1f); auxCPT.addValueAt (3 , 0.9f);
    // // / / prepare the algorithm to compile network
    // JunctionTreeAlgorithm alg = new JunctionTreeAlgorithm () ;
    // alg.setNetwork( net );
    // alg.run() ;

    // for (Node node: net.getNodes()) {
    //     System.out.println(node.getDescription());

    //     for (int i=0; i < node.getStatesSize(); i++) {
    //         System.out.println(node.getStateAt(i) + " : " + (( ProbabilisticNode ) node ). getMarginalAt (i));

    //     }
    // }

    // ProbabilisticNode findingNode = ( ProbabilisticNode ) net.getNodes().get(0);

    // findingNode.addFinding(0);
    // float likelihood [] = new float[ newNode . getStatesSize () ];
    // likelihood [0] = 1f;
    // likelihood [1] = 0.8f;
    // newNode.addLikeliHood ( likelihood );

    // net.updateEvidences();

    // System.out.println (" **** Updated **** ");
    // for (Node node: net.getNodes()) {
    //     System.out.println(node.getDescription());

    //     for (int i=0; i < node.getStatesSize(); i++) {
    //         System.out.println(node.getStateAt(i) + " : " + (( ProbabilisticNode ) node ). getMarginalAt (i));

    //     }
    // }
    Gateway app = new Gateway();
    
    
    // app is now the gateway.entry_point
    GatewayServer server = new GatewayServer(app);
    server.start();
  }
}


