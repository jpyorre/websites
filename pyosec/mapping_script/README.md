Get LAT and LON for any new locations I present at:
https://www.latlong.net/convert-address-to-lat-long.html

Then add that to the file joshtravel.txt.

Then run python update_map.py.

When done, copy map.html into the pyosec/content/extra/ dir

From the pyosec directory, run pelican content -s pelicanconf.py -t ./bootstrap2/

Upload the files.