--List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
select
	*
from
	employees
Where 
	first_name = 'Hercules'
	and last_name like 'B&'
order by
	 last_name asc;

	