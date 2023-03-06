const close = document.querySelector(".close-popup"),
    newArticle = document.querySelector(".newArticle");

function openPopup(em, name, di) {

    const u = document.getElementById('url');
    u.value = name;
    const e = document.getElementById('name');
    e.value = em;
    const d = document.getElementById('description');
    d.value = di;
    const x = document.getElementById('state');
    x.value = em;

    newArticle.classList.add("active");
}

function openPopup1() {
    newArticle.classList.add("active");
}

function closePopup() {
    newArticle.classList.remove("active");
}
// خلصني و اشتغل
let popup = document.querySelector(".newArticle-form ");
window.addEventListener("resize", () => {
    if (window.innerHeight < 550) {
        popup.style.cssText = "top:calc(41px + 1rem)";
    } else {
        popup.style.cssText = "top:0";
    }
});