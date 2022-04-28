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
    
call search_universities(0, 75, 0, 60000, 50000, 100000, 1450, 1600, 1, 10, 0, 10000, 0, 300, 0, 10);

select * from university where name = "Northwestern University";

DELETE FROM watchlisted_university WHERE name = "Columbia University";
select * from watchlisted_university;
    
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

call add_to_watchlist("Northwestern University", "another great school");
select * from watchlisted_university;

select r.star_rating, r.description, r.author, r.university, u.name from review as r
join university as u
on r.university = u.federal_school_code
order by university;








