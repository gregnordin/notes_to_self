## Installation

### With `brew` on mac os

See See https://gist.github.com/midwire/048d983ac4ddd96d81f6 for installing ffmpeg with all options and 12/28/17 entry at [[GN - 2015 MacBook Pro Software Installation and Use]] for example useage.

---

## Documentation

[ffmpeg Documentation](http://www.ffmpeg.org/ffmpeg.html)  
[FFmpeg Filters Documentation](https://ffmpeg.org/ffmpeg-filters.html)  
<span style="color:red">&#x2605;</span> [Filtering - Introduction](https://ffmpeg.org/ffmpeg-filters.html#Filtering-Introduction)  
<span style="color:red">&#x2605;</span> [Filtergraph description](https://ffmpeg.org/ffmpeg-filters.html#Filtergraph-description)  
[FFmpeg Filtering Guide](https://trac.ffmpeg.org/wiki/FilteringGuide)  

---

## Information

<span style="background: lightgreen">Excellent!</span> - [Extract images frame by frame from a video file using FFMPEG](http://www.bugcodemaster.com/article/extract-images-frame-frame-video-file-using-ffmpeg)  
[FFmpeg command to find key frame closest to 3rd minute](https://superuser.com/questions/536987/ffmpeg-command-to-find-key-frame-closest-to-3rd-minute). A keyframe will have the highest image quality.  
[How to apply 2 filters drawtext and drawbox using FFMPEG](https://stackoverflow.com/questions/45000183/how-to-apply-2-filters-drawtext-and-drawbox-using-ffmpeg)  

---

## Example Commands

### What filters are available?

	ffmpeg -filters 
    
If there are a lot of filters, use grep to search for what you want:

	ffmpeg -filters -hide_banner | grep -i <search term>

### Extract multiple key frames

	ffmpeg -ss 00:02:10 -i mixer3_4red_2water_2.mp4 -vf select="eq(pict_type\,I)" -vframes 2 out_test_%03d.png -hide_banner
    
**Explanation**
- `-ss 00:02:10` start seeking at 2:10 into the video
- `-i mixer3_4red_2water_2.mp4` specify input file
- `-vf select="eq(pict_type\,I)"` apply video filter (-vf) to get all keyframes (index frames)
- `-vframes 2` get 2 frames (this could be any number from >= 1)
out_test_%03d.png output file, which is a png file. %03d means append a 3 digit integer to the end of the file name.
- `-hide_banner` hide ffmpeg compilation information

### Extract single frame at 3 seconds into video

	ffmpeg -ss 00:00:03.000 -i 171213_p2_mixer3_iphone_videos/raw_video/171213_p2_mixer3_3water3red_0mix_slow.MOV -vframes 1 171213_p2_mixer3_iphone_videos/images_GN/171213_p2_mixer3_3water3red_0mix_slow.png -hide_banner

### Draw text on every video frame

	ffmpeg -i 171009_p2_pump3_050ms_phase_trimmed.mp4 -vf \
        "drawtext=fontfile=/Library/Fonts/Verdana.ttf:text='300 um': \
	    fontcolor='white':fontsize=20:x=615:y=50" temp_with_text.mp4

### Draw text only on range of frames

Frames between 1 and 3 seconds into video:

    ffmpeg -i 180111_p4_pump_40px_vacuum.MOV -vf \
        "drawtext=fontfile=/Library/Fonts/Verdana.ttf:text='300 um': \
        fontcolor='white':fontsize=50:x=500:y=100:enable='between(t,1,3)'" temp_text_seconds1-3.mp4

Frames 10 to 62 into video:

    ffmpeg -i 180111_p4_pump_40px_vacuum.MOV -vf \
        "drawtext=fontfile=/Library/Fonts/Verdana.ttf:text='300 um': \
        fontcolor='white':fontsize=50:x=500:y=100:enable='between(n,10,62)'" temp_text_seconds1-3.mp4


### Draw line using `drawbox`

This draws a scalebar 300 &mu;m long on top of the displacement chamber in the video. The default box line thickness is 3 pixels so setting `h=6` means the box will appear as a line 6 pixels wide.

	ffmpeg -i 171009_p2_pump3_050ms_phase_trimmed.mp4 -vf \ 
    	"drawbox=x=358:y=128:w=245:h=6:color=white" temp_with_box.mp4
        
        
### Draw scalebar and text

Key point (see [Filtergraph syntax](https://ffmpeg.org/ffmpeg-filters.html#Filtergraph-syntax-1)): *A **filterchain** consists of a sequence of connected filters, each one connected to the previous one in the sequence. A filterchain is represented by a list of ","-separated filter descriptions.* Note that this is distinct from a **filtergraph**: *A filtergraph consists of a sequence of filterchains. A sequence of filterchains is represented by a list of ";"-separated filterchain descriptions.*

Scalebar and text in upper right in video:

	ffmpeg -i 171009_p2_pump3_050ms_phase_trimmed.mp4 -vf \
    	"drawtext=fontfile=/Library/Fonts/Verdana.ttf:text='300 um': \
    	fontcolor='white':fontsize=24:x=615:y=50, \
    	drawbox=x=530:y=25:w=245:h=6:color=white" temp_with_text_and_box_upper.mp4

Scalebar and text in lower right in video:

    ffmpeg -i 171009_p2_pump3_050ms_phase_trimmed.mp4 -vf \
        "drawtext=fontfile=/Library/Fonts/Verdana.ttf:text='300 um': \
        fontcolor='white':fontsize=24:x=815:y=637, \
        drawbox=x=730:y=665:w=245:h=6:color=white" temp_with_text_and_box.mp4
        
### Cut video

Cut the video, starting at 00:00:03 and going for a duration of 00:00:08

	ffmpeg -i movie.MOV -ss 00:00:03 -t 00:00:08 -async 1 cut.MOV

Cut the video, starting at 00:00:03 and ending at 00:00:08

	ffmpeg -i movie.MOV -ss 00:00:03 -to 00:00:08 -async 1 cut.MOV

> [ffmpeg Documentation](https://ffmpeg.org/ffmpeg.html):  
> -t duration (input/output)  
>When used as an input option (before -i), limit the duration of data read from the input file.

>When used as an output option (before an output url), stop writing the output after its duration reaches duration.

>duration must be a time duration specification, see (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual.

>-to and -t are mutually exclusive and -t has priority.

>-to position (input/output)  
Stop writing the output or reading the input at position. position must be a time duration specification, see (ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual.

&nbsp;

>-async 1 is a special case where only the start of the audio stream is corrected without any later correction.  
>... This option has been deprecated. Use the aresample audio filter instead.

        
### Put frame time on each frame

Format: X.XXXXXX seconds:

	ffmpeg -i 180111_p4_pump_40px_vacuum.MOV -vf \
        "drawtext=fontfile=/Library/Fonts/Verdana.ttf:text='timestamp\: %{pts \: flt}': \
        fontcolor='white':fontsize=50:x=200:y=100:" temp_text_frametimetemp_text_frametime_flt_format.mp4

Format: Hours:Minutes:Seconds.XXXX:

    ffmpeg -i 180111_p4_pump_40px_vacuum.MOV -vf \
        "drawtext=fontfile=/Library/Fonts/Verdana.ttf:text='timestamp\: %{pts \: hms}': \
        fontcolor='white':fontsize=50:x=200:y=100:" temp_text_frametime_hms_format.mp4

Format: Hours:Minutes:Seconds:

    ffmpeg -i 180111_p4_pump_40px_vacuum.MOV -vf \
        "drawtext=fontfile=/Library/Fonts/Verdana.ttf:text='timestamp\: %{pts\:gmtime\:0\:%M %S}': \
        fontcolor='white':fontsize=50:x=200:y=100:" temp_text_frametime.mp4

