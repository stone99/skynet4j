import offshoot


class Serpentmenghuan_agentGameAgentPlugin(offshoot.Plugin):
    name = "Serpentmenghuan_agentGameAgentPlugin"
    version = "0.1.0"

    plugins = []

    libraries = []

    files = [
        {"path": "serpent_menghuan_agent_game_agent.py", "pluggable": "GameAgent"}
    ]

    config = {
        "frame_handler": "PLAY"
    }

    @classmethod
    def on_install(cls):
        print("\n\n%s was installed successfully!" % cls.__name__)

    @classmethod
    def on_uninstall(cls):
        print("\n\n%s was uninstalled successfully!" % cls.__name__)


if __name__ == "__main__":
    offshoot.executable_hook(Serpentmenghuan_agentGameAgentPlugin)
