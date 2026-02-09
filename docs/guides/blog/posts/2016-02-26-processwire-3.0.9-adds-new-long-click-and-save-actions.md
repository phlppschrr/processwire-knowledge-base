# ProcessWire 3.0.9 adds new long-click and save actions

Source: https://processwire.com/blog/posts/processwire-3.0.9-adds-new-long-click-and-save-actions/

## Sections


## ProcessWire 3.0.9 adds new long-click and save actions

26 February 2016 by Ryan Cramer [ 6 Comments](/blog/posts/processwire-3.0.9-adds-new-long-click-and-save-actions/#comments)


## ProcessWire 3.0.9

For this week we've got a new version of ProcessWire 3.x, version 3.0.9. This version adds some useful UI enhancements in the admin that were originally envisioned by members of the ProcessWire community. ProcessWire 3.0.9 and also has a few other refactoring, bug fixes and tweaks.


### New long-click modal actions

Back in December, forum member [matjazp](/talk/user/2202-matjazp/) sent over a module to me that he had made with another forum member [tpr](/talk/user/3156-tpr/), which he said was itself based on ideas from an earlier module called [FancyAdminMode](/talk/topic/2380-fancy-admin-mode/) by [Soma](/talk/user/100-soma/). The concept is to enable modal editing of pages from within the page list.

The module by matjazp and tpr enabled modal editing of a page when the page label was long-clicked. After using it several times I found it to be very useful and thought it was something you would like too, though taken a little further, and with a slightly different implementation.

**This week we implemented long-click actions in the page list for the "edit" and "view" actions.** If you click and hold either of those actions for about a second, it'll open the action in a modal window rather than in the current window. This can be really handy when you want to make a quick edit, or quickly view the page on the front-end.

**We've also added a similar long-click action in the page editor for the "View" tab.** Currently if you click the "View" tab, it takes you to the front-end of your site to view the page. We've updated it so that if you long-click that "View" tab, then it opens the page on the front-end of your site in a modal window.


### New page-edit save actions

Some of you might be familiar with the [Admin Save Actions](http://modules.processwire.com/modules/after-save-actions/) module by [Nik](/talk/user/481-nik/), released back in January 2013. We've added something similar in utility to the core page editor, though with a different implementation.

Here's how it works: any "save" or "publish" buttons in the page editor work the same as usual. But if you hover your mouse over the button for a little under a second (700ms to be exact) a dropdown appears with the button, giving you additional actions you can perform in addition to the save/publish operation.

These actions are primarily focused on things you are most likely to do after submitting the page edit form, such as exiting and returning to the page list, viewing the page, or adding another page of the same type.

I've found this to be quite handy in testing here this week, as it can very often save a step, and thus time. We'll likely be expanding support for this elsewhere in the admin, and building support directly into our InputfieldSubmit module so that the capability can be easily used by 3rd party modules too.


### New version of ProDrafts released

[Last week](/blog/posts/prodrafts-now-available-in-pre-release/) we released the initial beta of [ProDrafts](/api/modules/prodrafts/), version 1. This week we've released version 2, which is still beta, though we've not had any major issue reports so ProDrafts may be out of beta in as soon as next week. The ProDrafts coupon code PWPD-BETA will expire on on March 1 (Tuesday). Version 2 greatly expands on what ProDrafts can do:


### ProDrafts video demonstrates some of the new features

I posted this video in the forum earlier this week, so if you are a regular there you have probably already seen it. But just in case you haven't, here's a short video that demonstrates some of the new features described above.
