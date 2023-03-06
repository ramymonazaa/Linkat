let arr = [];
// initialize localstorage empty when empty
if (!localStorage.getItem("favorite")) {
    let icon1 = {
        index: "-1",
        state: 1,
    };
    arr.push(icon1);
}
// to store data in localstorage
if (localStorage.getItem("favorite")) {
    arr = JSON.parse(localStorage.getItem("favorite"));
}
localStorage.setItem("favorite", JSON.stringify(arr));
loadData();
let clicked = (id) => {
    let colored = 0;
    let icon = {
        index: id,
        state: 1,
    };

    if (localStorage.getItem("favorite")) {
        JSON.parse(localStorage.favorite).forEach((element) => {
            if (element.index == id) {
                colored = element.state;
            }
        });
    }
    // alert("id");
    let arr = JSON.parse(localStorage.favorite);
    if (colored == 0 || colored == 2) {
        if (colored == 0) {
            arr.push(icon);
        }
        arr.forEach((element) => {
            if (element.index == id) {
                element.state = 1;
            }
        });
        document.getElementById(id).classList = "fas fa-heart red_heart";
        document.location.href = "add_fav " + id;

    } else {
        document.getElementById(id).classList = "fal fa-heart";
        // let url = "{% url'home'%}";
        arr.forEach((element) => {
            if (element.index == id) {
                element.state = 2;
            }
        });
        document.location.href = "del_fav " + id;
    }
    localStorage.setItem("favorite", JSON.stringify(arr));
};

function loadData() {

    if (localStorage.getItem("favorite")) {
        JSON.parse(localStorage.favorite).forEach((element) => {
            if (element.index != "-1" && element.index != "1") {

                if (element.state == 1) {
                    document.getElementById(element.index).classList = "fas fa-heart red_heart";
                } else {
                    document.getElementById(element.index).classList = "fal fa-heart";
                }
            }
        });
    }
}