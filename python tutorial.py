# Factory
    class SongSerializer:
        def serialize(self, song, format):
            serializer = get_serializer(format)
            return serializer(song)


    def get_serializer(format):
        if format == 'JSON':
            return _serialize_to_json
        elif format == 'XML':
            return _serialize_to_xml
        else:
            raise ValueError(format)


    def _serialize_to_json(song):
        payload = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(payload)


    def _serialize_to_xml(song):
        song_element = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_element, 'title')
        title.text = song.title
        artist = et.SubElement(song_element, 'artist')
        artist.text = song.artist
        return et.tostring(song_element, encoding='unicode')