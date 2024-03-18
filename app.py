from datetime import datetime as dt
from dotenv import load_dotenv
from time import sleep

import argparse
import docker
import json
import os
import sys

def main(project):
    print(f"[{dt.now()}]: Comienza la carga de la configuración del proyecto.")
    # obtener la configuración del proyecto
    try: 
        # se cargan los settings del .env
        load_dotenv()

        # se abre el archivo de configuraciones del proyecto
        config = open_json_file(project)
        config["docker_img"] = os.getenv("DOCKER-IMG")
    except Exception as e:
        print(f"[{dt.now()}]: Ocurrió un error al intentar obtener la configuración del proyecto a escanear: {e}")
        sys.exit()

    print(f"[{dt.now()}]: Termina la carga de la configuración del proyecto.")

    # se levanta el contenedor
    print(f"[{dt.now()}]: Comienza la ejecución del contenedor SonarCli.")
    try:
        dc = docker.from_env()
        container = dc.containers.run(config["docker_img"],
                                    auto_remove=True,
                                    environment={
                                        "SONAR_HOST_URL": f"http://{config['sonarqube_url']}",
                                        "SONAR_SCANNER_OPTS": f"-Dsonar.projectKey={config['project_key']}",
                                        "SONAR_LOGIN": config["login"]
                                    },
                                    name="sonnarcli",
                                    network=config["network"],
                                    volumes=config["volumes"])
        container_log = container.decode("ascii")
        container_logs = container_log.split("\n")
        for line in container_logs: print(line)
    except Exception as e: print(f"[{dt.now()}]: Ocurrió un error al intentar ejecutar el contenedor SonarCli: {e}")
    print(f"[{dt.now()}]: Termina la ejecución del contenedor SonarCli.")


def open_json_file(file_name):
    f = open(f"./projects/{file_name}.json")
    return json.load(f)

if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="El nombre del proyecto que se va a escanear.")
    args = parser.parse_args()
    main(args.project)