# Tests for your routes go here

"""# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)"""

"""
When we make POST request to add to albums
And: I add title=Voyage, release_year=2022, artist_id=2
Then: I should get a 200 response and confirmation the album has been added
"""

def test_add_album_to_repository(web_client, db_connection):
    db_connection.seed('seeds/music_web_library.sql')
    response = web_client.post('/albums', data = {
        'title': 'Voyage',
        'release_year': '2022',
        'artist_id': '2'
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album created successfully."

    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album(1, Doolittle, 1989, 1)\nAlbum(2, Surfer Rosa, 1988, 1)\nAlbum(3, Waterloo, 1974, 2)\nAlbum(4, Super Trouper, 1980, 2)\nAlbum(5, Bossanova, 1990, 1)\nAlbum(6, Lover, 2019, 3)\nAlbum(7, Folklore, 2020, 3)\nAlbum(8, I Put a Spell on You, 1965, 4)\nAlbum(9, Baltimore, 1978, 4)\nAlbum(10, Here Comes the Sun, 1971, 4)\nAlbum(11, Fodder on My Wings, 1982, 4)\nAlbum(12, Ring Ring, 1973, 2)\nAlbum(13, Voyage, 2022, 2)"
    
def test_get_artists(web_client, db_connection):
    db_connection.seed('seeds/music_web_library.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone"

def test_add_new_artist_is_in_artists(web_client, db_connection):
    db_connection.seed('seeds/music_web_library.sql')
    response = web_client.post('/artists', data = {
        'name':'Wild nothing',
        'genre':'Indie'
        })
    assert response.status_code == 200
    
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"


    