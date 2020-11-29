select e.emp_no, e.last_name, e.first_name, e.sex, s.salary
from employees as e
inner join salaries as s on 
e.emp_no = s.emp_no;

select e.first_name, e.last_name, e.hire_date
from employees as e
where e.hire_date between '1985-12-31' and '1987-01-01';

select d.dept_no, d.dept_name, e.emp_no, e.last_name, e.first_name
from departments as d
inner join dept_manager as dm on 
d.dept_no = dm.dept_no
inner join employees as e on
dm.emp_no = e.emp_no;

select e.emp_no, e.last_name, e.first_name, d.dept_name 
from departments as d
inner join dept_emp as de on 
d.dept_no = de.dept_no
inner join employees as e on
de.emp_no = e.emp_no;

select e.first_name, e.last_name, e.sex
from employees as e
where e.first_name='Hercules' and e.last_name like 'B%';

select e.emp_no, e.last_name, e.first_name, d.dept_name 
from departments as d
inner join dept_emp as de on 
d.dept_no = de.dept_no
inner join employees as e on
de.emp_no = e.emp_no
where d.dept_name='Sales';

select e.emp_no, e.last_name, e.first_name, d.dept_name 
from departments as d
inner join dept_emp as de on 
d.dept_no = de.dept_no
inner join employees as e on
de.emp_no = e.emp_no
where d.dept_name='Sales' or d.dept_name='Development';

select last_name, count(last_name) 
from employees
group by last_name
order by last_name desc;