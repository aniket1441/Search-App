var admin = require("firebase-admin");
var { getAuth } = require("firebase-admin/auth");
var serviceAccount = JSON.parse(process.env.GOOGLE_CREDS);
// console.log(process.env.GOOGLE_CREDS);
const app = admin.initializeApp(
  {
    credential: admin.credential.cert(serviceAccount),
  },
  "app2"
);
const bucket = app.storage().bucket("ss");
const db = app.firestore();
const otherAuth = getAuth(app);
module.exports = { getAuth: otherAuth , db , bucket };