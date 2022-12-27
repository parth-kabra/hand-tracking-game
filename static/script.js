let count = 0;

setInterval(()=>{
    socket.emit("send_data", 1);
}, 600)

function fingerCount(array){
    let count = 0;
    array.forEach(finger => {
        count += finger;
    });
    return count;
}

socket.on("hand", (dict)=>{
    if(dict["hand"]){
        const array = dict["handCount"];
        let count = fingerCount(array);
        document.getElementById("console").innerHTML += `
            <p class="console__fing">
                Fingers = [${array}]<br>
                Finger Count = (${count})
            </p>
        `
        let console = document.getElementById("console")
        console.scrollTop = console.scrollHeight
        document.getElementById("finger__count").innerText = `Finger Count: ${count}`
        document.getElementById("tracker__console").innerHTML = `
            <img src="../static/${count}.jpg" width="62%">
        `
    }
    else{
        document.getElementById("finger__count").innerText = `Finger Count: 0`
        document.getElementById("tracker__console").innerHTML = `
        <span>
        <br>
        <p class="h5 not__found" align="center">No hand detection was possible.</p>
        <p class="text-muted h6" align="center">Make sure you show your <br>hand properly.</p>
        </span>
        `
    }
})

