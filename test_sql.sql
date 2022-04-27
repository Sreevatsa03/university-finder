use universities;

select c.name as club_name, c.type, u.name as university_name from club as c
	join university as u
		on c.university = u.federal_school_code
	order by university_name;
        
select n.first_name, n.last_name, n.occupation, n.est_net_worth, n.graduating_class, u.name as university_name from notable_alum as n
	join university as u
		on n.university = u.federal_school_code
	order by university_name;
    
select d.name, d.num_students, u.name as university_name from department as d
	join university as u
		on d.university = u.federal_school_code
	order by university_name;
    
    
DELIMITER $$
create trigger update_avg_star_rating
	after insert on review 
    for each row
begin
	declare new_star float;
    select get_avg_star_rating(new.university) into new_star from review;
	update watchlisted_university
		set avg_star_rating = new_star
		where federal_school_code = new.university;
end $$
delimiter ;

call add_to_watchlist("Columbia University", "cool also");
select * from watchlisted_university;