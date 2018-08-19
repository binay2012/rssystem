
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table


engine = create_engine('postgresql://postgres:123456@localhost/RSSystems')
metadata = MetaData()
print(metadata.tables)

metadata.reflect(bind=engine)
# print(metadata.tables)
# print conn.bookratings.query.all()
# rates = Base.bookratings.query.all()
# print rates

print metadata.tables