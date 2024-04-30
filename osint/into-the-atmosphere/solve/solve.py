#!/usr/bin/env python3
import datetime

# https://en.wikipedia.org/wiki/Snowflake_ID
# https://discord.com/developers/docs/reference#snowflakes
url = "https://cdn.discordapp.com/attachments/225994578258427904/1234925610271248385/Punting_Jelly.mov?ex=66328199&is=66313019&hm=178d140210d08a1576022f55228e37445ad069cd5cd2ef8db9ae2b407a250fbc&"
server_snowflake = int(url.split("/")[4])

# `fromtimestamp` expects timestamps in seconds, not ms
server_timestamp = (server_snowflake >> 22) / 1000
discord_epoch = datetime.datetime(
    year=2015,
    month=1,
    day=1,
    tzinfo=datetime.timezone.utc,
).timestamp()

created_time = datetime.datetime.fromtimestamp(
    discord_epoch + server_timestamp,
    datetime.timezone.utc
).isoformat()

print(created_time)

# or just use https://snowsta.mp/?s=225994578258427904
