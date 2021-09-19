from gui import Gui


class Analaser(Gui):
    def init(self):
        self.gui_creation()


if __name__ == "__main__":
    app = Analaser()
    app.init()
    app.start_app()
