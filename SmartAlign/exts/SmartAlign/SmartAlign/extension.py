import omni.ext
import omni.ui as ui
import omni.kit.commands

from pxr import Usd, Sdf, Gf, Tf, UsdGeom, UsdPhysics, UsdShade
from omni.ui import color as cl


# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print("[SmartAlign] some_public_function was called with x: ", x)
    return x ** x


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class SmartalignExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[SmartAlign] SmartAlign startup")

        self._count = 0

        self._window = ui.Window("Smart Align", width=300, height=300)
        with self._window.frame:
            with ui.VStack():
                label = ui.Label("")


                def on_click():
                    self._count += 1
                    label.text = f"count: {self._count}"

                def on_reset():
                    self._count = 0
                    label.text = "empty"

                on_reset()

                with ui.HStack():
                    ui.Button("Add", clicked_fn=on_click)
                    ui.Button("Reset", clicked_fn=on_reset)

    def on_shutdown(self):
        print("[SmartAlign] SmartAlign shutdown")
