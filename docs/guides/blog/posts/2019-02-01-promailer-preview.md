# A closer look at ProcessWire ProMailer

Source: https://processwire.com/blog/posts/promailer-preview/

## Sections


## A closer look at ProcessWire ProMailer

1 February 2019 by Ryan Cramer [ 11 Comments](/blog/posts/promailer-preview/#comments)

This week we take a closer look at the upcoming ProMailer module with a lot more details and screenshots. Plus an update on next steps with the new website and development schedule in the weeks ahead.

In the last few weeks we launched the new ProcessWire website and with that now running smoothly one of the next projects will be to redo the modules.processwire.com website to be consistent with the main site. That will probably happen in March. It took awhile to build the new website, so I had to delay a lot of client work, which I’ve been starting to get caught up with this week. I’ve got a lot to catch up with, so like this last week, February may be a more quiet month in terms of core updates and blog posts, while I get caught up with my client projects (though thankfully it’s still all PW work of course).

I'm always making continuous optimizations, improvements and issue resolutions to the core, and that happens regardless of client work. I've got some minor core updates to share, but going to wait to commit them till I've got 3.0.126 ready, which will probably be next week or the week after. While I don’t have core updates to write about in the week’s post, [last week’s post](/blog/posts/pw-3.0.125/) had some really useful additions that I’d suggest checking out if you haven’t already.

I wasn’t planning to write a post this week, but I’ve had a few people ask me about the ProMailer module that I mentioned in a previous post, and after just sending out the PW Weekly newsletter using ProMailer, it occurred to me that perhaps we should take a closer look at that this week. After all, this module is fully developed and very close to being ready for release, and while I wasn't planning on writing about it, it actually seems like a good time to. My plan is to make it available to [ProDevTools](/store/pro-dev-tools/) subscribers sometime in the next few weeks. At this point the code is largely complete and I’m focused on documentation for it.


### ProMailer background

While ProMailer is a brand new module developed alongside the new ProcessWire website, it’s also the 4th bulk-mailer module that I’ve built, with the first one being back in 2003. The 3rd version was built around 2012 and used on the old ProcessWire website. This 4th version is much more comprehensive and full-featured than the previous ones. Though I’ve learned quite a bit in developing the others, and so feel like this new one is hitting the right notes in doing all the things I’ve wanted out of email distribution, while leaving out the less useful stuff I've experienced in dedicated bulk email services. While I expect everyone’s needs are a little different, my hope is that some of you will find this new module and helpful as I have.


### About ProMailer

ProMailer is a convenient and easy-to-use tool for creating and managing bulk email distributions and subscriber lists in ProcessWire. It’s ideal for those that have real email distribution needs but don’t want or need to use a dedicated external service like MailChimp, Constant Contact or any number of other services out there. Though for many ProcessWire users, it might also be a lot more convenient because it does things that external services can’t. ProMailer puts you in full control over your email distribution, while giving you a ProcessWire-focused means of managing it. Below are a few of the key features:

**Email source flexibility:** ProMailer enables you to create emails that originate from ProcessWire pages, external URLs, or pasted in text and/or HTML.

**Subscriber/list flexibility:** ProMailer enables you to use dedicated subscriber/email lists managed directly in ProMailer, but you can also create dynamic email lists that originate from pages matching a selector.

**Custom fields:** For ProMailer managed lists, you can easily create custom fields for the subscribers, as well as import and/or export CSV files. Of course, for page-based lists, you’ve already got custom fields as well.

**Scalability:** Like almost everything in ProcessWire, ProMailer is built to scale. It can handle distributions of any size.

**Forms:** ProMailer provides both subscribe and un-subscribe forms, managing the entire subscribe/un-subscribe processes, while also giving you full control over the output.

**Double opt-in:** For new subscribers, ProMailer handles the entire double opt-in process and confirmation emails, while giving you full control over the output. Subscribers don’t become part of the list until they double opt-in. Subscribers that do not double opt-in are automatically deleted after a set number of days.

**Distribution flexibility:** ProMailer lets you choose which WireMail module you want to perform each email distribution, and lets you control how the messages are sent in terms of frequency and throttling. If your email provider limits you to a certain quantity of emails per hour (or the like) ProMailer has you covered.

**Live & background sending:** ProMailer can perform a live send that you can monitor from the browser, or it can perform a background email distribution over time that is triggered by regular website traffic. You can login to your ProcessWire admin to monitor the progress, and ProMailer will also email you when it has completed the job.

**Easy for clients:** ProMailer is exceptionally easy to use, and will be comfortable for your clients. When you are in ProMailer in the ProcessWire admin, you are either managing subscribers or messages, and that’s all there is to it.

**Comprehensive API:** For those that want it, ProMailer also has a comprehensive API for managing every aspect of messages, lists, subscribers and background queues. In fact, it may have the most comprehensive API I’ve built in a Pro module thus far. While you don’t need to use it, you may find it handy should you want to connect with web hooks from your email provider (for example, web hooks or reacting to email bounces, which vary from provider to provider).


### ProMailer Screenshots

When in ProMailer you are either managing subscribers or messages, and you can create any number of each. Messages refer to something that you are going to send via email, and subscribers refer to a list of people that will receive the email.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2541/promailer-dropdown.png)

