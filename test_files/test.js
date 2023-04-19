const pug = require('pug');
const fs = require('fs') 

fs.writeFile('test.html', pug.renderFile('test.pug'), (err) => { 
    if(err) { 
        throw err; 
    }
    console.log("Data has been written to file successfully."); 
}); 

