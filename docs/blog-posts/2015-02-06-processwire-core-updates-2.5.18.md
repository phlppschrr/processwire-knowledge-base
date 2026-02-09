# ProcessWire core updates (2.5.18)

Source: https://processwire.com/blog/posts/processwire-core-updates-2.5.18/

## Sections


## ProcessWire core updates (2.5.18)

6 February 2015 by Ryan Cramer [ 3 Comments](/blog/posts/processwire-core-updates-2.5.18/#comments)

Discussion on the latest updates to ProcessWire's dev branch, available as version 2.5.18.


### Field editor now lets you target templates

Previously the only way to add a field to templates was from the template editor (Setup > Templates > some-template). If you created a new field and needed it in a lot of templates, you'd likewise be editing a lot of templates.

As has been the trend in recent weeks, we've added another time-saving optimization this week. Now you can add a field to one or more templates directly from the field editor. And thanks to a follow-up PR from Adrian, you can remove them too.

Next time you are adding or editing a field, take a look at the new "Actions" tab in the field editor (Setup > Fields > some_field). You'll see something like this screenshot below. Essentially, it enables you to check boxes next to any template to automatically add the field to the template. Or you can un-check already checked boxes to remove the field from those templates. The next screen confirms your changes, giving you the opportunity to choose where exactly the field should be added in each of your selected templates.

You might also notice this screen serves a useful informational purpose, telling you exactly how many pages have populated data for the field you are editing. If you are editing a field that supports multiple values, you will also see a "Rows" column, that tells you how many rows of data total are populated (which will usually be some number higher than the quantity of pages).

Next is the confirmation screen. Here you can choose where new fields will be placed in each of your selected templates. If you've opted to remove any fields from templates, you'll be asked to confirm that too, as you'll be deleting rows of data from the database.


### Optimization to field cloning

We've also put in an improvement to the field cloning process. The "clone field" option now lives on the new "Actions" tab in the field editor. Previously it was a checkbox that–when checked–would create a duplicate copy of the field. If you were cloning field "body" it would create a copy called "body_1". The problem with that was that it always necessitated going back and editing the new "body_1" field and renaming it to your designed field name. We've now removed that unnecessary step. The new "clone field" option now asks you for the name of the clone you want to create, saving you more time.


## Session improvements

Several improvements have been put in place to sessions this week:

- A separate session log is now kept of all logins, logouts, and failed logins. You'll see it under Setup > Logs > session.
- If sessions aren't writable to the file system for one reason or another, PW will now automatically switch to database-driven sessions.
- And a lot more… see below:


### Live-updated session viewing tool

The session viewing tool included with our database-driven sessions module (SessionHandlerDB) is now more useful, giving you a real-time, live-updated view of all users on your site and what page they are visiting. It's rather fun to watch when you've got a lot of visitors. If you've not tried out database-driven sessions in ProcessWire before, you might like the additional access to sessions that it provides. You can install it from Modules > Install > SessionHandlerDB.


### Session cleanup on certain Debian-based servers

Those running on certain Debian-based servers may have found that session files never get cleaned up. It turns out that they replaced PHP's session cleanup (garbage collection) with something proprietary that doesn't replace the expected behavior of PHP's native session cleanup. The result was session files that never get deleted. But it's not all a bad thing, as there are apparently some security benefits to letting these servers have full control over the session files. So we now attempt to detect this environment and accommodate it. Specifically, we let those Debian-based installs store session in the alternate location where their garbage collector works, rather than in PW's default sessions directory (where their session cleanup doesn't work).


### Configurable session fingerprints

Session fingerprints (a security feature) are now configurable. See your /wire/config.php for the various options. To summarize, you can now configure whether you want sessions fingerprinted to actual IP address, forwarded (client) IP address, browser user agent string, or any combination of these. Most will likely have no reason to configure this, but there are some that need to deal with users on dynamic IPs, where this will be very handy. Configurable fingerprints enable you to you benefit from the additional security of session fingerprints rather than having to disable them completely in such dynamic IP scenarios.


### Session history from the API

There is a new `$config->sessionHistory` variable that contains the number of last-visited pages to remember for each session. That history can be retrieved at any time from the new `$session->getHistory()` method. That method returns an array of session history, with each item itself being an array that contains url, page (id), and time (unix timestamp). The url property includes any URL segments or page numbers as well. At the simplest level, you might use this to display a "pages you recently visited" navigation list to the user. This feature is not enabled by default. If you'd like to use it, simply set the `$config->sessionHistory = 10;` in your /site/config.php file, replacing "10" with whatever quantity of most-recent history items you want it to remember for each session.
