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