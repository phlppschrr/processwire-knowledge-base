# ProcessWire 2.6.21 upgrades comments + more on PW 3.x

Source: https://processwire.com/blog/posts/processwire-2.6.21-upgrades-comments-more-on-pw-3.x/

## Sections


## ProcessWire 2.6.21 upgrades comments + more on PW 3.x

23 October 2015 by Ryan Cramer [ 14 Comments](/blog/posts/processwire-2.6.21-upgrades-comments-more-on-pw-3.x/#comments)


## ProcessWire 2.6.21

This week work continued on ProcessWire 2.7. We fixed several minor issues as reported in GitHub issue reports. This week we also added a new feature that users of the comments field might be interested in… ProcessWire 3.0 made a lot of progress this week too!


### New star ratings for comments fields

This week we upgraded the core comments field to support a 5-star rating system that can accompany each comment. This is something that's been requested a few times, and it tied in directly with client work in progress this week, so it found its way into the core.

When enabled, anyone submitting a comment can choose to rate the subject they are commenting on using a 1-5 star scale. This is likely to be used in instances where you are using the comments field for reviews, as opposed to just blog comments. Though I've enabled the star ratings here so you can try them out (scroll to the bottom and leave a comment). Or for an example with better context, check out the comments for a bike tour on Tripsite like [this one](https://www.tripsite.com/bike/tours/around-lake-constance/#comments) where I've left a comment as an example. Special thanks to [Tripsite bike tours](https://www.tripsite.com) for sponsoring this new feature.

To enable the 5-star rating system for your own comments, upgrade to the latest ProcessWire (2.6.21)* and in your admin go to Setup > Fields > your comments field, and click the "Details" tab. Scroll down to the field "Use star ratings?" and enable it from there. You can choose to make star ratings optional or required.

*If you want the star ratings system but are using the current stable PW 2.6.1 master, you can always just replace your /wire/modules/Fieldtype/FieldtypeComments/ files with those from PW 2.6.21, as there are no other dev branch dependencies for this particular new feature.


### More updates on ProcessWire 3.0

In addition to preparing ProcessWire 2.6.21, much of the time this week went towards continuing work on ProcessWire 3.0. This week the focus was on multi-instance support and I'm glad to say we are now there–hopefully! Though I'm not going to suggest you start testing it out just yet, as I need to do a lot more testing here before I take up your time. But in initial tests here, multi-instance support is working well and I'm able to successfully have multiple PW installs talk to each other while running from the same core.

We will definitely be using the new multi-instance system here to make our currently-separate processwire.com, modules.processwire.com, cheatsheet.processwire.com sites talk to each other and share data. Once I've spent more time in testing here, I'll follow-up in a future post with some practical examples, as well as code examples of how you can try it out yourself too.

The rest of this gets into the technical details of how it works–the stuff I love to talk about, but that I know probably isn't that interesting to most. So if you aren't interested, feel free to skip this next part. But if you are a module developer, you may want to read on to learn a little more about how you can also support multi-instance in your modules.

Achieving multi-instance support involved changing the entire manner in which ProcessWire's API variables work. In ProcessWire 2.x, API variables use a static container that is shared among all objects descended from the Wire class. For that reason, you could only ever have one instance of ProcessWire available to the API. In ProcessWire 3.x, we've switched to a dependency injection system. API variables are now injected to each newly created object when appropriate. Meaning, you could have multiple Page instances in memory, wired to different ProcessWire instances.


### Multi-instance with 3rd party modules and PW 3.x

These will enable your modules to be able to support multi-instance too:

By the way, the old `wire()` procedural function (without $this before it) that you may have used, is still there in 3.x. But because it exists out of the object/instance scope, it can only refer to the last accessed ProcessWire instance. It is just fine to use it in your template files, as PW notifies wire() what the instance is going to be before rendering a template file. But when in the scope of a module or an object, the non-procedural version `$this->wire()` is preferable. Though that's already been the case in 2.x too.

Hope you have a great weekend and remember to visit the [ProcessWire weekly](http://weekly.pw).
