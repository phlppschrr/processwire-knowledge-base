# ProcessWire 3.0.59, module updates and more

Source: https://processwire.com/blog/posts/processwire-3.0.59-module-updates-and-more/

## Sections


## ProcessWire 3.0.59, module updates and more

7 April 2017 by Ryan Cramer [ 3 Comments](/blog/posts/processwire-3.0.59-module-updates-and-more/#comments)


## ProcessWire 3.0.59


### Working from dev to master

The latest version of the core dev branch is 3.0.59, and this version brings us one step closer to the new master version. While there aren't any major new features in this version, it does continue with minor bug fixes, tweaks and documentation improvements, consistent with the latest couple of weekly versions.

A big thanks to those that have been helping to test and report issues on GitHub. While there are always things to tweak and adjust, there haven't been any major issues to arise thus far, so if that continues another week it may be that 3.0.60 could be our next master version–we'll have to see how it goes. If you've upgraded an existing installation to the current dev branch and everything works well, we'd like to hear from you too – perhaps just reply here if you get a chance. Thanks again for helping us to test.


### Pro module updates

Several of the Pro modules have had new versions released this week. This includes the following:

- [FormBuilder](/blog/categories/form-builder/) v31
- [ListerPro](/api/modules/lister-pro/) v111
- [ProFields Repeater Matrix](/api/modules/profields/repeater-matrix/) v4
- [ProFields Textareas](/api/modules/profields/textareas/) v7
- [ProFields Multiplier](/api/modules/profields/multiplier/) v11

For details on changes to each of these modules, see the dedicated support boards or changelog files included with each release. For the most part, there aren't major features to announce with these versions, but rather these are maintenance releases that are focused by fixing bugs and making optimizations. Note that new versions are typically released with a beta tag, which we remove a few weeks later.

New versions of [ProCache](/blog/categories/procache/) and [ProFields Table](/api/modules/profields/table/) are also in progress and should be out as soon as this month. [ProDrafts](/api/modules/prodrafts/) is receiving a major update, which is why it's taking a little longer than planned, but wanted to let you know progress continues there as well.


### Working with PW and AWS

This last week I've been collaborating with [Jan VandenHengel](http://peragosolutions.com/) on moving moving several related mission critical ProcessWire installations to run on Amazon Web Services (AWS). You might remember Jan is the one that helped us with our [hosting configuration](/blog/posts/web-hosting-changes-and-server-upgrades/) last year and continues to help us maintain our web server. I know very little about AWS myself, but because these installations are moving to a redundant environment across multiple load balanced servers, my job is to make sure the ProcessWire core side of it works with scalable features provided by AWS that Jan sets up, in addition to getting everything upgraded.

These particular installations have been running ProcessWire for about 10 years, starting with ProcessWire 1.0 back around 2007, and working through the 2.x versions over the years. Though they are still running relatively old versions, with the newest being on 2.6. We're going to try and get them upgraded to the latest, along with updating them to serve assets via Amazon's CloudFront CDN with ProCache. Because the sites are quite large, and the upgrades are major, I'll likely be working on this with Jan for another couple of weeks.

I mention the above for a few reasons. It's a great opportunity to learn about ProcessWire in an environment I've not spent a lot of time with yet (AWS), and it may be an excellent case study opportunity for a future blog post here… I look forward to sharing what I learn. It may also reveal new opportunities for us to optimize for larger and larger scale with the core and with ProCache. Lastly, because I expect this to keep me a bit busy until we finish it, it may temporarily slow me down in other areas for a week or two, but luckily it's all about ProcessWire.

I hope that you all have a great weekend and remember to stop by the [ProcessWire Weekly](http://weekly.pw) for the latest news and updates.
