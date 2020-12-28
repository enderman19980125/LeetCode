create table Person
(
    Id    int,
    Email varchar(255)
);

Truncate table Person;
insert into Person (Id, Email)
values ('1', 'john@example.com');
insert into Person (Id, Email)
values ('2', 'bob@example.com');
insert into Person (Id, Email)
values ('3', 'john@example.com');

DELETE
FROM Person
WHERE Id NOT IN (
    SELECT Id
    FROM (SELECT MIN(Id) AS Id
          FROM Person
          GROUP BY Email
         ) AS T
);
