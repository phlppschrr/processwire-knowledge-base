# ProcessWire 3.0.36 and looking forward

Source: https://processwire.com/blog/posts/processwire-3.0.36-and-looking-forward/

## Sections


## ProcessWire 3.0.36 and looking forward

7 October 2016 by Ryan Cramer [ 0 Comments](/blog/posts/processwire-3.0.36-and-looking-forward/#comments)


## ProcessWire 3.0.36

So far things are going great for our new master version of ProcessWire, version 3.x. This week we continued enjoying our new stable version of ProcessWire 3, with the [latest version](https://github.com/processwire/processwire/) 3.0.36 master. While there aren't any *major* changes in this version relative to the previous, there are a significant number of *minor* additions, tweaks and fixes.

If you [look at our commit log](https://github.com/processwire/processwire/commits/master), it's been fairly busy–there's an entire pagination worth of updates. One thing you'll notice beyond the quantity of updates is that more people appear in the commit logs. This will continue as we follow through with more collaboration in 3.x.

One of our collaborators recently has been Francesco Schwarz. Last week we told you how he's helping us with the new processwire-issues and processwire-requests repositories. Now he is also administering the old issues repository and helping us with a smooth transition from there. He's put a lot of time into this and we really value his expertise. Big thanks to Francesco.


### Version strategy

In our old repository, many of you know that our "dev" branch was often more desirable than our "master" branch, because that's where all the new features went, plus all the fixes and commits related to issue reports. In the new repository, we've also added a "dev" branch this week, but we're going to use it more as a temporary minor-version dev branch rather than a major version dev branch. What we did this week was commit fixes, PRs and updates to this dev branch, and then merged them to the master at the end of the week.

The approach described above is the one we're likely to take more often with the new repository. I'm not suggesting we'll be having new versions on master every week, but we will be having a lot more master versions than before. That being said, we also appreciate all those that want to use the dev branch and help us test out new additions and fixes every week.


### WireMail now supports file attachments

Our [WireMail](../../../full/wire/core/WireMail/index.md) class now has a new [attachment()](../../../full/wire/core/WireMail/method-attachment.md) method that was added by LostKobrakai via a pull request this week. This method enables you to add file attachments to outgoing emails. Note however that while supported by the core WireMail class, it may not yet be supported by 3rd party WireMail modules. However, eventually we are likely to see support for it in those as well. Read more about the new attachment method in the API reference [here](../../../full/wire/core/WireMail/method-attachment.md).


### With 3.x out, what’s next?

With a new stable version of ProcessWire out, we're going to stick close to our issue reports and most updates will be focused on ensuring the rock solid stability of 3.x, even if they may only be minor tweaks. Though it won't be long till we're back to the additions and improvements that these posts so often focus on.

With lots of major goals now accomplished with 3.x, we're going to go back to our roadmap and begin to establish new goals as well. So be on the lookout for roadmap updates in the near future.

I've been reminded this week that our [demo site](http://demo.processwire.com) is antiquated and it's time we did something new with that. After all, the demo site is basically identical to how it was when it launched in 2010. While it's true that the front-end has absolutely nothing to do with ProcessWire, someone new to PW is not going to realize that. It's primarily the front-end that's antiquated, as the back-end is running the latest version of ProcessWire and the site structure is still solid. So we may just focus on rebuilding that front-end. Though we'd also like your feedback to consider whether we should explore going in an entirely different direction for the demo site too.

Now is also a good time for us to get back into revisiting our main site and perhaps moving forward with implementing some of the excellent redesign work that's already been done for it.

Upgrades are also in the works for all of the Pro modules. In addition, the ProFields set of modules will be growing with another interesting new Fieldtype/Inputfield combination in the near future. Hope that you all have a great weekend and enjoy the [ProcessWire Weekly](http://weekly.pw).
