document.getElementById('snippetForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const content = document.getElementById('content').value;
    const isPublic = document.getElementById('isPublic').checked;
    const expiresAt = document.getElementById('expiresAt').value;

    try {
        const response = await fetch('/api/v1/snippets/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                content,
                is_public: isPublic,
                expires_at: expiresAt || null,
            }),
        });

        if (response.ok) {
            const data = await response.json();
            document.getElementById('snippetLink').href = `/${data.link}`;
            document.getElementById('snippetLink').textContent = `${window.location.origin}/${data.link}`;
            document.getElementById('result').style.display = 'block';
        } else {
            const errorData = await response.json();
            alert(`Failed to create snippet: ${errorData.detail}`);
        }
    } catch (error) {
        alert('Failed to create snippet. Please try again.');
        console.error(error);
    }
});