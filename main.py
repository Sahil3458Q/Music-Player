import PySide6.QtWidgets as p ,sys
import PySide6.QtCore as q
import PySide6.QtGui as g

class GUI(p.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music player")
        self.resize(700,500)

        self.window = p.QWidget()
        self.setCentralWidget(self.window)
        self.central = p.QVBoxLayout(self.window)

        #album Frame
        self.album = p.QFrame()
        self.central.addWidget(self.album,alignment=q.Qt.AlignmentFlag.AlignCenter)
        self.album.setFrameShape(p.QFrame.Shape.Box)
        self.album.setFixedSize(250,250)
        self.alb_lay = p.QVBoxLayout(self.album)
        self.alb_label = p.QLabel("ALBUM")
        self.alb_lay.addWidget(self.alb_label ,alignment=q.Qt.AlignmentFlag.AlignTop | q.Qt.AlignmentFlag.AlignCenter)

        self.image = g.QPixmap("image.png").scaled(250,250,aspectMode=q.Qt.AspectRatioMode.KeepAspectRatio)
        self.alb_label.setPixmap(self.image )
        
        self.central.addStretch()
        self.song_title = p.QLabel("--")
        self.song_title.setFixedSize(300,40)
        self.song_title.setAlignment(q.Qt.AlignmentFlag.AlignCenter)
        self.central.addWidget(self.song_title,alignment=q.Qt.AlignmentFlag.AlignCenter)
        self.artist = p.QLabel("--")
        self.artist.setAlignment(q.Qt.AlignmentFlag.AlignCenter)
        self.artist.setFixedSize(300,40)
        self.central.addWidget(self.artist,alignment=q.Qt.AlignmentFlag.AlignCenter)

        self.central.addStretch()
        #progress Bar 
        self.prg = p.QSlider(q.Qt.Orientation.Horizontal)
        self.prg.setRange(0,100)
        self.central.addWidget(self.prg,alignment=q.Qt.AlignmentFlag.AlignCenter)
        self.prg.setFixedWidth(300)

        self.time = p.QHBoxLayout()
        self.current= p.QLabel("0:00")
        self.current.setAlignment(q.Qt.AlignmentFlag.AlignCenter)
        self.current.setFixedSize(80,20)
        self.total = p.QLabel("0:00")
        self.total.setFixedSize(80,20)
        self.total.setAlignment(q.Qt.AlignmentFlag.AlignCenter)
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
        self.volume = p.QSlider(q.Qt.Orientation.Horizontal)
        self.volume.setFixedWidth(70)
        self.volume.setRange(0,100)
        self.commands.addWidget(self.volume)

        #Properties
        self.artist.setObjectName("header")
        self.song_title.setObjectName("header")

        self.current.setObjectName("time")
        self.total.setObjectName("time")

        self.setObjectName("main")
        

app = p.QApplication()
window = GUI()
app.setStyleSheet(open("style.qss").read())
window.show()
sys.exit(app.exec())
