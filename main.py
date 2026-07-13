from tts import Piper

def main():
    piper = Piper(volume=0.05, speed=0.75)

    piper.speak("Hello from Alt!")
    piper.speak("Nice to meet you.")
    piper.speak("Going to adjust wallpaper...")


if __name__ == "__main__":
    main()
