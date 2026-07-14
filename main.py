from modules.actions import Actions
from modules.tts import Piper

MODEL = "ryan"
VOLUME = 0.3
SPEED = 0.9


def main():
    print("Spinning up Delamain...")
    print(f"Using model {MODEL} with volume {VOLUME} and a speed of {SPEED}.")

    piper = Piper(model=MODEL, volume=VOLUME, speed=SPEED)
    actions = Actions()

    notification = actions.notify(head="Delamain", body="Now listening...")

    piper.speak("Hello, here is Dellamain!")
    piper.speak("Nice to meet you.")

    input("Press enter to kill the notification...")

    actions.clear_notification(notification)


if __name__ == "__main__":
    main()
