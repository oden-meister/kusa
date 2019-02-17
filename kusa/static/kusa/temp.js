window.addEventListener("load", function(event) {
    var touchStartX;
    var touchStartY;
    var touchMoveX;
    var touchMoveY;
    // 開始時
    window.addEventListener("touchstart", function(event) {
        event.preventDefault();
        // 座標の取得
        touchStartX = event.touches[0].pageX;
        touchStartY = event.touches[0].pageY;
    }, false);

    // 移動時
    window.addEventListener("touchmove", function(event) {
        event.preventDefault();
        // 座標の取得
        touchMoveX = event.changedTouches[0].pageX;
        touchMoveY = event.changedTouches[0].pageY;
    }, false);
    // 終了時
    window.addEventListener("touchend", function(event) {
        // 移動量の判定
        if (touchStartX > touchMoveX) {
            if (touchStartX > (touchMoveX + 50)&&touchStartX-(touchMoveX+50)>150) {
                //右から左に指が移動した場合
                hide();
            }
        }else if (touchStartX < touchMoveX) {
            if ((touchStartX + 50) < touchMoveX&&touchMoveX-(touchStartX+50)>150) {
                //左から右に指が移動した場合
                show();
            }
        }
    }, false);
}, false);

function hide(){
                window.document.getElementById("menucontent").style.visibility="visible"
                window.document.getElementById("amenu").style.visibility="hidden"
                window.document.getElementById("humb1").style.visibility="hidden";
                window.document.getElementById("humb2").style.visibility="hidden";
                window.document.getElementById("humb3").style.visibility="hidden";
}

function show(){
                window.document.getElementById("menucontent").style.visibility="hidden"
                window.document.getElementById("amenu").style.visibility="visible";
                window.document.getElementById("humb1").style.visibility="visible";
                window.document.getElementById("humb2").style.visibility="visible";
                window.document.getElementById("humb3").style.visibility="visible";
}