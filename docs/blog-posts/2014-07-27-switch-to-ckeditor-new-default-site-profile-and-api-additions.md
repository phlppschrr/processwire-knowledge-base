# July 2014 Core Updates

Source: https://processwire.com/blog/posts/switch-to-ckeditor-new-default-site-profile-and-api-additions/

## Sections


## July 2014 Core Updates

27 July 2014 by Ryan Cramer [ 1 Comment](/blog/posts/switch-to-ckeditor-new-default-site-profile-and-api-additions/#comments)


## Switch to CKEditor, new default site profile and API additions


### Goodbye TinyMCE / Hello CKEditor

TinyMCE has been dropped from the core and has been added to the modules directory as a 3rd party module. We will continue to maintain it as a 3rd party module. TinyMCE 3 is a great rich text editor, but I'm currently of the opinion that CKEditor 4 works better as our core default.

As a result, CKEditor has been added to the core as the new default rich text editor. While I would love to include both editors in the core, there are plenty of people that think we shouldn't have any rich text editor in the core, so having two giant RTEs would be too much.

If you want to continue to use TinyMCE in PW 2.4.9+ that is no problem. After upgrading to the latest dev (or once you upgrade to PW 2.5 stable) simply install InputfieldTinyMCE from the modules directory immediately after upgrading your ProcessWire core (or at least, before you go editing pages and/or fields).


### HTML Purifier

MarkupHTMLPurifier has also been added to the core. This is something that CKEditor inline mode requires, but I think it's a good addition regardless.

We have added a `$sanitizer->purify($html)` method that makes use of the HTML Purifier module. For more about HTML Purifier, be sure to visit [http://htmlpurifier.org](http://htmlpurifier.org/).


### New additions to $page

Added new `$page->hasChildren()` method, which works exactly the same as `$page->numChildren()` except that it returns only number of visible children (you can also pass a selector string to either method).

While we already had essentially the same thing before, I've not been satisfied with it from the API side. That's because `$page->numVisibleChildren` is too much of a mouthful and `$page->numChildren(true)` is too ambiguous (nobody wants to look up what "true" means), so `$page->hasChildren()` is something that I think is more readable in our code. Though the old methods/properties will continue to work too.

Added new `$page->editUrl` (or `$page->editURL` if you prefer) property that returns the URL to the page editor for the current page.


### New default site profile

Our default site profile has been looking dated for awhile, and it wasn't even responsive. We've been working on multiple replacements for it, but with so many different ways to do things in ProcessWire, it's hard to settle on just one.

We've come to the conclusion that there need to be multiple profile install options right from the installer. One should be completely blank, one should be a very minimal introductory profile, and one should go a little further in introducing various concepts. Today I replaced the existing default site profile with a more minimal profile. There is probably still work to do with this one (feedback appreciated as always).

The existing default site profile will be coming back, but under the name "site-classic". We've got to keep it around, or at least available, since it's the best demonstration we have of direct output head.inc/foot.inc template methodology, and it's also a prerequisite to some other profiles. I just don't want it to be the first and only thing that people see when they install ProcessWire.

Another profile in the works (and nearly done) is one that builds upon [a templated.co template called Iridium](http://templated.co/iridium). This one serves as a good example of using ProcessWire to work with an existing design/template.
