# New User Activity module features and ProcessWire 3.0.206

Source: https://processwire.com/blog/posts/user-activity-v6/

## Sections


## New User Activity module features and ProcessWire 3.0.206

7 October 2022 by Ryan Cramer [ 0 Comments](/blog/posts/user-activity-v6/#comments)

This week we have ProcessWire 3.0.206 on the dev branch and a new version of the ProDevTools UserActivity module, which we'll take a closer look at in this post.


## ProcessWire User Activity v6

Version 6 of the [UserActivity](https://processwire.com/store/pro-dev-tools/user-activity/) module adds two new experimental features that expand upon how UserActivity can resolve page editor conflicts. In the past it solved this by alerting users when they might be interfering with each other's edits. This new version adds features that go beyond alerts and instead make it possible for multiple users to edit the same page at the same time, so long as they aren't editing the same field.


### New “limit-save” feature

Requires ProcesWire 3.0.206.

This experimental feature updates ProcessWire’s page-editor behavior so that when a page is saved, any unchanged fields are skipped during processing. This helps to prevent potential page edit collisions.

To explain how limit-save works, let's first discuss what happens *without* the UserActivity module installed, by way of these examples:

Let's say we've got 2 editors: Joe and Susan. Joe starts editing a page, and shortly after, Susan starts editing the same page. Joe modifies the "title" field and then saves. Susan modifies the "body" field and then saves. Because Susan started editing before Joe saved his changes, Susan had an older version of the "title" field, and thus has overwritten Joe's changes. The same thing could happen in reverse too: if Susan had saved before Joe did, then when Joe saves he would overwrite the "body" changes made by Susan.

A page increments an integer field named "counter" every time it is viewed. Joe is back, and he goes and edits this page. While editing, the page is viewed 5 times. When Joe finishes editing, he saves the page. In doing that, he overwrites the "counter" value to whatever it was when he first started editing, losing those 5 page views from the counter value.

**The “limit-save” feature helps to prevent these situations from occurring by saving only fields that have changed directly in the page editor. **

It does this by monitoring changes to fields from the client side (Javascript) and then including this information in the submitted POST data when a page is saved. This enables it to skip over modifying any fields that were not known to have changed, thereby avoiding unintentional overwrites.


### New “auto-reload” feature

ProcessWire 3.0.206 recommended but not required.

This experimental feature solves a similar problem to the “limit-save” feature, but in a very different and more entertaining way. (Actually, it is optimal to use “auto-reload” and “limit-save” together.)

When you are editing a page and some field value on the page changes outside of your edit session (whether by another user in the page editor, or the API), the field is automatically reloaded (via ajax) to reflect the changes. This keeps your page-editor up-to-date with the latest changes. This ensures that when you save, you won't overwrite changes made elsewhere.

A good way to demonstrate this feature is to edit the same page in two different windows and place them side-by-side. Make a change to the page in the first window and then save. Shortly after that, you should then see that same change appear in the second window automatically.

In order to make it more obvious, UserActivity adds a background color to fields that auto-reload in this way, just to make it clear that it was reloaded while you were in the editor. (You can also turn the background color off in the module settings if you want to).

Continuing our first example from the “limit-save” feature: When the “auto-reload” feature is enabled and Joe saves his changes to the "title" field, those changes automatically appear in Susan’s editor as well. Susan makes changes to the “body” field and saves, they likewise appear in Joe’s editor.

**What happens if 2 people both modify the same field?** If both Joe and Susan have modified the same field, then we have 2 versions of a field value and thus an edit collision. Joe saves before Susan and his changes get committed to the database. Once that happens. Susan is alerted that the field value has changed, and that if she saves then she will overwrite Joe's changes. The auto-reload feature does not automatically reload the field in this case since it would cause Susan's changes to be lost. So at this point Susan can decide either to replace Joe's changes or abandon her own changes.

**Consider disabling some of the alerts** The auto-reload feature reduces the need for several of the alert features built into UserActivity. In fact, some of them may become an annoyance once you start using auto-reload. However, I recommend keeping the *modified* and *modified-self* alerts enabled, as UserActivity updates their behavior to be more useful when using auto-reload. It adjusts them so that they only alert you if there's an unresolvable conflict, such as both Joe and Susan modifying the same field at the same time.


### New “live changelog” feature

In order to support the auto-reload feature, UserActivity now has to maintain its own internal changelog of every field that's changed on each page. Though it only needs to maintain this information for a short period (like a day). But because it is now storing this information, I thought that the UserActivity Process module should also have an option to display it.

If you go to Access > Users > Active Users, you should see a "Live changelog" button at the bottom. This screen updates automatically to show every change made to a page, as each is made. It doesn't have a lot of information and may not be that useful outside of being a “live” changelog, but it's there if you want it, perhaps to keep an eye on edits or for quick checks. For a full featured and genuinely useful changelog I highly recommend Teppo’s [ProcessChangelog](https://processwire.com/modules/process-changelog/) module.

Please consider these new features "experimental" in this version, as testing so far has been limited and there may be other factors in your own sites and environments that are not yet accounted for. If you decide to test these features, please let me know if you run into any issues. Avoid using experimental UserActivity features in ProDrafts or other modules involved in saving page fields.

UserActivity is part of the [ProDevTools](https://processwire.com/store/pro-dev-tools/) module package. This new version of UserActivity shoud be considered beta test at this stage and can be downloaded by users subscribed in the ProDevTools support board, in the [ProcessWire support forums](/talk/).


## Core updates


### ProcessWire 3.0.206 dev

ProcessWire 3.0.206 on the dev branch contains 16 commits (relative to 3.0.205) with a mixture of new features, feature requests and issue resolutions. Highlights include:

For version-by-version core updates and additional weekly news and commentary, be sure to follow along in the our [News & Announcements board](https://processwire.com/talk/forum/7-news-amp-announcements/), and the [ProcessWire Weekly](https://weekly.pw). If you missed it last week, check out the new [invoice application profile](https://processwire.com/talk/topic/27638-weekly-update-%E2%80%93%C2%A030-september-2022-%E2%80%93-invoice-app-profile/) for ProcessWire, currently in development. Currently we are also working towards the next master version which we are aiming to release before the end of the year, or sooner.
