# ProcessWire 2.6.13 and a preview of ProDrafts

Source: https://processwire.com/blog/posts/processwire-2.6.13-and-a-preview-of-prodrafts/

## Sections


## ProcessWire 2.6.13 and a preview of ProDrafts

14 August 2015 by Ryan Cramer [ 12 Comments](/blog/posts/processwire-2.6.13-and-a-preview-of-prodrafts/#comments)


## ProcessWire 2.6.13

The new version of ProcessWire this week includes some useful improvements, as well as bug fixes and tweaks. More about that below. The biggest update this week is actually with regard to the upcoming ProDrafts module. It's not ready for release just yet, but it's getting close to being ready for beta testing, and scheduled for public release in September. Since I've been working on it a lot this week, I wanted to include a sneak peek at a few things coming with ProDrafts.


## ProcessWire 2.6.13 core updates


### Pages “Add New” menu now sortable

[Last week](/blog/posts/processwire-2.6.12-core-updates-updates-to-several-pro-modules-and-more/) we expanded upon the "Add New" button that you see on the PageList, and made it available as a menu item under "Pages" that you can access from anywhere in your site. Over the last week, there have been a couple of requests to make it possible to control the order that those shortcuts appear in (they sort alphabetically by default). This week we added the ability to control the sort order manually by drag and drop. See the *ProcessPageAdd* module settings:


### Dynamic loading for page editor “Children” tab

Over the last few weeks, we introduced dynamic loading AJAX Inputfields. Now we're starting to expand usage of them in the core. This week we made the "Children" tab that you see in the page editor dynamic, so that it doesn't load unless you click on it.

The benefits here are improved performance in the page editor. The "Children" tab contains a separate PageList, which fired off a separate AJAX request every time the page editor was loaded. Likewise for the "Parent" field, editable on the settings tab (parent was converted to dynamic loading a couple of weeks ago). So in past versions of PW, every time you opened the page editor, it fired off at least two other AJAX requests to load page lists. Now it doesn't fire off any additional requests, unless you specifically need to view or edit something on the Children tab or Parent field. We think you'll notice that the page editor loads faster now.

If for some reason you don't want these dynamically loaded fields by default, you can easily convert them to non-dynamic with the $config->pageEdit array settings (which you can override in your /site/config.php file). For more details see ProcessWire's main /wire/config.php file.


### Updated to CKEditor 4.5.2

Our previous upgrade to CKEditor 4.5.1 on the dev branch introduced an issue where inserting an image into an inline CKEditor field, and then clicking the "Save" button, would prevent the contents of the of the CKEditor field from getting saved. We updated to CKEditor 4.5.2, hoping that would fix the problem, but it didn't. It turns out there is a bug in 4.5.1/4.5.2 (and perhaps some previous versions) that they have a fix coming for in 4.5.3. However, we figured out a workaround so that you don't need to be affected by this particular bug, and that workaround is included in ProcessWire 2.6.13. We will upgrade to CKEditor 4.5.3 as soon as it is released on their stable branch, though 4.5.2 with the workaround seems to be working quite well now.


## A preview of ProDrafts

I've been busy at work on ProDrafts and am hoping to have a beta ready within the next 1-2 weeks, and public release ready in September. Since it's been my biggest focus this week, I thought it would be a good time to tell you a little about it and include some screenshots. Likewise, if you have any questions about it, please respond in the comments below and I'd be happy to discuss it more.


### About ProDrafts

ProDrafts is ProcessWire's newest "Pro" (commercial) module that manages separate draft versions of live pages and introduces more workflow possibilities to ProcessWire.

ProcessWire already enables you to maintain drafts of pages that aren't yet published. But as soon as they are published, any changes you make are likewise published. ProDrafts gives you the option of changing that behavior. When ProDrafts is installed, you can save changes to a draft version of the page without affecting the live published version.

While this in itself is a useful convenience, it also enables the potential for more advanced workflow, should you want it. For instance, you can have users that are allowed to make edits, but not publish those edits. A separate user can then approve or abandon edits as a whole, or individually on a field-by-field basis.

ProDrafts provides the tools for reviewing and comparing live versus draft data, side-by-side. Of course, you can also preview your drafts on the front-end of your site, just as if they were published.

ProDrafts also enables you to assign statuses to your drafts, for more advanced workflow possibilities. For instance, if a user doesn't have publish permission, they can assign a "publish requested" status to the draft, indicating that they are submitting the draft for approval and publishing by the appropriate person. We'll cover this and more statuses in the near future.


### ProDrafts Screenshots

When ProDrafts is installed, the usual "Save" button in the page editor instead becomes separate "Publish" and "Save Draft" buttons. The "Publish" button works the same as the "Save" button you are used to. While the "Save Draft" button saves changes without committing them to the Page.

Whenever a field has pending draft changes, it is accompanied by a paperclip icon at the top, and a note at the bottom. Clicking the paperclip or the note opens a modal window showing both the live and draft versions of the field, along with a diff comparison, when applicable.

ProDrafts also comes with a Drafts manager, accessible from Pages > Drafts. This shows you all pending drafts and a summary of what's contained in each. From here you can view, compare, publish or abandon pending drafts. The ability to publish or abandon drafts is reserved for users with page-publish permission.

A minor point, but pages that have a draft version available also appear with the paperclip icon in page lists.

That's it for this week. If you'd like to keep in touch, please [subscribe to our newsletter here](/contact/subscribe/). Also be sure to check out the [ProcessWire weekly](http://weekly.pw) at it's awesome new site (weekly.pw) on Saturday!
