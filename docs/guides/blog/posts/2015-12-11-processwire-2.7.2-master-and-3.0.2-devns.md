# ProcessWire 2.7.2 master and 3.0.2 devns

Source: https://processwire.com/blog/posts/processwire-2.7.2-master-and-3.0.2-devns/

## Sections


## ProcessWire 2.7.2 master and 3.0.2 devns

11 December 2015 by Ryan Cramer [ 2 Comments](/blog/posts/processwire-2.7.2-master-and-3.0.2-devns/#comments)

This week we don't have any major new features to introduce to you, but we do have two new ProcessWire versions! Plus we have a look at what's coming in the weeks ahead.


### ProcessWire 2.7.2 (master)

ProcessWire 2.7.2 has been merged to the master branch. This version contains several minor fixes and tweaks relative to the previous 2.7.1 master. There aren't any new features per-se, but rather just a lot of minor issue fixes that surfaced in the last two weeks. More details on specifics can be found in master branch [commit log](https://github.com/ryancramerdesign/ProcessWire/commits/master).


### ProcessWire 3.0.2 (devns)

Like the 2.7.2 version, this one doesn't introduce any new features, but contains several optimizations to what was already there. This version also migrates all the minor fixes and tweaks that appear on the 2.7.2 master into the 3.x branch. There were also a couple of optimizations made to the file compiler, further improving the scenarios that it can handle.

Some improvements were made to the front-end page editor to handle cases where editable content contained links, or was contained entirely in a link. Previously you couldn't double click on that content, because it would just load the link. However, now it can differentiate between single and double click to identify whether you intend to follow the link or edit the content contained within it. We've also added a dedicated [front-end documentation page](/api/modules/front-end-editing/), which currently contains roughly what was in last week's blog post, but will continue to be expanded with more information and API reference.

Rather than continuing to refer to 3.x as alpha-[n] versions, we're now just going to be referring to it as the 3.x or devns branch. We'll also be incrementing the version number like we've done with the master and dev branches. By the time 3.x is the new master, we'll probably be in to 3.0.23 or something like that. :)

I'm now using 3.x in multiple production sites and feeling confident that it's more stable than the "alpha" tag would imply, which is in part why I've dropped that tag in this weeks' version. I'm not suggesting you should start using it in production yet though. But if you are starting a new site in development, and not dependent upon many 3rd party modules, you might consider starting with 3.x. There's also the benefit that you can switch between 2.x and 3.x very easily since their underlying database schema is identical.


### What’s coming up next

In the coming weeks we'll be continuing to focus on ensuring that the 2.7.x master is as perfect as possible and covering any issue reports that appear. Unlike with past major versions of ProcessWire, we're not working towards a next major 2.x version, so the 2.7 master branch is likely to stay current within 1-2 weeks of the 2.7 dev branch, with any fixes and tweaks finding their way to the master branch a lot more quickly than in the past. Most of the experimental stuff and new features will instead happen on the 3.x branch. Last week's introduction of the front-end page editing is just one example.

As we get near the end of the year, I've also got a lot of client work to wrap up and clear off my desk. Thankfully, all of it is ProcessWire related. Developing ProcessWire is my favorite thing to do, but developing sites and applications within it is my second favorite. :) I've always felt that it's really important to be a major user of software that you develop, so I try to keep one hand in client work (that uses ProcessWire) whenever possible. I'm mentioning this because I may have to slow down for a couple weeks on the scope of these posts and introduction of new things while I help to launch a couple of new client sites, but will be back full steam ahead once we get through the holidays!

Finalizing and releasing ProDrafts should happen in early January. We're really excited about this module!

Thanks for reading and remember to read the [ProcessWire Weekly](http://weekly.pw) this weekend.
