#!/usr/bin/env python
# coding: utf-8

# # Quistion-22
# 
# In a jupyter notebook solve the following question using both python and SQL. Please upload the notebook to GitHub and provide the link submission box below.
# 

# | Column Name   | Type    |
# |---------------|---------|
# | id            | int     |
# | recordDate    | date    |
# | temperature   | int     |

# id is the column with unique values for this table.
# This table contains information about the temperature on a certain day.
#  
#  
# 
# Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
# 
# Return the result table in any order.
# 
# Please use the following input Weather table for your solution. To receive full marks you will need to create the database, create the table, insert the data below and execute the SQL query.
# 
#  Input: 
# Weather table:
# 

# | id | recordDate | temperature |
# |----| -----------|-------------|
# | 1  | 2015-01-01 | 10          |
# | 2  | 2015-01-02 | 25          |
# | 3  | 2015-01-03 | 20          |
# | 4  | 2015-01-04 | 30          |

# Output: 

# 
# | id |
# |----|
# | 2  |
# | 4  |
# 

# 
# Explanation: 
# In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
# In 2015-01-04, the temperature was higher than the previous day (20 -> 30).

# In[27]:


import sqlite3

# Creating the database 
conn = sqlite3.connect('weather_data.db')
cur = conn.cursor()


# In[28]:


# Deleting if the table already exists
cur.execute('''DROP TABLE IF EXISTS Weather''')

# Creating the table
cur.execute('''
    CREATE TABLE Weather (
        id INTEGER PRIMARY KEY,
        recordDate DATE,
        temperature INTEGER)
        ''')


# In[29]:


given_data = [
    (1, '2015-01-01', 10),
    (2, '2015-01-02', 25),
    (3, '2015-01-03', 20),
    (4, '2015-01-04', 30)
]

# Inserting the data into the table
cur.executemany('INSERT INTO Weather (id, recordDate, temperature) VALUES (?, ?, ?)', given_data)
conn.commit()


# In[30]:


# Defining the SQL query to solve the problem
query = '''
        SELECT w1.id
        FROM Weather w1
        JOIN Weather w2 ON DATE(w1.recordDate) = DATE(w2.recordDate, '+1 day')
        WHERE w1.temperature > w2.temperature
        '''

cur.execute(query)

# Printing the SQL Query results
rows = cur.fetchall()
print("id")
for row in rows:
    print(row[0])
    
# Closing the database connection
conn.close()

