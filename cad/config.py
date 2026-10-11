"""Modular variant configuration (enclosure-forge target #2).

Every option combination is a config dict; build_config() maps it to
solid builders. New combos fall out of the flag matrix instead of new
hand-named variants.

    {
      "board":   "main" | "full",       # keyboard breakaway removed/kept
      "screen":  "none" | "popout" | "open",
      "keypad":  "none" | "bay" | "well",
      "battery": bool,                  # battery pocket + service slot
      "usb":     bool,                  # USB-C wall opening
      "profile": "slim" | "slab",       # stepped vs uniform silhouette
    }

Constraints (boolean-provable, not stylistic):
  * keypad bay      -> profile slim + board full
  * keypad well     -> profile slab + board full
  * screen open     -> screen popout (same print, panel popped)
"""

from __future__ import annotations

from . import parameters as P
from . import shell as S

DEFAULT = {
    "board": "full",
    "screen": "popout",
    "keypad": "well",
    "battery": True,
    "usb": True,
    "profile": "slab",
}


def normalize(cfg: dict | None) -> dict:
    c = dict(DEFAULT)
    c.update(cfg or {})
    if c["keypad"] != "none":
        assert c["board"] == "full", "keypad integration needs the full board"
    if c["keypad"] == "bay":
        assert c["profile"] == "slim", "bay is the stepped-profile treatment"
    if c["keypad"] == "well":
        assert c["profile"] == "slab", "well is the uniform-slab treatment"
    if c["screen"] == "open":
        c["screen"] = "popout"
        c["_popped"] = True
    return c


def name(cfg: dict) -> str:
    c = normalize(cfg)
    tag = f"{c['board']}-{c['profile']}-{'scr' if c['screen'] != 'none' else 'noscr'}"
    if c["keypad"] != "none":
        tag += f"-kp{c['keypad']}"
    if not c["battery"]:
        tag += "-nobat"
    if not c["usb"]:
        tag += "-nousb"
    if c.get("_popped"):
        tag += "-open"
    return tag


def build_config(cfg: dict | None):
    """Return (bottom, lid) for any valid config."""
    c = normalize(cfg)
    popped = bool(c.get("_popped"))
    if c["profile"] == "slab":
        bottom = S.slab_bottom(battery=c["battery"], usb=c["usb"])
        lid = S.slab_lid(screen=c["screen"], keypad=c["keypad"],
                         battery=c["battery"], popped=popped)
    else:
        flare = c["keypad"] == "bay"
        bottom = S.bottom_shell(c["board"], flare=flare,
                                battery=c["battery"], usb=c["usb"])
        variant = ("terminal" if flare else
                   "kb_blister" if c["keypad"] != "none" or c["board"] == "full"
                   else ("popout" if c["screen"] != "none" else "closed"))
        lid = S.lid(variant, c["board"],
                    screen_window=c["screen"] != "none",
                    led_window=True, screen_popped=popped)
    return bottom, lid
