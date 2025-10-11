import subprocess
import time

from application.git import ApplicationGit
from application.log import ApplicationLog
from application.yaml import ApplicationYaml


class Application:
    def __init__(self, yaml_file_path: str):
        self.yaml_file_path: str = yaml_file_path
        self.yaml: ApplicationYaml = ApplicationYaml(yaml_file_path)
        self.log: ApplicationLog = ApplicationLog(self.yaml.settings.log_file_path)
        self.git: ApplicationGit = ApplicationGit(self.yaml.repository.path, self.yaml.repository.branch)

    def run(self) -> None:
        while True:
            self.yaml.load()
            self.log.load()
            self.git.load()

            self.git.repository_fetch()
            self.log.info("Repository fetched")

            if not self.git.has_updates():
                self.log.info("No updates found")
                time.sleep(self.yaml.settings.interval_seconds)
                continue

            self.git.repository_pull()
            self.log.info("Repository updated")

            for command in self.yaml.commands.commands:
                self.log.info(f"Running command: {command}")
                subprocess.run(command, shell=True)
                self.log.info(f"Command completed: {command}")
            time.sleep(self.yaml.settings.interval_seconds)

def main() -> None:
    application = Application("config.yaml")
    application.run()

if __name__ == "__main__":
    main()
