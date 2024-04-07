from abc import ABC, abstractmethod

# Interface for functional commands
class FunctionalInterface(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def rewind(self):
        pass

    @abstractmethod
    def fast_forward(self):
        pass

# Audio player class implementing the FunctionalInterface
class AudioPlayer(FunctionalInterface):
    def play(self):
        print("Audio is playing.")

    def pause(self):
        print("Audio is paused.")

    def stop(self):
        print("Audio is stopped.")

    def rewind(self):
        print("Rewinding audio.")

    def fast_forward(self):
        print("Fast forwarding audio.")

# Video player class implementing the FunctionalInterface
class VideoPlayer(FunctionalInterface):
    def play(self):
        print("Video is playing.")

    def pause(self):
        print("Video is paused.")

    def stop(self):
        print("Video is stopped.")

    def rewind(self):
        print("Rewinding video.")

    def fast_forward(self):
        print("Fast forwarding video.")

# Streaming platform class implementing the FunctionalInterface
class StreamingPlatform(FunctionalInterface):
    def play(self):
        print("Streaming is playing.")

    def pause(self):
        print("Streaming is paused.")

    def stop(self):
        print("Streaming is stopped.")

    def rewind(self):
        print("Rewinding streaming.")

    def fast_forward(self):
        print("Fast forwarding streaming.")

# Main function to test the media player
def main():
    audio_player = AudioPlayer()
    video_player = VideoPlayer()
    streaming_platform = StreamingPlatform()

    # Testing audio player
    audio_player.play()
    audio_player.pause()
    audio_player.stop()
    audio_player.rewind()
    audio_player.fast_forward()

    # Testing video player
    video_player.play()
    video_player.pause()
    video_player.stop()
    video_player.rewind()
    video_player.fast_forward()

    # Testing streaming platform
    streaming_platform.play()
    streaming_platform.pause()
    streaming_platform.stop()
    streaming_platform.rewind()
    streaming_platform.fast_forward()

if __name__ == "__main__":
    main()
