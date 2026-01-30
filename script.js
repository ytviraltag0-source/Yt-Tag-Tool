function generate(){
  let q = document.getElementById("keyword").value;
  fetch("/api?q=" + q)
  .then(res => res.json())
  .then(data => {
    let box = document.getElementById("output");
    box.innerHTML = "";
    data.forEach(tag => {
      let div = document.createElement("div");
      div.className = "tag";
      div.innerHTML = tag + " <span onclick='this.parentElement.remove()'>×</span>";
      box.appendChild(div);
    });
  });
}

function copyTags(){
  let tags = [...document.querySelectorAll(".tag")]
    .map(t => t.innerText.replace("×",""))
    .join(", ");
  navigator.clipboard.writeText(tags);
  alert("Copied!");
}
