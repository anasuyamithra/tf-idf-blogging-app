const mongoose = require('mongoose');
const marked = require('marked');
const slugify = require('slugify');
const createDomPurify = require('dompurify');
const { JSDOM } = require('jsdom');
const dompurify = createDomPurify(new JSDOM().window);
const Schema = mongoose.Schema;

const ArticleSchema = new Schema({
    title: {
        type: String,
    },
    description: {
        type: String,
    },
    body: {
        type: String
    },
    tags: [{
        type: String
    }],
    createdAt: {
        type: Date,
        default: Date.now,
    },
    slug: {
        type: String,
        required: true,
        unique: true
    },
    sanitisedHTML: {
        type: String,
        required: true
    }
});

ArticleSchema.pre('validate', function(next) {
    if (this.title) {
        this.slug = slugify(this.title, { lower: true, strict: true })
    }
    if (this.body) {
        this.sanitisedHTML = dompurify.sanitize(marked(this.body));
    }

    next();
})

module.exports = mongoose.model('Article', ArticleSchema);