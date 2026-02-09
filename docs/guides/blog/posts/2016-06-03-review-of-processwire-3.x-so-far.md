# ProcessWire 3.0.20 updates, plus a review of ProcessWire 3.x so far

Source: https://processwire.com/blog/posts/review-of-processwire-3.x-so-far/

## Sections


## Recap and Review of ProcessWire 3.x so far

3 June 2016 by Ryan Cramer [ 5 Comments](/blog/posts/review-of-processwire-3.x-so-far/#comments)


## ProcessWire 3.0.20

Working through GitHub issue reports was the focus of this week, and it looks like we've got one more week to go in working through the current queue. There have not been any major bugs in 3.x, so things are looking more and more stable. Most updates in this weeks version (3.0.20) are about fixing minor bugs and various cosmetic things.

There's nothing particularly exciting to report in this version other than that. But working towards a fully stable 3.x master version is itself an exciting thing. So rather than focus on the small tweaks and fixes from this week, lets backtrack and review all that's new in 3.x relative to the current 2.7 master version.


## What’s changed between 2.x and 3.x?


### Namespaces

Technically, the biggest difference between 2.x and 3.x is that 3.x uses PHP namespaces. This either matters to you a lot, or not at all, but it's a good thing for the growth of ProcessWire as a project. [More](/blog/posts/processwire-2.6.20-and-surprise-processwire-3.0-alpha-1/#what-benefits-will-using-namespaces-bring)


### Support for compiled modules and template files

In order to ease the transition to namespaces for modules and template files, ProcessWire 3.x originally came with a compatibility mode ($config->compat2x). However, *FileCompiler* was later introduced to 3.x, which eliminated the need for any kind of compatibility mode. ProcessWire is able to automatically compile non-namespaces modules or template files into a format that makes them recognize namespaces. [More](/blog/posts/processwire-3.0-alpha-2-and-2.6.22-rc1/#processwire-3.0-alpha-2)


### Front-end editing

Built-in, front-end editing capabilities come with ProcessWire 3.x, opening a whole new path for page edits. [More](/api/modules/front-end-editing/)


### Major image field upgrades

Image fields got a major upgrade in 3.x thanks to a redesign by Renobird and development help from LostKobrakai. The design was originally introduced in [this post](/blog/posts/a-preview-of-coming-attractions-to-processwires-image-tools/) by Renobird, and the results now appear in the current 3.x version with more info and screencasts [here](/blog/posts/major-images-field-upgrade/) and [here](/blog/posts/more-images-upgrades/).


### New $pages->findOne() method

ProcessWire 3.x adds a [new $pages->findOne() method](/blog/posts/merry-christmas-heres-processwire-3.0.3-and-2.7.3-and-some-more/#new-pages-gt-findone-selector-api-method) that behaves as kind of a hybrid between the $pages->find() and $pages->get() methods.


### New $pages->getPath() and $pages->getByPath() methods

The getPath() method enables you to get the path to a page without actually loading it, making it a nice optimization for several instances. And the getByPath() method enables you to retrieve a Page object when you only know the path. Of course you can already do that with any page finding method that accepts a selector, but the difference is that getByPath() is very task focused and can do it a lot more quickly, and with a few extras as well. [More](/blog/posts/processwire-3.0.6-brings-pages-upgrades-and-link-abstraction/#new-optimized-pages-api-methods)


### New $pages->touch() method

This method works very much like the unix "touch" command. Given a $page, it quickly updates that page's modification time (in the database) to now. [More](/blog/posts/processwire-3.0.6-brings-pages-upgrades-and-link-abstraction/#pages-gt-touch)


### New $pages->findMany() method

This new method enables you to find thousands upon thousands of pages at once, and even iterate them without running out of memory! [More](/blog/posts/find-and-iterate-many-pages-at-once/)


### New link abstraction features

Full page link abstraction is now built into the core Textarea field, making it possible to move or rename linked pages and have any internal links to them get updated automatically. [More](/blog/posts/processwire-3.0.6-brings-pages-upgrades-and-link-abstraction/#new-link-abstraction-features)


### Repeater upgrades

Repeaters have a ton of upgrades in 3.x, making them far more useful and efficient than before. Read more [here](/blog/posts/processwire-3.0.4-repeaters-revisited-preview-of-profields-matrix/#major-upgrades-to-repeater-fields) and [here](/blog/posts/more-repeaters-repeater-matrix-and-new-field-rendering/#repeater-upgrades-continued-in-pw-3.0.5).


### Repeater Matrix support

In combination with some of the Repeater upgrades mentioned above, 3.x also supports the ProFields Repeater Matrix Fieldtype, which is opens up a whole new landscape of editing possibilities. [More](/blog/posts/processwire-3.0.4-repeaters-revisited-preview-of-profields-matrix/#new-profields-repeater-matrix-field)


### Page tree upgrades

One of my favorite tweaks in 3.x are the page tree upgrades that make it remember where you left it and also enables it to load the page list much faster than before. [More](/blog/posts/processwire-3.0.8-brings-smarter-faster-page-tree/#page-tree-upgrades)


### Image resizing upgrades

Thanks to the work of Horst, we added support for new ImageSizerEngine modules and bundled the new ImageMagick resizing engine as a faster alternative to the built in GD resizing engine. [More](/blog/posts/processwire-3.0.10-expands-image-resize-options/)


### Field rendering template files

ProcessWire 3.x also adds support for a new kind of template file. You can now have template files for any field in ProcessWire, and those template files can be used to render output for any given field. Read more [here](/blog/posts/more-repeaters-repeater-matrix-and-new-field-rendering/#processwire-3.0.5-introduces-field-rendering-with-template-files) and [here](/blog/posts/processwire-3.0.7-expands-field-rendering-page-path-history-and-more/#field-rendering-with-template-files).


### New page view options

You now have a lot more options when it comes to viewing a page on the front-end. Our "view" link is now a drop-down letting you choose to view it in the same window, in a modal, in a panel or in a new window. [More](/blog/posts/pw-3.0.15/#new-page-view-options)


### Improvements to sub-selectors

The speed at which sub-selectors operate has now been [greatly improved](/blog/posts/processwire-3.0.6-brings-pages-upgrades-and-link-abstraction/#speed-improvements). Basically, they are now hundreds of times faster than before. 3.x also now supports [nested sub-selectors](/blog/posts/processwire-3.0.6-brings-pages-upgrades-and-link-abstraction/#support-for-nested-sub-selectors).


### Extended page names

We added support for extended page names enable you to have URLs containing almost any UTF-8 characters. This is great for multi-language sites too. [More](/blog/posts/hello-%E5%81%A5%E5%BA%B7%E9%95%B7%E5%A3%BD%C2%B7%E7%B9%81%E6%A6%AE%E6%98%8C%E7%9B%9B/)


### Multi-instance support

ProcessWire 3.x lets you boot multiple copies of ProcessWire at the same time, which opens new possibilities for sharing data among multiple installations.


### Panel support

In addition to the common modal windows that you see in ProcessWire, we now support [panels](/blog/posts/pw-3.0.15/#processwire-panels) and are using them in our [page list quick tree](/blog/posts/pw-3.0.15/#new-quick-tree-page-list-panel) and the new [debug tools panel](/blog/posts/pw-3.0.15/#new-debug-tools-panel). Panels are also an option when [viewing a page](/blog/posts/pw-3.0.15/#new-page-view-options).


### And much more…

- ProcessWire 3.x goes all-in on Composer support! [More](/blog/posts/composer-google-calendars-and-processwire/)
- The PagePathHistory module now supports multi-language URLs. [More](/blog/posts/processwire-3.0.7-expands-field-rendering-page-path-history-and-more/#page-path-history-now-multi-language)
- Nice improvements to the ~= text finding operator. [More](/blog/posts/merry-christmas-heres-processwire-3.0.3-and-2.7.3-and-some-more/#improvements-to-the-operator-in-page-finding-operations)
- New long-click modal actions. [More](/blog/posts/processwire-3.0.9-adds-new-long-click-and-save-actions/#new-long-click-modal-actions%C2%A0)
- New submit buttons with dropdown actions. More [here](/blog/posts/processwire-3.0.9-adds-new-long-click-and-save-actions/#new-page-edit-save-actions) and [here](/blog/posts/processwire-3.0.13-selector-upgrades-and-new-form-builder-version/#enhancements-to-dropdown-submit-buttons).
- You can now use selector arrays in addition to selector strings. [More](/blog/posts/processwire-3.0.13-selector-upgrades-and-new-form-builder-version/#selector-engine-array-support)
- New options for required fields. [More](/blog/posts/processwire-3.0.14-updates-file-compiler-fields-and-more/#required-fields-in-processwire)
- New 3.x comprehensive API reference documentation. [More](/blog/posts/processwire-3.x-api-reference/)
- And yes there's a lot more too that isn't mentioned here, but mostly smaller optimizations and tweaks.


## Have a great weekend

As you can see, 3.x is really coming along nicely and a huge upgrade. We're also feeling very good about the stability of it, and think we may be getting close to making it the new master.

Next week we'll be continuing to cover GitHub issue reports and hope to get into some of the PRs as well. For those that like using the 2.x branch, we may also have some news you'll like coming very soon.

Have a great weekend and remember to read the [ProcessWire Weekly](http://weekly.pw)!
