from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
post = Table('post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('body', String(length=140)),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
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
    post_meta.tables['post'].columns['about_me'].create()
    post_meta.tables['post'].columns['email'].create()
    post_meta.tables['post'].columns['last_seen'].create()
    post_meta.tables['post'].columns['nickname'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['post'].columns['about_me'].drop()
    post_meta.tables['post'].columns['email'].drop()
    post_meta.tables['post'].columns['last_seen'].drop()
    post_meta.tables['post'].columns['nickname'].drop()
