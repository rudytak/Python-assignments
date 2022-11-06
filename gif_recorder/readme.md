# Module uses

The gif_recorder python module can be used on it's own or parts of the code can be imported to be used in other projects.

# Module classes

## Recorder

The `Recorder` class allows the user to capture the screen content and save the data to a GIF file. Each `Recorder` instance uses it's own StoppableThread instance that allows for parallelized running, which is useful for the GUI class. The thread is running an infinite while loop that calls the `Recorder.tick()` function. The `Recorder` constructor takes one argument called `fps` which denotes the target frames per second. This value only limits the maximum frames per second and a slow system might not be able to process the images in time which would lead to incorrect timings.

### Instanciation

The `Recorder` has a default `fps` value of `10` and can me instanciated like so:

```python
# a new Recorder instance will be created with target capture fps of 24 frames/s
rec = Recorder(24)
```

### Recording

The Recorder recording can be started and stopped with the following command:

```python
# start the recording
rec.start() 

# stop the recording
# stopping the recording will cause an automatic export
rec.stop()
```

The `Recorder` has a public non-static boolean property `Recorder.recording` which indicates whether a `Recorder` instance is currently capturing frames.

### Manual clearing

Or the `Recorder` frames can be manually cleared by calling:

```python
rec.reset() # stops recording and clears frame
```

### Exporting

The .GIF file will automatically be exported in the next internal tick if the recording has been stopped and at least one frame has been saved. The output format is `%d-%m-%Y_%H-%M-%S.gif` at the time when the exporting process has started. During the time that the export is ongoing, a public non-static boolean property `Recorder.processing` is set to `True` and after the export is finished, the recorder resets itself using the `Recorder.reset()` function and the property `Recorder.processing` is set back to `False`. The exporting process can take a long time and it is evaluated inline just like a normal tick. Due to this any changes/function calls will only be reflected in the next tick after the exporting is done. E.g. recording while at the same time exporting is not possible.

## StoppableThread

The StoppableThread class is a helper class used to create infinitely looping function calls inside a thread, that can be successfully destroyed after the program is killed. During construction it takes in 3 arguments: `target`, `fail_callback` and `fail_value`. `target` is the target function that shall be called infinitely in the loop, `fail_callback` is a function that will be called after the `target` function call returns a value that is equal to `fail_value`, which will cause the `StoppableThread` to stop itself using `StoppableThread.stop()`. `fail_value` is by default set to `-1`. Each `StoppableThread` instance allocates a single internal thread, which exectues the `StoppableThread.exec()` function. This function runs an infinite while loop in which it calls the `StoppableThread.target` function property and takes care of stoping itself and handling `StoppableThread.fail_callback`.

### Instanciation

```python
import time

# an example class that counts up to 10 and sleep after each increment
class Foo:
    def __init__(self):
        self.x = 0
    
    # our goal is to run this function in a thread to not halt other parts of the program
    def bar(self):
        self.x += 1
        time.sleep(1000)

        if(self.x >= 10):
            return False
        else:
            return True
    
    # this represents the fail_callback and will be called after the goal is reached
    def baz(self):
        print("Done")


t = StoppableThread(f.bar, f.baz, False)

# Output:
# *10 second delay*
# > Done
```

### External stopping

The stopppable thread can be stopped externally using `StoppableThread.stop()` like so:

```python
f = Foo()
t = StoppableThread(f.bar, f.baz, False)
t.stop() # stops the thread externally
```

The thread is stopped by internally raising an exception in the next loop cycle.

## GUI

The GUI class handle some simple UI for when the module is run by itself. It uses a `StoppableThread` to run `GUI.eventLoop()` which takes care of visually updating contents in the UI window to reflect the behaviour of it's internal `Recorder` instance. This instance always runs at the set framerate of `10`.

# Running

The default UI can be run using the `main.exe` file or by exectuing `main.py` in a viable python interpretter.