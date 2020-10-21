/* Дана таблица employees всех сотрудников компании. Поля:
full_name TEXT (PK),
position TEXT,
department TEXT.
Напиши запрос, выводящий все отделы, в которых меньше 5 разработчиков (position = 'Software Developer').
*/

SELECT department
FROM employees
WHERE position = 'Software Developer'
GROUP BY department
HAVING COUNT(position) < 5