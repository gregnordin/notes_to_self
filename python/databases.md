# SQLite

## Information

- [Introduction to Python SQL Libraries - realpython](https://realpython.com/python-sql-libraries/)
- [SQLite Tutorial](https://www.sqlitetutorial.net)
    - [SQLite Date & Time](https://www.sqlitetutorial.net/sqlite-date/)
- [SQLAlchemy — Python Tutorial](https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91)
- [Corey Schafer - Python SQLite Tutorial: Complete Overview – Creating a Database, Table, and Running Queries](https://coreyms.com/development/python/python-sqlite-tutorial-complete-overview-creating-database-table-running-queries)
- [sentdex - SQLite3 - Simple Databases with Python](https://www.youtube.com/playlist?list=PLQVvvaa0QuDezJh0sC5CqXLKZTSKU1YNo)


## SQLite software tools

- [sqlite3 command line tool](https://www.sitepoint.com/getting-started-sqlite3-basic-commands/)
- DB Browser for SQLite.app
- [SQLiteStudio](https://github.com/pawelsalawa/sqlitestudio) - Yuk, tried it and didn't like it


# SQLAlchemy

## Information

[Pycon 2020 Talk: Hannah Stepanek - Let's talk Databases in Python: SQLAlchemy and Alembic](https://www.youtube.com/watch?v=36yw8VC3KU8).  
[Slides](https://docs.google.com/presentation/d/1PDFYvNheocsaVLVu4ibqplJTzOuKnkaS_AX3_Mhczmw/edit#slide=id.p).  

- `import sqlalchemy as sa`
- `sa.Index` does what?
- Set up a session context manager. See [this slide](https://docs.google.com/presentation/d/1PDFYvNheocsaVLVu4ibqplJTzOuKnkaS_AX3_Mhczmw/edit#slide=id.g52b1b0b3f2_0_474)
- [Session scoping](https://docs.google.com/presentation/d/1PDFYvNheocsaVLVu4ibqplJTzOuKnkaS_AX3_Mhczmw/edit#slide=id.g52b1b0b3f2_0_493) - *a session should follow the lifecycle of a request*
- Connection Pools are very nice, SQLAlchemy does automatically
    - [How to keep connections alive in Connection Pool](https://docs.google.com/presentation/d/1PDFYvNheocsaVLVu4ibqplJTzOuKnkaS_AX3_Mhczmw/edit#slide=id.g52b1b0b3f2_0_445)
- Querying
- Creating the Database
- Database Migrations - Alembic, allows you to roll back database changes, looks pretty good

Learn how to do joins: [Querying with Joins](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying-with-joins).

- Look at example of creating a specific query with a class at [SqlAlchemy Tutorial - Basic Model, database Creation and Data Load](https://python-forum.io/Thread-SqlAlchemy-Tutorial-Basic-Model-database-Creation-and-Data-Load) (need to scroll down)
- Still not sure what "join" does since filter seems to accomplish the same thing.
- **This looks really helpful**: [Constructing Database Queries with SQLAlchemy](https://hackersandslackers.com/database-queries-sqlalchemy-orm/)

To understand and implement foreign keys and relationships, follow [Working with relationships](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#building-a-relationship).



# peewee

As an alternative to SQLAlchemy, [peewee](http://docs.peewee-orm.com/en/latest/peewee/quickstart.html#) looks very good. It has as reptuation for being simpler than SQLAlchemy. Also, Hua says its search capability is more extensive.


# General Database Information

[Whats is your decision process between CSV, JSON, XML, and SQL &NoSQL database?](https://old.reddit.com/r/learnpython/comments/glbuog/whats_is_your_decision_process_between_csv_json/)

    Generally speaking,
    
    1) how do you decide which file format to use to store data?
    
    2) at what point it's better to use a database?
    
    3) how do you decide when to use SQL database or NoSQL database?
    
    UPDATE: I didnt know I would get so many respond. thank you all and this amazing community.
    

>mooglinux answer:
    
>The universal answer is “It Depends” as unhelpful as that may be at first. Here are some questions it depends on though:
    
>What is the source of the data? If it’s an external source, what format does it come in?
How is the data structured? Is it a hierarchy of objects? A list of uniform records? Is it text or binary?
How do you plan on accessing the data? Does it just need to be read once in a while or will it be continually queried?
What sort of processing do you need to do with it? Are you running data analytics? Performing lookups on individual items? Or do you need to process blobs of binary data such as images?
How much data are you working with? Gigabytes of server logs or a couple megabytes of application settings?
All that said, here are a few guidelines:
    
>Learn basic file types first, because you would be surprised how far you can get with CSV, the configparser module, and pickle. Json is also a great option.
Your default choice for a database should be SQLite, because it’s built-in to the standard library and is quite fast. Don’t move on unless you have a specific reason (for example, if multiple processes will be writing to the database simultaneously)
Relational databases (SQL) should generally be your default when you move up from SQLite. I recommend Postgres.
    “NoSQL” databases are each designed to be better at some specific use cases where more traditional databases used to struggle. They’re specialized tools, so only use one if you know it’s the right tool for your particular application.

