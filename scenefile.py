from pathlib import Path


class SceneFile(object):

    def __init__(self, path):
        path = Path(path)
        self.folder_path = path.parent
        self.ext = path.suffix
        self.descriptor, self.task, self.ver = path.stem.split("_")
        self.ver = int(self.ver.split("v")[-1])

    @property
    def filename(self):
        pattern = "{descriptor}_{task}_v{ver}{ext}"
        return pattern.format(descriptor=self.descriptor,
                              task=self.task,
                              ver=self.ver,
                              ext=self.ext)

    @property
    def path(self):
        return self.folder_path / self.filename


scene_file = SceneFile("C:/Users/abrar/Desktop/Abrar_model_v001.ma")
print(scene_file.folder_path)
print(scene_file.descriptor)
print(scene_file.task)
print(scene_file.ver)
print(scene_file.ext)
print(scene_file.filename)
print(scene_file.path)