Below is a very small list of subscribers I made for a screenshot. (I didn't want to expose anyone's email addresses except my own.) For each subscriber in this screenshot we've got an email address, a double opt-in status, and any number of custom fields (3 in this case). This is a tiny list, but if it were larger then of course you'd see pagination as well.

The next screenshot shows what appears in the "Tools" fieldset (which is collapsed in the screenshot above). As you can see we've got options for adding and removing subscribers in bulk, as well as an import CSV option. There is also an option for exporting to CSV (not shown). The most interesting part of this screenshot is the custom fields definition. Here you specify the name of the field followed by the name of a sanitizer method. Like introduced in last week's post, you can combine sanitizer methods with an underscore and/or add a maximum length when using PW 3.0.125 or newer. This method of definition remains backwards compatible with any version of ProcessWire, just without the combined sanitizer or max length instructions.

In the screenshots above you saw the built-in subscriber list options, but you can also create dynamic subscriber lists from pages. For instance, maybe you want to email all users in your ProcessWire site. Or in our case, maybe we want to email everyone in our Sites, Modules, or Developer directories every once in awhile to ask them to check that their listing is still up-to-date. As you can see, you use InputfieldSelector to match which pages should become part of the list:

Now lets take a look at the other part of ProMailer—Messages. Like with subscriber lists, you can create any number of messages. Though when it comes to sending the ProcessWire Weekly email, I typically re-use the same message and just update the subject and page that it points to. Here is what a typical message edit screen looks like below. On this screen you are telling it what it should send, who it should send it to, and how it should send:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2541/promailer-message-1.png)

Note the collapsed "placeholders" fieldset above—below is a screenshot with it opened. You can see we have predefined placeholders, as well as dynamic placeholders based on our custom fields. For page-based subscriber lists, you can also refer to any field on the subscriber page with placeholders like `{page.field_name}`. All placeholders are replaced with values from the subscriber when the email is rendered, right before it gets sent.

The last thing I'd like to show you a screenshot of is the "send" screen. This is what appears when you click the "Start sending" button the Message editor. For a "Live" send, you must remain on the screen while it completes the send, as your browser is technically triggering the server for each group of messages that gets sent. For a "Background" send, you do not have to remain on the page, as the server will take care of sending it in the background. Though you can still return to the screen any time you like to check on the progress. Once a background send finishes, it'll also send you an email to let you know it completed.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2541/pwpm-send2.png)

That's all I've got for this week. Thanks for reading, and if you have any other questions about ProMailer feel free to email me (you can see my email in some of the screenshots above) or reply below. Hope you all have a great weekend and stop by the [ProcessWire Weekly](https://weekly.pw) for the latest ProcessWire news and updates.
