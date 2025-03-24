document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("tahminForm");
    const input = document.getElementById("tahminInput");

    // Sayfa yüklendiğinde input alanını otomatik seç
    input.focus();

    // Form gönderildiğinde input'u temizleyip tekrar seç
    form.addEventListener("submit", (event) => {
        event.preventDefault(); // Sayfanın yenilenmesini engelle

        const formData = new FormData(form);

        // Form verisini arka planda gönder
        fetch("/", {
            method: "POST",
            body: formData
        })
        .then(response => response.text())
        .then(html => {
            document.body.innerHTML = html; // Sayfa içeriğini güncelle
            document.getElementById("tahminInput").focus(); // Input alanını tekrar seç
        })
        .catch(error => console.error("Hata:", error));
    });
});

