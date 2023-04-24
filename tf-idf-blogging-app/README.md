# 📝 Tf-IDF Blog CMS with _search_ and _automated tagging_ 

```diff
+ Sample CMS built with MEN Stack
+ Automated Tagging added (stopwords for markdown not added)
+ Search functionality added (using document similarity implemented with cosine similarity)
```
This project seeks to create a content management system (CMS) for a online publishing platform with features to enhance user retention, overall user friendliness and help admin users to perform CRUD operations on their respective articles.

The project seeks to automate the process of placing the articles under topics/tags without the need for users to add it in themselves, helping the users focus solely on the content they upload, rather than how viewers find their articles.

It uses the NLP Text Pre-Processing Alogrithm, TF-IDF, to automate this task and properly annotate each article with tags generated on how important a specific feature is to the article.

When a query is passed into the search bar, we use _cosine similarity_ to find the most similar document(article) which corresponds to the query. Thus the query can be typed in natural language, and the web application will provide the top 4 similar articles to the query made.


### 🔧 Working with the following technologies:

- Node.js and Express.js
- Mongoose and MongoDB
- Passport's authentication
- EJS's templates

### 🈯 Languages used:
- Python
- Javascript

### 👷 Working Example:
- #### Working of Search Functionality
<img src="https://user-images.githubusercontent.com/60477228/113505811-cb95f900-955e-11eb-9a37-f54f71df72ff.png" width="500">
<img src="https://user-images.githubusercontent.com/60477228/113505837-e6686d80-955e-11eb-86ed-3268f61b5901.png" width="500">


- #### Working of Automated Tagging

<img src="https://user-images.githubusercontent.com/60477228/113505992-af468c00-955f-11eb-8769-7309f03c1eb3.png" width="500">
<img src="https://user-images.githubusercontent.com/60477228/113505981-9d64e900-955f-11eb-848c-6c1e6f8fbfdb.png" width="500">
<img src="https://user-images.githubusercontent.com/60477228/113506902-1ca8eb80-9565-11eb-948f-3016cee2f140.png" width="500">



- #### Navigating to category specific pages
<img src="https://user-images.githubusercontent.com/60477228/113505879-22033780-955f-11eb-9e3b-fbb99c30bea5.png" width="500">


