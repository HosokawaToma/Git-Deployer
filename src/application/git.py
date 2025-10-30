import os

from git import Repo


class ApplicationGit:
    def __init__(self, repository_path: str, branch: str):
        self.repository_path: str = repository_path
        self.branch: str = branch
        self.repo: Repo | None = None
        self.load()

    def load(self) -> None:
        if self.repository_path is None:
            raise ValueError("Repository path is required")
        if self.branch is None:
            raise ValueError("Branch is required")
        if not os.path.exists(self.repository_path):
            raise FileNotFoundError(f"Repository path {self.repository_path} does not exist")
        if not os.path.exists(os.path.join(self.repository_path, '.git')):
            raise FileNotFoundError(f"Repository path {self.repository_path} is not a git repository")
        self.repo = Repo(self.repository_path)

    def get_repository_latest_commit(self) -> str:
        return self.repo.head.commit.hexsha

    def get_repository_latest_remote_commit(self) -> str:
        return self.repo.remotes.origin.refs[self.branch].commit.hexsha

    def has_updates(self) -> bool:
        return self.get_repository_latest_commit() != self.get_repository_latest_remote_commit()

    def repository_fetch(self) -> None:
        self.repo.remotes.origin.fetch()

    def repository_pull(self) -> None:
        self.repo.remotes.origin.pull()
