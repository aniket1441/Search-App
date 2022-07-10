const express = require("express");
const app = express();
const cors = require("cors");
const bodyParser = require("body-parser");
const dotenv = require('dotenv').config();
const  querystring = require("querystring");
const qs = require('qs') 
const { default: axios } = require("axios");
const {Router} = require('./routers/Router')
app.use(express.json());
app.use(
  cors({ 
    origin: 'http://localhost:3000',
    credentials: true,
  })
);


const port = 3000;

app.use('/',Router);


app.listen(port, () => {
    console.log(`APP IS RUNNING AT ${port}`);
  });