const express = require('express');
const mongoose = require('mongoose');
const { PythonShell } = require('python-shell');
const dotenv = require('dotenv');
const path = require('path');
const passport = require('passport');
const unicorn = require('unicorn').install();
const methodOverride = require('method-override');
// import forms from './dbForms.js'

const logger = require("./server/middleware/logger");
const connectDB = require('./server/config/db.js');
const mongoConnect = require('./server/util/database').mongoConnect;



// Load config
dotenv.config({ path: './server/config/config.env' })
mongoose.set('useCreateIndex', true);
// connectDB(); // Mongo Stuff

// App Config
const app = express();
const PORT = process.env.PORT || 8001;

// DB Config




// Body Parser Middleware
app.use(express.text())
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// Handlebars Middlebars
// app.engine('.hbs', exphbs({
//     defaultLayout: 'main',
//     extname: 'hbs',
// }));
//app.set('view engine', '.hbs');

app.set('view engine', 'ejs');

app.use(express.static(path.join(__dirname, 'server', 'public'))); // static path
app.use(methodOverride('_method'));

app.use('/', require('./server/routes/index.js'));
app.use('/articles', require('./server/routes/articles.js'));


// app.use(logger);







// DB Config     Mongo Stuff
// mongoose.connect(connection_url, {
//     useNewUrlParser: true,
//     useCreateIndex: true,
//     useUnifiedTopology: true,
// });

mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => {
        app.listen(PORT, () => {
            console.log(`Server listening on ${PORT}`.cyan().blinking().underline());

        });
    })
    .catch(err => console.log(err));


// App Endpoints