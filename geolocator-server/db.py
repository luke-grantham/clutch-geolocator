#import psycopg2
import psycopg2-binary

conn = psycopg2.connect(host="localhost", port = 5432, database="postgres", user="postgres")

cur = conn.cursor()

cur.execute("""SELECT name FROM gis.states where intptlat='+44.6309071' and intptlon='-089.7093916'""")
query_results = cur.fetchall()
print(query_results)

cur.close()
conn.close()
