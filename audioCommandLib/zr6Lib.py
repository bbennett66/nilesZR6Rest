#!/usr/bin/env python3

from audioCommandLib import socketLib

GLOBAL_CACHE_IP = "192.168.2.151"
SERIAL_PORT = 4999

ZONE_01 = "01"
ZONE_02 = "02"
ZONE_03 = "03"
ZONE_04 = "04"
ZONE_05 = "05"
ZONE_06 = "06"
ZONE_07 = "07"
ZONE_08 = "08"
ZONE_09 = "09"
ZONE_10 = "10"
ZONE_11 = "11"
ZONE_12 = "12"
ZONE_SET_ACTIVE = "znc,4,{zone}\r"
ZONE_SPECIFIC_COMMAND = "zsc,{zone},{command}\r"
ZONE_SPECIFIC_COMMAND_RETURN = "rsrc,{zone},{command},OK"
REQUEST_RESPONSE_SET_ACTIVE = "rznc,4,{zone}\r"
REQUEST_GLOBAL_COMMAND = "znt,{command},h\r"
REQUEST_GLOBAL_COMMAND_RETURN = "rznt,{command},OK"
REQUEST_STATUS = "znc,5\r"
#
#   Command: znc,5,[cr] (request status information for the active zone)
#   ZR-6 Response: usc,2,2,3,1,14,0,0,0[cr] (status of the active zone)
#   usc, identifies a response to a status request
#   2, identifies the response as an answer to a status request
#   2, is the number of the current active zone for which status is provided
#   3, number of the currently selected source (1-6) in the active zone
#   1, On/Off status of the active zone (1=On, 0=Off)
#   14, active zone volume level (0-99)
#   0, active zone mute status (1=muted, 0=unmuted)
#   0, active zone bass level (-7 to +7)
#   0 active zone treble level (-7 to +7)
#   [cr] is a carriage return
#
COMMAND_SOURCE_SELECT_2 = "02"
COMMAND_SOURCE_SELECT_3 = "03"
COMMAND_SOURCE_SELECT_4 = "04"
COMMAND_SOURCE_SELECT_5 = "05"
COMMAND_SOURCE_SELECT_6 = "06"
COMMAND_VOLUME_UP = "12"
COMMAND_VOLUME_DOWN = "13"
COMMAND_MUTE = "11"
COMMAND_OFF = "10"
COMMAND_PLAY = "17"
COMMAND_STOP = "18"
COMMAND_ON = "49"  # Power
FAILED = "UNKNOWN FAILURE"


def send_command(command):
    return socketLib.send_command(command, GLOBAL_CACHE_IP, SERIAL_PORT)


def set_current_zone(zone_in):
    return send_command(ZONE_SET_ACTIVE.format(zone=zone_in))


def get_current_zone():
    return send_command(REQUEST_STATUS)


def send_zone_command(zone_in, command_in):
    message = ZONE_SPECIFIC_COMMAND.format(zone=zone_in, command=command_in)
    return send_command(message)


def set_zone_on(zone_in):
    return send_zone_command(zone_in, COMMAND_SOURCE_SELECT_2)


def set_zone_off(zone_in):
    return send_zone_command(zone_in, COMMAND_OFF)


def set_all_zones_on():
    message = REQUEST_GLOBAL_COMMAND.format(command=COMMAND_SOURCE_SELECT_2)
    return send_command(message)


def set_all_zones_off():
    message = REQUEST_GLOBAL_COMMAND.format(command=COMMAND_OFF)
    return send_command(message)


def debug():
    print(set_current_zone(ZONE_05))
    print(get_current_zone())
    print(set_zone_on(ZONE_05))
    print(get_current_zone())
    print(set_zone_off(ZONE_05))
    print(get_current_zone())
    # set_zone_on(ZONE_05)
    # print(get_current_zone())
    # set_zone_off(ZONE_05)
    # print(get_current_zone())
    # set_whole_home_on()
    # set_whole_home_off()


def main():
    debug()


# main()
