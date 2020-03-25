/*
Querying for the most popular games in the stream
table
*/

SELECT game, count(*)
FROM stream
GROUP BY 1
ORDER BY 2 DESC;

/*
Leaugue of Legends is clearly the highest.
Want to know where the streamers are located
*/

SELECT country, count(*)
FROM stream
WHERE game = 'League of Legends'
GROUP BY 1
ORDER BY 2 DESC;

/*
streamers are mostly located in the US.
Want to assign genres for certain games as
either Multiplayer Online Battle Arena (MOBA),
First Person Shooter (FPS), Survival, and 
Other
*/

SELECT game,
 CASE
  WHEN game = 'Dota 2'
      THEN 'MOBA'
  WHEN game = 'League of Legends' 
      THEN 'MOBA'
  WHEN game = 'Heroes of the Storm'
      THEN 'MOBA'
    WHEN game = 'Counter-Strike: Global Offensive'
      THEN 'FPS'
    WHEN game = 'DayZ'
      THEN 'Survival'
    WHEN game = 'ARK: Survival Evolved'
      THEN 'Survival'
  ELSE 'Other'
  END AS 'genre',
  COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 3 DESC;

/*
Good understanding of the type of games, streamers
and viewers.
Want to understand how the view count changes
over the course of a day for the US, since
it has the highest number of streams
*/

SELECT strftime('%H', time), count(*)
FROM stream
WHERE country = 'US'
GROUP BY 1;

/*
More users on Twitch as the hours get later
into the night but the largest group of
streams are uncategorized and have the hour
missing. People stream between 10am - 11pm
*/