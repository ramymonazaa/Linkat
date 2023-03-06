let sidebar = document.querySelector(".sidebar");
// profile__contribution
state = "11"
localStorage.setItem("section", state);

function toggleSidebar() {
    sidebar.classList.toggle("close");
}
let list = document.querySelectorAll(".sidebar__list li"),
    profile = document.querySelectorAll(".profile__content");

function execute1(section) {
    document.getElementById("11").style.display = "none";
    document.getElementById("22").style.display = "none";
    document.getElementById("33").style.display = "none";
    document.getElementById("44").style.display = "none";
    document.getElementById(section).style.display = "block";

    document.querySelectorAll(".sidebar__list li.active")
        .forEach((li) => {
            li.classList.remove("active");
        });
    list.forEach((li) => {
        if (li.dataset.toggle == section) {
            li.classList.add("active")
        }
    })
}

function execute(section) {
    document.location.href = "change_section " + section;
    execute(section);
}
// function execute(section) {
//     alert(section);

//     profile.forEach((content) => {
//         //alert("2");
//         if (section != "disabled") {
//             //alert("3");
//             document.querySelectorAll(".profile .active").forEach((element) => {
//                 element.classList.remove("active");
//             });
//             if (content.classList.contains(section)) {
//                 content.classList.add("active");
//                 alert("4");
//             }
//         }
//     });
// }
// list.forEach((e) => {
//     e.addEventListener("click", () => {
//         alert(e.dataset.toggle);
//         if (e.dataset.toggle != "disabled") {
//             document.querySelectorAll(".profile .active").forEach((element) => {
//                 element.classList.remove("active");
//             });
//             document
//                 .querySelectorAll(".sidebar__list li.active")
//                 .forEach((li) => {
//                     li.classList.remove("active");
//                 });
//         }
//         profile.forEach((content) => {
//             if (e.dataset.toggle != "disabled") {
//                 if (content.classList.contains(e.dataset.toggle)) {
//                     content.classList.add("active");
//                     // e.classList.add("active");
//                 }
//             }
//         });
//     });
// });

// file upload 
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
            $('#imagePreview').hide();
            $('#imagePreview').fadeIn(650);
        }
        reader.readAsDataURL(input.files[0]);
    }
}
$("#imageUpload").change(function() {
    readURL(this);
});
//