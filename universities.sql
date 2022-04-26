create database universities;
use universities;
create table location (
  state varchar(2) not null,
  city varchar(17) not null,
  population int check (
    population between 0
    and 10000000
  ),
  political_standing varchar(10),
  -- "republican" or "democrat"
  climate_description varchar(1000),
  -- "summer: LOW-HIGH F; winter: LOW-HIGH F"
  primary key (state, city)
);
create table university (
  federal_school_code varchar(6) not null primary key,
  name varchar(60) not null,
  application_fee int check (
    application_fee between 0
    and 1000
  ),
  has_early_application bool,
  tuition int not null check (
    tuition between 0
    and 100000
  ),
  avg_aid_awarded int check (
    avg_aid_awarded between 0
    and 100000
  ),
  avg_SAT int check (
    avg_SAT between 400
    and 1600
  ),
  top_major varchar(60),
  ranking int not null,
  student_body_size int check(
    student_body_size between 0
    and 200000
  ),
  campus_size int check(
    campus_size between 0
    and 30000
  ),
  is_public bool,
  acceptance_rate float not null check(
    acceptance_rate between 0
    and 100
  ),
  state varchar(2) not null,
  city varchar(17) not null,
  foreign key (state, city) references location(state, city) -- define relationship - university "in" location
  on update cascade on delete cascade
);
create table review (
  review_id int auto_increment not null primary key,
  star_rating int check (
    star_rating between 1
    and 5
  ),
  description varchar(1000),
  author varchar(30),
  university varchar(6) not null,
  foreign key (university) references university(federal_school_code) -- define relationship - university "has" review
  on update cascade on delete cascade
);
create table department (
  department_id int auto_increment not null primary key,
  name varchar(60) not null,
  num_students int,
  university varchar(6) not null,
  foreign key (university) references university(federal_school_code) -- define relationship - university "has" department
  on update cascade on delete cascade
);
create table club (
  club_id int auto_increment not null primary key,
  name varchar(60) not null,
  type varchar(30),
  university varchar(6) not null,
  foreign key (university) references university(federal_school_code) -- define relationship - sponsor "donates to" university
  on update cascade on delete cascade
);
create table notable_alum (
  first_name varchar(30) not null,
  last_name varchar(30) not null,
  occupation varchar(30) not null,
  est_net_worth bigint not null check (
    est_net_worth between 0
    and 1000000000000
  ),
  graduating_class year not null,
  university varchar(6) not null,
  primary key (first_name, last_name),
  foreign key (university) references university(federal_school_code) -- define relationship - notable alumn "graduated from" university
  on update cascade on delete cascade
);
create table watchlisted_university (
  federal_school_code varchar(6) not null primary key,
  name varchar(60) not null,
  ranking int not null,
  notes varchar(1000),
  avg_star_rating float,
  foreign key (federal_school_code) references university(federal_school_code) -- define relationship - watchlisted university "is" university
  on update cascade on delete cascade
);