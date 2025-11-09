from diagrams import Cluster, Diagram, Edge
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Ingress
from diagrams.onprem.network import Nginx
from diagrams.onprem.client import Client

# Generates "IS436_Application.png" by default (show=False)
with Diagram("IS436_Application", show=False, direction="TB"):

    user = Client("User")

    with Cluster("Kubernetes"):
        with Cluster("Nginx"):
            nginx = Nginx("")

        with Cluster("MyApp"):
            myapp_ing = Ingress("ingress")
            with Cluster("Pods"):
                myapp_pods = Pod("myapp")

        with Cluster("MySQL"):
            myapp_db = Pod("myapp-db")

    # Flow: User -> Nginx -> Ingress -> Pod -> DB
    user >> Edge(headport="c", tailport="c", minlen="1", lhead="cluster_Kubernetes") >> nginx
    nginx >> Edge(headport="c", tailport="c", minlen="1", lhead="cluster_MyApp") >> myapp_ing
    myapp_ing >> Edge(headport="c", tailport="c", minlen="1", lhead="cluster_MyApp Pods") >> myapp_pods
    myapp_pods >> myapp_db
