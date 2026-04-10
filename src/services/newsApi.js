
// Updated: 2026-04-10 15:00:00
export const fetchNews = async (category) => {
  const res = await fetch(`/api/news?cat=${category}`);
  return res.json();
};
