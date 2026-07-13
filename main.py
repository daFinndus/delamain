from modules.tts import Piper
from modules.wakeword import Waker

def main():
    piper = Piper(model = "ryan", volume = 0.3, speed = 0.9)

    piper.speak("Hello from Dellamain!")
    piper.speak("Nice to meet you.")
    piper.speak("Going to adjust wallpaper...")



if __name__ == "__main__":
    main()
