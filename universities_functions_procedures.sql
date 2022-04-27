use universities;

# search by name
DELIMITER $$
create procedure search_by_name
(
	name_p varchar(30)
)
begin
    if not exists (select * from university where name = name_p) then
		select "There are no schools with that name in the database." as message;
	else
		select * from university where name = name_p;
	end if;
end $$
DELIMITER ;

# search by federal_school_code
DELIMITER $$
create procedure search_by_federal_school_code
(
	federal_school_code_p varchar(6)
)
begin
	if not exists (select * from university where federal_school_code = federal_school_code_p) then
		select "There are no schools with that federal school code in the database." as message;
	else 
		select * from university where federal_school_code = federal_school_code_p;
	end if;
end $$
DELIMITER ;

# search by application_fee
DELIMITER $$
create procedure search_by_application_fee
(
	application_fee_min int,
    application_fee_max int
)
begin 
	if not exists (select * from university where (application_fee >= application_fee_min and application_fee <= application_fee_max)) then
		select "There are no schools that have an application fee within the given range" as message;
	else
		select * from university where (application_fee >= application_fee_min and application_fee <= application_fee_max);
	end if;
end $$
DELIMITER ;

# search by has_early_application
DELIMITER $$
create procedure search_by_has_early_application
(
	has_early_application_p bool
)
begin
	if not exists (select * from university where has_early_application = has_early_application_p) then
		select "There are no schools that have the inputted early application option" as message;
	else 
		select * from university where has_early_application = has_early_application_p;
	end if;
end $$
DELIMITER ;

# search by tuition
DELIMITER $$
create procedure search_by_tuition
(
	tuition_min int,
    tuition_max int
)
begin 
	if not exists (select * from university where (tuition >= tuition_min and tuition <= tuition_max)) then
		select "There are no schools that have a tuition within the given range" as message;
	else
		select * from university where (tuition >= tuition_min and tuition <= tuition_max);
	end if;
end $$
DELIMITER ;

# search by avg_aid_awarded
DELIMITER $$
create procedure search_by_avg_aid_awarded
(
	avg_aid_awarded_min int,
    avg_aid_awarded_max int
)
begin 
	if not exists (select * from university where (avg_aid_awarded >= avg_aid_awarded_min and avg_aid_awarded <= avg_aid_awarded_max)) then
		select "There are no schools that award average aid within the given range" as message;
	else
		select * from university where (avg_aid_awarded >= avg_aid_awarded_min and avg_aid_awarded <= avg_aid_awarded_max);
	end if;
end $$
DELIMITER ;

# search by avg_SAT
DELIMITER $$
create procedure search_by_avg_SAT
(
	avg_SAT_min int,
    avg_SAT_max int
)
begin 
	if not exists (select * from university where (avg_SAT >= avg_SAT_min and avg_SAT <= avg_SAT_max)) then
		select "There are no schools that have an average SAT score within the given range" as message;
	else
		select * from university where (avg_SAT >= avg_SAT_min and avg_SAT <= avg_SAT_max);
	end if;
end $$
DELIMITER ;

# search by ranking
DELIMITER $$
create procedure search_by_ranking
(
	ranking_top int,
    ranking_bottom int
)
begin 
	if not exists (select * from university where (ranking >= ranking_bottom and ranking <= ranking_top)) then
		select "There are no schools that rank within the given range" as message;
	else
		select * from university where (ranking >= ranking_bottom and ranking <= ranking_top);
	end if;
end $$
DELIMITER ;

# search by student_body_size
DELIMITER $$
create procedure search_by_student_body_size
(
	student_body_size_min int,
    student_body_size_max int
)
begin 
	if not exists (select * from university where (student_body_size >= student_body_size_min and search_by_student_body_size <= search_by_student_body_size_max)) then
		select "There are no schools that have a student body size within the given range" as message;
	else
		select * from university where (student_body_size >= student_body_size_min and search_by_student_body_size <= search_by_student_body_size_max);
	end if;
end $$
DELIMITER ;

# search by campus_size
DELIMITER $$
create procedure search_by_campus_size
(
	campus_size_min int,
    campus_size_max int
)
begin 
	if not exists (select * from university where (campus_size >= campus_size_min and campus_size <= campus_size_max)) then
		select "There are no schools that have a campus size within the given range" as message;
	else
		select * from university where (campus_size >= campus_size_min and campus_size <= campus_size_max);
	end if;
end $$
DELIMITER ;

# search by is_public
DELIMITER $$
create procedure search_by_is_public
(
	is_public_p bool
)
begin
	if not exists (select * from university where is_public = is_public_p) then
		select "There are no schools that are the inputted type of university" as message;
	else 
		select * from university where is_public = is_public_p;
	end if;
end $$
DELIMITER ;

# search by acceptance_rate
DELIMITER $$
create procedure search_by_acceptance_rate
(
	acceptance_rate_min float,
    acceptance_rate_max float
)
begin 
	if not exists (select * from university where (acceptance_rate >= acceptance_rate_min and acceptance_rate <= acceptance_rate_max)) then
		select "There are no schools that have a campus size within the given range" as message;
	else
		select * from university where (acceptance_rate >= acceptance_rate_min and acceptance_rate <= acceptance_rate_max);
	end if;
end $$
DELIMITER ;

# search by state
DELIMITER $$
create procedure search_by_state
(
	state_p varchar(2)
)
begin
	if not exists (select * from university where state = state_p) then
		select "There are no schools that are located in the given state in the database." as message;
	else 
		select * from university where state = state_p;
	end if;
end $$
DELIMITER ;

# search by city
DELIMITER $$
create procedure search_by_city
(
	city_p varchar(60)
)
begin
	if not exists (select * from university where city = city_p) then
		select "There are no schools that are located in the given city in the database." as message;
	else 
		select * from university where city = city_p;
	end if;
end $$
DELIMITER ;

# write a review
DELIMITER $$
create procedure write_review
(
	star_rating_p int,
    description_p varchar(1000),
    author_p varchar(30),
    university_p varchar(6)
)
begin
	insert into review (star_rating, description, author, university)
    values(star_rating_p, description_p, author_p, university_p);
end $$
DELIMITER ;


-- drop procedure search_by_name;
-- drop procedure search_by_federal_school_code;

-- SAMPLE DATA
-- insert into location values("NJ", "Princeton", 31000, "democratic", "summer: 59-85 F; winter: 21-50 F");
-- insert into university values("002627", "Princeton University", 70, TRUE, 56010, 61928, 1505, "computer science", 1, 5321, 600, FALSE, 5.6, "NJ", "Princeton");

-- delete from university where name = "Princeton University";

-- call search_by_name("Princeton University");

-- call search_by_federal_school_code("002627");

-- call search_by_campus_size(100, 300);


