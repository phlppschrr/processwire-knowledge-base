# ProcessWire 2.5.2 and more

Source: https://processwire.com/blog/posts/processwire-2.5.2/

## Sections


## ProcessWire 2.5.2 and more

27 September 2014 by Ryan Cramer [ 0 Comments](/blog/posts/processwire-2.5.2/#comments)


### ProcessWire 2.5.2 pushed to master

The biggest news this week is that we've updated the master/stable version to 2.5.2. While there haven't been any major bugs found in ProcessWire 2.5.0, version 2.5.2 fixes several smaller and cosmetic details. It also adds some nice new features, as mentioned in the last couple of previous posts.

I'm also comfortable in now saying that **ProcessWire 2.5 is officially released**. It's been out there for a couple of weeks, reports have been very positive, and there have not been any major issues to surface that we are aware of. If you are not yet using ProcessWire 2.5, I don't see any reason to delay further. As always, if upgrading an existing site, make sure to test everything thoroughly on a staging/non-production server before upgrading your live server. Please see our [upgrade instructions](https://github.com/ryancramerdesign/ProcessWire/blob/master/README.md#upgrades) and there is also a section on [upgrading from 2.4 to 2.5](https://github.com/ryancramerdesign/ProcessWire/blob/master/README.md#upgrading-from-processwire-24), which is what likely most are upgrading from.

What's changed between 2.4 and 2.5? Well quite a lot actually, here's a [changelog](/blog/posts/processwire-2.5-changelog/). We're still adding contextual links and expanding on a few details, so consider it a work in progress.

This coming week we'll send out a press release introducing ProcessWire 2.5. Stay tuned for a more official announcement.


### New beginner version of default site profile

There has been some feedback that the direct output method (used by the old default profile, now called classic profile) was easier for beginners to understand than the delayed output method used in the new default site profile. Of course, being easy-to-understand for beginners is very important to us. As a result, we've added another version of the default site profile called the Beginners edition. This edition uses the same exact strategy that was used by the previous default site profile (called direct output). The main default site profile has been renamed to the Intermediate edition. Read more about the [beginner edition](/docs/tutorials/default-site-profile/page2), [intermediate edition](/docs/tutorials/default-site-profile/page3) and [multi-language edition](/docs/tutorials/default-site-profile/page4) of the default site profile [here](/docs/tutorials/default-site-profile/).


### Recent pages in your admin navigation

If you are following the dev branch, there's a new addition for you in 2.5.3. This adds a new "Recent" option to the Pages navigation. A screenshot probably explains it best:

This option will appear automatically when you install 2.5.3, no need to install anything else. Before this hits the stable branch, it will be updated with configuration options that enables you to adjust what gets shown.


### New wireRenderFile() and wireIncludeFile() functions

This week we've added a couple of new functions that you might find handy in your own template files.

The `wireRenderFile()` is actually just a quick way to use the TemplateFile class. Give it a filename, and it'll pass the file all of PW's API variables, and it will render the file as a PHP file and return the output to you. If you want to send along some additional variables, just specify them in the second argument as an associative array. See the [function definition](https://github.com/ryancramerdesign/ProcessWire/blob/master/wire/core/Functions.php#L930) for more. But here's a typical usage:

```
$photo = $page->photos->getRandom();
$sidebar = wireRenderFile("inc/fancy_sidebar", array('photo' => $photo));
```

We've also added a related `wireIncludeFile()` which works exactly the same way except that it does a literal PHP include() of the file for direct output, rather than returning the output to you. See the [function definition](https://github.com/ryancramerdesign/ProcessWire/blob/master/wire/core/Functions.php#L1016) for more. Some more points to mention about these functions:

- They receive all of ProcessWire's API variables, and optionally your own specified variables (in the same way demonstrated above).
- They assume a starting point in /site/templates/, unless you point them somewhere else.
- They will only allow files that are somewhere within the directory structures started by /site/templates/, /site/modules/ or /wire/modules/ … adding a little more safety.
- The .php file extension is assumed for any files you give it, so you can optionally omit it. Of course you can use a different extension if you want to, but just note that if the file has a .php extension, it's optional to specify it.
