from mutagen.easyid3 import EasyID3
import re, os, sys

def cleanup(value):
    if isinstance(value, list):
        for key, _ in enumerate(value):
            value[key] = cleanup(value[key])
        return value
    else:
        # print "VALUE:", value
        pattern = re.compile("(-\s)*www.songs.pk", re.IGNORECASE)
        output = pattern.sub("", value)
        return output.strip()

def cleanUpFile(filePath):
    audio = EasyID3(filePath)
    changed = 0
    for fieldName in audio:
        if audio[fieldName] == "":
            continue
        cleanValue = cleanup( audio[fieldName] )
        if not cleanValue == audio[fieldName]:
            changed = 1
        audio[fieldName] = cleanValue
    if changed == 1:
        print audio["title"]
        print audio.save()
    
if __name__ == "__main__":
    filePath = sys.argv[1]
    cleanUpFile(filePath)

