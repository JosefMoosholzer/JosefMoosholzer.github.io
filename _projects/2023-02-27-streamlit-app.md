---
title: My first web application
subtitle: 'with Streamlit, OpenAI and Notion'
date: 2023-02-27 00:00:00
description: Creating a workout generator through Streamlit and APIs to OpenAI and Notion
featured_image: /images/Streamlit/Streamlit_Hero.png
---

## Summary - TL;DR
I created a [web application](https://josefmoosholzer-workoutgenerator-app-2ju42h.streamlit.app/) with Streamlit that generates workouts according to some user-inputs. The workout is either generated from the GPT-3 Davinci model through the OpenAI-API or from a Notion-workbook that is also retrieved through an API (Notion). The user has also the option to put in his email address to receive his workout via email, through another API (Google)!
The whole project is written in Python (and some css), and is done to my best abilitites to annotate class-types and docstrings.
You can see the whole project on [Github](https://github.com/JosefMoosholzer/WorkoutGenerator).

# Background
## the Idea
Having the whole month of February off, I took the time to reflect a little on my life. There I thought about the habits that I wanted to take into my upcoming job, and so some of my effort went into conceptualizing a morning routine. At the end of this two and a half hour long routine I am supposed to workout, before heading to the office.

So far, I have been very succesful with my routine, but since the routine is compressed of many activities, I have not much time to make up a workout in advance. Though I know what muscle area I will do once I am at the gym, I don't feel inclined to make up an exact workout for that session. And since I don't wanna pay 20€/month for an app, to just do exactly that, I came up with the idea to create a web application that generates a set of exercises for me, which should dictate my workout or at least provide some sort of inspiration for that day.

## the Prototype
At first, I did not consider building a web app, and instead I remembered the [Twilio](https://www.twilio.com/) SMS notifier that I once set up. I liked this option, because it made it possible to send the generated workout to my phone, where it was saved in an SMS. However, there are certain drawbacks to Twilio.
- You are given a certain budget for free, whereas every SMS sent consumes some of it.
    - There was only enough budget left for about 30 SMSs, until I had to start paying.
- You can only send SMSs to phone numbers that have been verified previously.
    - New users, wouldn't be able to receive any workouts until I registered their number, and they clicked the registration link

![Chatbot GIF](/images/Streamlit/Chatbot.gif)
Furthermore, the prototype was an a python file that I had to run from the terminal of my computer. Hence, I had to remember to run the script before I headed out to the gym.

**In short: the usability and scalability was clearly lacking.**

## the Alternative
When my girlfriend told me that this project has no use, unless you can generate workouts straight through a smartphone, I knew that I had to deploy my project to the web. Django came first to my mind, but since my progress on [Codecademy's Django-course](https://www.codecademy.com/learn/paths/build-python-web-apps-with-django) is currently around 50%, I decided to use since it is a tool that is much easier to implement without any deeper knowledge on web design and CRUD-methods.

For this project it seemed to be sufficient enough to provide the tools to deploy my workout generator to the web. I think that Streamlit can be a very handy possibility for Data Analysts to quickly deploy a reporting system to outside stakeholders, and so I was keen to learn it on the fly.

# Methods
## the Database
Since the usability became one of the KPIs of this project I wanted to have a list of exercises that I was able to change through my phone and laptop, so I not only would be able to add new exercises that came to my mind, but more importantly, I could adjust the intensity of exercises whenever I was at the gym and felt like the workout was too easy or too hard.

Something I have also started using since February is [Notion](https://notion.so), which I have been confronted with many times before, but only recently have fallen in love with it. Luckily for me, Notion turned out to be the perfect fit for listing exercises since it provides an API that enables Python to access my notes in real-time.

The full list of exercises can be found [here](https://dapper-lobe-3ac.notion.site/Workouts-e46955bc195a484087a9c3e7e9f57418) and follows a certain scheme, which lets my python script read in each bullet point and creates an Exercise-object out of it, more on that in <a href="#the-transformation">the next section</a>.

## the Transformation
Since I want my workouts to be flexible and adjust to a given intensity, every exercise is given a function, that takes that said *intensity* as an argument and returns the resulting amount of repetitions and possibly an amount of (extra) weight.

However, such function is not possible to save in a Notion notebook, hence, a one-argument function has to be extracted out of a string, and provided to an Exercise-object. The Exercise-class entails the following.
- A name for the exercise: string
- Number of sets: integer
- The targeted muscle area: self-created Enum-Class
- to_str(intensity)-method returning a string-representation.

The two classes that inherit from the Exercise-class are...
- WeightedExercises; with functions for the range of repetitions and weights
- BodyExercises; with functions for the exact amount of repetitions and possibly extra weights beginning at a higher intensity.

A Workout-class, has a list of Exercise-objects, an intensity, and its string representation. Furthermore, it has also two methods, to increasing / decrease its intensity, though, they won't be used, see <a href="#the-limitations">Limitations</a>.

Anyone who is interested in the details, can have a look at the [git-repo](https://github.com/JosefMoosholzer/WorkoutGenerator).

## the Generation
There are two ways of generating a workout in the web application. 
The first option is through the OpenAI-API, in which a prompt is created out of the parameters, and fed to their **GPT-3 Davinci model**, which, at the time of writing, is the most capable model for text generation, since that's all I need here.  
The other option, and more reliant one is through the creation of workouts based on the Notion-workbook, since it provides consistent repetitions and weights for a given intensity, and has a comprehensive increment through the levels of intensity.

## the Notification
Due to the fact that workouts cannot be saved and retrieved later on again (and the web app really likes to reload itself ASAP, see <a href="#the-limitations">Limitations</a>), I had to provide an option to store the workout in another way. And with the theme of this project to work with APIs, I added a third API to the mix: Google's API.  
This API allows me to sign in with my Google account and send the workouts per email, to whomeever filled in their email before letting a workout being generated.

# Coding
## great Challenge
This project might have been the most complex so far. I created 4 python classes plus an Enum-class, I split my work into 8 python files and one css-file, created a repository in Github and created a virtual environment and a requirements.txt file for it. I had to make sure that my API keys, were stored in a secrets.toml-file, which was listed in my gitignore-file, so things were safe but also worked locally and on the cloud.

## best Practices
For that reason, I created an *UML-ish diagram* on my whiteboard, conceptualizing before coding. Furthermore, I tried my best at annotating types for each and every variable and function possible. I even added docstrings to the more complex functions in the code, which might save me some hours later when I come back to this project.

# Conclusion
## the Limitations
Streamlit seemed to be great for this project, but not perfect. Something I have already been hinting towards in the text above is that with it being a web application, there is no information temporarily stored in the cache. What that means for this project is, that everytime a button is clicked, the app runs completely anew. The information from the Notion-workbook gets (unnecessarily) retrieved again and a new workout is generated, while the old one gets lost. Hence, it is not possible to continue with the current workout (that you might like but find a bit too easy) and, for instance, increase the intensity. 
This also runs into the problem, that you will have to decide whether or not you wanna get the workout to be sent to your email before you even have seen the workout, since it is only possible for the application to sent a workout that was generated in the same run.

So it seems, that I will have to learn Django after all, and I think that's a good sign. But that will take a while...

## Lessons learned
There are many new skills I have learned or refreshed during this project. To list the most important:
- I learned to create my own first web application (as the title might have spoiled).
- I finally had the opportunity to work with websites that provided an API as a refreshing contrast to scraping information with Selenium.
- I improved my understanding of Python classes
- I improved my understanding of working in a virtual environment and commiting to Github
- I learned to write better code with type annotations and docstrings.