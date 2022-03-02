select
	e.emp_no,
	e.first_name,
	e.last_name,
	d.dept_name
from 
	employees e
	join dept_manager dm on e.emp_no = dm.emp_no
	join departments d on d.dept_no = dm.dept_no;




