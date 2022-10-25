---
title: 'A reminder that documentation benefits the author the most.'
subtitle: 'Note to myself: Start documenting your work!'
date: 2022-10-25 00:00:00
description: My painful journey towards understanding the importance of documenting my workflow.
featured_image: '/images/BlogHeros/Doggo.jpg'
---

# Regret
I am currently at the midst of writing the documentation about the work I have been doing for the past 20 months at my working-student job.

Having done tidious tasks that always got delegated to working students, for the beginning of my occupation, were not worthy of a documentation. Not only because I automated the biggest task there was (see [Price Research project](/project/price-research)), but also for the lack of longevity and complexity, that would have made a documentation necessary for others to pick up on my previous work.

But with time I proved my Excel skills to my boss. From smaller twists, like a dynamic calendar that defined days as working and non-working days according to a list of holidays, to bigger tweaks &#151; trimming down the fact-table of last years' sales to 1/4 of the original size by aggregating entries by month, dealer, and product type before loading it into the data model.

I did most of these things in a single workday, after coming up with the idea. So, why would I need to write these things down? It can't be that complex, right...?  
Well, this is where the problem started. With my boss gaining confidence in my abilities, he let go of our central reporting file (Excel) and delegated the responsibility onto me &#151; I finally I was assigned a bigger task!  
When the reporting file needed a new functionality or something wasn't working, it was, for the most part, outsourced. I was included in the meetings where my boss defined the requirements, but for the most part I was struggling. Not only did I had to catch up on the structure of the file and the tools it used (PowerQuery, PowerPivot, and VBA) but also on the field knowledge and sales structure. Hence, when I got that file assigned I tried to understand every little detail of it. My conclusion: it's a big f&#8727;&#8727;&#8727;&#8727;&#8727;&#8727; mess.
* nomenclature was inconsistent
* some queries & connections existed which were not necessary/used
* measures were written inefficently
* occasionally wrong calculations or falsely copied/dragged formulas to other cells
* etc. etc.

Nonetheless, I quickly made the outsourcing obsolete. This had as a consequence that colleagues quickly realized that the file could easily be improved or extended by telling me to do so. So did my boss, but he knew that the file's size and working memory increased. And with the database's unreliability increasing as we reached the end of the fiscal year I carried the bag of trash just over the finish line.  

My new year's resolution: build the reporting file from ground up. And so I did. With my master thesis' deadline being in February, I gave myself the four weeks of January, before I headed into vacation to finish my masters program.

But with all that time pressure, I left one crucial thing undone.
Documenting my work.
I felt the pain of undocumented work, not only from taking over the project, but also when I decided to rebuild the file I sometimes could not recall my thought process for the features I, myself, implemented since then.

I was the primary victim of my own lack of documentation. Nonetheless, back then, I did not feel the need to change my workflow accordingly.

# Realization
The realization did not come until a few months back, when I read ***The Mythical Man Month*** by Frederick P. Brooks, where a whole chapter is dedicated to documentation. He cites
> "By documenting a design, the designer exposes himself to the criticisms of everyone, and he must be able to defend everything he writes. If the organizational structure is threatening in any way, nothing is going to be documented until it is completely defensible" -  John Cosgrove, 1971

Which perfectly describes the situation I found myself in during January. Eager to improve upon the previous file. I started to get my hands dirty right away, instead of taking a step back and thinking profoundly about the underlying data model, data sets, structure & **design** of the file.

Luckily, I had the older file as a comparable model on how (not) to do it and I constantly received feedback from my boss who kept me on the right track.
But even with the file finally set and done, from time to time the necessity for minor adjustments makes me go back (e.g. PowerQuery) to parts of my code, and it takes some minutes before I know where I need to change something.

With all that said, as a conclusion I will list the benefits and cons that come to my mind about documentation, so that this concept becomes ingrained into my workflow.
## Benefits
* Makes the undertaken measures clear to everyone.
* Co-workers can retrieve information from the docs (less E-Mails).
* Co-workers can learn from the docs (even less E-Mails, or maybe more 🙃)
* Every step is reflected once more.
* Lack of knowledge or concept has to be resolved.
* You can easily pick up from where you left last time.
* You have proof of your work.
* You don't struggle explaining how you did something (important during meetings with stakeholders).
* Only a worthy design is implemented, and can therefore save you from dropping hours of workload.

## Cons
* The design has to constantly proof itself worthy.
* Higher workload for more trivial things.
* Not the most fun part of coding/building.