const ArticleInfo = require('../models/Article');

exports.postArticle = async(req, res) => {
    const Article = new ArticleInfo({
        title: req.body.title,
        description: req.body.description,
        body: req.body.body
    })
    console.log(Article);
    try {
        article = await Article.save();
        res.redirect(`/articles/${article.id}`)
    } catch (error) {
        console.log(error);
        res.render('new', { article: article });
    }
}