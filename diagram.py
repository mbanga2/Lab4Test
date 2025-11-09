from diagrams import Diagram, Cluster
from diagrams.programming.framework import Angular, Spring
from diagrams.programming.language import Java, PHP
from diagrams.programming.flowchart import Database as SQL
from diagrams.onprem.client import Users
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.ci import Jenkins

# Creates "IS436.png" (show=False)
with Diagram("IS436", show=False, direction="TB"):
    client = Users("client")

    # Front-end to back-end toolchain
    Angular("Angular") >> Java("Java") >> Spring("Spring")

    with Cluster("Group component"):
        workers = Jenkins("Jenkins")

    with Cluster("Group Cluster"):
        backend = PHP("Backend")
        db = SQL("DB")
        pg = PostgreSQL("pgAdmin")

        backend >> db >> pg

    # Client interacts with backend
    client << backend
    client >> backend
