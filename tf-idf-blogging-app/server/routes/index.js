const express = require('express');
const path = require('path');
const router = express.Router();

// const ContactControls = require('../controllers/ContactControls');
const ArticlesControls = require('../controllers/ArticlesControls');
const ArticleModel = require('../models/Article');


// @desc Login/Landing page
// @route GET /
router.get('/', async(req, res) => {
    const article = await ArticleModel.find().sort({ createdAt: 'desc' });
    res.render('home', { articles: article });
})
router.get('/home', async(req, res) => {
    const article = await ArticleModel.find().sort({ createdAt: 'desc' });
    res.render('home', { articles: article });
})

// @desc Sorting by categories page
// @route GET /categories/:tag
router.get('/categories/:tag', async(req, res) => {
    const article = await ArticleModel.find({ tags: req.params.tag }).sort({ createdAt: 'desc' });
    res.render('category', { articles: article, category: req.params.tag });
})







module.exports = router;