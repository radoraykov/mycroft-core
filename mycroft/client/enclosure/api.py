# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.


from mycroft.messagebus.message import Message
from mycroft.util.log import getLogger

__author__ = 'jdorleans'

LOGGER = getLogger(__name__)


class EnclosureAPI:
    """
    This API is intended to be used to interface with the hardware
    that is running Mycroft.  It exposes all possible commands which
    can be sent to a Mycroft enclosure implementation.
    """

    def __init__(self, ws):
        self.ws = ws

    def system_reset(self):
        self.ws.emit(Message("enclosure.system.reset"))

    def system_mute(self):
        self.ws.emit(Message("enclosure.system.mute"))

    def system_unmute(self):
        self.ws.emit(Message("enclosure.system.unmute"))

    def system_blink(self, times):
        self.ws.emit(Message("enclosure.system.blink", {'times': times}))

    def eyes_on(self):
        self.ws.emit(Message("enclosure.eyes.on"))

    def eyes_off(self):
        self.ws.emit(Message("enclosure.eyes.off"))

    def eyes_blink(self, side):
        self.ws.emit(Message("enclosure.eyes.blink", {'side': side}))

    def eyes_narrow(self):
        self.ws.emit(Message("enclosure.eyes.narrow"))

    def eyes_look(self, side):
        self.ws.emit(Message("enclosure.eyes.look", {'side': side}))

    def eyes_color(self, r=255, g=255, b=255):
        self.ws.emit(Message("enclosure.eyes.color",
                             {'r': r, 'g': g, 'b': b}))

    def eyes_brightness(self, level=30):
        self.ws.emit(Message("enclosure.eyes.level", {'level': level}))

    def eyes_reset(self):
        self.ws.emit(Message("enclosure.eyes.reset"))

    def eyes_timed_spin(self, length):
        self.ws.emit(Message("enclosure.eyes.timedspin",
                             {'length': length}))

    def eyes_volume(self, volume):
        self.ws.emit(Message("enclosure.eyes.volume", {'volume': volume}))

    def mouth_reset(self):
        self.ws.emit(Message("enclosure.mouth.reset"))

    def mouth_talk(self):
        self.ws.emit(Message("enclosure.mouth.talk"))

    def mouth_think(self):
        self.ws.emit(Message("enclosure.mouth.think"))

    def mouth_listen(self):
        self.ws.emit(Message("enclosure.mouth.listen"))

    def mouth_smile(self):
        self.ws.emit(Message("enclosure.mouth.smile"))

    def mouth_viseme(self, code):
        self.ws.emit(Message("enclosure.mouth.viseme", {'code': code}))

    def mouth_text(self, text=""):
        self.ws.emit(Message("enclosure.mouth.text", {'text': text}))

    def weather_display(self, img_code, temp):
        self.ws.emit(Message("enclosure.weather.display",
                             {'img_code': img_code, 'temp': temp}))

    def activate_mouth_events(self):
        self.ws.emit(Message('enclosure.mouth.events.activate'))

    def deactivate_mouth_events(self):
        self.ws.emit(Message('enclosure.mouth.events.deactivate'))
