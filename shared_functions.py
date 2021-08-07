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

def convert_tags_to_string(tags):
    tagstr = "["
    for i in range(len(tags)):
        tagstr += "{"
        tag = tags[i]
        keys = list(tag.keys())
        for j in range(len(keys)):
            key = keys[j]
            val = tag[key]
            tagstr += key + "=" + val
            if j < len(tag.keys()) - 1:
                tagstr += ","
        if i < len(tags) - 1:
            tagstr += "},"
        else:
            tagstr += "}"
    tagstr += "]"
    return tagstr