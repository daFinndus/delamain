import subprocess


class Actions:
    def __init__(self) -> None:
        pass

    # Creates a notification, either persistent or with time
    def notify(self, head: str, body: str, time: int = 0) -> int:
        try:
            result = subprocess.run(
                ["notify-send", "-p", "-t", str(time), head, body],
                capture_output=True,
                text=True,
                check=True,
            )

            id = int(result.stdout.strip())

            print(f"Got notification id: {id}")

            return id
        except Exception as e:
            print(f"notify-send failed: {e}")

        return 10000

    def replace_notification(self, id: int, head: str, body: str, time: int = 0):

        try:
            subprocess.run(["notify-send", "-r", str(id), "-t", str(time), head, body])

            print(f"Replaced notification id: {id}")
        except Exception as e:
            print(f"replace_notification for {id} failed: {e}")

    # This will basically kill a notification based on a specific notification id
    def clear_notification(self, id: int | None):
        if id is None:
            print("Provided faulty id in clear_notification.")
            return

        try:
            subprocess.run(
                [
                    "gdbus",
                    "call",
                    "--session",
                    "--dest",
                    "org.freedesktop.Notifications",
                    "--object-path",
                    "/org/freedesktop/Notifications",
                    "--method",
                    "org.freedesktop.Notifications.CloseNotification",
                    str(id),
                ],
                check=True,
                stdout=subprocess.DEVNULL,
            )
        except Exception as e:
            print(f"clear_notification for id {id} failed: {e}")
