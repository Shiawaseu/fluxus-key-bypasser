const req = require('./request.js')
const cheerio = require('cheerio')
const args = process.argv;


async function bypass(hwid) {
    const start_url = "https://flux.li/windows/start.php?HWID=" + hwid
    const header = {
        'Referer': 'https://linkvertise.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }
    console.log("Starting bypass")
    await req.request(start_url, {'Referer': 'https://fluxteam.net/'})
    // Step 1 (Start)
    await req.request("https://flux.li/windows/start.php?updated_browser=true&HWID=" + hwid, {'Referer': start_url})
    console.log("\nBypassed checkpoint 1")
    // Step 2
    await req.request("https://fluxteam.net/windows/checkpoint/check1.php", header)
    console.log("\nBypassed checkpoint 2")
    // Step 3
    await req.request("https://fluxteam.net/windows/checkpoint/check2.php", header)
    // Final (get key)
    const response = await req.request("https://fluxteam.net/windows/checkpoint/main.php",
        header // "Trying to bypass the Fluxus key system will get you banned from using Fluxus."
    )
    console.log("\nBypassed final checkpoint & getting key...")
    const parsed = cheerio.load(response['data'])
    const key = parsed("body > main > code:nth-child(5)").text()
    console.log("\nYour key is:", key.replace(/\s+/g, '') + '\n')
    console.log("If your key is a warning, run the program again.")
}

// Hacks part
bypass(args[2])
