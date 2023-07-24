/*
 Made by MEMEZNUT999, modified by some kid
*/
const req = require('./request.js')
const cheerio = require('cheerio')
const args = process.argv;

async function bypass(hwid) {
	try {
    const commoncookie = "Anti-Bypass=BypassersKHTTP_VERSION5069e4e61337c2fbea2368f9da1a07725f2a65bb1eab2d8de6dc9cf83e7a683e; .pipe=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJLMGc4SjNsRmY1TW43UWw4bVh5bytpNnVBeGh4aWFSYTU2bldDZEcxQnlNPSIsImUiOjE2ODkyNTAyODEsImlzc3VlZCI6MTY4OTI0NjY4MS44MzksInNhbHQiOiJzYWx0eSIsImNvbm5lY3RvciI6LTF9.tHnUGnosgCctAafGTgta4F1_1KQezhvdIATrj9YwQU0"
    const start_url = "https://flux.li/windows/start.php?HWID=" + hwid
    const commonheader = {
        'Referer': 'https://linkvertise.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }
    console.log("Starting bypass")
    await req.request(start_url, {
        'Referer': 'https://fluxteam.net/',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    })
    await req.request("https://flux.li/windows/start.php?7b20bcc1dfe26db966bb84f159da392f=false&HWID=" + hwid, {
        'Referer': start_url,
        'Cookie': commoncookie
    })
    console.log("\nBypassed checkpoint 1")
    await req.request("https://fluxteam.net/windows/checkpoint/check1.php", commonheader)
    console.log("\nBypassed checkpoint 2")
    await req.request("https://fluxteam.net/windows/checkpoint/check2.php", commonheader)
    const response = await req.request("https://fluxteam.net/windows/checkpoint/main.php",
        commonheader // "Trying to bypass the Fluxus key system will get you banned from using Fluxus."
    )
    console.log("\nBypassed final checkpoint & getting key...")
    const parsed = cheerio.load(response['data'])
    const key = parsed("body > main > code:nth-child(5)").text()
    console.log("\nYour key is:", key.replace(/\s+/g, '') + '\n')
	} catch (error) {console.error("Socket died.. Retry."); bypass(hwid)}
}

bypass(args[2])
