alias rr := render_remote

render_remote scene:
    cd .. && rsync -azP expos-vc kali:~ --exclude=".git" --exclude="videos" --exclude=".idea"
    ssh kali  "pwd && cd ~/expos-vc && just lrf {{scene}} && exit"
    cd .. && rsync -azP kali:~/expos-vc/media/videos/main/2160p60/{{scene}}.mp4 expos-vc/videos
    just open {{scene}}

edit:
    open Notebook.wls -a "Mathematica"
    
open scene:
    qil "QuickTime Player"
    sleep 0.5
    open videos/{{scene}}.mp4 -a "QuickTime Player"

lrvl scene:
    just render_local manim_very_low.cfg {{scene}}

lrl scene:
    just render_local manim_low.cfg {{scene}}

lrf scene:
    just render_local manim.cfg {{scene}}

render_local config scene caching="yes":
    manim \
        --format mp4 \
        -c cfg/{{config}} \
        {{ if caching == "yes" { "" } else { "--disable_caching" } }} \
        -p \
        main.py {{scene}}
