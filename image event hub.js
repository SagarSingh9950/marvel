const http = require("http");

// Store that massive HTML in a variable
const htmlContent = `<!DOCTYPE html>
<html class="dark" lang="en">
... (paste ypu code here) ...
</html>`;

const MarvelServer = http.createServer((req, res) => {
    // Set the header to HTML so the browser renders it
    res.writeHead(200, { "Content-Type": "text/html" });
    res.end(htmlContent);
});

MarvelServer.listen(3000, () => {
    console.log("Server Started at http://localhost:3000");
});