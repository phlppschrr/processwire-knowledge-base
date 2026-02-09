# Three new ProcessWire versions + a couple of surprises

Source: https://processwire.com/blog/posts/three-new-processwire-versions-and-surprises/

## Sections


## Three new ProcessWire versions + a couple of surprises

27 November 2015 by Ryan Cramer [ 12 Comments](/blog/posts/three-new-processwire-versions-and-surprises/#comments)


## ProcessWire 2.7.1, 2.7.2 + 3.0 alpha-3!

This week we've got three new versions of ProcessWire out there, 2.7.1 master (stable), 2.7.2 dev, and 3.0 alpha 3 on the devns branch, where we've got some particularly interesting developments.


### We are now running ProcessWire 3.0!

We're happy to report that this site (processwire.com) is now running ProcessWire 3.0, and everything is purring along smoothly.

**We didn't update any of our template files or modules for 3.0. **We just replaced the /wire/ directory and /index.php file and that's it. Meaning, all of our template files, and all of our 3rd party modules (and we have a lot) are getting compiled for 3.0 support by ProcessWire 3.0's file compiler, without any issue at all.

The next time we do a redesign here, we'll upgrade everything to be native 3.0 (and use namespaces), but it's satisfying to know that you don't have to. In our case, the upgrade to 3.0 turned out to be just as easy as the upgrade from 2.6 to 2.7.

This site is the first production site that I've upgraded to ProcessWire 3.0, but I've got several development sites that I have already upgraded from 2.x to 3.0, with identical results. As a result, I'm starting to feel good about the stability and reliability of our new version, though we no doubt still have a lot of testing to do. But things are looking good for 3.0!


### ProcessWire 2.7.1 master

This version replaces version 2.7.0 master/stable. It contains several small fixes and improvements relative to 2.7.0. If you are already running 2.7.0 we recommend the upgrade, though it's also not urgent. Here's a summary of what this version has relative to 2.7.0:

- Support for IDNs (international domain names) in URL fields and in the `$sanitizer->url()` method.
- Upgrade to Lister to enable sorting by subfield (when applicable).
- Fix for InputfieldSelector when using multiple datepicker fields.
- Fix for orphaned rows of data in field tables when removing fields from templates having fewer than 200 populated pages.
- Upgrade *"check field data"* in ProcessField to support detection and removal of orphan data per the previous bullet.
- Fixes to some 'requiredIf' field dependency issues.
- Add support for `page-edit-images` optional permission to enable access control to the image editor.
- Fix `Pageimage::maxSize()` method that wasn't always working as intended.
- Fix issue that prevented Pages > Add New menu from appearing in some instances.


### ProcessWire 2.7.2 dev

The updates on 2.7.2 dev are relatively minor coming from 2.7.1. The main difference is that it backtracks a bit on the [bookmarks feature](/blog/posts/processwire-2.6.17-expands-admin-navigation-with-bookmarks/) for "Pages > Edit" and "Pages > Tree" that you see in your top navigation.

These features can be genuinely useful on large ProcessWire installations, but are unnecessary elements on many others, especially smaller installations. Rather than having them always visible, they now are hidden by default, but can be enabled from the *ProcessPageEdit* and *ProcessPageList* module config screens. When you install 2.7.2, you will no longer see the "Pages > Edit" and "Pages > Tree" navigation items unless you enable them in each module's settings. I think this helps to keep things more simple, which is always a goal for our admin interface.

This is an update I think we should have in our official stable version of 2.7, but rather than putting it into this week's 2.7.1 version, I wanted to test it for another week on the dev branch before migrating to the master branch.

Note that this doesn't affect the similar bookmarks features available for "Pages > Find" and "Pages > Add New". I think those are useful in all installations, so they will be left as-is.


### ProcessWire 3.0 alpha-3

The alpha-3 version of 3.0 primarily makes the same upgrades and fixes to 3.0 that appear between 2.7.0 and 2.7.2. It also continues with improvements and optimizations to the file compiler and other 3.x-specific features. This version also makes numerous updates to the README file to reflect the simpler upgrade process, as well as the deprecation of 2.x compatibility mode (a mode which thankfully turns out to be completely unnecessary).


### ProcessWire 3.0 adds front-end editing capabilities

*Note: after this blog post was written, there have been several improvements, changes and refinements to front-end editing, so some things have changed relative to the information below. [See this follow-up post for more up-to-date information on front-end editing](/blog/posts/front-end-editing-now-in-processwire-3.0-alpha-4/) as well as our [front-end editing documentation page](/api/modules/front-end-editing/). Front-end editing is now available and ready-to-use on the ProcessWire 3.0 (devns) branch. *

Our philosophy for editing content has always been that it should be edited in an interface intended for that purpose. The front-end of a site is primarily for outputting content rather than inputting it, and the what's best for output is rarely best for input and management of content. Whereas the back-end of the site (admin) is built specifically for managing and inputting content. It also ensures that editors stay focused on the actual content rather than styling of that content.

…and yet there are those times where I spot a typo on the front-end and I want to fix it right there, before I lose track of it (especially in something like this post). And there are also those times where I'm working with a unique site design that seems like a few parts might lend themselves well to front-end editing… at least for some of the text blocks (like title and body). There have also been several instances where I know front-end editing would not be the best, but wished I had it for eye-candy purposes, potentially helping to seal the deal on a new project.

Even if I don't think front-end editing is suitable for most cases, I also can't deny that there are many cases where it is definitely a nice-to-have. ProcessWire aims to be the most flexible system out there, and part of that flexibility means supporting a diversity of input scenarios. So front-end editing is something that I think we should support as an option. Yet, ProcessWire doesn't control the front-end markup at all (you do), so it's not as straightforward of a thing to support as it might be other platforms out there.


### A little surprise

Still reading? If so, I've got a little surprise for you. The version of ProcessWire we're using here fully supports front-end editing (and saving), and I'll be pushing this version to the 3.0 (devns) branch within the next two weeks, with the alpha-4 version.


### Some more details

I looked into some existing solutions to build from, but in the end decided to roll our own using html5 "contenteditable" attributes and CKEditor. I think most of the value in front-end editing comes with fields that be represented by text, number and textarea types. That's because their output tends to be very similar to their input, and they don't necessarily need a supporting administrative interface to be fully editable. Rich text editing may be an exception, but CKEditor's inline mode is also exceptional – it's just as happy running on the front-end of a site as it is on the back-end. And when it's running on the front-end, you can edit your content in its exact context and appearance (which is cool, though maybe not the best for keeping editors focused purely on content). You can also manipulate images and links just like you can in the back-end.


### How does it work?

When configuring a field (Setup > Fields), on the "Input" tab you have a new option to "Allow front-end input?" This appears for text and number fields, or any fields derived from them (like CKEditor). We may support more input types too, but we'll be starting with these, as they seem like the most potentially useful on the front-end.

Multi-language is also supported, so long as you are using multi-language page names. This ensures that you can edit each language content individually as a page, in its proper language context.


### Does it require any front-end code?

If usin option A, ProcessWire takes care of it for you. Meaning, your field becomes front-end editable as soon as you check the box to enable front-end editing for that field. You don't have to code for it, unless you want to customize the output (though most of the time you might want to). For instance, if you wanted to make editable fields appear with an icon or a different background color, you could add a couple styles to your existing stylesheet.

A single API function `$page->edit()` is also provided which enables you to turn on or off the editing capability when you want to. For instance, if you are outputting `$page->title` in both an `<h1>` tag and a `<title>` tag, you probably only want it to be editable in the <h1> tag. So a single API function lets you control that for those cases.

*Questions? Please reply in the comments below and I'll be happy to write more.*


### Happy Thanksgiving

Here in the US we are currently on our Thanksgiving holiday, which is one of the bigger holidays every year. The purpose is to reflect on the things that you are thankful for. I'm incredibly thankful for all of you, the ProcessWire community, and all that you do. Thank you for being here, we have an exciting future!
