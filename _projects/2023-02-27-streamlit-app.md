---
title: My first web application
subtitle: 'with Streamlit, OpenAI and Notion'
date: 2023-02-27 00:00:00
description: Creating a workout generator through streamlit and APIs to OpenAI and Notion
featured_image: /images/Streamlit/Streamlit_Hero.png
---

# Background
## the Idea
Having the whole month of February off, I took the time to reflect a little on my life. There I thought about the habits that I wanted to take into my upcoming job, and so some of my effort went into conceptualizing a morning routine. At the end of this two and a half hour long routine I am supposed to workout, before heading to work.

So far, I have been very succesful with my routine, but since the routine is compressed of many activites, I have not much time to make up a workout in advance. Though I know what muscle area I will do once I am at the gym, I don't feel inclined to make up an exact workout for that session. And since I don't wanna pay 20€/month for an app, just to do exactly that, I came up with the idea to create a web application that generates a set of exercises for me, which should dictate my workout or at least provide some sort of inspiration for that day.

## the Prototype
At first, I did not consider building a web app, and instead I remembered the [Twilio](https://www.twilio.com/) SMS notifier that I once set up. I liked this option, because it made it possible to send the generated workout to my phone, where it was saved in an SMS. However, there are certain draw backs to Twilio.
- You are given a certain budget for free, whereas every SMS sent consumes some of it.
    - There was only enough budget left for about 30 SMS, until I had to start paying.
- You can only send SMS to phone numbers that have been verified previously.
    - New users, wouldn't be able to receive any workouts until I registered their number, and they clicked the registration link

Furthermore, the prototype was an a python file that I had to run from the terminal of my computer. Hence, I had to remember to run the script before I headed out to the gym.

In short, the usability and scalability was clearly lacking.

## the Alternative
When my girlfriend told me that this project has no use, unless you can generate workouts straight through a smartphone, I had to deploy my project to the web. Django came first to my mind, but since my progress on [Codecademy's Django-course](https://www.codecademy.com/learn/paths/build-python-web-apps-with-django) is currently around 50%, I decided on [Streamlit](https://streamlit.io/), which I came accross through one of [Shashank Kalanithi](https://www.youtube.com/@ShashankData)'s videos, since it is a tool that is much easier to implement without any deeper knowledge on web design and CRUD-methods.

For this project it seemed to be sufficient enough to provide the tools to deploy my workout generator to the web. I think that Streamlit can be a very handy possibility for Data Analysts to quickly deploy a reporting system to outside stakeholders, and so I was keen to learn it.

# Methods
# the Database
Since the usability became one of the KPIs of this project I wanted to have a list of exercises that I was able to change through my phone and laptop, so I was able to not only add new exercises that came to my mind, but more importantly, I could adjust the repetitions

<a id='the-idea'>test</a>


https://github.com/JosefMoosholzer/WorkoutGenerator