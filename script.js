document.addEventListener('DOMContentLoaded', () => {
    const apiKey = '83d08170fd3245729536b8e272339346';
    const searchInput = document.getElementById('search-input');
    const searchButton = document.getElementById('search-button');
    const newsContainer = document.getElementById('news-container');
  
    async function fetchNews(query = 'general') {
      try {
        const response = await fetch(`https://newsapi.org/v2/everything?q=${query}&apiKey=${apiKey}`);
        const data = await response.json();
        return data.articles;
      } catch (error) {
        console.error('Error fetching news:', error);
        return [];
      }
    }
  
    function displayNews(articles) {
      newsContainer.innerHTML = '';
      articles.forEach(article => {
        const newsItem = document.createElement('div');
        newsItem.classList.add('news-item');
        newsItem.innerHTML = `
          <img src="${article.urlToImage || 'https://via.placeholder.com/300x200?text=News'}" alt="${article.title}">
          <h2>${article.title}</h2>
          <p>${article.description}</p>
          <a href="${article.url}" target="_blank">Read more</a>
        `;
        newsContainer.appendChild(newsItem);
      });
    }
  
    async function init() {
      const articles = await fetchNews();
      displayNews(articles);
    }
  
    searchButton.addEventListener('click', async () => {
      const query = searchInput.value.trim();
      if (query) {
        const articles = await fetchNews(query);
        displayNews(articles);
      }
    });
  
    searchInput.addEventListener('keypress', async (e) => {
      if (e.key === 'Enter') {
        const query = searchInput.value.trim();
        if (query) {
          const articles = await fetchNews(query);
          displayNews(articles);
        }
      }
    });
  
    init();
  });
  
  