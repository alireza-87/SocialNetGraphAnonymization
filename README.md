# SocialNetGraphAnonymization
Socialnetwork graph anonymization by perturbation  
Development Enviroment:  

* VsCode
* Python 3.7.6
* Ubuntu
* mini-conda venv
* Xming(if you want to develop in WSL)
* Dependencies
  * matplotlib
  * networkx-2.2
  * numpy

The repository contain a sample dataset.gml however you can set your own dataset while the app running  
How Algorithm work:  
1. Anonymize graph by naive
1. remove and add some connection randomly
1. plot removed connection
1. plot added connection
1. plot final graph
1. display graph info

Add and remove connection to the graph is done by probability:
1. Generate a random number
1. if the number below our expectation then add or remove a random conncetin
1. we execute this step for all nodes in graph

We start from 10% and increase the probeblity to 100%, as you will see , by increasing the probeblity more data will be lose  
In 100% probeblity our graph will be a random graph, however, the nodes never change 
  
Orginal Graph:    
![Orginal Graph](/image/orginal.png)  
add 10%:  
![added_10](/image/added_10.png)  
remove 10%:  
![removed_10](/image/removed_10.png)  
final 10%:  
![final_10](/image/final_10.png)  
