# browse.sh — open catalog of browser automation skills

> 来源：<https://browse.sh/>
> 抓取时间：2026-11-02（Asia/Shanghai）
> 说明：PPT 引用外链归档（非课堂转写）。版权归原作者／机构所有；图片未下载。
> Product/catalog homepage snapshot; not a recursive asset dump.
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
- search-listingsairbnb.com Search Airbnb for short-term rental listings in a given location and date window — supporting the full filter surface (dates, guests, price, place + property type, bedrooms / beds / baths, amenities, booking options, accessibility, host language, the top-of-page category rail, and map bounding box) — and return each matching property as structured JSON via the SSR StaysSearch GraphQL blob embedded in the page. Read-only. Browser
- search-listingscraigslist.org Search Craigslist in a given city and category for listings matching a query, returning each listing's title, price, location, posting date, and listing URL. API
- find-snapshotarchive.org Find Internet Archive Wayback Machine snapshots for a URL — single closest, date range, host/prefix enumeration, or full history — returning archived URL, capture timestamp, HTTP status, MIME type, SHA-1 digest, and WARC-record length. Read-only. API
- find-trains12306.cn Query China Railway (12306.cn) for the train schedule between two stations on a given date — train number, departure/arrival station + time, journey duration, and per-class seat availability. Read-only; no login. Hybrid
- find-and-add-to-cartvuoriclothing.com Search the Vuori Clothing catalog for a product, open the product detail page, select the requested size and color, and add one unit to the bag. Read-only beyond the cart drawer — never proceeds to checkout. Browser
- search-recipesallrecipes.com Search Allrecipes for recipes (keyword, ingredient list, category browse, or direct recipe URL) and return structured JSON with ratings, ingredients, instructions, nutrition, times, and full media — by parsing the SSR HTML search cards and each recipe page's schema.org LD+JSON Recipe block. API
- discover-industrial-opportunitiesamericanreindustrialization.com Discover companies, startups, suppliers, and job opportunities across American reindustrialization — manufacturing, energy, defense, aerospace, robotics, semiconductors, and industrial software — via the site's public JSON REST API at /api/* (companies, jobs, categories, tags). API
- search-rentalsapartments.com Search Apartments.com for rental listings in a city (optionally filtered by price, bedrooms, or type) and return each property's name, address, rent range, bed range, phone, and listing URL plus the total result count. Read-only. Browser
- search-documentationalgolia.com Search algolia.com/doc for documentation pages matching a free-text query and return ranked hits with section hierarchy, snippets, and direct anchor URLs — via the public hosted DocSearch API, with a per-page markdown fallback. API
- find-yoga-meditation-classapp.ompractice.com Find upcoming live yoga, meditation, tai chi, breathwork, and movement classes on Ompractice that match a user's interests, availability, experience level, intensity preference, and class-length preference. Uses Ompractice's unauthenticated DRF API at api.ompractice.com. Read-only — does not book. API
- search-tennis-utrapp.utrsports.net Search Universal Tennis Rating (UTR) for players by name and return each match's UTR (singles + doubles), three-month rating, profile id, nationality, location, pro status, and third-party rankings via the public api.utrsports.net REST API. API
- ai-company-searchartificialintelligencecompanies.com Search artificialintelligencecompanies.com to find AI vendors and startups serving a given niche or addressing a given problem, returning name, canonical URL, and description per match via the site's public JSON API and JSON-LD category pages. API
- manage-candidate-profileashbyhq.com Search Ashby ATS for a candidate by email or name, read their full profile (contact info, applications, tags, custom fields, notes), add a note, and submit structured interview feedback against an application — via Ashby's documented REST API. API
- cli-setupauto.dev Install, authenticate, and use the Auto.dev `auto` CLI (npm @auto.dev/sdk) for any automotive-data task — VIN decode, specs, listings, recalls, payments, plate lookup — plus MCP wiring for AI agents. CLI
- longtermavis.com Search Avis.com for long-term (15-330 day) rental car options at US locations. Returns per-class daily/total prices with pay-now vs pay-later, plus the cheapest deal across the fleet. Read-only; designed for looped multi-location scans to surface unusually cheap long-term deals. Browser
- compare-savings-ratesbankrate.com Return ranked Bankrate savings, money-market, and CD rates as structured JSON — bank name, account name, APY, minimums, fees, FDIC/NCUA status, Bankrate score, editorial copy, last-updated timestamp, and affiliate Open Account URLs (captured, never followed). Lead with a Browserbase Fetch of the editorial best-of article; fall back to a remote browser session for the dynamic WRT (Wealth Rate Table) widget when filter dimensions exceed what static HTML exposes. Fetch
- news-homepagebbc.co.uk Return the current set of top stories from the BBC News homepage — title, summary, canonica

*[Snapshot truncated for archival size; images omitted.]*
