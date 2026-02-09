# A look at the new Page Edit Restore module

Source: https://processwire.com/blog/posts/page-edit-restore-module/

## Sections


## A look at the new Page Edit Restore module

12 May 2023 by Ryan Cramer [ 2 Comments](/blog/posts/page-edit-restore-module/#comments)

The new Page Edit Restore module helps to prevent page edits in the admin from getting lost when the user’s session is lost.

It prevents lost page edits in a couple of different ways. First, it pings the server in the background at regular intervals to prevent the session from timing out. But if the user still gets logged out (for whatever reason) it alerts them that they are no longer logged in, and gives them instructions on how to save their edits. When there are unsaved edits present, the page editor provides the ability to restore, preview, test or delete them. In this post, we'll take a closer look at this new module.


## Why use this module?

What might cause someone to lose their session while editing page (and thus lose edits)? It's surprisingly not that uncommon, and this module attempts to limit or completely prevent the cases where someone could lose work. Below are a couple examples of cases where this module can save the day.


### User starts editing a page and returns later to save

A common source of session loss is when a user starts making edits to a page and then leaves before saving their changes. They might assume they can come back tomorrow and save, and all will be fine. But if a significant amount of time passes, their session may timeout, leaving them logged-out. When they come back a day or two later to save their changes, they hit “Save” and discover that they are no longer logged in, and their changes are lost.


### User’s dynamic IP address changes while making edits

For security, ProcessWire maintains what's called a “session fingerprint” in order to validate the user session. This is a typically snapshot of the user’s IP address and details of their browser. If any of these details change, the session is no longer valid (and user is logged out). This ensures that an attacker can’t capture a user’s cookies, substitute them in their browser, and then take over the session. So having a session fingerprint is a valuable security measure.

The downside of having a session fingerprint is when you have a regularly changing dynamic IP address, like you might have when using a cellular network for your internet. But your IP can also occasionally change even on a wired internet connection, unless you literally have a static IP address.

Also consider the case of a user that starts making an edit on their notebook computer at work, closes it, takes it home and continues making edits. Their IP address would change in this case, so the session that began at work would no longer be logged in, once at home. If the user had the page editor open at work and didn't save their edits, those edits would be lost if they tried to save them at home.

In ProcessWire, you can disable the session fingerprint by setting `$config->sessionFingerprint = false;` in your /site/config.php file. But since it's a good security measure, it's obviously not ideal to disable it. So for most, a change of IP address or other browser details will cause the session to be lost.


### Other reasons for session loss

These ones are less common for production sites, but there are cases where the session can be lost due to PHP session settings, aggressive garbage collection, output prior to http headers, load balancers, and more. A session is something that requires a lot of details coming together in just the right way, and occasionally it's not obvious why a session was lost.


## How does it work?

This module monitors POST requests to the page editor URL that are made from a non-authenticated (guest) user. When it detects such a request, it checks the validity of it (see the “How is security maintained?” section), and then it saves all the data in that POST request to a temporary file on the server.

Whether this module is installed or not, ProcessWire responds to such requests by displaying the login form. So when this module is installed, it delivers a notification above this login form indicating that the user’s edits have been saved, and what they need to do to restore them to the page.

Once the user is logged-in and editing the same page, a new field appears at the top of the page editor telling them that there are unsaved changes. It gives them the following options:

- Restore unsaved changes now
- Test what will be changed when restoring unsaved changes
- Preview unsaved changes in a modal window (raw POST data as JSON)
- Delete unsaved changes
- Ignore (decide later)

Assuming the user just lost their edits due to unintended logout, chances are they'll want the "Restore unsaved changes now" option, though they may want to "Test" or "Preview" first.

If the user doesn't remember losing any changes, then they'll want to "Delete unsaved changes".


### What kinds of changes can the module save and restore?

This module doesn't focus on (and isn't aware of) any particular types of fields, and instead just focuses on saving and restoring the raw POST data.

The largest use case for this module is likely TinyMCE and CKEditor fields, where someone might spend significant time making text edits, and where the loss of a session could result potentially in a lot of lost work. However, this module will save and restore *all* the data for *all* the fields that were present in the POST request. So far, this seems to be compatible with all the fields I have tested with, but there are feasibly cases where it might not work, cases that just haven't been identified yet. In any case, the hope is that we can at least restore most of the data that would otherwise get lost without this module.

File uploads are one case we can identify so far where this module is not going to allow restoring of unsaved changes. The reason for that is that we save the data from the `$_POST` and not from PHP’s `$_FILES`, or ajax-submitted file data.


### Crossover with the UserActivity Pro module

This module duplicates one feature of the UserActivity module, which is to prevent the session from timing out by routinely pinging the server in the background.

The UserActivity module takes this feature further by also enabling you to set an idle timeout, where the pinging will slow or stop after a defined period of time. Though having an idle timeout can be seen as useful or not, depending on your needs.

The UserActivity module also maintains the ping throughout the entire ProcessWire admin, while the PageEditRestore module maintains it just in the page editor, where session loss is most likely to affect a user.

While the UserActivity module does a lot more than this module does, it does not have the ability to restore unsaved changes the way that this module does. After all, that's not the purpose of the UserActivity module. As a result, you may find it worthwhile to have both UserActivity and PageEditRestore installed together. Should you have them both installed, I recommend setting the "ping time" setting for this module to a higher value, such as 600 (10 minutes) or higher. That way it won't overlap as much with the UserActivity pinger.


## How is security maintained?

This is the tricky part because we are essentially bypassing the requirement of a logged-in user to save content in the page editor, or at least that's how it appears. In reality, the page editor is never loaded if the user isn't logged in, and this module is just monitoring POST requests to the URL that *would be* for the page editor, if the user was logged in.

