# ProcessWire 3.0.41 and a look at API Explorer

Source: https://processwire.com/blog/posts/processwire-3.0.41-and-a-look-at-api-explorer/

## Sections


## ProcessWire 3.0.41 and a look at API Explorer

18 November 2016 by Ryan Cramer [ 2 Comments](/blog/posts/processwire-3.0.41-and-a-look-at-api-explorer/#comments)


## ProcessWire 3.0.41

This week we have a new master version released: 3.0.41. This version is 42 commits ahead of the previous master version. For full details on what's different, see our [master branch commit log](https://github.com/processwire/processwire/commits/master).

Last week we told you the new master version was going to be 3.0.40, but since most of the commits over the last week were already stable, we went ahead and included them all in the new master version. Relative to last week's dev version (3.0.40) version 3.0.41 has the following:

The dev branch this week (future 3.0.42) differs from the master branch by 1 commit, which includes a [PR](https://github.com/processwire/processwire/pull/32) from @derixithy that adds support for a cookie domain to our sessions. This is useful for those that need to be able to maintain a session across multiple sub-domains.


### Introducing the API Explorer module

[Last week](/blog/posts/a-look-at-the-new-profilerpro-module/) I mentioned we'd tell you about ProDocs module this week, which is part of the ProDevTools modules. That's what I'm going to do here, except that I opted to name it API Explorer rather than ProDocs. While ProfilerPro is the flagship of our ProDevTools set of modules, we think you'll find the API Explorer module to be incredibly hepful as well.

Chances are you are already familiar with some of this module via our official [API reference](../api-full/index.md) documentation, which uses this module to generate the ProcessWire API documentation in real-time.

What's neat about the API Explorer module (and our API reference) is that the documentation it generates is pulled directly from the code, merging information available from our phpdoc tags, ProcessWire documentation tags, and PHP's Reflection library. Meaning, the documentation is always up-to-date with the version of ProcessWire that it's running on top of. This enables us to maintain most of our API documentation from the PHP code itself. We've found this increases the accuracy and usefulness, and portability of the documentation.


### While our online API reference is already powered by this module, the API Explorer can do quite a bit more than what the API reference reveals:

We've installed a copy of API Explorer on the ProcessWire demo site. [Please feel free to try it out](http://demo.processwire.com/admin/setup/api/). You might notice that API Explorer has some other updates not yet present in our online API reference. We'll be updating our API reference to use this new version of API explorer soon, after a few adjustments. We're also working to update the Cheatsheet so that it pulls its data from API Explorer as well.


### API Explorer screenshots

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1166/api-exp-1.png)

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1166/api-exp-2.png)

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1166/api-exp-3.png)

Both ProfilerPro and API Explorer should be ready for release by this time next week. These are the first two modules in our ProDevTools set of modules.

*An interesting tidbit:* while ProfilerPro is the flagship of ProDevTools, the API Explorer has 3 times the amount of code as ProfilerPro, making it one of the largest modules I've built. That's not by choice, it's just that some things take a lot of code to accomplish. The good news is that it was worth it–I'm finding API Explorer incredibly handy here, and think you will too.

Thanks for your interest and hope that you all have a great weekend. We hope you'll take some time to relax and enjoy reading the [ProcessWire Weekly](http://weekly.pw) as well.
