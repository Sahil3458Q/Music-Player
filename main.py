import PySide6.QtWidgets as p 
import PySide6.QtCore as q
import PySide6.QtGui as g
import PySide6.QtMultimedia as m
import os
import sys

class GUI(p.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music player")
        self.resize(600,500)

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

        self.imageurl = "image.png"
        self.image = g.QPixmap(self.imageurl).scaled(250,250,aspectMode=q.Qt.AspectRatioMode.KeepAspectRatio)
        self.alb_label.setPixmap(self.image)
        
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
        self.opn = p.QPushButton("Open")
        self.commands.addWidget(self.opn)
        self.commands.addWidget(self.prevs)
        self.commands.addWidget(self.play)
        self.commands.addWidget(self.nxt)
        self.central.addLayout(self.commands)
        self.volume = p.QSlider(q.Qt.Orientation.Horizontal)
        self.volume.setFixedWidth(80)
        self.volume.setRange(0,100)
        self.commands.addWidget(self.volume)


        #Properties
        self.artist.setObjectName("header")
        self.song_title.setObjectName("header")

        self.current.setObjectName("time")
        self.total.setObjectName("time")

        self.album.setObjectName("frame")
        self.setObjectName("main")

        #signals

        self.opn.clicked.connect(self.open_file)
        self.play.clicked.connect(self.play_Song)
        self.prg.sliderMoved.connect(self.prg_change)
        self.volume.sliderMoved.connect(self.volumechange)

        #MUSIC
        self.player = m.QMediaPlayer()
        self.audio = m.QAudioOutput()
        self.volume.setValue(self.audio.volume()*100)
        self.player.setAudioOutput(self.audio)
        self.player.positionChanged.connect(self.prg_song)
        self.player.durationChanged.connect(self.prepare)
        


    def open_file(self):
        self.file = p.QFileDialog.getOpenFileName(
            self,
            "Select Audio File",
            "",
            "Audio Files (*.mp3 *.wav)"
        )
    
        if self.file[0]:
            self.player.setSource(q.QUrl.fromLocalFile(self.file[0]))
            self.player.play()


    def prepare(self):
        dur = self.player.duration()
        self.prg.setRange(0,dur//1000)
        min = dur//60000 if dur//1000>60 else 0
        sec = (dur//1000 - min*60)
        self.total.setText(f"{min}:{sec}")

        metadata = self.player.metaData()
        title = m.QMediaMetaData.value(metadata,m.QMediaMetaData.Key.Title)
        self.song_title.setText(title)
    
        self.artist.setText("By : "+m.QMediaMetaData.value(metadata,m.QMediaMetaData.Key.ContributingArtist)[0])

        cover = metadata.value(m.QMediaMetaData.Key.ThumbnailImage)

        if not cover.isNull():
            pixmap = g.QPixmap.fromImage(cover).scaled(250,250,aspectMode=q.Qt.AspectRatioMode.KeepAspectRatio)
            self.alb_label.setPixmap(pixmap)

    def play_Song(self):
        if self.player.isPlaying(): 
            self.player.pause()
            self.play.setText("Play")
        else:
            self.player.play()
            self.play.setText("Pause")


    def volumechange(self ,value):
        self.audio.setVolume(value/100)
 
    def prg_song(self,position):
        self.prg.setValue(position//1000)
        min = position//60000 if position//1000>60 else 0
        sec = str(position//1000 - min*60) if (position//1000 - min*60)>10  else str("0")+str(position//1000 - min*60)
        self.current.setText(f"{min}:{sec}")

    def prg_change(self ,pos):
        self.player.setPosition(pos*1000)
        

def resource_path(filename):
    if getattr(sys, "frozen", False):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

app = p.QApplication()
window = GUI()
app.setStyleSheet(open(resource_path("style.qss" ),"r").read())
window.show()
sys.exit(app.exec())


