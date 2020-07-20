# Learn from SQLBolt

Website: [SQLBolt](https://sqlbolt.com)

## Lessons

[SQL Lesson 6: Multi-table queries with JOINs](https://sqlbolt.com/lesson/select_queries_with_joins) 

    SELECT column, another_table_column, …
    FROM mytable
    INNER JOIN another_table 
        ON mytable.id = another_table.id
    WHERE condition(s)
    ORDER BY column, … ASC/DESC
    LIMIT num_limit OFFSET num_offset;
    
    
>Depending on how you want to analyze the data, the INNER JOIN we used last lesson might not be sufficient **because the resulting table only contains data that belongs in both of the tables**.


[SQL Lesson 7: OUTER JOINs](https://sqlbolt.com/lesson/select_queries_with_outer_joins)

    SELECT column, another_column, …
    FROM mytable
    INNER/LEFT/RIGHT/FULL JOIN another_table 
        ON mytable.id = another_table.matching_id
    WHERE condition(s)
    ORDER BY column, … ASC/DESC
    LIMIT num_limit OFFSET num_offset;
    
>Like the INNER JOIN these three new joins have to specify which column to join the data on.
When joining table A to table B, a LEFT JOIN simply includes rows from A regardless of whether a matching row is found in B. The RIGHT JOIN is the same, but reversed, keeping rows in B regardless of whether a match is found in A. Finally, a FULL JOIN simply means that rows from both tables are kept, regardless of whether a matching row exists in the other table.

>When using any of these new joins, you will likely have to write additional logic to deal with NULLs in the result and constraints (more on this in the next lesson).


[SQL Lesson 8: A short note on NULLs](https://sqlbolt.com/lesson/select_queries_with_nulls)

    SELECT column, another_column, …
    FROM mytable
    WHERE column IS/IS NOT NULL
    AND/OR another_condition
    AND/OR …;
    
[SQL Lesson 9: Queries with expressions](https://sqlbolt.com/lesson/select_queries_with_expressions)

    SELECT particle_speed / 2.0 AS half_particle_speed
    FROM physics_data
    WHERE ABS(particle_position) * 10.0 > 500;

    SELECT col_expression AS expr_description, …
    FROM mytable;
    
    SELECT column AS better_column_name, …
    FROM a_long_widgets_table_name AS mywidgets
    INNER JOIN widget_sales
      ON mywidgets.id = widget_sales.widget_id;
      

[SQL Lesson 10: Queries with aggregates (Pt. 1)](https://sqlbolt.com/lesson/select_queries_with_aggregates)

    Select query with aggregate functions over all rows:
    SELECT AGG_FUNC(column_or_expression) AS aggregate_description, …
    FROM mytable
    WHERE constraint_expression;
    
>Without a specified grouping, each aggregate function is going to run on the whole set of result rows and return a single value. And like normal expressions, giving your aggregate functions an alias ensures that the results will be easier to read and process.

>Grouped aggregate functions

>In addition to aggregating across all the rows, you can instead apply the aggregate functions to individual groups of data within that group (ie. box office sales for Comedies vs Action movies).
This would then create as many results as there are unique groups defined as by the GROUP BY clause.

    Select query with aggregate functions over groups:
    SELECT AGG_FUNC(column_or_expression) AS aggregate_description, …
    FROM mytable
    WHERE constraint_expression
    GROUP BY column;

>The GROUP BY clause works by grouping rows that have the same value in the column specified.

[SQL Lesson 11: Queries with aggregates (Pt. 2)](https://sqlbolt.com/lesson/select_queries_with_aggregates_pt_2)

>One thing that you might have noticed is that if the GROUP BY clause is executed after the WHERE clause (which filters the rows which are to be grouped), then how exactly do we filter the grouped rows?

>Luckily, SQL allows us to do this by adding an additional HAVING clause which is used specifically with the GROUP BY clause to allow us to filter grouped rows from the result set.

    Select query with HAVING constraint:
    SELECT group_by_column, AGG_FUNC(column_expression) AS aggregate_result_alias, …
    FROM mytable
    WHERE condition
    GROUP BY column
    HAVING group_condition;

>The HAVING clause constraints are written the same way as the WHERE clause constraints, and are applied to the grouped rows.

[SQL Lesson 12: Order of execution of a Query](https://sqlbolt.com/lesson/select_queries_order_of_execution)

    Complete SELECT query:
    SELECT DISTINCT column, AGG_FUNC(column_or_expression), …
    FROM mytable
        JOIN another_table
          ON mytable.column = another_table.column
        WHERE constraint_expression
        GROUP BY column
        HAVING constraint_expression
        ORDER BY column ASC/DESC
        LIMIT count OFFSET COUNT;

>Not every query needs to have all the parts we listed above, but a part of why SQL is so flexible is that it allows developers and data analysts to quickly manipulate data without having to write additional code, all just by using the above clauses.

[SQL Topic: Subqueries](https://sqlbolt.com/topic/subqueries)

>You might have noticed that even with a complete query, there are many questions that we can't answer about our data without additional post, or pre, processing. In these cases, you can either make multiple queries and process the data yourself, or you can build a more complex query using SQL subqueries.

>A subquery can be referenced anywhere a normal table can be referenced. Inside a FROM clause, you can JOIN subqueries with other tables, inside a WHERE or HAVING constraint, you can test expressions against the results of the subquery, and even in expressions in the SELECT clause, which allow you to return data directly from the subquery.
>
>Because subqueries can be nested, each subquery must be fully enclosed in parentheses in order to establish proper hierarchy. Subqueries can otherwise reference any tables in the database, and make use of the constructs of a normal query


# SQLAlchemy

## Left outer join

- [How to execute “left outer join” in SqlAlchemy](https://stackoverflow.com/questions/26142304/how-to-execute-left-outer-join-in-sqlalchemy)

        q = session.query(Table1.field1, Table1.field2)\
            .outerjoin(Table2)\ # use for cases in which you have relationship defined
            .filter(Table2.tbl2_id == None)

- Another example using `group_by` and `sum`

        # This assumes a relationship where Table2.date_id is tied to
        # Table1.id using sa.relationship and foreign key
        q = session.query(Table1.date, Table1.field2, sa.func.sum(Table2.field1))\
            .outerjoin(Table2)\
            .group_by(Table2.date)

## Get equivalent SQL command

Create the query without actually executing it:

    q = session.query(Main.date, Main.weight, Main.calories_eaten, 
                      sa.func.sum(Exercise.calories_burned)) \
            .outerjoin(Exercise) \  # Left outer join because of table relationship
            .group_by(Main.date)

Get equivalent SQL command:

    print(str(q))
    # Output:
        SELECT main.date AS main_date, main.weight AS main_weight, main.calories_eaten AS main_calories_eaten, sum(exercise.calories_burned) AS sum_1 
        FROM main LEFT OUTER JOIN exercise ON main.id = exercise.date_id GROUP BY main.date
    # Reformatted:
        SELECT main.date AS main_date, 
           main.weight AS main_weight, 
           main.calories_eaten AS main_calories_eaten, 
           sum(exercise.calories_burned) AS sum_1 
        FROM main 
        LEFT OUTER JOIN exercise 
            ON main.id = exercise.date_id 
        GROUP BY main.date