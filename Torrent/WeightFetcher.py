import libtorrent as lt
import time

ses = lt.session()
ses.listen_on(6881, 6891)

params = {
    'save_path': '/content/data',
    'storage_mode': lt.storage_mode_t(2),
    'paused': False,
    'auto_managed': True,
    'duplicate_is_error': True}

link = "MAGNET LINK OF THE FILE ON TORRENT NETOWORK"
handle = lt.add_magnet_uri(ses, link, params)
ses.start_dht()

print "Dowlaoding Metadata..."

while (not handle.has_metadata()):
    time.sleep(1)
    
print "Meta Data Received, Start Downloading Weights..."
while (handle.status().state != lt.torrent_status.seeding):
    s = handle.status()
    state_str = ['queued', 'checking', 'downloading metadata', 'downloading', 'finished', 'seeding', 'allocating']
    print '%.2f%% Complete (Down: %.1f kb/s Up: %.1f kB/s Peers: %d) %s' % \
            (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
            s.num_peers, state_str[s.state])
    time.sleep(5)
