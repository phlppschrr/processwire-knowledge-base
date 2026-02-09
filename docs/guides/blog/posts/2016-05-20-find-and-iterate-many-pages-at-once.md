# ProcessWire 3.0.19 lets you work with thousands of pages at once

Source: https://processwire.com/blog/posts/find-and-iterate-many-pages-at-once/

## Sections


## ProcessWire 3.0.19 lets you work with thousands of pages at once

20 May 2016 by Ryan Cramer [ 4 Comments](/blog/posts/find-and-iterate-many-pages-at-once/#comments)


## ProcessWire 3.0.19

This week we have something different and wonderful, thanks to our friends at [Avoine](https://www.avoine.fi/)!


### Handling large quantities of pages

At Avoine, they use ProcessWire with really large data sets, often working with groups of 50k pages or more. They really use ProcessWire at the big scale! In fact, many do this, as ProcessWire handles large quantities of pages nicely. But there's no way you are going to fit 50k pages in memory at once, so you have to paginate them, perhaps handling 500 or 1000 at a time, then uncaching them, and loading another set. That can be a little tedious, especially if it's something you have to do regularly.

Avoine (with [sforsman](https://processwire.com/talk/user/2543-sforsman/) and [apeisa](https://processwire.com/talk/user/18-apeisa/)) came up with a solution that enables ProcessWire to load huge quantities of pages at once. Now you can do a page finding operation and retrieve nearly unlimited quantities of pages in a single API call, without need for pagination.


### The new $pages->findMany() method

Because this type of "unlimited find" is a little different under-the-hood, we've put the functionality into a new [$pages->findMany()](../../../full/wire/core/Pages/method-findmany.md) method, rather than making the [$pages->find()](../../../full/wire/core/Pages/method-___find.md) method perform it. The findMany() method works exactly the same way as the find() method except that it returns a PageArray containing pages that aren't actually loaded yet.

Pages returned from findMany() don't actually load until you iterate them or access some property from them. When you do iterate them, like with a `foreach()`, it loads (and unloads) them in groups of about 1000 pages at a time. Though these technical details are completely hidden from view. You can go about using `$pages->findMany()` the same way as you would `$pages->find()`, and simply not worry about the quantity.


### How $pages->findMany() differs from $pages->find()

While these two methods may work exactly the same from the API perspective, they are fundamentally different in terms of what they do behind the scenes. For most page finding operations, you'll still want to use [$pages->find()](../../../full/wire/core/Pages/method-___find.md), because it's technically more efficient for most of the cases you would encounter in developing a website. But if you are dealing with potentially large quantities, and you don't want to place limits on the quantity of returned results, look no further than [$pages->findMany()](../../../full/wire/core/Pages/method-findmany.md).

Down the road, I'd like to find a way for ProcessWire to auto-detect which type of find operation would best suit the case, and automatically choose which method to use, leaving you with just needing to use only `$pages->find()`.


### Where would you use something like this?

One of the likely use cases is when you need to perform some calculation on a huge amount of pages. Like if you had several thousand pages representing orders from a store, and needed to add up the total revenue brought in by all of them. Another case might be generating a site map for a really large site. Yet another case might be performing large data imports. The sky is the limit, this opens up so much new potential.


### Testing things out

Locally, most of the testing was done on a site with a little over 21k pages, and it worked beautifully. The actual find operation that retrieved most of those 21k pages executed in less than one second. That's a lot of pages in very little time! If you tried to do that with a `$pages->find()`, you would have waited for awhile and then ran out of memory.

Finding pages and iterating them are two different things. Pages are loaded in groups as you iterate them, so if you really do need to iterate tens of thousands, or hundreds of thousands of pages, you should still plan on that taking some time. In my test case, while it took less than a second to find 21k pages, it took a good 15 seconds to render those 21k pages "name" field into the output of a website, and there's probably no getting around that. Meaning, if you are using a findMany() to render a giant sitemap, you'll probably still want to cache the output.

I haven't actually bumped the ProcessWire version up to 3.0.19 just yet, as I want to have the folks at Avoine double check that our adaption of their idea and code continues to work as intended in their really large data sets. But once that's confirmed, you'll see the version bumped up. Though if you want to try out this feature now, it is available for download in the latest commits to 3.0.18.

The new `$pages->findMany()` capability is a seemingly magic, mind blowing upgrade to our API. Huge thanks to [Avoine](https://www.avoine.fi/) for this.

Be sure to see the [documentation page for $pages->findMany()](../../../full/wire/core/Pages/method-findmany.md) in the 3.x API reference (which includes an example of it in action), and keep up-to-date with the [ProcessWire Weekly](http://weekly.pw) this weekend!
