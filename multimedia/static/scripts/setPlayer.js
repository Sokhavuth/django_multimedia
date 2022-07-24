//asset/js/setPlayer.js

function setScreen(entry,id,click){
    if(entry['type'] == 'OK'){
        var url = `//ok.ru/videoembed/${entry['video_id']}`
    }else if(entry['type'] == 'YouTube'){
        var url = `https://www.youtube.com/embed/${entry['video_id']}`
    }else if(entry['type'] == 'YouTubePlaylist'){
        var url = `https://www.youtube.com/embed/videoseries?list=${entry['video_id']}`
    }else if(entry['type'] === "Facebook"){
        var url = `https://www.facebook.com/watch/?v=${entry['video_id']}`
    }else if(entry['type'] === "GoogleDrive"){
        var url = `https://docs.google.com/file/d/${entry['video_id']}/preview`
    }else if(entry['type'] === "Vimeo"){
        var url = `https://player.vimeo.com/video/${entry['video_id']}`
    }else if(entry['type'] === "Dailymotion"){
        var url = `https://www.dailymotion.com/embed/video/${entry['video_id']}`
    }

    if(entry['type'] !== 'Facebook'){
        var iframe = `<div>
        <iframe id="player" src="${url}" frameborder="0" allowfullscreen></iframe>
        </div>`;
      }else{
        var iframe = `<div class="fb-video" data-href="${url}" data-width="auto" data-show-captions="true"></div>`;
    }

    if(click){
        $('.Post .main .content .playlist #part'+clicked)
            .css({'background':'lightgrey','color':'rgb(71, 71, 71)'})
    }
    
    $('.Post .main .content .playlist #part'+id)
        .css({'background':'var(--background-dark)','color':'white'})


    $('.Post .main .content .video .screen').html(iframe)
    if((entry['type'] === "Facebook")&&(fb_api)){
        FB.XFBML.parse()
    }  

    clicked = id
}

