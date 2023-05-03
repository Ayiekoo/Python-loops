#!/usr/bin/env python
# coding: utf-8

# In[1]:


##### python loops
####### for loop ### executes a block of code repeatedly for each item in a python sequence (tuples, lists)
####### while loop ##### executes a block of code repeatedly while a given condition is true

## for loop ##
flower_types = ['Pnsies', 'Sunflower', 'Pimrose', 'Marigold', 'Baneberry']
for value in flower_types:
    print(value)

    # for each loop in the item in the list is assigned
    # to the value and then printed


# In[2]:


###### the range function
# use range(n) ###### loops a specific number n times
#### produces a series fo values from 0 to a number n-1
######### example; range(5): produces values from 0 to 4, must always be an integer

for number in range(5):
    print(number)


# In[5]:


####### range() function
# we can start, stop and step size: range(start, stop, step)

###### start = start the number rather than default 0
###### stop = number where the iteraction will stop
###### step = the interval of iteraction

for number in range(10, 20, 2):
    print(number)


# In[6]:


#### looping through a list with range() function

for flower in range(len(flower_types)):
    print(flower)
    
# used len() to get the length of list


# In[9]:


########## NESTED FOR LOOPS ######
## example##

rows = 5
# outer loop
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')


# In[11]:


########## NESTED FOR LOOPS ######
## example##

rows = 5
# outer loop
for i in range(1, rows + 1):
    # inner loop
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')
else:
    print('Triangle pattern created')


# In[13]:


##### while loops #####

# initialize loop counter
counter = 0
while counter < 5:
    counter = counter + 1 # incorret count by 1 for each iteraction
    print('Learning python')
print('I am here since the condition is false')


# In[14]:


####### loop control statements; break and continue #####
flower_types = ['Pensies', 'Sunflower', 'Pimrose', 'Marigolds', 'Baneberry']
for value in flower_types:
    if value == 'Pimrose':
        # check if current value is 'Pimrose' if True stop looping
        break
    print(value)
    
    # if you want 'Pimrose' displayed,
    # specify the print(value) before the if condition


# In[15]:


######### break statement #######
# initialize loop counter
counter = 0
while counter < 5:
    counter = counter + 1
    if counter == 3:
        break
    print('Learning python')
print('I am here since the condition is false')


# In[16]:


####### The continue statement ######
flower_types = ['Pensies', 'Sunflower', 'Pimrose', 'Marigolds', 'Baneberry']
for value in flower_types:
    # check if currenrt value is 'Pimrose' if True skip it go to the next item
    if value == 'Pimrose':
        continue
    print(value)


# In[ ]:




