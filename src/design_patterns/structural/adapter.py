

class AudioPlayer:
    
    @staticmethod
    def play(media_type, file_name):
        '''
        By default can play mp3-s, if the <media_type> is 
        something else, will delegate it to MediaAdapter
        '''
        media_type = (media_type or '').lower()
        if media_type == 'mp3':
            print('playing MP3: "%s"' % file_name)
        elif not MediaAdapter.play(media_type, file_name):
            print('Unrecognized format, failed to play: "%s"' % file_name)
        


class MediaAdapter:
    
    @staticmethod
    def play(media_type, file_name):
        media_type = (media_type or '').lower()
        if media_type == 'mp4':
            player = MP4Player()
            player.play(file_name)
            return True
        elif media_type == 'flac':
            player = FLACPlayer()
            player.play(file_name)
            return True
        
        return False
            
            
class MP4Player():
    
    def __init__(self):
        pass  # some initializing
    
    def play(self, file_name):
        print('playing MP4: "%s"' % file_name)
    

class FLACPlayer():
    
    def __init__(self):
        pass  # some initializing
    
    def play(self, file_name):
        print('playing FLAC: "%s"' % file_name)
    
            
if __name__ == '__main__':
    player = AudioPlayer()
    player.play('mp3', 'banana.mp3')
    player.play('mp4', 'mango.mp3')
    player.play('FLAC', 'haha.flac')
    player.play('avi', 'no way.avi')
            
