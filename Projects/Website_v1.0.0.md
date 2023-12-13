Title: BryceKeen.com
Date: 2023-12-10 14:32
Category: Project

Just over a year ago I started this project not knowing a single thing about web development. Going from not knowing a thing to now making my first official release (a little arbitrary since I am the only one working on it) it has been quite the big milestone for me. Though to be honest, web development is definitely not my forte. I have made my fair share of mistakes, and learned some important engineering techniques the hard way and will definitely be carrying them over to my next projects. One other thing that I have gained from this project is a new found respect for web developers and touch of annoyance to. As for me though, I think I will be sticking to working with low level systems.

## BryceKeen.com v1.0.0

This website was made from scratch as a project aimed for hosting my different projects and things that are interesting to me. The tools to accomplish this were selected primarily out of ignorance of the realm of web development. Though each tool was added gradually at the time to solve a specific problem. The end result was an unnecessarily complex system. View the code [here on Github](https://github.com/PebPeb/my-website). Now with no further to do I present to you [BryceKeen.com](https://brycekeen.com).

<img class="center" src="{attach}/repo/assets/BryceKeenWebsite.png" style="max-width: 90%;" ></img>

Through a variety of decisions this website has grown to be powered by five major tools in addition to basic HTML, CSS, and Javascript.

1. React
2. Webpack
3. Nodejs
4. Pelican
5. Jinja2

The addition of [React](https://react.dev/) was originally to provide a more object oriented style of programming. You can see some of the big components done with react such as the Navbar and the Home page. Though with react comes the issue of search engine optimization (SEO). Having everything in javascript would require server side rendering if there was any hope for search engines to accurately index the site. This problem was not known until many of the major components were developed, so it was not solved until later.

[Webpack](https://webpack.js.org/) was initially added in as a bundler for the React components. At the time I did not have a full understanding of both React and Webpack and began to include more components into Webpack other than just react. Later as the system grew and more tools were added making the system more complex this became more of an hinderance than a help. With [nodejs](https://nodejs.org/en) being Webpack's primary compiler this made my site heavily dependent on it, for both development and deployment. 

<img class="center" src="{attach}/repo/assets/pelican.png" style="max-width: 70%;" ></img>

As for [Pelican](https://getpelican.com/), it was the last tool to be added to the site. Pelican takes advantage of [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) templates and I was able to leverage them for use outside of Pelican as well. Looking back this probably should have been my primary approach since I ended up going with more of a static site. This also ended up solving my SOE problem. With all the content of the site being static there was no need for a server side rendering of the site.

It was definitely a different challenge for me taking on some web development. Though it is not perfect and I probably learned more of how not to design a website. I am proud of what I was able to accomplish.

## Lessons Learned

- "Is this the simplest solution?" - Asking that question more often maybe would have saved a lot of time and headaches. Though a lot of these issues may have stemmed from my lack of knowledge.
- Planning - Having a better road map initial would probably have solved a lot of the problems encountered earlier on. Along with eliminating some of the unnecessary complexity introduced into the system.
- Tools - Sticking to as few technologies as possible and only adding new tools if necessary. This ended up being the main source of complexity. If I stuck to Python libs like Django, Pelican and Jinja2 it would probably would have reduced complexity.
- In the future I should just use Wordpress (no need to reinvent the wheel).

## Purpose

But why do all this work to build a website? Learn all these lessons and go through so much trouble. Well there are a few things I hope to accomplish from doing all of this.

- Challenge myself and others to learn new things.
- Improve my ability to communicate as an educator.
- Challenge my creativity as an engineer and a presenter.
- Demonstrate **God** through all my work.

Proverbs 14:23 - "In all toil there is profit, but mere talk tends only to poverty"
