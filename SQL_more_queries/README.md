# SQL - More queries

SQL scripts that practice users, privileges, constraints and foreign keys on a MySQL server.

- `0-privileges.sql`: script that lists the privileges of user_0d_1 and user_0d_2
- `1-create_user.sql`: script that creates user_0d_1 with all privileges
- `2-create_read_user.sql`: script that creates the database hbtn_0d_2 and the read-only user user_0d_2
- `3-force_name.sql`: script that creates the table force_name with a name that cannot be null
- `4-never_empty.sql`: script that creates the table id_not_null with a default id
- `5-unique_id.sql`: script that creates the table unique_id with a unique id
- `6-states.sql`: script that creates the database hbtn_0d_usa and the table states
- `7-cities.sql`: script that creates the table cities with a foreign key to states
- `8-cities_of_california_subquery.sql`: script that lists the cities of California with a subquery
- `9-cities_by_state_join.sql`: script that lists all cities with the name of their state
- `10-genre_id_by_show.sql`: script that lists the shows that have at least one genre
- `11-genre_id_all_shows.sql`: script that lists all shows, with NULL when there is no genre
- `12-no_genre.sql`: script that lists the shows without a genre
- `13-count_shows_by_genre.sql`: script that lists the genres with the number of shows linked to each
- `14-my_genres.sql`: script that lists the genres of the show Dexter
- `15-comedy_only.sql`: script that lists all Comedy shows
- `16-shows_by_genre.sql`: script that lists all shows with their genres, NULL if none
