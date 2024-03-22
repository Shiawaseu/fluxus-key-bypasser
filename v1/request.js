const axios = require('axios');

async function handler(...args) {
    let config = {
        headers: args[1]
    }
    await axios.get(args[0], config)
        .then(async function(res) {
            response = res
        })
        .catch(function(error) {
            console.log(error)
        })
    return response
}

module.exports = {handler}

