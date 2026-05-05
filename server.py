"""
pigate.server — WireGuard server setup and lifecycle
"""

import subprocess
from pathlib import Path

import wgconfig

from .config import PigateConfig
from .keys import KeyPair, generate_keypair, save_keypair, load_keypair


KEYS_FILE = "config/server_keys.json"


class PigateServer:
    def __init__(self, config: PigateConfig):
        pass

    @property
    def keypair(self) -> KeyPair:
        pass

    def setup(self, force: bool = False):
        """One-time setup: generate keys, write WireGuard config, enable forwarding."""
        pass

    def _enable_ip_forwarding(self):
        """Allow packets to flow through the Pi (essential for VPN routing)."""
        pass

    def _write_server_config(self):
        """Write the WireGuard server config file."""
        pass

    def start(self):
        """Bring the WireGuard interface up."""
        pass

    def stop(self):
        """Bring the WireGuard interface down."""
        pass

    def status(self):
        """Print current WireGuard status."""
        pass

    def enable_autostart(self):
        """Enable the VPN to start automatically on reboot via systemd."""
        pass
