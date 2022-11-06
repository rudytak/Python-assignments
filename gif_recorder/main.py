import imageio.v3 as iio
import imageio
import cv2

import time
from datetime import datetime
import PySimpleGUI as gui
import pyautogui

import sys
import threading

class StoppableThread:
    def __init__(self, target, fail_callback, fail_value=-1):
        # target function to be called forever
        self.target = target
        # function to be caled when the function returns the fail value
        self.fail_callback = fail_callback
        self.fail_value = fail_value

        # keep track whether thread should be aborted
        self.should_end = False

        # execution thread inicialization
        self.thread = threading.Thread(target=self.exec)
        self.thread.start()

    def exec(self):
        # execution thread
        while True:
            # call the function and get the code
            code = self.target()

            # check if the function has failed
            if code == self.fail_value:
                # call the callback and stop itself
                self.fail_callback()
                self.stop()

            if self.should_end:
                # quietly stop running the thread if it has been stopped externally
                sys.exit()

    def stop(self):
        # stop the thread
        self.should_end = True

class Recorder:
    def __init__(self, fps=10) -> None:
        # init fps and reset to default stat
        self.fps = fps
        self.processing = False
        self.reset()

        # create a thread to execute the tick function
        self.thread = StoppableThread(self.tick, self.reset)

    def reset(self):
        # reset the recorder
        self.frames = []
        self.recording = False

    def start(self):
        self.reset()
        # start the recording
        self.recording = True

    def stop(self):
        # end the recording
        self.recording = False

    def tick(self):
        # measure the time it takes to read the screen
        start = time.time()

        # if we're recording
        if self.recording:
            # add a frame
            frame = iio.imread("<screen>")
            cv2.circle(frame, pyautogui.position(), 10, [255, 0, 0], -1)
            self.frames.append(frame)
        else:
            if len(self.frames) > 0:
                # save the gif
                self.processing = True
                imageio.mimsave(
                    "./" + datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".gif",
                    self.frames,
                    duration=1 / self.fps,
                )
                self.processing = False

                self.reset()
            else:
                pass
        end = time.time()

        # sleep for some additional time on top, to make the playback almost consistent
        if 1 / self.fps - (end - start) > 0:
            time.sleep(1 / self.fps - (end - start))

class GUI:
    def __init__(self) -> None:
        # create a recorder
        self.rec = Recorder(16)

        # define the layout
        layout = [
            [gui.Text("", key="message")],
            [gui.Button("▶️", key="startBtn")],
        ]

        # create the UI window
        self.window = gui.Window(title="Recorder", layout=layout, margins=(75, 15))

        # start event loop thread
        self.thread = StoppableThread(self.eventLoop, self.windowClosed)

    def eventLoop(self):
        event, values = self.window.read(timeout=10)

        if event in (None, "Exit"):
            # if the exit button ahs been pressed, return the fail value
            return -1
        if event == "__TIMEOUT__":
            # set the correct button style
            if self.rec.processing:
                # set red record circle
                self.window["startBtn"].update("⏺")
                self.window["startBtn"].update(
                    button_color=("orange", gui.theme_button_color_background())
                )

                self.window["message"].update("Exporting... Please wait...")
                self.window["message"].update(text_color="orange")
            else:
                if self.rec.recording:
                    # set red record circle
                    self.window["startBtn"].update("⏺")
                    self.window["startBtn"].update(
                        button_color=("red", gui.theme_button_color_background())
                    )

                    self.window["message"].update("Recording...")
                    self.window["message"].update(text_color="red")
                else:
                    # set back to start recording triangle
                    self.window["startBtn"].update("▶️")
                    self.window["startBtn"].update(
                        button_color=("white", gui.theme_button_color_background())
                    )

                    self.window["message"].update("Ready...")
                    self.window["message"].update(text_color="lime")
        if event == "startBtn":
            # button has been clicked
            if self.window["startBtn"].ButtonText == "▶️":
                # start recording
                self.rec.start()
            else:
                # stop recording
                self.rec.stop()

    def windowClosed(self):
        # clean up all the threads
        self.rec.thread.stop()
        self.thread.stop()

        # close the window
        self.window.close()

if __name__ == "__main__":
    # start the app
    g = GUI()
