document.addEventListener('DOMContentLoaded', () => {
  const chatBox = document.getElementById('chat-box');
  const userInput = document.getElementById('user-input');
  const sendButton = document.getElementById('send-button');

  const API_URL = 'http://localhost:8000/faq/';

  function appendMessage(text, isUser) {
      const messageDiv = document.createElement('div');
      messageDiv.classList.add('message');
      messageDiv.classList.add(isUser ? 'user-message' : 'bot-message');
      messageDiv.textContent = text;
      chatBox.appendChild(messageDiv);
      chatBox.scrollTop = chatBox.scrollHeight;
  }

  function sendMessage() {
      const query = userInput.value.trim();
      if (query === '') return;

      appendMessage(query, true);
      userInput.value = '';

      fetch(`${API_URL}?query=${encodeURIComponent(query)}`)
          .then(response => response.json())
          .then(data => {
              if (data.result && data.result.answer) {
                  appendMessage(data.result.answer, false);
              } else {
                  appendMessage('I’m sorry, I don’t have an answer for that.', false);
              }
          })
          .catch(error => {
              console.error('Error:', error);
              appendMessage('There was an error. Please try again later.', false);
          });
  }

  sendButton.addEventListener('click', sendMessage);

  userInput.addEventListener('keypress', event => {
      if (event.key === 'Enter') {
          sendMessage();
      }
  });
});
