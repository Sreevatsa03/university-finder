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
	if not exists (select * from university where (student_body_size >= student_body_size_min and student_body_size <= student_body_size_max)) then
		select "There are no schools that have a student body size within the given range" as message;
	else
		select * from university where (student_body_size >= student_body_size_min and student_body_size <= student_body_size_max);
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
    university_p varchar(60)
)
begin
	declare uni_fsc varchar(6);	
    
    select federal_school_code into uni_fsc from university where name = university_p;
	
	insert into review (star_rating, description, author, university)
    values(star_rating_p, description_p, author_p, uni_fsc);
end $$
DELIMITER ;

# search university
DELIMITER $$
create procedure search_universities
(
	application_fee_min int,
    application_fee_max int,
	tuition_min int,
    tuition_max int,
	avg_aid_awarded_min int,
    avg_aid_awarded_max int,
	avg_SAT_min int,
    avg_SAT_max int,
	ranking_bottom int,
    ranking_top int,
	student_body_size_min int,
    student_body_size_max int,
	campus_size_min int,
    campus_size_max int,
	acceptance_rate_min float,
    acceptance_rate_max float
)
begin
    if not exists (select * from university 
				where (application_fee >= application_fee_min and application_fee <= application_fee_max)
				and (tuition >= tuition_min and tuition <= tuition_max)
				and (avg_aid_awarded >= avg_aid_awarded_min and avg_aid_awarded <= avg_aid_awarded_max)
				and (avg_SAT >= avg_SAT_min and avg_SAT <= avg_SAT_max)
				and (ranking >= ranking_bottom and ranking <= ranking_top)
				and (student_body_size >= student_body_size_min and student_body_size <= student_body_size_max)
				and (campus_size >= campus_size_min and campus_size <= campus_size_max)
				and (acceptance_rate >= acceptance_rate_min and acceptance_rate <= acceptance_rate_max))
	then
		select "There are no schools with these search options in the database." as message;
	else
		select * from university 
			where (application_fee >= application_fee_min and application_fee <= application_fee_max)
            and (tuition >= tuition_min and tuition <= tuition_max)
            and (avg_aid_awarded >= avg_aid_awarded_min and avg_aid_awarded <= avg_aid_awarded_max)
            and (avg_SAT >= avg_SAT_min and avg_SAT <= avg_SAT_max)
            and (ranking >= ranking_bottom and ranking <= ranking_top)
            and (student_body_size >= student_body_size_min and student_body_size <= student_body_size_max)
            and (campus_size >= campus_size_min and campus_size <= campus_size_max)
            and (acceptance_rate >= acceptance_rate_min and acceptance_rate <= acceptance_rate_max);
	end if;
end $$
DELIMITER ;

# search location by city
DELIMITER $$
create procedure search_location_by_city
(
	city_p varchar(60)
)
begin
	if not exists (select l.state, l.city, l.population, l.political_standing, l.climate_description, u.name, u.federal_school_code 
					from location as l join university as u
					on l.state = u.state and l.city = u.city
					where l.city = city_p) then
		select "There are no schools that are located in the given city in the database." as message;
	else 
		select l.state, l.city, l.population, l.political_standing, l.climate_description, u.name , u.federal_school_code 
			from location as l join university as u
            on l.state = u.state and l.city = u.city
            where l.city = city_p;
	end if;
end $$
DELIMITER ;

# search location by state
DELIMITER $$
create procedure search_location_by_state
(
	state_p varchar(2)
)
begin
	if not exists (select l.state, l.city, l.population, l.political_standing, l.climate_description, u.name, u.federal_school_code  
					from location as l join university as u
					on l.state = u.state and l.city = u.city
					where l.state = state_p) then
		select "There are no schools that are located in the given state in the database." as message;
	else 
		select l.state, l.city, l.population, l.political_standing, l.climate_description, u.name, u.federal_school_code  
			from location as l join university as u
            on l.state = u.state and l.city = u.city
            where l.state = state_p;
	end if;
end $$
DELIMITER ;

# search location by city and state
DELIMITER $$
create procedure search_location
(
	city_p varchar(60),
    state_p varchar(2)
)
begin
	if not exists (select l.state, l.city, l.population, l.political_standing, l.climate_description, u.name 
					from location as l join university as u
					on l.state = u.state and l.city = u.city
					where l.city = city_p
                    and l.state = state_p) then
		select "There are no locations in the database with the given city and state" as message;
	else 
		select l.state, l.city, l.population, l.political_standing, l.climate_description, u.name 
			from location as l join university as u
            on l.state = u.state and l.city = u.city
            where l.city = city_p
            and l.state = state_p;
	end if;
end $$
DELIMITER ;

# function that gets the avg star rating of a university
DELIMITER $$
create function get_avg_star_rating
(
	code_p varchar(30)
)
returns int
deterministic
begin
	declare avg_rating float;
    
    select avg(r.star_rating) into avg_rating
		from review as r join university as u
		on r.university = u.federal_school_code
        where r.university = code_p;
	return(avg_rating);
end $$
DELIMITER ;

# trigger that updates average star rating of watchlisted university when review is added
DELIMITER $$
create trigger update_avg_star_rating
	after insert on review 
    for each row
begin
	declare new_avg_rating float;
    select get_avg_star_rating(new.university) into new_avg_rating;
    
	update watchlisted_university
    set avg_star_rating = new_avg_rating
    where federal_school_code = new.university;
end $$
delimiter ;

# add to watchlist by university name
DELIMITER $$
create procedure add_to_watchlist
(
	university_p varchar(30),
    notes_p varchar(1000)
)
begin
	declare uni_fsc varchar(6);
    declare uni_rank int;
    declare avg_star_rating float;
    
    select federal_school_code into uni_fsc from university where name = university_p;
    select ranking into uni_rank from university where name = university_p;
    select get_avg_star_rating(uni_fsc) into avg_star_rating;
    
	insert into watchlisted_university
    values(uni_fsc, university_p, uni_rank, notes_p, avg_star_rating);
end $$
DELIMITER ;

#update the notes of a watchlisted university
DELIMITER $$
create procedure update_notes
(
	university_p varchar(60),
    notes_p varchar(1000)
)
begin
	update watchlisted_university
    set notes = notes_p
    where name = university_p;
end $$
DELIMITER ;

# delete watchlisted university
DELIMITER $$
create procedure remove_from_watchlist
(
	university_p varchar(60)
)
begin
	delete from watchlisted_university where name = university_p;
end $$
DELIMITER ;

#filter reviews based on star rating
DELIMITER $$
create procedure filter_reviews
(
	star_rating_p int
)
begin
	if not exists (select * from review where star_rating = star_rating_p) then
		select "There are no reviews with the given star rating in the database." as message;
	else 
		select * from review where star_rating = star_rating_p;
	end if;
end $$
DELIMITER ;