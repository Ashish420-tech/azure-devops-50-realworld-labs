const http = require("http");

http.createServer((req, res) => {
  res.end("Lab-13: Auto deployed from Azure DevOps 🚀");
}).listen(3000);

console.log("Server running on port 3000");
