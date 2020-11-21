#!/usr/bin/env python
import os
import json
import sys

chartFile = "jaja"
errorCount = 0

if len(sys.argv) > 1:
    chartFile = sys.argv[1]
else:
    chartFile = "Chart.json"

if not os.path.exists(chartFile):
    input("File NOT exist! Press ENTER to Contiune...")
    exit()

with open(chartFile) as f:
    chart = json.loads(f.read())
print("Checking...")
notes = chart["note_list"]
notes.sort(key=lambda x: x["id"])
idMax = notes[-1]["id"]

notes.sort(key=lambda x: x["tick"])
xUsed = [[0 for i in range(100 + int(notes[-1]["tick"] / 5))] for i in range(20)]

for note in notes:
    # print('note '+str(note['id'])+': tick.'+str(note['tick'])+', x.'+str(note['x']))
    if note["x"] >= 1:
        note["x"] = 0.99
    if xUsed[int(note["x"] * 20)][int(note["tick"] / 5)] > 0:
        print(
            "note "
            + str(note["id"])
            + ": tick."
            + str(note["tick"])
            + ", x."
            + str(note["x"])
        )
        errorCount += 1
    for i in range(-1, 1):
        for j in range(-5, 6):
            if int(note["x"] * 20) + i >= 0 and int(note["tick"] / 5) + j >= 0:
                xUsed[i + int(note["x"] * 20)][j + int(note["tick"] / 5)] += 1
    if note["id"] % 100 == 0:
        print(str(note["id"]) + " Checked.")
input("All " + str(errorCount) + " error(s) in all "+ str(idMax+1) +" note(s). Press ENTER to Contiune...")
