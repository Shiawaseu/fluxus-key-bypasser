/*

 Github: https://github.com/MEMEZNUT999/fluxus-key-bypasser

 Not working as expected? Start an issue or contact me directly.

*/
const req = require('./request.js')
const cheerio = require('cheerio')
const args = process.argv;
// Socket reset-fix
const wait = ms => new Promise(res => setTimeout(res, ms * 1000))

async function bypass(hwid) {
    const start_url = "https://flux.li/windows/start.php?HWID=" + hwid
    const commonheader = {
        'Referer': 'https://linkvertise.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }
    console.log("Starting bypass")
    await req.request(start_url, {
        'Referer': 'https://fluxteam.net/'
    })
    await wait(3)
    await req.request("https://flux.li/windows/start.php?7b20bcc1dfe26db966bb84f159da392f=false&HWID=" + hwid, {
        'Referer': start_url
    }) // This was the patch?? It's legit static LMAO
    await wait(1)
    console.log("\nBypassed checkpoint 1")
    await req.request("https://fluxteam.net/windows/checkpoint/check1.php", commonheader)
    console.log("\nBypassed checkpoint 2")
    await req.request("https://fluxteam.net/windows/checkpoint/check2.php", commonheader)
    await wait(1)
    const response = await req.request("https://fluxteam.net/windows/checkpoint/main.php",
        commonheader // "Trying to bypass the Fluxus key system will get you banned from using Fluxus."
    )
    console.log("\nBypassed final checkpoint & getting key...")
    const parsed = cheerio.load(response['data'])
    const key = parsed("body > main > code:nth-child(5)").text()
    console.log("\nYour key is:", key.replace(/\s+/g, '') + '\n')
}

// We don't really need to sanitize data, it's for you not me.
bypass(args[2])
