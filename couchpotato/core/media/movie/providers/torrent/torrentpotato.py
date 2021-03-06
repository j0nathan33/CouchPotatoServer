from couchpotato.core.helpers.encoding import tryUrlencode
from couchpotato.core.helpers.variable import getIdentifier
from couchpotato.core.logger import CPLog
from couchpotato.core.media._base.providers.torrent.torrentpotato import Base
from couchpotato.core.media.movie.providers.base import MovieProvider

log = CPLog(__name__)

autoload = 'TorrentPotato'


class TorrentPotato(MovieProvider, Base):

    def buildUrl(self, media, host):
        arguments = tryUrlencode({
            'user': host['name'],
            'passkey': host['pass_key'],
            'imdbid': getIdentifier(media),
        })
        return '%s?%s' % (host['host'], arguments)
