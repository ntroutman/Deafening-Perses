drop table if exists rituals;
create table rituals(
    id integer primary key autoincrement,
    name character(250) not null,
    email character(250) not null,
    create_date timestamp default null,
    occupation character(250) not null,
    location character(250) not null,
    gender character(1) not null,
    rituals_text text not null
)