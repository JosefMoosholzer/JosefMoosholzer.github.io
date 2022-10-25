---
title: 'Note to myself: Start documenting your work!'
date: 2022-10-25 00:00:00
description: A reminder that documentation benefits the author the most.
featured_image: '/images/Doggo.jpg'
---

# Regret
I am currently at the midst of writing the documentation about the work I have been doing for the past 20 months at my working-student job.  
Having done tidious tasks, that always got delegated to working students, for the beginning of my occupation were not worthy of a documentation. Not only because I automated the biggest task (see [Price Research project](/project/price-research)) there was, but also for the lack of longevity and complexity, that would have made a documentation necessary for others to pick up on my previous work.  
But with time I proved my Excel skills to my boss. From smaller twists, like a dynamic calendar that defined days as working and non-working days according to a list of holidays, to bigger tweaks - trimming down the fact_table of last years' sales to 1/4 of the original size by aggregating entries by month, dealer, and product type before loading it into the data model.  
I did most of these things in a single workday, after coming up with the idea. So, why would I need to write these things down? It can't be that complex, right...?  
Well, this is where the problem started. With my boss gaining confidence in my abilities, he let go of our central reporting file and delegated the responsibility onto me - I finally I was assigned a bigger task! The reporting file was for the most part outsourced when it needed a new functionality or something wasn't working. I was included in the meetings where my boss defined the requirements, but for the most part I was struggling. Not only did I had to catch up on the structure of the file and the tools it used (PowerQuery and PowerPivot by the way) but also on the field knowledge and chain of sales. Hence, when I got that file assigned I tried to understand every little detail of it. My conclusion: it's a big f****** mess.
* nomenclature was inconsistent
* queries & connections existed which were not necessary
* measures were written inefficently
* wrong calculations here and there
* etc. etc.

Nonetheless, I quickly made the outsourcing obsolete. This had as a consequence that colleagues quickly realized that the file could easily be improved or extended by telling me to do so. So did my boss, but he knew that the file's size and working memory increased. And with the database's unreliability increasing as we reached the end of the fiscal year I carried the bag of trash just over the finish line.  

My new year's resolution: build the reporting file from ground up. And so I did. With my master thesis' deadline being in February, I gave myself the four weeks of January, before I headed into vacation to finish my masters program.

But with all that time pressure, I left one crucial thing undone.
### Documenting my work.

## Benefits

This page is a demo that shows everything you can do inside portfolio and blog posts.

We've included everything you need to create engaging posts about your work, and show off your case studies in a beautiful way.

**Obviously,** we’ve styled up *all the basic* text formatting options [available in markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

You can create lists:

* Simple bulleted lists
* Like this one
* Are cool

And:

1. Numbered lists
2. Like this other one
3. Are great too

You can also add blockquotes, which are shown at a larger width to help break up the layout and draw attention to key parts of your content:

> “Simple can be harder than complex: You have to work hard to get your thinking clean to make it simple. But it’s worth it in the end because once you get there, you can move mountains.”

The theme also supports markdown tables:

| Item                 | Author        | Supports tables? | Price |
|----------------------|---------------|------------------|-------|
| Duet Jekyll Theme    | Jekyll Themes | Yes              | $49   |
| Index Jekyll Theme   | Jekyll Themes | Yes              | $49   |
| Journal Jekyll Theme | Jekyll Themes | Yes              | $49   |

And footnotes[^1], which link to explanations[^2] at the bottom of the page[^3].

[^1]: Beautiful modern, minimal theme design.
[^2]: Powerful features to show off your work.
[^3]: Maintained and supported by the theme developer.

You can throw in some horizontal rules too:

---

### Image galleries

Here's a really neat custom feature we added – galleries:

<div class="gallery" data-columns="3">
	<img src="/images/demo/demo-portrait.jpg">
	<img src="/images/demo/demo-landscape.jpg">
	<img src="/images/demo/demo-square.jpg">
	<img src="/images/demo/demo-landscape-2.jpg">
</div>

Inspired by the Galleries feature from WordPress, we've made it easy to create grid layouts for your images. Just use a bit of simple HTML in your post to create a masonry grid image layout:

```html
<div class="gallery" data-columns="3">
    <img src="/images/demo/demo-portrait.jpg">
    <img src="/images/demo/demo-landscape.jpg">
    <img src="/images/demo/demo-square.jpg">
    <img src="/images/demo/demo-landscape-2.jpg">
</div>
```

*See what we did there? Code and syntax highlighting is built-in too!*

Change the number inside the 'columns' setting to create different types of gallery for all kinds of purposes. You can even click on each image to seamlessly enlarge it on the page.

---

### Image carousels

Here's another gallery with only one column, which creates a carousel slide-show instead.

A nice little feature: the carousel only advances when it is in view, so your visitors won't scroll down to find it half way through your images.

<div class="gallery" data-columns="1">
	<img src="/images/demo/demo-landscape.jpg">
	<img src="/images/demo/demo-landscape-2.jpg">
</div>

### What about videos?

Videos are an awesome way to show off your work in a more engaging and personal way, and we’ve made sure they work great on our themes. Just paste an embed code from YouTube or Vimeo, and the theme makes sure it displays perfectly:

<iframe src="https://player.vimeo.com/video/148003889" width="640" height="360" frameborder="0" allowfullscreen></iframe>

---

## Pretty cool, huh?

We've packed this theme with powerful features to show off your work.

Why not put them to use on your new portfolio?

<a href="https://jekyllthemes.io/theme/personal-website-jekyll-theme" class="button button--large">Get This Theme</a>