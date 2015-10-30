from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
post = Table('post', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('body', VARCHAR(length=140)),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
    Column('about_me', VARCHAR(length=140)),
    Column('email', VARCHAR(length=120)),
    Column('last_seen', DATETIME),
    Column('nickname', VARCHAR(length=64)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=64)),
    Column('email', String(length=120)),
    Column('about_me', String(length=140)),
    Column('last_seen', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].columns['about_me'].drop()
    pre_meta.tables['post'].columns['email'].drop()
    pre_meta.tables['post'].columns['last_seen'].drop()
    pre_meta.tables['post'].columns['nickname'].drop()
    post_meta.tables['user'].columns['about_me'].create()
    post_meta.tables['user'].columns['last_seen'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].columns['about_me'].create()
    pre_meta.tables['post'].columns['email'].create()
    pre_meta.tables['post'].columns['last_seen'].create()
    pre_meta.tables['post'].columns['nickname'].create()
    post_meta.tables['user'].columns['about_me'].drop()
    post_meta.tables['user'].columns['last_seen'].drop()
