import psycopg2

conn = psycopg2.connect(host="localhost", port = 5432, database="postgres", user="postgres")

cur = conn.cursor()

#lat_lng = (44.6309071,-089.7093916)
lat_lng = (35.6762, 139.6503)

#cur.execute("""SELECT NULLIF(name,'') FROM gis.states where intptlat='+44.6309071' and intptlon='-089.709'""")
cur.execute("SELECT name FROM gis.states where ST_CONTAINS(geom, ST_SetSRID( ST_POINT(" + str(lat_lng[1]) + "," + str(lat_lng[0]) + "), 4326))")
query_results = cur.fetchall()
print(query_results)

cur.close()
conn.close()
