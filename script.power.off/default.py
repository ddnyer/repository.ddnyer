#!/usr/bin/python
import xbmc, xbmcaddon, time

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_NAME = ADDON.getAddonInfo('name')
LOG_MESSAGE = ADDON.getAddonInfo('name') + ': {}'


def log(message):
    xbmc.log(LOG_MESSAGE.format(message), level=xbmc.LOGINFO)


log("Turn off the TV")

if xbmc.getCondVisibility("Player.HasMedia"):
    log("Stop player first")
    xbmc.executebuiltin("PlayerControl(Stop)")
    time.sleep(1)

xbmc.executebuiltin("ActivateScreensaver")
