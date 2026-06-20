document.addEventListener('DOMContentLoaded', () => {
  const apiKey = 'pub_64589c9d465102db105324eadd353146be502';
  const searchInput = document.getElementById('search-input');
  const searchButton = document.getElementById('search-button');
  const newsContainer = document.getElementById('news-container');
  
  async function fetchNews(query = 'general') {   
      try {
          const response = await fetch(`https://newsdata.io/api/1/latest?apikey=${apiKey}&q=${query}&language=en`);
          if (!response.ok) {
              throw new Error(`HTTP Error: ${response.status}`);
          }
          const data = await response.json();
          return data.results || [];
      } catch (error) {
          console.error('Error fetching news:', error);
          return [];
      }
  }

  function displayNews(articles) {
      if (!articles || articles.length === 0) {
          newsContainer.innerHTML = '<p>No news articles found. Please try another search.</p>';
          return;
      }
      newsContainer.innerHTML = '';
      articles?.forEach(article => {
          const newsItem = document.createElement('div');
          newsItem.classList.add('news-item');
          newsItem.innerHTML = `
              <img src="${article.image_url || 'https://via.placeholder.com/300x200?text=No+Image'}" alt="${article.title || 'News'}">
              <h2>${article.title || 'No Title Available'}</h2>
              <p>${article.description || 'No Description Available'}</p>
              <a href="${article.link}" target="_blank">Read more</a>
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
