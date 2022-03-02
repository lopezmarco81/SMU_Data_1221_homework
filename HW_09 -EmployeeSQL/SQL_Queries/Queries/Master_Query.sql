--1. List the following details of each employee: employee number, last name, first name, sex, and salary.

Select
	s.emp_no,
	s.salary,
	e.emp_no,
	e.last_name,
	e.first_name,
	e.gender
from
	employees e
	join salaries s on e.emp_no = s.emp_no
order by
	salary desc;

--2. List first name, last name, and hire date for employees who were hired in 1986.
SELECT 
	e.first_name, 
	e.last_name, 
	e.hire_date 
FROM 
	employees e
WHERE 
	extract(year from e.hire_date) = 1986


--3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.
select 
	d.dept_no, 
	d.dept_name, 
	e.emp_no, 
	e.last_name, 
	e.first_name
from 
	departments as d
	join employees as e on d.dept_no = d.dept_no;

--4. List the department of each employee with the following information: employee number, last name, first name, and department name.
Select
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
From
	departments as d
	join employees as e on d.dept_name = d.dept_name;
	
--5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
select
	*
from
	employees
Where 
	first_name = 'Hercules'
	and last_name like 'B&'
order by
	 last_name asc;

--6. List all employees in the Sales department, including their employee number, last name, first name, and department name.


Select 
	d.dept_no,
	d.dept_name,
	e.emp_no,
	e.first_name,
	e.last_name
From
	employees e
	join dept_emp de on e.emp_no = de.emp_no
	join departments d on d.dept_no = de.dept_no
where 
	dept_name = 'Sales'
order by
	e.last_name asc
limit 15 

--7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
Select
	d.dept_no,
	d.dept_name,
	e.emp_no,
	e.last_name,
	e.first_name
From
	employees e
	join dept_emp de on e.emp_no = de.emp_no
	join departments d on d.dept_no = de.dept_no
Where
	d.dept_name = 'Development' 
	or d.dept_name = 'Sales'
order by 
	dept_name desc;
	
From
	employees e
group by
	e.last_name
order by
	num_employees desc;
	
--9. Epilogue
select
	*
from 
	employees
where 
	emp_no = 499942