Nevertheless, this module is still saving data that will ultimately be loaded into the page editor when the user chooses to "Restore" their unsaved changes. if the module were in wide use, it seems like it could be a potential target for anonymous undesirable POST requests. To combat this, the module does 3 things:


### Step 1: Maintaining a unique token per page and user

In order for a non-authenticated POST request to be allowed, it must contain a token unique for the page being edited and the user making the edits. The token is a combination of the page id and creation time, user id and creation time, the ProcessWire installation timestamp, and the ProcessWire installation’s unique `$config->tableSalt` value (a unique string created by the ProcessWire installer). So an attacker would have to have access to both the database and the file system, or the user’s browser at the time they are making or saving edits, in order to obtain all of these values.

This unique token is bundled into each edit made to the page while in the page editor. When this module saves the non-authenticated POST (containing unsaved changes) this token must be present and have the correct value before it'll save the non-authenticated POST request.


### Step 2: Setting a cookie for the user in the page editor

When an authenticated user opens a page for editing, ProcessWire creates a cookie with a long random value that is set to the client and server simultaneously. This cookie persists whether the user is logged-in or not, and the cookie must be present in the non-authenticated POST request before this module will accept the data as unsaved changes for the page.

The intention of this cookie is just to identify that the user at least *was* in the page editor, editing a particular page. The random value that it contains must match a copy of the same value stored on the server.


### Step 3: Setting a cookie for a non-authenticated POST

If the two above conditions are met, and we've reached the state of accepting a non-authenticated POST request as unsaved changes for a page, we set yet another cookie to indicate that the client *did* submit an accepted POST request. Like the previous cookie, this one also contains a long random string that is duplicated on the server.

Once the user is logged-in and editing the page that unsaved-changes were submitted to, the cookie that was set prior to login must still be present and have the expected random value before this module will let the user do anything with the data.

The intention of this cookie is to verify that the now logged-in user editing the page is, in fact, the same user (and browser) that submitted the non-authenticated POST request (that contained the unsaved changes).


### Previewing before restoring

Finally, the user can preview the data they are going to restore before actually restoring it. This module adds a link to a modal window that reveals the full contents of the unsaved changes, enabling the user to inspect and preview these changes before they restore them. This is essentially raw POST data encoded as readable JSON, as it has not yet been restored to a page.


### Placing limits on what can be restored

In addition to the security measures above, this module places some additional limitations on what it will let you restore. One user cannot restore data for another, for instance. Meaning, if there is unsaved data for a page, only the user that created it will be able to see it, restore it, or even know about it. This ensures that irrelevant unsaved changes are properly ignored (or deleted) and that all unsaved changes are tied directly to a specific page and user and remains confidential to the user until they are ready to commit them to the page.

Also note that unsaved changes that are saved, but not restored within 1 day, are automatically deleted.


### Disabling the security cookies

If the user lost their session due to all their cookies getting cleared (for whatever reason) then the security cookies mentioned in Step 2 and 3 above would prevent the user from saving their unsaved changes. For this reason, you can optionally disable the security cookies in the module’s settings. However, I think the loss of cookies is less likely, unless the user has some security software that wiping out their cookies automatically.


## Installing and configuring the module

The module is installed by extracting and placing its files in a new directory (that you create) called /site/modules/PageEditRestore/. Once the files are placed in that directory, login to your admin and to go Modules > Refresh. Click “Install” for the PageEditRestore module.

By default, this module is configured with everything enabled, and this is likely the best place to start. If you find you need to disable some part of it, return to the configuration and adjust as needed.


### Testing the module

I recommend that you test the module to make sure that it works properly in your environment. Here is a simple test that you can perform:

Next you'll want to test the logout popup notification. This is what alerts you when you've been logged out and gives you further instruction.

Once you've verified that everything above works as you expect, you don't need to do anything further. PageEditRestore should be otherwise invisible, working quietly in the background. You likely won't see it again until you need it due to a session loss.


## Other considerations

There are times when a session and its data really should expire, because the data is old. It's feasible that this module might invite cases where someone saves edits that have been sitting around for days, and are truly out-of-date. Saving such edits might overwrite more up-to-date content already saved by another user or in another session.

For this reason, the PageEditRestore module alerts the user when the page they are restoring to contains more recent edits that may be lost by restoring. But whether the user ultimately pays attention to that is another matter.

The important thing to note is just that providing the ability to restore edits does open up new considerations with regard to the age of data being saved. These considerations become more important as the quantity of people making edits increases.


## Should it be a core module?

I've built this module with the idea that it may be added to the core. It's one of those things that I think most people won't know they need until the situation strikes. So it would be ideal to have it present in any ProcessWire installation. You may only ever need it once, but once is enough to make it worthwhile, as it may save significant time and frustration for you or your clients.

On the other hand, some may never need it, and it's an autoload module that would always be running in the background, even if quite well optimized. And admittedly, I have a certain level of discomfort with providing an ability to save non-authenticated data that’s ultimately intended for the page editor… though I think I've allayed that, see the Security section.

So I'm not sure whether this module will go in the core, remain in the modules directory, or go into ProDevTools (since it has some crossover with that module set). I'm seeking your input on where you think it belongs? Or perhaps, do some parts of this module belong in the core (like the ping feature) while others belong in a separate module?


## Download

This module is available for download and installation now in the modules directory.

[ Download module](https://github.com/ryancramerdesign/PageEditRestore/archive/refs/heads/main.zip) [ Module directory page](https://processwire.com/modules/page-edit-restore/)
