from pathlib import Path


class SceneFile(object):

    def __init__(self, path):
        path = Path(path)
        self.folder_path = path.parent
        self.ext = path.suffix
        self.descriptor, self.task, self.ver = path.stem.split("_")

   