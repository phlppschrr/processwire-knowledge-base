# Merry Christmas! Here's ProcessWire 3.0.3 and 2.7.3, and some more!

Source: https://processwire.com/blog/posts/merry-christmas-heres-processwire-3.0.3-and-2.7.3-and-some-more/

## Sections


## Merry Christmas! Here's ProcessWire 3.0.3 and 2.7.3, and some more!

25 December 2015 by Ryan Cramer [ 3 Comments](/blog/posts/merry-christmas-heres-processwire-3.0.3-and-2.7.3-and-some-more/#comments)

Merry Christmas! (and/or other holiday that you may be celebrating today). Today we've got two new ProcessWire versions for you, some great comments manager upgrades and more. Plus, LostKobrakai has also put together a great advanced tutorial for us this week.


## ProcessWire 3.0.3


### Improvements to the `~=` operator in page finding operations

The `~=` operator is what you use in a selector strings when you want to locate a page that contains all of the whole-worlds in a given field. For instance: `body~=foolish bar` would match pages that contain both of the words “foolish” and “bar” anywhere in the “body” field. They can be in any order.

The trouble is that it typically can’t match the word “bar” or any words with fewer than 4 characters. That’s because MySQL’s default full-text index minimum word length is 4 (though can be changed by the MySQL administrator). An upgrade was made to how ProcessWire treats the ~= operator this week, so that now it can match words with fewer than 4 characters in this instance. Plus it can now match MySQL stop words as well. It does this by falling back to using a MySQL REGEXP command when your search includes a word that falls below MySQL’s ft_min_word_length (minimum indexed word length).

It will still use the MySQL full-text index for any words that are indexable. The nice thing about this update is that it removes the "why can't I match this short word" question that inevitable comes up in many site search scenarios, ultimately making your job simpler.


### New $pages->findOne($selector) API method

We added a `$pages->findOne($selector)` API method that is a hybrid between $pages->find() and $pages->get(). Like find() it filters for page status (hidden, unpublished, etc.) and access control. And like get(), it returns only the first matching page, as the name implies.

This method is a nice alternative to $pages->get() for those cases where you are asking it to retrieve a page that you don’t really know what it is ahead of time (like a page selector derived from user input). This method saves you the step of having to check that the resulting page is viewable.

When you want to retrieve a single specific page, you'll still want to use $pages->get() – it's always going to be a little faster and give you exactly what you requested. But for those cases where you are requesting something and don't really know what it is ahead of time, consider using the new $pages->findOne() as an alternative.


### New “clear compiled files” button

Many installations of ProcessWire 3.x are using compiled modules and/or templates. ProcessWire automatically tracks when a file changes and automatically recompiles it. But there are some instances where you want to force it to recompile, like when the source file hasn't actually changed, but the ProcessWire version has (perhaps fixing compiler issues that were in the previous version).

Now you can click a button to clear ProcessWire's compiled files. This button is located in Modules > Site, at the very bottom of the screen. Note that after clicking it, you may experience a delay for a few requests afterwards as ProcessWire re-compiles all the files in use. It may be that we no longer need this function once 3.0 reaches master/stable status. But for those helping to test ProcessWire 3 now, it's a good thing to know about, and is worthwhile to use after upgrading your core between PW3 minor versions, especially if you find any 3rd party modules that aren't working properly at first.


### And more…

- Support for a combined average stars rating (for all comments on a page) via the $page->comments->stars(); and $page->comments->renderStars() methods.* We don't yet have it in use on this site, but will soon. See [bike/boat tours at Tripsite](https://www.tripsite.com/bike-boat/) for a good example of this method in action.
- Various file compiler tweaks to cover some rare instances and API usages.
- Improvements to our DatabaseQuery classes that now support bound parameters in fluent interface calls.
- Some various tweaks and fixes to the front-end editor features.
- Built-in cache busting for CKEditor custom config/style files, tracking file modification time.
- The PW version number is now suppressed from the login screen, making the PW version only knowable if the user is logged in. This is a good best practice, thanks @er314 for the suggestion.*
- Fixed an issue where the File/Image fieldtype modules only supported one textformatter module being applied to file descriptions, when they were intended to support multiple textformatters.*
- Various other minor tweaks and fixes throughout, see the [commit log](https://github.com/ryancramerdesign/ProcessWire/commits/devns) for full details.

**These changes are also included in ProcessWire 2.7.3 dev. *


## ProcessWire 2.7.3 dev

This version includes some minor fixes and adjustments relative to 2.7.2. It also includes the starred items in the bulleted list above, plus it includes the new comments manager upgrades, discussed in the section below. For more details see the [dev branch commit log](https://github.com/ryancramerdesign/ProcessWire/commits/dev).


## New tutorial by LostKobrakai

This week Benjamin Milde (who many of you know as LostKobrakai from the forums) has written an advanced tutorial on how to use and extend ProcessWire to create custom page types. Using his techniques you can add convenience to your workflow, and learn a lot of useful tips along the way. [Read this new tutorial here](/docs/tutorials/using-custom-page-types-in-processwire/) in our tutorials section. Big thanks to LostKobrakai for sharing his knowledge with us putting together this great writeup.


## Major upgrades to the comments manager

**Now included in core 2.7.3 and 3.0.3!** Those using ProcessWire's built-in comments manager *ProcessCommentsManager,* know how useful and important this tool is on sites where you have to manage a lot of comments (or even just a few comments). Peter Knight in the forums came up with some [excellent suggestions](/talk/topic/11655-better-comment-management/) for it, and Kongondo [implemented them](/talk/topic/11664-comments-manager-enhanced-proof-of-concept/) in as a proof of concept module, and he did a great job. Inspired by that, we went ahead and added these new features to the core comments manager, plus a few more. Below is a list of what we've added and upgraded.


### Summary of comments manager upgrades

- Ability to change how many comments are shown per pagination (10, 25, 50, 100).
- Ability to perform bulk actions on selected comments (approve pending, send to spam, delete, change status, and reset up-votes or down-votes).
- Select-all capability for comments, to select all comments on the current pagination for bulk actions.
- Ability to change the sort order that comments are shown in (date descending or ascending, star rating, up-votes or down-votes).
- Improved input for stars, now using actual stars for input rather than a number input.
- Improvements to responsive layout for mobile devices.
- Improvements to the user interface and presentation throughout.

Special thanks to Peter Knight and Kongondo for the ideas. Here's a screenshot of the updated comments manager. If you'd like to test it out, grab the latest 2.7.3 or 3.0.3 version and please let us know how it works for you.


### Hope that you all have a great Christmas/holiday!
