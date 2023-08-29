#!/usr/bin/env python
# coding: utf-8

# Q-1 What is flask framework ? What are the advantages of flask framework ?

# Ans-1 Flask is a web framework that provide libraries to build lightwieght web applications in python . It is developed by Armin Ronacher who leads an international group of python enthusiats (POCCO) . It is based on WSGI toolkit and JINJA2 template engine .flask is considered as a micro framework .
# 
# Advantages of flask framework :-
# 
# 1. It is a lightwieght framework that offers hassle-free development.
# 2. It is suitable for small projects .
# 3. offers a built-in development server and fast debugger .
# 4. Easily scalable for the applications .
# 5. Support for secure cookies.

# Q-3 What is APP routing in flask ? Why do we use app routes ?
# 

# Ans-3 APP routing is the technique used to map the specific URL with the associated function intended to perform some task . The latest web frameworks use the routing technique to help users remember application URLs . It is helpful to access the desired page directly without navigating from the home page .
# 
# 
# USES of flask :
# 
# 1. URL Mapping : APP routing allows you to define the relationship between URLs and view functions.
# By using the @app.route() decorator , you can specify which URL patterns should trigger specific functions to genrate the response.
# 
# 2. Handling HTTP Methods : In web development , different HTTP methods like GET ,POST,PUT,DELETE etc , are used to perform different actions on resources . with app routing , you can associate a view function with a specific HTTP method, ensuring that the correct function is called depending on the type of request .

# Q-2 Create a simple flask apllication to display 'Hellow World!!' .Attach the screenshot of the output in jupyter Notebook.

# In[1]:


from flask import flask
app=flask(__name__)

@app.route('/')
def hellow_world():
    retur 'hello world'
    
if __name__=='__main__':
    app.run()


# Q-4 Create a "/welcome" route to display the welcome message "welcome to ABC corporation" and a "/" route to show the following details :
# 
# company Name : ABC Cortporation 
# Location : India
# Contact Details : 999-999-9999

# In[1]:


from flask import flask
app=flask(__name__)

@app.route('/')
def welcome_to_ABC_carporation:
    return 'welcome_to_ABC_carporation'

@app.route('/')
class company:
    def __init__(self ,name ,location ,contact details):
        self.name=name
        self.location=location
        self.contact details=contact details
        
c1=company("ABC Corporation","India",999-999-9999)
print(c1.name)
print(c1.location)
print(c1.contact details)


# Q-5 What function is used in flask for URL  Building ? Write a python code to demonstrate the working of the URL_for() function.

# Ans-5 In flask the function used for url building is called url_for(). The url_for() function takes the endpoint name of the target view function as its first argument and can accept additional keyword arguments that represent the dynamic part of URL pattern . It then returns the URL for the specified jendpoint , including any dynamic values if provided.
# 
# 

# In[2]:


from flask import flask ,url_for

app=flask(__name__)

@app.route('/')
def index():
    return "welcome to the homepage!"

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User:{username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'post ID :{post_id}'

if __name__=='__main__':
    with  app.test_request_context():
        print(url_for('index')) #output:/
        print(url_for('show_user_profile',username='john')) #output:/user/john
        print(url_for('show_post',post_id=123)) #output:/post/123


# In[ ]:




