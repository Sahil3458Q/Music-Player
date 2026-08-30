import PySide6.QtWidgets as p ,sys
import PySide6.QtCore as q

class GUI(p.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music player")
        self.resize(700,500)

        self.window = p.QWidget()
        self.setCentralWidget(self.window)
        self.central = p.QVBoxLayout(self.window)
        
        self.central.addStretch()
        self.song_title = p.QLabel("--")
        self.song_title.setAlignment(q.Qt.AlignmentFlag.AlignCenter)
        self.central.addWidget(self.song_title)
        self.artist = p.QLabel("--")
        self.artist.setAlignment(q.Qt.AlignmentFlag.AlignCenter)
        self.central.addWidget(self.artist)

        self.central.addStretch()
        #progress Bar 
        self.prg = p.QSlider(q.Qt.Orientation.Horizontal)
        self.prg.setRange(0,100)
        self.central.addWidget(self.prg,alignment=q.Qt.AlignmentFlag.AlignCenter)
        self.prg.setFixedWidth(300)

        self.time = p.QHBoxLayout()
        self.current= p.QLabel("0:00")
        self.total = p.QLabel("0:00")
        self.time.addStretch()
        self.time.addWidget(self.current)
        self.time.addStretch()
        self.time.addWidget(self.total)
        self.time.addStretch()
        self.central.addLayout(self.time)

        #Commands
        self.commands = p.QHBoxLayout()
        self.prevs = p.QPushButton("Previous")
        self.play = p.QPushButton("Play")
        self.nxt = p.QPushButton("Next")
        self.commands.addWidget(self.prevs)
        self.commands.addWidget(self.play)
        self.commands.addWidget(self.nxt)
        self.central.addLayout(self.commands)
        

app = p.QApplication()
window = GUI()
window.show()
sys.exit(app.exec())

