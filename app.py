import lightning as L


class WordComponent(L.LightningWork):
    def __init__(self, word):
        super().__init__(cloud_compute=L.CloudCompute()) # modify L.CloudCompute() if you wish to use a different config, e.g. L.CloudCompute("gpu")
        self.word = word

    def run(self):
        drive = L.storage.Drive("lit://my_drive", component_name="word", allow_duplicates=True)
        print("Before saving the file to the drive:", drive.list("."))

        with open("a.txt", "w") as f:
            f.write("Hello World from the file!")

        drive.put("a.txt")
        print("After saving the file to the drive:", drive.list("."))

        print(self.word)


class LitApp(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.hello = WordComponent("hello")
        # The second component can be enabled:
        # self.world = WordComponent("world")

    def run(self):
        print("This is a simple Lightning app, make a better app!")
        self.hello.run()
        # self.world.run()


app = L.LightningApp(LitApp())
