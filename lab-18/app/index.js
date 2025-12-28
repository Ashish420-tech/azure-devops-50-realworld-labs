const http = require('http');

const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
  res.end('Lab-17 Azure DevOps CI Pipeline');
});

server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
