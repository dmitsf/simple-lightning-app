import lightning as L


class WordComponent(L.LightningWork):
    def __init__(self, word):
        super().__init__(cloud_compute=L.CloudCompute()) # modify L.CloudCompute() if you wish to use a different config, e.g. L.CloudCompute("gpu")
        self.word = word

    def run(self):
        drive = L.storage.Drive("lit://drive111", component_name="word")
        print("=======>", drive.list("."))

        with open("a.txt", "w") as f:
            f.write("Hello World !")

        drive.put("a.txt")
        print(drive.list("."))
        print(drive.get("a.txt"))  # Get the file into the current worker

        #drive.delete("a.txt")
        #drive.list(".")

        print(self.word)


class LitApp(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.hello = WordComponent("hello")
#        self.world = WordComponent("world")

    def run(self):
        print("This is a simple Lightning app, make a better app!")
        self.hello.run()
#        self.world.run()


app = L.LightningApp(LitApp())
