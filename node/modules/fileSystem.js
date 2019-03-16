const fs = require('fs');

const files = fs.readdirSync("./")
console.log(files)

fs.readdir('$',(error, files)=>{
    if(error) console.error('Error', error)
    else console.log("Result:", files)
})