import subprocess
import time

from application.git import ApplicationGit
from application.yaml import ApplicationYaml


class Application:
    def __init__(self, yaml_file_path: str):
        self.yaml_file_path: str = yaml_file_path
        self.yaml: ApplicationYaml = ApplicationYaml(yaml_file_path)
        self.git: ApplicationGit = ApplicationGit(self.yaml.repository.path, self.yaml.repository.branch)

    def run(self) -> None:
        while True:
            self.yaml.load()
            self.git.load()

            self.git.repository_fetch()

            if not self.git.has_updates():
                time.sleep(self.yaml.settings.interval_seconds)
                continue

            self.git.repository_pull()

            for command in self.yaml.commands.commands:
                subprocess.run(command, shell=True)
            time.sleep(self.yaml.settings.interval_seconds)

def main() -> None:
    application = Application("config.yaml")
    application.run()

if __name__ == "__main__":
    main()
