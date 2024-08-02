select count(*) FROM (select moz_bookmarks.title from moz_bookmarks join moz_places where moz_bookmarks.fk = moz_places.id)
select * from moz_placesx;