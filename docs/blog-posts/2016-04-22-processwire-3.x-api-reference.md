# The New ProcessWire 3.x API Reference

Source: https://processwire.com/blog/posts/processwire-3.x-api-reference/

## Sections


## The New ProcessWire 3.x API Reference

22 April 2016 by Ryan Cramer [ 12 Comments](/blog/posts/processwire-3.x-api-reference/#comments)

This week I've got to keep it a little brief because I've been so caught up in this weeks' updates that I've run out of time to write much in this blog post! The updates this week are not actually to the core code, but rather to the API reference documentation for ProcessWire 3.x. There's lots more work to do still, but I definitely have a good start, so going to introduce it here in this post.


### Introducing the ProcessWire 3.x API Reference Documentation

**[Here is the ProcessWire 3.x API reference documentation](../api-full/index.md)**. Currently all of the API variables are covered, but the individual classes (like WireData, WireArray, etc.) and non-API variable modules have not yet been covered–that'll be next week.

Please take a look around, there's a lot of new stuff here. Not new stuff in terms of code or functionality, but rather new stuff in terms of documentation coverage. Many API methods include detailed code examples, comprehensive options lists, and more. Hookable methods also get their own section that shows you how to hook the method, what the arguments are that you can hook, and examples of how to do so.


### Something unique about this API reference

I've always struggled a bit to keep our existing API reference documentation fully up-to-date with the actual code. It's a matter of time and resources. That will no longer be a problem. This API reference is actually powered by a module built this week (ProcessWireAPI) that pulls all the documentation directly from the core code itself. It does this using a combination of PHP's Reflection classes, manual parsing of phpdoc comments, custom hash tags, and example blocks that have been added to the core.

What this means is that the documentation will always be fully up-to-date with the core version that processwire.com is running on. Or if we wanted to have different versions of the documentation, we'd just let each version run off of different versions of the core. The entire API reference (hundreds to thousands of URLs) is powered by one single page in the system, and none of the documentation content is coming from content stored in ProcessWire–just in the actual PHP code of the core source.

It also means that the source code documentation in core files is going to be getting a lot more comprehensive, since it's now powering the actual API reference documentation. This week I've re-written huge amounts of the documentation present in the core source code, which you'll see committed to the devns branch next week. Though you'll see that already powering the 3.x API reference linked above.


### What about the cheatsheet?

Part of the reason I wanted to get the API reference powered by a module, is so that there could be an API to the API. :) Meaning, we'll be able to use the ProcessWireAPI's module API to display API reference material in the cheatsheet. Though the cheatsheet already has a lot of good content, so we'll try to find a way to make sure that all the good features and content already in the cheatsheet remain, while taking advantage of the ProcessWireAPI module to ensure everything is always up-to-date. Basically, the cheatsheet is one of our most important resources, so all of this is kind of planned around that.


### What else is coming for the API reference documentation?

Right now the API reference documentation focuses largely on the API variables. But there's a lot more to cover, especially in terms of other ProcessWire classes (like WireArray, WireData, and dozens of others). Technically, the API reference documentation can display information for any PW class already. But I'm trying to avoid linking to those classes until I've gone through and curated each one, like was done for the API variables this week.

By curating, I mean making sure the content is as high quality as it can be, as opposed to just being informal developer comments in the code. Curating also means figuring out what's important and what's not, and making sure that largely "internal" stuff doesn't get in the way of the more important stuff. It also means grouping things in a logical manner that make sense for documentation. Basically, it's a lot of work, but really worthwhile I think.

The API documentation obviously needs a bit more navigationally in terms of UI too, so that'll be coming as well. Though since we're going to get back to our redesign soon, we probably won't focus too much on look and feel of the API reference until we're in the process of the overall site redesign.

With this weeks' updates the intention is to bring our API documentation up to the level of the API that it covers. Next week I hope to finish re-writing documentation for most of the remaining classes. Hope that you all have a great weekend and see you at the [ProcessWire Weekly](http://weekly.pw)!
