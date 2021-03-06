from google.colab import drive
drive.mount('/content/drive')



!apt install python3-libtorrent

import libtorrent as lt
import time
import datetime
print("IndyGod King of Downloading")
ses = lt.session()
ses.listen_on(6881, 6891)
params = {
    'save_path': '/content/drive/My Drive/Torrent/',
    'storage_mode': lt.storage_mode_t(2),
    'paused': False,
    'auto_managed': True,
    'duplicate_is_error': True}
print("Enter your magnet link!")
link = input()

handle = lt.add_magnet_uri(ses, link, params)
ses.start_dht()

print ('IndyGod is getting information...')
while (not handle.has_metadata()):
    time.sleep(1)
print ('IndyGod is starting your download...')

while (handle.status().state != lt.torrent_status.seeding):
    s = handle.status()
    state_str = ['queued', 'checking', 'downloading metadata', \
            'downloading', 'finished', 'seeding', 'allocating']
    print ('%.2f%% complete (speed: %.1f kb/s up: %.1f kB/s peers: %d) %s ' % \
            (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
            s.num_peers, state_str[s.state]))
    time.sleep(2)

print(handle.name(), "COMPLETE")
print("™IndyGod™")
