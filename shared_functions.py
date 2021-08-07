#!/usr/bin/env python3

def get_host_ids_from_input(guide_text):
    inputString = input(guide_text + " ")
    hostIdStrings = inputString.split(" ")
    hostIds = []
    for hostIdStr in hostIdStrings:
        hostId = int(hostIdStr)
        if hostId < 0:
            return []
        hostIds.append(hostId)
    return hostIds