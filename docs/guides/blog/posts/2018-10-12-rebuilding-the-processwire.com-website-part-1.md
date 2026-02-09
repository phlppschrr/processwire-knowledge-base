# Rebuilding the ProcessWire.com website (part 1)

Source: https://processwire.com/blog/posts/rebuilding-the-processwire.com-website-part-1/

## Sections


## Rebuilding the ProcessWire.com website (part 1)

12 October 2018 by Ryan Cramer [ 7 Comments](/blog/posts/rebuilding-the-processwire.com-website-part-1/#comments)

This week I shifted gears and started working on the new ProcessWire.com site finally. It's hard to believe it is already just about mid October, the year sure has gone fast. Over the coming weeks I'll be focusing on both the next core master version and continuing development on the new ProcessWire.com site. In this post, I'll tell you a little bit about the plans for the new website. Some of this might change as things move forward, but here's what I know so far.


### Starting fresh

In the new version of the website, I've started with a fresh copy of the database, rather than continuing to build upon the original site database that we're still using (which is now eight years old). A lot of the site structure is going to change and I just thought it'd be cleaner to develop it from the ground up this time around. ProcessWire's page export/import tools make this relatively simple. Rather than using MyISAM (DB engine) and UTF8 (DB charset), we'll be using InnoDB and UTF8MB4 this time around.

We'll be starting with all of PW's multi-language modules installed. This will enable us to support parts of the site in additional languages, as translation resources become available. This will reduce or exclude the need for maintaining separate alternate-language sites for ProcessWire.


### Strategy and framework

The new site uses markup regions for the template file development strategy, along with the Uikit 3 front-end framework. (Uikit 3 is now beyond beta and at release candidate #19). This is similar to the “Regular” site profile that's currently included with the PW core. On the CSS side, we're using SCSS. The new site is being developed as something that can be shared as a site profile, with a limited subset of the content. Given that, I haven't felt the need to have the design all figured out, and am instead focusing more on structure, site map and content.


### Design

For now the design emphasizes consistency with the existing brand while applying most of the focus towards optimizing the content presentation. It is likely to evolve as we go, so not yet ready to post screenshots just yet. The look/feel at this stage is familiar relative to the current site, and to some extent, the Reno and Uikit admin themes. Even at this stage, the new site design is subjectively quite a bit more modern and clean than the current site. (The existing site has been great for us, but it is starting to show its age). In developing it as a site profile that can be shared, it's likely the look will evolve once some of the more skilled designers in our community work with it—I'm hopeful there may be interest. Modifying the look/feel of the profile does not require maintaining and compiling a custom version of Uikit, though you certainly can if it is your preference. If you are comfortable working with the “Regular” site profile, you'll be comfortable working with the new PW site profile. Though I should mention the new site profile looks nothing like the Regular site profile.


### Inside out

When possible I prefer to develop websites from the inside-out. By that I mean focus on the inside (the meat of the content), fully understand that and get it right, then work outwards, eventually finishing with the homepage. In doing this I find there is less ambiguity about what direction the homepage should take, better understanding of the content, more clarity on what's possible, more opportunity for code reusability, less speculation time, and a stronger result. It also tends to encourage a quality and attention to detail that remains consistent whether viewing a page deep in the site, or viewing the homepage. That's the plan for the new ProcessWire.com site, and eventual homepage. Which is to stay, there's not yet been tangible focus on the homepage, because it comes later. This is another area where I'm also hoping we can all benefit from the expertise of the skilled designers in our community when the time comes.


### Related sites

ProcessWire.com is actually a few sites, including the main site, the forum, the modules directory, the developer directory, the cheatsheet and others. By developing the new site as a profile that can be shared, this will simplify adaptation into the other related sites, with the biggest being the modules directory. Speaking of the modules directory, it likely won't be re-built from the ground up like the main site, but it will undergo a major refresh once the new design is fully worked out and the main site has been updated.

That's all I've got for this week, but I'll continue adding more detail every week as this project moves further along. Next week, ProcessWire 3.0.117 should be ready on the dev branch as well. Thanks for reading, have a great weekend, and be sure to check out the [ProcessWire Weekly](http://weekly.pw) for the latest ProcessWire news and updates.
