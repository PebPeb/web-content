Title: BryceKeen.com
Date: 2023-12-10 14:32
Category: Project

Just over a year ago I started this project not knowing a single thing about web development. Going from not knowing a thing to now making my first official release, (a little arbitrary since I am the only one working on it) it has been quite the milestone for me. Though to be honest, web development is definitely not my forte. I have made my fair share of mistakes, and learned some important engineering techniques the hard way. Which I will definitely be carrying over to my next projects. One other thing that I have gained from this project is a new found respect for web developers along with a touch of annoyance. As for me, I think I will stick to working with low level systems.

## BryceKeen.com v1.0.0

This website was made from scratch as a project aimed for hosting my different projects and things that are interesting to me. The tools to accomplish this were selected primarily out of ignorance of the realm of web development. Though each tool was added gradually to solve a specific problem. The end result was an unnecessarily complex system. You can view the code [here on Github](https://github.com/PebPeb/my-website). Without further ado, I present to you [BryceKeen.com](https://brycekeen.com).

<img class="center" src="{attach}/repo/assets/BryceKeenWebsite.png" style="max-width: 90%;" ></img>

This website started out originally on Wordpress, though through a variety of decisions that quickly changed. From those decisions this website has grown to be powered by five major tools in addition to basic HTML, CSS, and Javascript.

1. React
2. Webpack
3. Nodejs
4. Pelican
5. Jinja2

The addition of [React](https://React.dev/) was originally to provide a more object oriented style of programming. You can see some of the big components done with React such as the navigation bar (*navbar*) and the *home* page. Though with React comes the issue of search engine optimization (SEO). Having everything in Javascript requires server side rendering, if there was any hope for search engines to index the site. This problem was not known until many of the major components were developed. Therefore, it was not solved until later.

[Webpack](https://webpack.js.org/) was initially added in as a bundler for the React components. At the time I did not have a full understanding of both React and Webpack and began to include more components into Webpack than React. Later as the system grew and more tools were added, Webpack started to became more of an hinderance than a help. With [Nodejs](https://Nodejs.org/en) being Webpack's primary compiler this made the site heavily dependent on it, for both development and deployment. 

<img class="center" src="{attach}/repo/assets/pelican.png" style="max-width: 60%;" ></img>

As for [Pelican](https://getpelican.com/), it was the last tool to be added to the site. Pelican takes advantage of [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) templates and I was able to leverage these templates outside of Pelican. Looking back this probably should have been my primary approach since I ended up going with more of a static site. Moving to a static site also ended up solving my SOE problem. With all the content of the site being static there was no need for server side rendering.

It was definitely a different challenge for me taking on some web development. Though it is not perfect, and I probably learned more of how *not* to design a website; I am proud of what I was able to accomplish.

## Lessons Learned

- "Did I find the simplest solution?" - Asking that question more along the way would have saved me some time and headaches. However, a lot of these issues may have stemmed from my lack of knowledge.
- Planning - Having a better road map initial would have solved a lot of the problems I encountered earlier on. It would have also helped with eliminating some of the unnecessary complexity introduced into the system.
- Tools - Sticking to as few technologies as possible and only adding new tools if necessary; this ended up being the main source of complexity. If I stuck to Python libraries like Django, Pelican and Jinja2 it would probably would have reduced complexity.
- In the future I should just use Wordpress (no need to reinvent the wheel).

## Purpose

But why do all this work to build a website, learn all these lessons, and go through so much trouble? Well there are a few overarching goals I hoped to accomplish from doing all of this.

- Challenge myself and others to learn new things.
- Improve my ability to communicate as an educator.
- Challenge my creativity as an engineer and a presenter.
- Demonstrate **God** through all my work.

Proverbs 14:23 - "In all toil there is profit, but mere talk tends only to poverty"
