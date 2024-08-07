# SQL Commands Reference

## Querying Data

### Query Data in Columns
```sql
SELECT c1, c2 FROM t;
```

### Query All Rows and Columns
```sql
SELECT * FROM t;
```

### Query Data and Filter Rows with a Condition
```sql
SELECT c1, c2 FROM t WHERE condition;
```

### Query Distinct Rows
```sql
SELECT DISTINCT c1 FROM t WHERE condition;
```

### Sort the Result Set
```sql
SELECT c1, c2 FROM t ORDER BY c1 ASC [DESC];
```

### Skip Offset of Rows and Return the Next n Rows
```sql
SELECT c1, c2 FROM t ORDER BY c1 LIMIT n OFFSET offset;
```

### Group Rows Using an Aggregate Function
```sql
SELECT c1, aggregate(c2) FROM t GROUP BY c1;
```

### Filter Groups Using HAVING Clause
```sql
SELECT c1, aggregate(c2) FROM t GROUP BY c1 HAVING condition;
```

## Querying from Multiple Tables

### Inner Join t1 and t2
```sql
SELECT c1, c2 FROM t1 INNER JOIN t2 ON condition;
```

### Left Join t1 and t2
```sql
SELECT c1, c2 FROM t1 LEFT JOIN t2 ON condition;
```

### Right Join t1 and t2
```sql
SELECT c1, c2 FROM t1 RIGHT JOIN t2 ON condition;
```

### Full Outer Join
```sql
SELECT c1, c2 FROM t1 FULL OUTER JOIN t2 ON condition;
```

### Produce a Cartesian Product of Rows
```sql
SELECT c1, c2 FROM t1 CROSS JOIN t2;
```

### Another Way to Perform Cross Join
```sql
SELECT c1, c2 FROM t1, t2;
```

### Join t1 to Itself Using INNER JOIN
```sql
SELECT c1, c2 FROM t1 A INNER JOIN t1 B ON condition;
```

## Using SQL Operators

### Combine Rows from Two Queries
```sql
SELECT c1, c2 FROM t1 UNION [ALL] SELECT c1, c2 FROM t2;
```

### Return the Intersection of Two Queries
```sql
SELECT c1, c2 FROM t1 INTERSECT SELECT c1, c2 FROM t2;
```

### Subtract a Result Set from Another Result Set
```sql
SELECT c1, c2 FROM t1 MINUS SELECT c1, c2 FROM t2;
```

### Query Rows Using Pattern Matching
```sql
SELECT c1, c2 FROM t1 WHERE c1 [NOT] LIKE pattern;
```

### Query Rows in a List
```sql
SELECT c1, c2 FROM t WHERE c1 [NOT] IN (value_list);
```

### Query Rows Between Two Values
```sql
SELECT c1, c2 FROM t WHERE c1 BETWEEN low AND high;
```

### Check if Values in a Table Are NULL
```sql
SELECT c1, c2 FROM t WHERE c1 IS [NOT] NULL;
```

## Managing Tables

### Create a New Table with Three Columns
```sql
CREATE TABLE t (
    id INT PRIMARY KEY,
    name VARCHAR NOT NULL,
    price INT DEFAULT 0
);
```

### Delete the Table
```sql
DROP TABLE t;
```

### Add a New Column to the Table
```sql
ALTER TABLE t ADD column;
```

### Drop Column
```sql
ALTER TABLE t DROP COLUMN c;
```

### Add a Constraint
```sql
ALTER TABLE t ADD constraint;
```

### Drop a Constraint
```sql
ALTER TABLE t DROP constraint;
```

### Rename a Table
```sql
ALTER TABLE t1 RENAME TO t2;
```

### Rename a Column
```sql
ALTER TABLE t1 RENAME COLUMN c1 TO c2;
```

### Remove All Data in a Table
```sql
TRUNCATE TABLE t;
```

## Using SQL Constraints

### Set c1 and c2 as a Primary Key
```sql
CREATE TABLE t(
    c1 INT, c2 INT, c3 VARCHAR,
    PRIMARY KEY (c1, c2)
);
```

### Set c2 Column as a Foreign Key
```sql
CREATE TABLE t1(
    c1 INT PRIMARY KEY,
    c2 INT,
    FOREIGN KEY (c2) REFERENCES t2(c2)
);
```

### Make Values in c2 Unique
```sql
CREATE TABLE t(
    c1 INT, c2 INT,
    UNIQUE(c2, c3)
);
```

### Ensure c1 > 0 and Values in c1 >= c2
```sql
CREATE TABLE t(
    c1 INT, c2 INT,
    CHECK(c1 > 0 AND c1 >= c2)
);
```

### Set Values in c2 Column as NOT NULL
```sql
CREATE TABLE t(
    c1 INT PRIMARY KEY,
    c2 VARCHAR NOT NULL
);
```

## Modifying Data

### Insert One Row into a Table
```sql
INSERT INTO t(column_list) VALUES (value_list);
```

### Insert Multiple Rows into a Table
```sql
INSERT INTO t(column_list) VALUES (value_list), 
       (value_list), ...;
```

### Insert Rows from t2 into t1
```sql
INSERT INTO t1(column_list) SELECT column_list FROM t2;
```

### Update New Value in Column c1 for All Rows
```sql
UPDATE t SET c1 = new_value;
```

### Update Values in Columns c1, c2 That Match the Condition
```sql
UPDATE t SET c1 = new_value, 
              c2 = new_value
WHERE condition;
```

### Delete All Data in a Table
```sql
DELETE FROM t;
```

### Delete Subset of Rows in a Table
```sql
DELETE FROM t WHERE condition;
```

## Managing Views

### Create a New View
```sql
CREATE VIEW v(c1, c2) AS SELECT c1, c2 FROM t;
```

### Create a New View with Check Option
```sql
CREATE VIEW v(c1, c2) AS SELECT c1, c2 FROM t
WITH [CASCADED | LOCAL] CHECK OPTION;
```

### Create a Recursive View
```sql
CREATE RECURSIVE VIEW v AS
select-statement -- anchor part
UNION [ALL]
select-statement; -- recursive part
```

### Create a Temporary View
```sql
CREATE TEMPORARY VIEW v AS SELECT c1, c2 FROM t;
```

### Delete a View
```sql
DROP VIEW view_name;
```

## Managing Indexes

### Create an Index on c1 and c2 of the t Table
```sql
CREATE INDEX idx_name ON t(c1, c2);
```

### Create a Unique Index on c3, c4 of the t Table
```sql
CREATE UNIQUE INDEX idx_name ON t(c3, c4);
```

### Drop an Index
```sql
DROP INDEX idx_name;
```

## Managing Triggers

### Create or Modify a Trigger
```sql
CREATE OR MODIFY TRIGGER trigger_name
WHEN EVENT
ON table_name
TRIGGER_TYPE
EXECUTE stored_procedure;
```

*WHEN*
- `BEFORE` – invoke before the event occurs
- `AFTER` – invoke after the event occurs

*EVENT*
- `INSERT` – invoke for INSERT
- `UPDATE` – invoke for UPDATE
- `DELETE` – invoke for DELETE

*TRIGGER_TYPE*
- `FOR EACH ROW`
- `FOR EACH STATEMENT`

### Delete a Specific Trigger
```sql
DROP TRIGGER trigger_name;
```

