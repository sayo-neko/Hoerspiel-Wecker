from mpd import MPDClient


class MPD:

    client = None

    conf = {
        'port': 6600
    }

    def __init__(self):
        if self.client is None:
            self.client = MPDClient()

        self.client.timeout = 10  # network timeout in seconds (floats allowed), default: None
        self.client.idletimeout = None  # timeout for fetching the result of the idle command is handled seperately, default: None

    def connect(self):
        self.client.connect("localhost", self.conf['port'])  # connect to localhost:6600

    def disconnect(self):
        self.client.close()  # send the close command
        self.client.disconnect()  # disconnect from the server

    def doSomething(self):
        print(self.client.mpd_version)  # print the MPD version
        print(self.client.findadd("file", "At The Gates - All Life Ends.mp3"))  # print result of the command "find any house"
        print(self.client.list('file'))
        print(self.client.currentsong())  # print result of the command "find any house"
        print(self.client.stats())  # print result of the command "find any house"

        self.client.command_list_ok_begin()  # start a command list
        self.client.update()  # insert the update command into the list
        self.client.status()  # insert the status command into the list

        print(self.client.command_list_end())  # results will be a list with the results

        self.client.iterate = True
        for song in self.client.playlistinfo():
            print(song["file"])

        # self.client.play(0)
        self.client.stop()
