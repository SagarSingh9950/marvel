const http = require("http");

const MarvelServer = http.createServer((req , res) => {
 console.log("req.headers");
 res.end("RAM RAM FROM MARVEL SERVER");
});

MarvelServer.listen(3000, () => console.log("server Started!"));
 