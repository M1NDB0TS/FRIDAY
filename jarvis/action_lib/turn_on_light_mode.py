from jarvis.action.base_action import BaseAction


class turn_on_light_mode(BaseAction):
    def __init__(self) -> None:
        super().__init__()
        self._description = "Using turn_on_light_mode() will change your system into the light mode."

    @property
    def _command(self):
        return 'shortcuts run "Light Mode"'

    # def _success(self):
    #     return "Successfully turned the system into the Light Mode"

    # def __call__(self, *args, **kwargs):
    #
    #     command = 'shortcuts run "Dark Mode"'
    #     try:
    #         # result = subprocess.run([command, "Dark Mode"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    #         result = subprocess.run([command], capture_output=True, check=True,
    #                                 text=True, shell=True, timeout=self.timeout, stdin=subprocess.DEVNULL)
    #         if result.returncode == 0:
    #             return result
    #     except subprocess.CalledProcessError as e:
    #         return e
        # except subprocess.TimeoutExpired:
        #     raise TimeoutError(f"Command '{command}' timed out after {self.timeout} seconds.")

