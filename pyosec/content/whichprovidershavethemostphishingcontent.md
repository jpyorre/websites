Title: Which Providers Have the Most Phishing Content?
Date: 2015-06-01 10:00
Category: Research


Phishing is an efficient method for an attacker to deliver malware or harvest credentials from unsuspecting victims. By sending out a mass or targeted email designed to look like it came from a bank or other legitimate source, an attacker can acquire a fair number of user credentials or deliver malware. Credentials can be used for identity theft, additional compromise or to send more seemingly legitimate phishing emails and convincing a user to install malware can give attackers access to a system.

![1]({static}/images/research/whichprovidershavethemostphishingcontent/1phishingproviders.png#center)

---

Phishing will typically use domains from one of three sources:

* Free hosting providers, often the most basic of phishes,

* Paid hosting, typically used for targeted attacks. In an attempt to appear more legitimate, an attacker may use a domain that is similar in name to the domain they’re impersonating,

* Compromised hosts or registrars. In these cases, a website is compromised and phishing content is hosted deep within the site

* or the registrar is compromised and subdomains are configured to point to phishing content on the same or different servers.

To get an idea of what kinds of domains phishing attacks are using at present, We’ve analyzed a portion of data from phishtank.com.

Phishtank is a website run by OpenDNS where members submit potential phishes for review by other members of the community. When enough votes confirm a phishing attack, it is labeled as a verified phish. Phishtank is a relatively small slice of phishing content on the internet. We are only looking at a data set of just over 3 million reported phishing attempts. However, looking at the verified phishing attacks for just this month, we are able to see some basic patterns.


![1]({static}/images/research/whichprovidershavethemostphishingcontent/2phishingproviders.png#center)

---

To get this data, we downloaded a copy of the verified phishing attempts that were online as of this month from the statistics page at phishtank.com and performed analysis on the data using python. With the Uniform Resource Name (the part after domain.com/), we were left with domains and subdomains. We then analyzed those using the OpenDNS Investigate API to collect ASN organizational information for each unique domain. That provided a summary of organizations responsible for domains hosting phishing content.

As of this writing, 3,256,785 phishes have been submitted to phishtank and 1,837,862 of those have been verified as valid.

31,219 are currently listed as online. In our analysis, we used only the second-level domain names from all the currently online phishes and removed duplicates, leaving 9,902 unique domain names.

1,072 of these domains had no organizational attribution as they no longer resolved to an IP address, leaving us with 8,830 domains still attributed to an ASN.

The following is a graphical view of the top 10 organizations with the most phishing content:


![1]({static}/images/research/whichprovidershavethemostphishingcontent/3phishingproviders.png#center)

---

Let’s take a look at the worst offender in this analysis, CyrusOne.

CyrusOne provides colocation services, so they may not be directly responsible for maintaining the compromised or purchased hosts that are used in phishing attacks. They may be the leader in phishes from this data set at the moment simply due to their size, with two dozen data centers across the United States, Europe, and Asia.

Looking at specific domains from this set, we can see how phishing attacks operate when targeted or when using compromised or free hosting.

### Targeted Hosting

*serviceyourpaypal[.]com*

This domain appears to have been purchased specifically for use in targeted phishing attacks with the goal of acquiring PayPal credentials and stealing money from PayPal customers.

*serviceyourpaypal[.]com* was registered on September 14, 2014 at *launchpad[.]com*. It’s using domain privacy services provided by *privacyprotect[.]org* to hide administrative and technical details for the person or organization who bought the domain name.

It is hosted at Hostgator, a well known and inexpensive hosting provider and is using a shared host at the IP address of *192.185.4[.]25*. This IP address is hosting a total of 369 domain names.

![1]({static}/images/research/whichprovidershavethemostphishingcontent/4phishingproviders.png#center)

---

We can see that there is a consistent, but small amount of DNS requests for this domain when looking at its requests through OpenDNS infrastructure. The domain is not serving any useful content at present, as can be seen in the following image:

![1]({static}/images/research/whichprovidershavethemostphishingcontent/5phishingproviders.png#center)

---

However, *serviceyourpaypal[.]com* could be re-activated at any time and used in future PayPal-themed phishing campaigns. Because of its name similarity to *paypal[.]com* along with using an ASN other than what legitimate PayPal domains use.

*applesverifications[.]com*

*applesverifications[.]com* was registered on September 2, 2015 at launchpad[.]com and does not hide it’s whois information behind a privacy service. That doesn’t necessarily mean it’s factual. In some cases, adding whois privacy costs extra when registering a domain. The domain is hosted with Hostgator and its IP address hosts a total of 907 domains. It had the following content when last analyzed:

![1]({static}/images/research/whichprovidershavethemostphishingcontent/6phishingproviders.png#center)

---

The DNS traffic had a very suspicious spike in traffic on May 10, 2015 after small and consistent amounts of DNS traffic, potentially indicating other campaigns or testing prior to this specific phishing campaign.

![1]({static}/images/research/whichprovidershavethemostphishingcontent/7phishingproviders.png#center)

---

### Compromised Hosting

*bankruptcylawyershawaii[.]net*

*bankruptcylawyershawaii[.]net* appears to be a legitimate website, but was compromised at some point and used in an attempt to harvest credentials with the following phishing page:

![1]({static}/images/research/whichprovidershavethemostphishingcontent/8phishingproviders.png#center)

---

Looking at the html source of this page, we can see that clicking the ‘Verify’ button will send credentials to the file: *weba-akp.php*, which is stored locally on the website. This is the standard behavior in most commodity phishing attacks in which the phish utilizes a compromised site. Often, credentials are sent to an email that’s configured statically in the php or other file with code designed to be run on the server.

![1]({static}/images/research/whichprovidershavethemostphishingcontent/9phishingproviders.png#center)

---

The domain was registered on March 21, 2014 at *godaddy[.]com*. The whois data is not hidden as it was with the more targeted *serviceyourpaypal[.]com*.

The domain is using private nameservers provided by Hostgator. These name servers are used by customers of Hostgators reseller, dedicated and VPS hosting plans. The IP address this domain uses as its A record is hosting a total of 11 domains.

When viewing DNS requests, it’s impossible to miss the suspicious spike in traffic around April 18. That is most likely when this phishing campaign was active.

![1]({static}/images/research/whichprovidershavethemostphishingcontent/10phishingproviders.png#center)

---

### Free Hosting

*upgrade2015a.wix[.]com*

The next phish was located at the free hosting provider, wix[.]com. Anyone can use wix[.]com to host a free website. As of June 29, 2015, the following phishing page was online at upgrade2015a.wix[.]com:

![1]({static}/images/research/whichprovidershavethemostphishingcontent/11phishingproviders.png#center)

---

Wix[.]com is hosted at GoDaddy and owned/administered by Incapsula. Incapsula only had 17 domains seen used in phishing from this data set and wasn’t actually part of the top 10 worst ASN’s, but it’s a good example of free hosting being used in phishing.

Looking at the DNS requests for this subdomain, there is an obvious change in the requests which suggests this campaign started on June 26, 2015. There may have been some testing on June 23, when we see only a few requests.

![1]({static}/images/research/whichprovidershavethemostphishingcontent/12phishingproviders.png#center)

---

### Conclusion

Using just a small sample of reported phishing content, we can capture a fairly good picture of which hosting providers may be more vulnerable to compromise or more forgiving of malicious behavior. This information can be useful when considering where to host your website or online service. Additionally, just a quick analysis of data from Phishtank can be used to build a training set of indicators to look for when working to protect users across a network.
