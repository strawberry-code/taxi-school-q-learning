import codecs
import json
from os import system
from time import sleep
import numpy as np


def serialize(q_table):
    print("Serializing the trained Q Table in JSON file...")
    np.arange(10).reshape(2, 5)
    b = q_table.tolist()
    file_path = "q_table.json"
    json.dump(b, codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)
    print("Serialization finished. Your trained Q Table has been written in q_table.json.")


def deserialize():
    print("Deserializing tra Q Table, if any...")
    obj_text = codecs.open("q_table.json", 'r', encoding='utf-8').read()
    b_new = json.loads(obj_text)
    print("Deserialization done, Q Table is now loaded in memory.")
    return np.array(b_new)


def print_frames(frames):
    for i, frame in enumerate(frames):
        system('clear')
        print(frame['frame'])
        print(f"Timestep: {i + 1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(.01)
