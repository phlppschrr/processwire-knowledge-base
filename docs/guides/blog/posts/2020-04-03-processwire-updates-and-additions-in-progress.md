# ProcessWire updates and additions in progress

Source: https://processwire.com/blog/posts/processwire-updates-and-additions-in-progress/

## Sections


## ProcessWire updates and additions in progress

3 April 2020 by Ryan Cramer [ 3 Comments](/blog/posts/processwire-updates-and-additions-in-progress/#comments)

This week we’ve got a few new and interesting core updates in progress, though none quite ready to release just yet. So rather than releasing version 3.0.154 today, I thought we'd instead take a brief look at what’s coming over the next few weeks…


### Expanded file and image field properties

ProcessWire’s file and image fields consider the files they store to be the source of properties like width, height, file size (bytes) and such. Meaning, this information is not stored in the database and is instead obtained directly from the files on the file system. That makes it quite efficient in that there’s no overlap or redundancy in duplicating information.

While this setup is efficient, there are also some drawbacks. This information obtained from the files can’t be easily searched the way everything else in ProcessWire is. For instance, we can’t currently do things like find all pages that have an image at least 1000 pixels wide and 600 pixels tall (or some other dimensions you choose). Nor can we tell which images are portrait or landscape (or some aspect ratio) without loading the page and accessing the images. When it comes to storage, we can’t move our assets to some other file storage system (like S3) since PW needs direct file system access to the files in order to know anything about their size or dimension.

Given all of this, I’ve been working on improving our file and image fields so that properties like file size, dimensions, aspect ratio and variations become properties of the file fields that are stored in the database. That way the information can be searched with the page finder, and it can be accessed and queried without needing to hit the file system. Not only does this have search and performance benefits, but it also means it’ll open the door to supporting more asset storage options.

This is a capability that will be rolled out in parts because it’s not something that can be just turned on and off. In order to store the information in the first place, it needs to load all those pages and access all their files. It might be something that takes some time to do on an existing large site. So what I’m looking to do in the short term is just have PW start to maintain and store the information as files are uploaded and/or pages are saved, ensuring its presence for future projects. Of course, we’ll also come up with a way to pre-populate the info for existing sites too.

Following these file and image field improvements, I’m also looking to provide API methods dedicated to searching files/images independently of pages. So if you wanted to find one (or many) images matching some criteria, you could do so, and it would find and return them regardless of what page they were found on (while still adhering to access control of course).


### New PageFamily API and class

ProcessWire’s rules for family relations between pages are currently not in any single defined location and I’ve been looking to give them a more formal and central API. This encompasses logic like identifying what parent and child types are allowed for any given page, where pages are allowed to be placed, and how many, and so on.

Currently the logic is kind of split between access control, template, page adding and saving methods/processes, with logic directly where it’s needed. This works fine, but as new needs arise, I’ve been wanting to bring these under a central location to avoid potential redundancy in logic. Much of it is currently being built out in a new PageFamily class. It is used by Page objects as a helper in the same way the existing PageTraversal and PageComparison classes are. I’ll cover more on this once it’s ready to commit to the core.


### New ProCache version with built-in crawler

Another thing I’ve been working on here is a new version of ProCache. It’s a major overhaul and refactoring of the module which finally drops support for PW 2.x versions and now takes advantage of being fully PW 3.x native.

One of the major new features in this version is a built-in web crawler that can crawl all the pages in your site, or just those matching some criteria that you specify. The main purpose of the crawler is so that you can now have the option of priming the cache with the crawler rather than with live traffic.

The crawler is also useful for other things too. For instance, I’m currently developing an existing site with a new design where all the image sizes of changed. Because there are a lot of images, and we need to generate multiple size variations (plus WebP versions of each), the first render can take literal minutes in some cases. So I let a crawler run overnight to take care of pre-rending all those image sizes and variations on the development site so that live traffic never has to wait.

The ProCache crawler is unique in that it’s a PW-specific crawler and knows about how PW handles multi-language, pagination and URL segments. It gets URLs to crawl directly from the database, so is not dependent upon link structure in the markup (though it is able to read it as well). It can also focus in on specific groups of pages, such as all pages using a particular template, or literally anything you can specify with a $pages->find() selector. The ProCache crawler can be used from the ProCache admin (via a special console window like the one in ListerPro), but it can also be used from the API, like in a shell script triggered from a cron job.

If all continues well with development and testing, this new version of ProCache should hopefully be ready by the end of the month.

Thanks for reading, and stay tuned for more details on all of these things as they are completed. So consider this just a brief introduction to some work in progress. I hope you all have a good weekend and be well. Enjoy reading the [ProcessWire Weekly](https://weekly.pw) for the latest ProcessWire news and updates, and [subscribe](https://processwire.com/community/newsletter/subscribe/) to the weekly newsletter.
