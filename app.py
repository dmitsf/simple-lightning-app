import lightning as L


class WordComponent(L.LightningWork):
    def __init__(self, word):
        super().__init__(cloud_compute=L.CloudCompute())
        self.word = word

    def run(self):
        print(self.word)


class LitApp(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.hello = WordComponent("hello")
        #self.world = WordComponent("world")

    def run(self):
        print("This is a simple Lightning app, make a better app!")
        self.hello.run()
        #self.world.run()


app = L.LightningApp(LitApp())
