class Config:
    conf = {
        "labels": {
            "pageTitle": "Hoerspielwecker V0.0.1"
        },
        "navigation": [
            {
                "url": "/",
                "name": "Home"
            },
            {
                "url": "/playlists",
                "name": "Playlists"
            }
        ]
    }

    def get_config(self):
        return self.conf

    def get(self, key):
        return self.conf[key]