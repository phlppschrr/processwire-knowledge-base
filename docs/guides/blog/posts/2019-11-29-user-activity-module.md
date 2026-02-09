# New User Activity module

Source: https://processwire.com/blog/posts/user-activity-module/

## Sections


## New User Activity module

29 November 2019 by Ryan Cramer [ 0 Comments](/blog/posts/user-activity-module/#comments)

This week we’ll take a quick break from core updates and have a look at a new module called UserActivity, just added to the ProcessWire ProDevTools package.

It’s been a holiday week here in the U.S. (Thanksgiving) and the family is home, so there’s not much work getting done this week. Since I don't have much to cover in terms of core updates, I thought it would be fun to have a closer look at this new UserActivity module. This module is particularly useful with ProcessWire-powered sites or applications that have multiple users that work in the admin at the same time. The module is part of the ProDevTools package and this post will cover all the details of what it does.


### Introduction

The UserActivity module keeps track of what all logged-in users are doing on the website or application. One of the primary goals is to prevent page edit collisions so that one user does not interfere with another’s page edits. Such collisions are a potential issue for any installation that has multiple editors working at the same time, so this module can help to prevent situations where one user would overwrite another’s edits.


### Features

Below is a summary of the module’s current feature set, many of which can be toggled on/off:

The module provides live updated indicators in the Page List (and Lister) for pages that are currently being edited, and what user is editing them. This is useful to see who is editing what, but also useful as a preventative measure to keep multiple users from opening the same pages in the editor. In the screenshot below, you'll see that users "karen" and "ryan" are editing pages. (The icons are animated, which is not visible in the screenshot).

The module alerts users when they attempt to edit a page that another user is already editing, and asks to confirm that they really want to continue:

The module warns users when a page they are currently editing has been saved by another user. If the user also saves the page, they may overwrite another’s changes. This feature prevents them from unknowingly doing so:

UserActivity alerts users when a page they are editing has also been opened by another user in the page editor (but not yet saved):

In addition, UserActivity alerts users when they’ve been idle for a long time (configurable) and asks them to click anywhere to resume. When this idle period occurs, the module stops ajax-refreshing their activity as current. That way an idle session does not show up as editing a particular page. It also prevents an idle session from staying logged-in indefinitely.

Another issue that editors sometimes experience is that they may unknowingly be working in the admin when their session is actually not logged in. This can be due to a window that was opened hours or days before and returned to. Or it can be a result of a session getting lost for some security issue, or perhaps the user intentionally logged out in another window. UserActivity has a solution for this—it identifies when a user’s session is no longer active and alerts them to the situation:

Also included is a secondary module called ProcessUserActivity. This is a tool to view current user activity both in the admin and on the front-end of your website or application. It shows you all of the users that are currently logged in and what pages they are viewing or editing on your website:

While the screenshot above shows just admin activities, I want to mention that UserActivity tracks both front-end and admin activities, and both will appear here. When I took this screenshot, all logged-in users were in the admin.

The UserActivity module is highly configurable. Though the default settings are probably just right for most:


### How it works

Once installed, the module monitors all logged-in user activity on the website or application and keeps track of it in a database table for a set period of time. One of the primary reasons for doing this is to prevent page edit collisions in the admin environment.

Page edit collisions are when multiple users might attempt to edit the same page. This is a problematic situation because if more than one user has the page open in the editor and also saves it, then the users will be overwriting changes made by another user. The UserActivity module helps to avoid this situation in three different ways:

In the primary admin page lists (PageList and Lister) it adds an icon and user indicator next to pages that are currently being edited (or recently have been). This provides a useful warning to users that they may not want to begin making edits to that page. In the primary PageList this is kept up-to-date without you having to reload anything, so new edit indicators appear automatically and disappear once they are no longer current. However, there are many other ways to navigate to the page editor, so this alone is not enough...

When you open a page in the page editor, if another user already has it open then it will produce a warning and pop-up a confirmation box asking if you really want to continue with editing the page. If you click Cancel, it will exit the page editor.

If another user starts editing a page you already have open in the editor, it will alert you of the situation. Note that the other user will be aware that you are already editing the page, as they will have received the alert when they started editing. In this case, they clicked "Ok" to keep editing, despite the warning.

If a page has been modified by another user while you have it open in the page editor, a warning alert will pop-up to let you know as soon as the situation is detected.

On the admin side, this module uses ajax to re-confirm that the activity is still current after a certain number of seconds (configured as the refresh seconds in the module settings). On the front-end, activities are not re-confirmed like this, so they are no longer considered current after a configured amount of seconds.


### Keeping sessions active or idling them

Because the admin side is confirmed with ajax requests, this module also has a secondary side effect of keeping a user’s session active (logged in) while they are in the admin environment. This helps to prevent the situation where a user makes some edits and steps away for a few hours before saving, only to find out their session has expired from inactivity and their edits are lost.

Whether that is a desirable situation or not depends on your needs. For some, you might not want to create a never-ending session. As a result, the module also includes a feature to detect when the user is idle and ask them if they are still there. If they don't respond then activity tracking pauses for the user until they return and respond. If they don't return, their session expires after some period of time, as it would without this module installed.

So whether your desire is to keep sessions active indefinitely or allow them to expire as normal, this module has you covered.


### Who this module is for

This module is primarily useful on websites with multiple editors that may be working at the same time. It helps to prevent and keep them informed of situations that may result in data loss from colliding edits.

This module is also useful if you simply want to keep track of what users are doing on your website or application. It tracks both the front-end and admin and gives you a real-time picture of all logged-in users and what pages they are on.

There really is only one case where this module would not be useful, and that is on a website or application that will only ever have just one logged-in user.


### API methods

For most users, this module will run on its own without you needing to do anything from the code side. However, there are a couple potentially useful methods, depending on your use case. These methods require the UserActivity module instance, which you can retrieve like this:

```
$userActivity = $modules->get('UserActivity');
```

Get user editing a page with the `getUserEditingPage()` method:

```php
// get any page
$p = $pages->get('/');

// ask who is editing this page ($p)
$u = $userActivity->getUserEditingPage($p);

if($u) {
  echo "Page is being edited by user $u->name";
} else {
  echo "Nobody is editing that page";
}
```

Find all pages being edited with the `findPagesEditing()` method:

```
// The $items return value is a PageArray
$items = $userActivity->findPagesEditing();

if($items->count()) {
  foreach($items as $p) {
    // an '_editingUser' property (User object) is populated to each page
    echo "<p>Page $p->path is being edited by {$p->_editingUser->name}</p>";
  }
} else {
  echo "<p>No users are editing pages.</p>";
}
```


### SystemNotifications vs. UserActivity

One thing to note is that the ability to warn about editor collisions is something that the core can do at the basic level, if you install the SystemNotifications module. However, you wouldn’t typically install the SystemNotifications module for just that purpose, as it takes over the entire notifications system in PW and does a lot more that you may or may not want. The SystemNotifications module is focused primarily on managing notifications rather than user activity, while the UserActivity module is focused exclusively on managing user activity in a multi-user environment. As a result, the UserActivity module goes a lot further in this area, is much more thorough in identifying and managing collisions, and does so with very little overhead.

The UserActivity module is now part of [ProDevTools](https://processwire.com/talk/store/category/12-prodevtools/) and available for download now in the ProDevTools support board in the [support forums](https://processwire.com/talk/) (login required). In the next blog post, we'll be looking at yet another new module that I've been working on over the last year, in addition to core updates. Thanks for reading and I hope that you have a great weekend! Be sure to visit the [ProcessWire Weekly](https://weekly.pw) this weekend for the latest ProcessWire news and updates.
