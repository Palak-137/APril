let express = require( 'express' );
const fs = require('fs');
const ndjson = require('ndjson');

let app = express();
let server = require( 'http' ).Server( app );
let io = require( 'socket.io' )( server );
let stream = require( './ws/stream' );
let path = require( 'path' );
let favicon = require( 'serve-favicon' );

app.use( favicon( path.join( __dirname, 'favicon.ico' ) ) );
app.use( '/assets', express.static( path.join( __dirname, 'assets' ) ) );

app.get( '/', ( req, res ) => {
    res.sendFile( __dirname + '/index.html' );
} );

let drawing = [];
fs.createReadStream('./src/assets/bear.ndjson')
  .pipe(ndjson.parse())
  .on('data', function(obj) {
   
    drawing.push(obj);
  })

  app.get('/bear', (req, res) => {
    const r = Math.floor(Math.random() * drawing.length);
    res.send(drawing[r]);
  });
  



io.of( '/stream' ).on( 'connection', stream );

server.listen( 3000 );
