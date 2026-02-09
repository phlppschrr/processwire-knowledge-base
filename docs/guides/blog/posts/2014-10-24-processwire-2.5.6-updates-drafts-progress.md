# ProcessWire 2.5.6 updates + drafts progress

Source: https://processwire.com/blog/posts/processwire-2.5.6-updates-drafts-progress/

## Sections


## ProcessWire 2.5.6 updates + drafts progress

24 October 2014 by Ryan Cramer [ 4 Comments](/blog/posts/processwire-2.5.6-updates-drafts-progress/#comments)


### Add page screen now with AJAX helper

The add page module (ProcessPageAdd) now alerts you as you are typing if the selected page name is already used by another page. Likewise, it gives you an "Ok" if there are no conflicts with your page name. Previously, it would modify the page name for you to make it unique automatically, but you wouldn't know about that until after submitting the form. Now you get alerted to the uniqueness of your new page's name as you are typing it.


### Fixes with ProcessWire in fastcgi environments

We discovered a couple of issues with ProcessWire 2.5 running in a PHP fastcgi environment, at least when combined with certain versions of PHP 5.3. Worst case scenario was that PW would simply not run in that environment, as PHP's method_exists() would incorrectly generate a fatal error. This is apparently a known issue in some versions of PHP 5.3, but one that must not be often seen. This week we finally saw it in a way we could duplicate, and we found a workaround. It's easier for us to workaround it than it is to get your web host to change their PHP version in many cases, so that's what we did.

Another scenario we fixed this week (which may also be related to PHP 5.3 fastcgi environments) was that you'd receive a message about a module dependency not being met, on every page in the admin. In our test case, that module dependency was for LanguageTabs, but the issue actually didn't have anything to do with LanguageTabs. Instead, the issue was one in PW's core not descending to a deep enough level of dependencies. For whatever reason, we've only seen it need to descend to that level in the PHP 5.3/fastcgi environment, but can't be certain it's limited to that. Regardless, if you've seen messages about missing dependencies in the admin when you shouldn't, you may want to test out ProcessWire 2.5.6 dev.


### Drafts for published pages, now in development

Jumping beyond the core, we've been working this week on draft capability for published pages, which will also include some nice workflow additions. Currently ProcessWire drafts are essentially unpublished pages. But there have been requests for keeping a separate draft version of already published pages. So that's what is being worked on here.

At the very basic level, when the drafts module is installed, your usual "Save" button on each page instead becomes separate "Publish" and "Save Draft" buttons (or just "Save Draft" if the user doesn't have page-publish permission). When you save a draft, the changes aren't visible on the front-end of the site, except to you when previewing it. The only significant limitation to mention here is that some fields can't be saved as drafts, specifically repeaters and PageTable, though we may be able to support PageTable later on. Otherwise, all Fieldtypes should work. In fact, all of the other core Fieldtypes and ProFields already work with it even in our early state of development.

Introducing drafts in this manner also is a good opportunity for us to introduce some nice workflow improvements, like isolating who can create drafts and who can approve and publish them. So that will be part of it. Likewise, a diff to compare published and draft versions is coming as well. I'll have more information in the coming weeks as we get further along with it.


### Next week

Next week we'll be making some updates and enhancements to the image resize functions thanks to more great contributions from Horst. He's got some really incredible stuff somewhat related to this in development too!
