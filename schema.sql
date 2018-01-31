drop table if exists users;
create table users (
    id integer primary key autoincrement,
    username string unique,
    password string
);
drop table if exists audios;
create table audios (
    id integer primary key autoincrement,
    music_name string unique,
    category string,
    path string
);
drop table if exists preferences;
create table preferences (
    user_id integer,
    audio_id integer,
    primary key (user_id , audio_id),
    foreign key (user_id) references users (id) on delete cascade on update cascade,
    foreign key (audio_id) references audios (id) on delete cascade on update cascade
);
drop table if exists detests;
create table detests (
    user_id integer,
    audio_id integer,
    primary key (user_id , audio_id),
    foreign key (user_id) references users (id) on delete cascade on update cascade,
    foreign key (audio_id) references audios (id) on delete cascade on update cascade
);


