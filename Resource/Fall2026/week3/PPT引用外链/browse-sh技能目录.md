# browse.sh 浏览器自动化技能目录

> 来源：<https://browse.sh/>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。下文为公开页可读内容的中文整理／翻译。
# browse.sh — 浏览器自动化技能开放目录

产品／目录首页快照：汇总可在浏览器自动化场景下复用的 agent skills。

## 正文摘录

- domain·skill·method·region
- sam.gov·contract-opportunity-search·api
- xcorestudio.com·book-class·hybrid
- ticketmaster.com·find-ticket·api
- flightaware.com·track-flight·fetch
- glassdoor.com·get-company-reviews·browser
The open web catalog
A browser CLI for your AI Agents
One CLI for skills, browser primitives, debugging, and cloud sessions, designed to be driven by AI Agents.
Give AI Agents the skills to automate websites from the open web catalog. Suggested DOM selectors and XHR requests cut token costs by 50x.
$ browse skills add alltrails.com
$ browse skills add recreation.gov
$ browse skills add weather.gov
$ browse skills add plugshare.com
$ browse skills add ramp.com
 
$ claude "Plan a road trip to Utah with EV charging stops and campsites for each night. Book and reimburse on Ramp."
Drive any page with low-level primitives: click, scroll, type, hover, press. Address elements by selector or by the AI Agent's accessibility refs.
$ browse click "input#search"
$ browse type "Apartments in SF"
$ browse select @8 "Single family unit"
$ browse press "Enter"
$ browse mouse scroll 50 50 10 10
$ browse screenshot
Tail the network and console of any browse session in real time. AI Agents (and you) see exactly what the page did.
$ browse network --tail
$ browse console --tailGET  /api/listings  200  124 ms
POST /api/filter    200   84 ms
 
warn  deprecated: useLayoutEffect on server
error Uncaught TypeError: cannot read 'id'
All CLI commands work natively with local Chromium. Switch to remote sessions on Browserbase's Platform by prefixing any command with cloud.
# create a remote chromium session on Browserbase
$ browse cloud sessions create
 
# use Browserbase's Search API
$ browse cloud search "Latest White House press release"
 
# use Browserbase's Fetch API
$ browse cloud fetch "https://www.nytimes.com/section/us"
Give AI Agents the skills to automate websites from the open web catalog. Suggested DOM selectors and XHR requests cut token costs by 50x.
$ browse skills add alltrails.com
$ browse skills add recreation.gov
$ browse skills add weather.gov
$ browse skills add plugshare.com
$ browse skills add ramp.com
 
$ claude "Plan a road trip to Utah with EV charging stops and campsites for each night. Book and reimburse on Ramp."
- contract-opportunity-searchsam.gov Search active federal contract opportunities on SAM.gov by status, notice type, place of performance (state/ZIP/country), date range, NAICS, and set-aside. Returns title, notice ID, agency hierarchy, place of performance, response deadline (with time zone), notice type, and the canonical /opp/{id}/view URL. API
- book-classxcorestudio.com Reserves the daily 7 AM xBURN class at X-Core Studio's West Portal location (Mariana Tek) for a signed-in member, firing at the exact second the booking window opens so it runs unattended overnight. Hybrid
- find-ticketticketmaster.com Find upcoming Ticketmaster events for an artist, team, or show — returns venue, date, on-sale window, presale times, sold-out/cancelled/postponed flags, and the canonical event URL. Read-only, uses Ticketmaster's unauthenticated internal artist-events API behind a residential proxy. API
- track-flightflightaware.com Given an airline+flight number or tail number (and optional date), return live FlightAware status: state, origin/destination, scheduled/estimated/actual times, aircraft, route, en-route position, delay, and live-map link. Fetch
- get-company-reviewsglassdoor.com Extract a company's overall rating, sub-rating averages, recommend/outlook/CEO-approval percentages, and a filtered slice of employee reviews from Glassdoor — accepting a URL, EmployerId, or company name (+ optional location disambiguator) and supporting the full review-page filter rail (stars, job title, location, employment status, language, employment type, sort, keyword, limit). Read-only. Browser
- cali-highway-trafficabc7news.com Return current real-time MPH for every California highway covered by ABC7's traffic map — per road, per direction, with active incidents — by querying the Sigalert/Total Traffic Network JSON backend that the abc7news.com/traffic/ page embeds via iframe. API
- picture-of-the-dayapod.nasa.gov Fetch NASA's Astronomy Picture of the Day (APOD) — today's curated image or video plus title, explanation, copyright, and HD image URL. Supports any date back to 1995-06-16. API
- search-trailsalltrails.com Search AllTrails for hiking, biking, running, climbing, backpacking, or paddling trails near a location and return matching trails (name, location, lat/lon, length, elevation gain, difficulty, route type, rating, photos, description, attributes, canonical URL) as structured JSON. Browser
- search-productsamazon.com Search Amazon for products matching a query with the full filter surface (department, brand, rating, price, deals, condition, sort, pagination) and return structured JSON per result: ASIN, title, price, rating, badges, image, and canonical /dp/ URL. Browser
- search-listingsa

*[Snapshot truncated for archival size; images omitted.]*
