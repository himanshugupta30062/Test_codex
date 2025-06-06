const chatForm = document.getElementById('chat-form');
const chatInput = document.getElementById('chat-input');
const messages = document.getElementById('messages');

if (chatForm) {
    chatForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const text = chatInput.value.trim();
        if (!text) return;
        const msgEl = document.createElement('div');
        msgEl.className = 'message you';
        msgEl.textContent = text;
        messages.appendChild(msgEl);
        messages.scrollTop = messages.scrollHeight;
        chatInput.value = '';
    });
}
