# Throttling AI bot traffic in ProcessWire

Source: https://processwire.com/blog/posts/throttling-ai-bot-traffic-in-processwire/

## Sections


## Throttling AI bot traffic in ProcessWire

12 September 2025 by Ryan Cramer [ 1 Comment](/blog/posts/throttling-ai-bot-traffic-in-processwire/#comments)

Many websites these days are the feeding ground for AI bots. In this post we look at a tool for taming all the hungry crawlers and bots.

One issue we’ve been running into at processwire.com is nonstop bot activity, especially from the latest breed of AI bots that have an endless appetite for collecting training data. I’m sure this issue isn’t unique to processwire.com and is probably affecting most of our sites.


### Scaling up

Because this site runs in an AWS scalable cluster, it almost never gets overloaded and instead it scales up with new server instances to accommodate all of the bot traffic. This affects the support forums more than the main PW site, as most of the main PW site is cached with [ProCache](/store/pro-cache/), and thus the bots don’t really affect it. But the [forums](/talk/) are the largest part of this site, so that’s where most of the bot activity is.


### Bots, crawlers and spiders

Many of the bots (especially AI bots) don’t seem to respect **crawl-delay** settings (from robots.txt). For instance, our crawl-delay is currently set at 10s, which the main search engine bots (GoogleBot, etc.) kindly follow. But the AI bots from OpenAI, Anthropic, Meta and Amazon (among others), seem to completely ignore the crawl-delay, and often just hit the site nonstop in rapid succession with no regard for server resources or crawl-delay. Then there are the bots that don’t reveal their identity and instead are disguised as regular web browsers, but hit the site just as hard. What to do?!

I learned recently that all of this AWS cluster scaling can get expensive, so I’ve been motivated to find a way to throttle all this bot traffic to follow the rules we’ve set in our robots.txt file. To do that, I’ve updated the [Wire Request Blocker](/store/pro-dev-tools/wire-request-blocker/) module to support a new throttling feature…


### Throttling the traffic

You can now specify “defined” throttles which throttle specific user agents (or IP addresses), and “general” throttles which throttle everything else. Once enabled and configured, when requests from the same client (or bot) come in too quickly in rapid succession, the server now responds with a “429 Too Many Requests” error. Then it counts down till they are un-throttled, and then automatically refreshes the page once the throttle time has passed (just in case it's a real user).


### Want to see it in action?

Go ahead and hit “reload” on any page in the [support forum](/talk/) 4 or 5 times quickly, and you should be able to trigger it. I’ve been running it here for a couple days and it’s made a dramatic difference in server load. I think it’s rare that real users get throttled, but we are throttling bots just about every second.

Because of this addition, the *WireRequestBlocker* module is now title “Wire Request Blocker and Throttler”. Though we’ll consider the throttling features beta until more people have had a chance to test it. It’s available for download now in the [ProDevTools](/store/pro-dev-tools/) support board [download thread](/talk/topic/14885-prodevtools-downloads-and-upgrades-updated-24-may-2024/) (login required).


### It can run outside of ProcessWire too

Unlike most ProcessWire modules, this one doesn’t actually require ProcessWire in order to block and throttle requests. That’s how it’s running here in our support forums (which uses IP.Board). You could just as easily run it in WordPress or another system. Though of course you'll be happiest in ProcessWire! The tools for configuring the module interactively from a web browser (which are optional) do require ProcessWire.


### Monitoring throttles and blocks

In addition to adding the throttling features, the latest version of the module also adds a *ProcessRequestBlocker* module, which provides an interactive and live updated view of throttled requests, which is actually pretty fun to keep a window open to. This is in addition to the blocked requests viewer, which were previously available on the module configuration screen, but are now in the *ProcessRequestBlocker* module (Setup > Blocks and Throttles).

WireRequestBlocker does a whole lot more than just throttle. There are many instances where blocking may be more appropriate than throttling. For details, see [what else Wire Request Blocker can do](/store/pro-dev-tools/wire-request-blocker/).


### Screenshots

Below: Throttle traffic for the last 5 seconds. Amazonbot and Meta's bot are blocked, and if Anthropic makes another request in the next 2 seconds, it'll also be blocked. Blocks expire after the crawl-delay time. We might have 100-200 clients being monitored for throttling at any given second.

Below: the throttles configuration screen. As you can see, we configure the throttle time for "defined agents/IPs" and "all other traffic" separately. The benefit of defining user agents to throttle is that we can throttle a bot like GPTBot (for example) that is enforced regardless of which IP address it comes from.


### Throttled bots

The *WireRequestBlocker* module comes with a default set of "defined" user agents, which are constantly being updated. Here's the current list of throttled bots below (A-Z), but you can add or remove them according to your needs.

AI2Bot, Ahrefs, Amazonbot, Applebot, Barkrowler, BitSightBot, BLEXBot, Bytespider, CCBot, Censys, ChatGPT, Cohere, Diffbot, DuckAssistBot, FacebookBot , GPTBot, Google-CloudVertexBot, Google-Extended, HeadlessChrome, ImagesiftBot, Kangaroo, MJ12Bot, MegaIndex.ru, Meta-ExternalAgent, Meta-ExternalFetcher, OAI-SearchBot, Omgili, PerplexityBot, Python-requests, SemrushBot, SERanking, Seznambot, Shodan, Sqlmap.org, Spider.cloud, Thinkbot, Timpibot, TikTokSpider, Webzio, YouBot, Vulnweb

This list is very much based on bot traffic we've seen at processwire.com, so think of it as a starting point only. Of course, user agents outside of your "defined" list are still throttled, but they are throttled by IP address rather than by user agent. We like to throttle by user agent when possible just because the same bot might hit you from many different IP addresses.
