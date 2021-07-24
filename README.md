# Kanizsa_illusion

A Python library for simply generating Kanizsa illusion graphics (triangles and rectangles).

<div class="video_play">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">

<style>
.animation {
    display: inline-block;
    text-align: center;
}
input[type=range].anim-slider {
    width: 374px;
    margin-left: auto;
    margin-right: auto;
}
.anim-buttons {
    margin: 8px 0px;
}
.anim-buttons button {
    padding: 0;
    width: 36px;
}
.anim-state label {
    margin-right: 8px;
}
.anim-state input {
    margin: 0;
    vertical-align: middle;
}
</style>


<div class="animation">
  <img id="_anim_imgc09ff29903134f97a22bd8f7b13bb28b">
  <div class="anim-controls">
    <input id="_anim_sliderc09ff29903134f97a22bd8f7b13bb28b" type="range" class="anim-slider"
           name="points" min="0" max="1" step="1" value="0"
           oninput="animc09ff29903134f97a22bd8f7b13bb28b.set_frame(parseInt(this.value));"></input>
    <div class="anim-buttons">
      <button title="Decrease speed" onclick="animc09ff29903134f97a22bd8f7b13bb28b.slower()">
          <i class="fa fa-minus"></i></button>
      <button title="First frame" onclick="animc09ff29903134f97a22bd8f7b13bb28b.first_frame()">
        <i class="fa fa-fast-backward"></i></button>
      <button title="Previous frame" onclick="animc09ff29903134f97a22bd8f7b13bb28b.previous_frame()">
          <i class="fa fa-step-backward"></i></button>
      <button title="Play backwards" onclick="animc09ff29903134f97a22bd8f7b13bb28b.reverse_animation()">
          <i class="fa fa-play fa-flip-horizontal"></i></button>
      <button title="Pause" onclick="animc09ff29903134f97a22bd8f7b13bb28b.pause_animation()">
          <i class="fa fa-pause"></i></button>
      <button title="Play" onclick="animc09ff29903134f97a22bd8f7b13bb28b.play_animation()">
          <i class="fa fa-play"></i></button>
      <button title="Next frame" onclick="animc09ff29903134f97a22bd8f7b13bb28b.next_frame()">
          <i class="fa fa-step-forward"></i></button>
      <button title="Last frame" onclick="animc09ff29903134f97a22bd8f7b13bb28b.last_frame()">
          <i class="fa fa-fast-forward"></i></button>
      <button title="Increase speed" onclick="animc09ff29903134f97a22bd8f7b13bb28b.faster()">
          <i class="fa fa-plus"></i></button>
    </div>
    <form title="Repetition mode" action="#n" name="_anim_loop_selectc09ff29903134f97a22bd8f7b13bb28b"
          class="anim-state">
      <input type="radio" name="state" value="once" id="_anim_radio1_c09ff29903134f97a22bd8f7b13bb28b"
             >
      <label for="_anim_radio1_c09ff29903134f97a22bd8f7b13bb28b">Once</label>
      <input type="radio" name="state" value="loop" id="_anim_radio2_c09ff29903134f97a22bd8f7b13bb28b"
             checked>
      <label for="_anim_radio2_c09ff29903134f97a22bd8f7b13bb28b">Loop</label>
      <input type="radio" name="state" value="reflect" id="_anim_radio3_c09ff29903134f97a22bd8f7b13bb28b"
             >
      <label for="_anim_radio3_c09ff29903134f97a22bd8f7b13bb28b">Reflect</label>
    </form>
  </div>
</div>
	<script type="text/javascript" src="video.js"></script>

</div>