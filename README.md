# Twitch

For this project I worked with two datasets described below. I used SQLite to query certain data from these datasets explained in SQLiteScript. I plotted the query results using Matplotlib and Pandas in Python. The code for this is found in PythonScript.

[Twitch.tv](www.twitch.tv) is the world's leading video platform and community where millions of people and thousands of interests collide in a beautiful explosion of video games, pop culture, and conversation.

- [x] [`stream.csv`](stream.csv)  
- [x] [`chat.csv`](chat.csv)  

The `stream.csv` has the following fields:

Headers | Description |
--- | --- |
`time` | date and time (YYYY-MM-DD HH:MM:SS)
`device_id` | device ID
`login` | login ID
`channel` | streamer name
`country` | country name abbreviation
`player` | streamed device
`game` | game name
`stream_format` | stream quality
`subscriber` | is the viewer a subscriber? (true/false)

The `chat.csv` has the following fields:

Headers | Description |
--- | --- |
`time` | date and time (YYYY-MM-DD HH:MM:SS)
`device_id` | device ID
`login` | login ID
`channel` | streamer name
`country` | country name abbreviation
`player` | chat device
`game` | game name

---

