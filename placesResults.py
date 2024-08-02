import sqlite3

def placesResults(searchfor=''):

    sql = f'''
    select mb.title, mp.url
    from moz_places as mp
    join moz_bookmarks as mb
    on mb.fk = mp.id
    where mb.title like '%{searchfor}%'
    --where moz_bookmarks.title not null
    --order by mb.title
    limit 10 offset 100
    '''
    print(sql)
    
    con = sqlite3.connect('places.sqlite')
    cur = con.cursor()
    results = cur.execute(sql)
    return results.fetchall()

