import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QWidget, QPushButton, QLabel, QTextEdit, QSplitter
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl

class FileUploaderApp(QMainWindow):
    def __init__(self):
        super(FileUploaderApp, self).__init__()

        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Splitter to display video and text side by side
        splitter = QSplitter(Qt.Horizontal)

        # Left Side: Video/Audio File Upload
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)

        self.video_label = QLabel('Upload Video/Audio File', self)
        left_layout.addWidget(self.video_label)

        self.video_button = QPushButton('Upload', self)
        self.video_button.clicked.connect(self.uploadVideo)
        left_layout.addWidget(self.video_button)

        splitter.addWidget(left_widget)

        # Right Side: Text File Upload
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)

        self.text_label = QLabel('Upload Text File', self)
        right_layout.addWidget(self.text_label)

        self.text_button = QPushButton('Upload', self)
        self.text_button.clicked.connect(self.uploadText)
        right_layout.addWidget(self.text_button)

        splitter.addWidget(right_widget)

        layout.addWidget(splitter)

        # Display Uploaded Content
        self.display_label = QLabel('Uploaded Content:', self)
        layout.addWidget(self.display_label)

        self.display_text = QTextEdit(self)
        self.display_text.setReadOnly(True)
        layout.addWidget(self.display_text)

        # Video Player
        self.video_player = QMediaPlayer(self)
        self.video_widget = QVideoWidget(self)
        layout.addWidget(self.video_widget)
        self.video_player.setVideoOutput(self.video_widget)

        self.setWindowTitle('File Uploader')
        self.setGeometry(100, 100, 800, 400)

    def uploadVideo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        video_file, _ = QFileDialog.getOpenFileName(self, "Select Video/Audio File", "", "Video Files (*.mp4 *.avi *.mkv *.mp3 *.wav);;All Files (*)", options=options)

        if video_file:

            # Play the video
            media = QMediaContent(QUrl.fromLocalFile(video_file))
            self.video_player.setMedia(media)
            self.video_player.play()

    def uploadText(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        text_file, _ = QFileDialog.getOpenFileName(self, "Select Text File", "", "Text Files (*.txt);;All Files (*)", options=options)

        if text_file:
            with open(text_file, 'r') as file:
                content = file.read()
                self.display_text.append(content)

            # Stop playing the video
            self.video_player.stop()


def main():
    app = QApplication(sys.argv)
    uploader_app = FileUploaderApp()
    uploader_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
