import datetime
import fontawesome as fa
from i3ipc import Connection, Event

i3 = Connection()

def update_workspace_name(i3, e):
    focused = i3.get_tree().find_focused()
    if focused.window_class is not None:
        window_name = filter_app_name(focused.window_class)
        ws_name = "%s:%s" % (focused.workspace().num, window_name)
    else:
        ws_name = "%s" % (focused.workspace().num)
    i3.command("rename workspace to %s" % ws_name)

def filter_app_name(app_name: str):
    if "firefox" in app_name:
        return fa.icons["firefox"] + "firefox"
    if "alacritty" in app_name.lower():
        return fa.icons["terminal"] + "alacritty"
    if "steam" in app_name.lower():
        return fa.icons["steam"] + "steam"

    return app_name.lower()

i3.on(Event.WINDOW_FOCUS, update_workspace_name)
i3.on(Event.WINDOW_CLOSE, update_workspace_name)

i3.main()
