# ProcessWire 2.5.3 & 2.5.4

Source: https://processwire.com/blog/posts/processwire-2.5.3-master-2.5.4-dev/

## Sections


## ProcessWire 2.5.3 & 2.5.4

4 October 2014 by Ryan Cramer [ 2 Comments](/blog/posts/processwire-2.5.3-master-2.5.4-dev/#comments)


## What's new on the master branch?


### ProcessWire 2.5.3 is the new master/stable

This version adds the following:

- The ability for PageTable fields to import children as items to the PageTable. As a result, if you happen to add an item to your PageTable through some alternate means, you can still add it into your PageTable field quite easily. You'll see the option as checkboxes below any PageTable field.
- The addition of a "Recent Pages" navigation option on your top Pages menu. In here you get options to go back to recently edited or added pages. You also get an option to add new pages using the same parent/template as other recently added pages under an option called "Add another..."
- A new API function: `wireDate()`. This function works the same as PHP's `date()` function except that: 1) it will accept a date format in either PHP `date()` or `strftime()` format, OR you can specify a blank string to use the system date format, "relative" for a relative time string, "rel" for an abbreviated relative time string or "r" for an extra-abbreviated relative time string; 2) the 2nd argument (timestamp) may be a unix timestamp or an already formatted date (so long as it's one that is recognized by strtotime). See additional details in the [wireDate](https://github.com/ryancramerdesign/ProcessWire/blob/master/wire/core/Functions.php#L1112) function definition.
- Various other minor tweaks and fixes are also included in 2.5.3.

We haven't sent out an official ProcessWire 2.5 press release just yet because we're hoping to get ProcessWire ListerPro ready to use and available in the ProcessWire store, so that we can accounce that at the same time. We are almost there! But if you are reading this, then of course you already know ProcessWire 2.5 is out and ready to use. Hopefully I can introduce ListerPro to you in next week's blog post.


## What's new on the dev branch?


### New notifications system

Antti (apeisa) and I are excited to accounce a new notifications system for ProcessWire. Special thanks to Avoine for sponsoring this. It's still in development, but far enough along to already be useful, so we've gone ahead and committed it to the dev branch.

The new notifications system builds upon and in many cases replaces ProcessWire's existing notices system. What is ProcessWire's notices system? … They are the success or error messages that you see at the top of the screen after performing some action. The new system, called "System Notifications" actually steals the existing notices and takes over responsibilty for displaying them. But that's just one of many things the new notifications system can do… We mention that to give you a point of reference, because both notices and notifications provide messages to users in the ProcessWire admin. Here's a few highlights of what makes the new notifications system so cool:

**They are live and ajax driven** An event that occurs at the server gets pushed to you immediately, rather than the next time you request a page. The new SystemNotifications module includes a few examples of this by letting you enable notifications for 404s, user logins and logouts. These may not be that useful for more than demonstration purposes, but they do a good job of revealing the the bigger picture of what's possible.

**They may be sent to any user (not just the current user)** If the user isn't logged in, they will get the notification next time they login. Notifications of this type will persist across requests until the user dismisses them. This is quite a contrast to the existing notices system which knows nothing about users or persistence. You can send a notification to any user from the API side simply by retrieving the user you want to send to and then populating their 'notifications' field with a new notification (more details coming soon).

**Flavors and customization** Notifications come in 3 primary flavors: message, warning and error. Each can be customized with icons, contain both a title and body (optionally in HTML).

**Email and progress** Notifications can be carbon-copied to the user's email address (using PW's WireMail). They can also support a progress state, enabling you to have a notification with a progress bar in it that live updates.

**They don't get in the way** The user can see that they've got notifications by the presence of a "bug" at the top of the screen with a number in it. When new notifications appear, they are also ghosted on the screen for a second or two. If the user wants to view their notifications, they can click the bug to reveal them.

**They have both a PHP and Javascript API** Notifications can be initiated from either the PHP side or the Javascript side. While we are still working out the details of the API, there is a lot of fun stuff coming here.

**How to install and test** This is a work in progress, to stay tuned for more. If you are on PW's dev branch (2.5.4) you may want to install the new SystemNotifications module. Here are the steps to do that:

- In the admin go to Modules > Refresh (so PW can self discover the modules)
- In the top navigation, drill down to Modules > Install > SystemNotifications, and complete the installation.
- Next you'll see the SystemNotifications configuration screen. Open another window and load a non-existent page or two on your website to see the 404 example notification. Next try logging in from another browser and you should get notifications about that.

Keep in mind these notifications are just for demo purposes, and you may want to disable these on a live site (especially the 404 one, so you don't end up with hundreds of notifications next time you login).

Next week we'll go a little more in depth on how to use the notifications system from the API side.

*Yes we'll come up with a different color for warning notifications. *
