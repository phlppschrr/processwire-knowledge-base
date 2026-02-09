# Lots of module updates

Source: https://processwire.com/blog/posts/lots-of-module-updates/

## Sections


## Lots of module updates (Matrix, FormBuilder, GoogleClientAPI)

17 May 2019 by Ryan Cramer [ 4 Comments](/blog/posts/lots-of-module-updates/#comments)

In this post we take a quick look at the new version of ProFields Repeater Matrix, yet another new version of FormBuilder, and a new version of the GoogleClientAPI module.

I’d planned on a more extensive blog post today, alongside several core updates. But found out today I’ve got to put my cat to sleep, and now don’t feel like doing much, so going to keep this blog post short. While we won't get into core updates, I do have some good module updates to mention here though.


### Another new version of FormBuilder

We had a new version of FormBuilder [last week](/blog/posts/formbuilder-v38-released/), and next week we’re going to have another. My biggest project of the week was getting the save-to-GoogleSheets (spreadsheet) action working in FormBuilder. And it’s now up and running, plugging along beautifully on a project already (a client needed it right away). Being able to watch live form submissions get submitted, process in Stripe, save to the server, and then get a copy inserted into a new row in a Google Sheets spreadsheet makes me smile. I think this is a great new feature for FormBuilder, and since it’s all functional already, I thought I’d go ahead and release it in the FormBuilder board next week.


### Google Client API module update

Related to the above, I’ve got a new version of the GoogleClientAPI module ready as well. It is required in order to have FormBuilder talk to Google Sheets. The updates are ready but I’m still working on the documentation and setup guide, so that’ll be coming out next week alongside the new version of FormBuilder. The GoogleClientAPI module is not a commercial module—this is instead an update to the existing module originally released in 2016, but now getting a major update, which I’ll post next week.

The module now includes a fairly extensive API to Google Sheets. Future plans for the module include expanding the existing Google Calendar API and adding an API for Google Drive as well. Google's API client already provides access to dozens of their services, but the problem is that their API is kind of difficult to use and extremely verbose and technical. So the goal of the ProcessWire GoogleClientAPI module is not just to take care of all Google authentication stuff, but also to build much simpler-to-use ProcessWire-like APIs on top of Google ones.


### Repeater Matrix v5

Finally, a new version of Repeater Matrix (v5) has been posted in the ProFields board today. Here’s a summary of what’s new:


### Screenshots

Configuring Google Sheets settings in FormBuilder:

ProFields Repeater Matrix: Clicking the gear icon at the top of the repeater item slides down a "Item type" selection, enabling you to change the type:

On the Repeater Matrix field configuration screen, you now have an Import button, enabling you to add a new type by importing from any other Repeater Matrix field. After clicking the button, a new item with label "New Matrix Type (Import)" appears:

You can now also configure what matrix types are shown on a per-template basis (known as field/template context). To access this, you would edit any template that has a Matrix field (Setup > Templates > Edit), then click on the Matrix field in the list of fields and it opens a modal, enabling you to configure settings for the field in the context of that template. Click the Input tab, and you'll see this option:

That's all for this week. Have a great weekend and hope to see you at [ProcessWire Weekly](https://weekly.pw).
