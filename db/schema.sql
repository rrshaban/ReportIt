drop table if exists complaints;
create table complaints (
  id integer primary key autoincrement,
  lat float(10,6) not null,
  lon float(10,6) not null,
  email text not null,
  cat1 text not null,
  cat2 text not null,
  description text not null,
  notify boolean not null,
  city text not null,
  country text not null,
  pic_url text not null
);


