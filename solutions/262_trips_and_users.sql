select
	t.request_at as Day,
	round(avg(case when status = 'completed' then 0 else 1 end), 2) as `Cancellation Rate`
from Users as u
join Trips as t on t.client_id = u.users_id and u.banned = 'No'
where t.request_at >= '2013-10-01' and t.request_at <= '2013-10-03'
group by t.request_at;
